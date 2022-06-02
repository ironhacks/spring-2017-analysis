import os
import config
from unidiff import PatchSet
import ntpath
import subprocess
import traceback

class Diff(object):
	def __init__(self, config, project1, project2, diffProject):
		self.config = config
		self.project1 = project1
		self.project2 = project2
		self.diffProjectName = ntpath.basename(diffProject.path) 
		self.diffProjectFolder = os.path.dirname(diffProject.path)
		self.diffProjectPath = diffProject.path

	def createDiffProject(self):
		curDir = os.getcwd()
		try:
			print(subprocess.check_output("git diff --no-index" \
				+" -w --ignore-space-at-eol -b \"" \
				+"{0}\" \"{1}\" >> \"{2}/git_diff_{3}.txt\"".format(\
					self.project1.path, self.project2.path, \
					self.diffProjectFolder, self.diffProjectName), shell=True))
		except subprocess.CalledProcessError:
			pass
		if not os.path.exists(self.diffProjectPath):
			os.makedirs(self.diffProjectPath)
		gitDiffFileName = "{0}/git_diff_{1}.txt".format(self.diffProjectFolder, \
			self.diffProjectName)
		try:
			with open(gitDiffFileName, 'r', encoding='utf-8', \
				errors='ignore') as diff_file:
				patch = PatchSet(diff_file)
				os.chdir(self.diffProjectPath)
				for changedFile in patch:
					print("Processing git diff for file {0}".format(changedFile.path))
					if changedFile.is_removed_file:
						continue						
					fileBaseName = os.path.basename(changedFile.path)
					bits = changedFile.path.split(ntpath.basename(\
						self.project1.path))
					baseDir = bits[-1].replace(fileBaseName, '')[1:]
					if baseDir and not os.path.exists(baseDir):
						os.makedirs(baseDir)
					writer = open(os.path.join(baseDir, fileBaseName), 'w')
					count = 0;
					flag = 1;
					for line in str(changedFile).splitlines():
						if(count < 3):
							count = count + 1
							continue
						if(line.startswith('@@ ')):
							continue
						if line[0] == '+':
							flag = 1
							line = line[1:]
						elif line[0] == '-':
							flag = 0
							line = line[1:]
						if flag==1:
							writer.write(line + '\n')
					writer.close()
		except:
			traceback.print_exc()
		os.chdir(curDir)
