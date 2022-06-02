import os
import config

class Dictionary(object):
	def __init__(self, type, filePath):
		self.type = type
		self.filePath = filePath
		self.features = set()

class DictionaryList(object):
	def __init__(self, config):
		self.config = config
		self.dictList = dict()

	def readDictionaryList(self):
		'''Lazy loading of just the dictionary metadata
		Doesn't really load the dictionary features
		'''
		curDir = os.getcwd()
		os.chdir(self.config.DICTIONARY_FOLDER)
		for content in os.listdir(os.getcwd()):
			# content = <type>-<name>.<extension>
			parts = content.split('.')
			extension = parts[-1]
			fileName = parts[0]
			dictType = fileName
			dictName = fileName
			dictKey = fileName
			dictValue = Dictionary(dictType, os.path.join(os.getcwd(), content))
			self.dictList[dictKey] = dictValue
		os.chdir(curDir)

	def loadDictionaryList(self):
		'''Actually load the dictionary lists
		'''
		for k, v in self.dictList.items():
			with open(v.filePath, 'r', encoding='utf8', errors='ignore') as f:
				for line in f:
					parameter = None
					if v.type == 'dictionary':
						parameter = line.split(',')[0]
					else:
						parameter = line.split(' ')[0]
					self.dictList[k].features = self.dictList[k].features | \
						{parameter}
