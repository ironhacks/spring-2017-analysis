import os
import config
from Dictionary import Dictionary, DictionaryList

class Project(object):
	def __init__(self, phase, path):
		self.phase = phase
		self.path = path
		self.l1Features = list()
		self.l2Features = list()

	def constructFeatureVector(self, dictList):
		blob = "" #Don't create this as data member, since this can become huge
		for file in os.listdir(self.path):
			if file.endswith(".js") or file.endswith(".html")\
			or file.endswith(".htm"):
				webFile = open(os.path.join(self.path, file), errors='ignore')
				blob += webFile.read()
				webFile.close()
		l1FeaturesDict = dict()
		for k, v in dictList.items():
			l1FeaturesDict.setdefault(v.type, 0)
			for feature in v.features:
				featureCount = blob.count(feature)
				self.l2Features.append(featureCount)
				l1FeaturesDict[v.type] += featureCount
		self.l1Features = l1FeaturesDict.values()

