import os
import config
import Dictionary
import csv

class Similarity(object):
	def __init__(self, distanceMetric=None):
		self.distanceMetric = 'Jaccard'

	def calculate(self, project1, project2):
		if(self.distanceMetric == 'Jaccard'):
			l1Common = [min(x,y) for x,y in zip(project1.l1Features, project2.l1Features)]
			l1Num = sum(l1Common)
			l1Denom = sum([x+y-z for x,y,z in zip(project1.l1Features, \
				project2.l1Features, l1Common)])
			l2Common = [min(x,y) for x,y in zip(project1.l2Features, project2.l2Features)]
			l2Num = sum(l2Common)
			l2Denom = sum([x+y-z for x,y,z in zip(project1.l2Features, \
				project2.l2Features, l2Common)])
			l1Sim = l1Num/l1Denom if l1Denom!=0 else 0
			l2Sim = l2Num/l2Denom if l2Denom!=0 else 0
			return (l1Sim, l2Sim)
		else:
			raise NotImplementedError('Distance metric {0} is not implemented\
				'.format(self.distanceMetric))

	def writeMatrixToFile(self, matrix, folder, filePrefix, phase):
		for i in range(1, 3):
			filePath = os.path.join(folder, filePrefix + \
				'-l{0}-similarity-phase{1}.csv'.format(i, phase))
			with open(filePath, 'w') as fout:
				writer = csv.writer(fout, delimiter=",", quotechar='"')
				count = 0
				for project1, internalDict in matrix.items():
					if count == 0:
						count = 1
						writer.writerow([""] + list(internalDict.keys()))
					writer.writerow([project1] + [x[i-1] for x in \
						list(internalDict.values())])

