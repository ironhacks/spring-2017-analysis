import os
import sys
import traceback
import config
import zipfile
from time import strftime
import subprocess
import shutil

class Preprocessor(object):
	def __init__(self, config, removeTemplate=False):
		self.config = config
		self.removeTemplate = removeTemplate

	def preprocess(self):
		self._moveAndDeleteFiles()

	def _moveAndDeleteFiles(self):
		curDir = os.getcwd()
		os.chdir(self.config.PHASE_DIRECTORY)
		for content in os.listdir(os.getcwd()):
		# Skip if not a directory or a directory starting with .
		    if os.path.isdir(content) and not content.startswith('.'):
		        # Empty dictionary incase it's required to update the references 
		        mapping = {}
		        for dirpath, dirnames, filenames in os.walk(content):
		            for filename in filenames:
		                if filename.endswith(".html") or filename.endswith(".htm")\
		                or filename.endswith(".js"):	
		                	filename_lc = filename.lower()
			                if self.removeTemplate and filename_lc.endswith(".js") \
			                and (filename_lc in self.config.TEMPLATE_FILE_KEYWORDS or 
			                   	dirpath in self.config.TEMPLATE_DIR_KEYWORDS):
			                	print("Deleting template file {0} from {1}".\
			                       	format(filename, dirpath))
			                	os.remove(os.path.join(dirpath, filename))
			                	print("Deleted template file {0} from {1}".\
		                        	format(filename, dirpath))
			                	continue
			                if dirpath == content:
		                		print("Skipping {0} since it".format(filename)+\
		                			" is already in the project root folder")
		                		continue
		                	print("Moving {0} from {1} to {2}".\
		               			format(filename, dirpath, content))
		                	if(os.path.exists(os.path.join(content, filename))):
		                		dirPart = dirpath.split('\\')[-1].split('/')[-1].\
		                    		replace(os.pathsep,'-')
		                		print(dirPart)
		                		newFilename = dirPart.replace(' ','-').replace('_','-') \
		                    		+ '-' + filename
		                		os.rename(os.path.join(dirpath, filename), \
		                    		os.path.join(dirpath, newFilename))
		                	else:
		                		newFilename = filename
		                	os.rename(os.path.join(dirpath, newFilename), \
		                    	os.path.join(content, newFilename))
		                	print("Moved {0} from {1} to {2}".\
		                    	format(newFilename, dirpath, content))
		os.chdir(curDir)
