import os
import sys
import traceback
import config
import zipfile
from time import strftime
import subprocess
import shutil

class Fetcher(object):
	def __init__(self, config):
		self.config = config

	def _preProcess(self):
		if os.path.exists(self.config.PHASE_DIRECTORY):
			print("Removing directory {0}".format(self.config.PHASE_DIRECTORY))
			shutil.rmtree(self.config.PHASE_DIRECTORY)
			print("Removed directory {0}".format(self.config.PHASE_DIRECTORY))

	def _rawFetch(self):
		subprocess.call(["git", "clone", self.config.URL, self.config.PHASE_DIRECTORY])

	def _postProcess(self):
		curDir = os.getcwd()
		os.chdir(self.config.PHASE_DIRECTORY)
		for dirFile in os.listdir(os.getcwd()):
			if dirFile.endswith('.zip'):
				subprocess.call(["unzip", dirFile])
				os.remove(dirFile)
		for content in os.listdir(os.getcwd()):
			# Skip if not a directory or a directory starting with .
			if os.path.isdir(content) and content == '.git':
				print("Deleting git directory: {0}".format(content))
				shutil.rmtree(content)
				print("Deleted git directory: {0}".format(content))
				continue
			if os.path.isdir(content) and not content.startswith('.'):
				newname = content.replace("-master", "")
				print("Renaming directory: {0} to {1}".format(content, newname))
				os.rename(content, newname)	
				print("Renamed directory: {0} to {1}".format(content, newname))
		os.chdir(curDir)

	def fetchCode(self):
		self._preProcess()
		self._rawFetch()
		self._postProcess()
