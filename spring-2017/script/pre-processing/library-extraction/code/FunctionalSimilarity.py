import os
import sys

import config
import collections
import Dictionary
from Project import Project
import Similarity
import Fetcher
import Preprocessor
import LibraryExtractor
from Diff import Diff

class FunctionalSimilarity(object):
	def __init__(self, hack, removeTemplate=False, numPhases=4, fetch=True):
		self.numPhases = numPhases
		self.hack = hack
		self.cfg = config.Config(self.hack, fetch=fetch)
		os.chdir(self.cfg.HOME_FOLDER)
		self.cfg.cleanFolders()
		self.removeTemplate = removeTemplate
		self.libExtractor = LibraryExtractor.LibraryExtractor()
		for phase in range(1, self.numPhases+1):
			self.cfg.updatePhase(phase)
			if self.cfg.FETCH:
				self.fetcher = Fetcher.Fetcher(self.cfg)
				self.fetcher.fetchCode()
			self.preprocessor = Preprocessor.Preprocessor(self.cfg, \
				self.removeTemplate)
			self.preprocessor.preprocess()
			self.libExtractor.getLibraryList(self.cfg)
		self.dictionaryListObj = Dictionary.DictionaryList(self.cfg)
		self.dictionaryListObj.readDictionaryList()
		self.dictionaryListObj.loadDictionaryList()
		self.projects = dict()
		self.projectNames = set()
		self.similarity = Similarity.Similarity('Jaccard')

	def _readInSamePhaseCode(self):
		for i in range(1, self.numPhases+1):
			curDir = os.getcwd()
			self.projects.setdefault(i, dict())
			self.cfg.updatePhase(i)
			for project in os.listdir(self.cfg.PHASE_DIRECTORY):
				if not os.path.isdir(os.path.join(curDir,self.cfg.PHASE_DIRECTORY,project)):
					continue
				path = os.path.join(self.cfg.PHASE_DIRECTORY, project)
				curProject = Project(i, path)	
				curProject.constructFeatureVector(self.dictionaryListObj.dictList)
				self.projectNames = self.projectNames | {project}
				self.projects[i][project] = curProject
			os.chdir(curDir)

	def _readInCrossPhaseCode(self):
		for i in range(1, self.numPhases):
			curDir = os.getcwd()
			crossPhase = str(i+1) + '-' + str(i)
			self.projects.setdefault(crossPhase, dict())
			self.cfg.updatePhase(crossPhase)
			if not os.path.exists(self.cfg.PHASE_DIRECTORY):
				os.makedirs(self.cfg.PHASE_DIRECTORY)
			for project in self.projectNames:				
				crossPhaseDir = os.path.join(self.cfg.PHASE_DIRECTORY, project)
				crossPhaseProject = Project(crossPhase, crossPhaseDir)
				diff = Diff(self.cfg, self.projects[i][project], \
					self.projects[i+1][project], crossPhaseProject)
				diff.createDiffProject()
				crossPhaseProject.constructFeatureVector(\
					self.dictionaryListObj.dictList)
				self.projects[crossPhase][project] = crossPhaseProject
			os.chdir(curDir)

	def calculateSamePhaseSimilarity(self):
		self._readInSamePhaseCode()
		for i in range(1, self.numPhases+1):
			self.cfg.updatePhase(i)
			similarityDict = collections.OrderedDict()
			for j, project1 in enumerate(self.projectNames):
				similarityDict.setdefault(project1, collections.OrderedDict())
				for k, project2 in enumerate(self.projectNames):
					if project1==project2:
						similarityDict[project1][project2] = (1, 1)
					elif k<j:
						similarityDict[project1][project2] = \
							similarityDict[project2][project1]
					else:
						similarityDict[project1][project2] = \
						self.similarity.calculate(self.projects[i][project1],\
							self.projects[i][project2])
			filePrefix = 'same-phase'
			filePrefix += '-with-template' if not self.removeTemplate\
			 else '-without-template'
			self.similarity.writeMatrixToFile(similarityDict, self.cfg.REPORTS_FOLDER,
				filePrefix, i)

	def calculateCrossPhaseSimilarity(self):
		self._readInCrossPhaseCode()
		for i in range(1, self.numPhases):
			crossPhase = str(i+1) + '-' + str(i)
			prevPhase = i
			self.cfg.updatePhase(crossPhase)
			similarityDict = collections.OrderedDict()
			for project1 in self.projectNames:
				similarityDict.setdefault(project1, collections.OrderedDict())
				for project2 in self.projectNames:	
					similarityDict[project1][project2] = \
					self.similarity.calculate(self.projects[i][project1],\
						self.projects[crossPhase][project2])
			filePrefix = 'cross-phase'
			filePrefix += '-with-template' if not self.removeTemplate\
			 else '-without-template'
			self.similarity.writeMatrixToFile(similarityDict, self.cfg.REPORTS_FOLDER,
				filePrefix, crossPhase)

if __name__ == '__main__':
	fetch = True
	hackName = 'spring2017-unal-goldironhack'
	numPhases = 5

	args = sys.argv[1:]

	if len(args) > 0:
		hackName = args[0]

	if len(args) > 1:
		numPhases = int(args[1])

	if len(args) > 2:
		fetch = int(args[2])

	print('Checking {} phases for hack {}, fetch={}'.format(numPhases, hackName, fetch))
	fSim = FunctionalSimilarity(hackName, False, numPhases, fetch=fetch)
	fSim.calculateSamePhaseSimilarity()
	fSim.calculateCrossPhaseSimilarity()
	fSim.libExtractor.writeLibraryList(fSim.cfg)
	os.chdir(fSim.cfg.CODE_FOLDER)
	withoutTemplateFSim = FunctionalSimilarity(hackName, True, numPhases, fetch=fetch)
	withoutTemplateFSim.calculateSamePhaseSimilarity()
	withoutTemplateFSim.calculateCrossPhaseSimilarity()
