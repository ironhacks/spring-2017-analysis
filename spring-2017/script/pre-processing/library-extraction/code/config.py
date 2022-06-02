#!/usr/bin/python3
import os
import subprocess
import shutil

class Config(object):
	def __init__(self, hack, repository=None, phase=None, templateFileKeywords=None,
		templateDirKeywords=None, fetch=True):
		self.HACK = hack
		self.FETCH = fetch
		if repository is not None:
			self.REPOSITORY = repository
		else:
			self.REPOSITORY = 'RCODI'
		if phase is None:
			self.PHASE = 1
		else:
			self.PHASE = phase
		if templateFileKeywords is None:
			self.TEMPLATE_FILE_KEYWORDS = ["jquery.js", "bootstrap.js", "angular.js", \
			"map.js", "tutorial.js", "radarchart.js"]
		else:
			self.TEMPLATE_FILE_KEYWORDS = templateFileKeywords
		if templateDirKeywords is None:
			self.TEMPLATE_DIR_KEYWORDS = ["node_modules"]
		else:
			self.TEMPLATE_DIR_KEYWORDS = stemplateDirKeywords
		self.GITHUB = 'https://github.com'
		self.PHASE_SEPERATOR = '-phase'
		self.EXTENSION = '.git'
		self.URL_SEPERATOR = '/'
		self.PHASE_DIRECTORY = None
		self.PHASE_FRAGMENT = None
		self.URL = None
		self.DATA_FOLDER = 'data'
		self.LOGS_FOLDER = 'logs'
		self.REPORTS_FOLDER = 'reports'
		self.HOME_FOLDER = '..'
		self.CODE_FOLDER = 'code'
		self.DICTIONARY_FOLDER = 'dictionary'
		self.OLD_REPORTS_FOLDER = 'old'
		self.OLD_LOGS_FOLDER = 'old'

	def updatePhase(self, phase):
		self.PHASE = phase
		self.PHASE_DIRECTORY = os.path.join(self.DATA_FOLDER, \
			self.HACK + self.PHASE_SEPERATOR + str(self.PHASE))
		self.PHASE_FRAGMENT = self.HACK + self.PHASE_SEPERATOR + \
			str(self.PHASE) + self.EXTENSION
		self.URL = self.URL_SEPERATOR.join([self.GITHUB, self.REPOSITORY, self.PHASE_FRAGMENT])

	def cleanFolders(self):
		if self.FETCH:
			if os.path.exists(self.DATA_FOLDER):
				shutil.rmtree(self.DATA_FOLDER)
			os.mkdir(self.DATA_FOLDER)
		if not os.path.exists(self.LOGS_FOLDER):
			os.mkdir(self.LOGS_FOLDER)
		os.chdir(self.LOGS_FOLDER)
		if not os.path.exists(self.OLD_LOGS_FOLDER):
			os.mkdir(self.OLD_LOGS_FOLDER)		
		subprocess.call(["mv", os.path.join("*.log"), self.OLD_LOGS_FOLDER])
		os.chdir(self.HOME_FOLDER)
		if not os.path.exists(self.REPORTS_FOLDER):
			os.mkdir(self.REPORTS_FOLDER)
		os.chdir(self.REPORTS_FOLDER)
		if not os.path.exists(self.OLD_REPORTS_FOLDER):
			os.mkdir(self.OLD_REPORTS_FOLDER)
		subprocess.call(["mv", os.path.join("*.log"), self.OLD_REPORTS_FOLDER])
		os.chdir(self.HOME_FOLDER)
