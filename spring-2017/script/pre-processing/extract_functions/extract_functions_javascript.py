import os
import re
import csv
import shutil
import subprocess

class extract_functions_javascript(object):
	def __init__(self, hack_name, phase, input, output):
		self.home_dir = os.getcwd()
		# store all projects file
		self.projects_list = list()
		# store all functions used by each project
		self.projects_functions_list = list()
		# store the name of projects
		self.name_list = list()
		# blck list for library
		self.library_black_list = list()
		# create black list
		with open('library_list.csv') as libraryblacklist:
			library_blacklist_reader = csv.reader(libraryblacklist)
			for row in library_blacklist_reader:
				self.library_black_list.append(row[0].strip())
				#print('{}'.format(row[0].strip()))
		self.function_filter = list()
		with open('function_filter.csv') as f_filter:
			function_filter_reader = csv.reader(f_filter)
			for row in function_filter_reader:
				self.function_filter.append(row[0].strip())
				#print('{}'.format(row[0].strip()))
		self.hack_name = hack_name
		self.phase = phase		
		self.input = input
		self.output = output

	def read_file(self, path):
		os.chdir(self.input)
		#os.chdir(path)
		# preprocess
		for root, dirs, files in os.walk(os.getcwd()):
			for file in files:
				if file.endswith('.zip'):
					subprocess.call(["unzip", '-o', os.path.join(root, file), '-d', root])
					os.remove(os.path.join(root, file))
		# in phase level folder
		for directory in os.listdir(os.getcwd()):
			if os.path.isdir(directory):
				files_list = list()
				self.name_list.append(directory)
				# enter project folder
				os.chdir(directory)
				# search all files in project folder
				for root, dirs, files in os.walk(os.getcwd()):
					# if it is a file:
					for file in files:
						# only need js,html
						if not file.endswith(('.js', '.html', 'htm')):
							# print('skip {}'.format(sub_directory))
							continue
						blackname_flag = 1
						# remove library
						for blackname in self.library_black_list:
							if file.find(blackname) != -1:
								blackname_flag = 0
								break
						if blackname_flag == 0:
							continue
						path = os.path.join(root, file)
						files_list.append(path);
				self.projects_list.append(files_list)
				os.chdir("..")
		#print(self.projects_list)
	def extract(self):
		reg = re.compile(r'[a-zA-Z]*\.[a-zA-Z]+(?:\.[a-zA-Z]+)*')
		for project in self.projects_list:
			functions_list = list()
			for file in project:
				try:
					f = open(file)
					for line in f.readlines():
						result = reg.findall(line)
						if len(result) != 0:
							#print(result)
							for function in result:
								function_skip_flag = 0
								for label in self.function_filter:
									if function.find(label) != -1:
										function_skip_flag = 1
										continue;
								if function_skip_flag != 1:
									functions_list.append(function)
									function_skip_flag = 0
				except Exception as e:
					print(e)
			#deduplication
			self.projects_functions_list.append(self.deduplication(functions_list))
		#print('{}'.format(self.projects_functions_list))

	def deduplication(self,seq):
		seen = set()
		seen_add = seen.add
		return [x for x in seq if not (x in seen or seen_add(x))]
	def output_to_file(self):
		os.chdir(self.home_dir)
		os.chdir(self.output)
		hack_phase = '{}-phase{}'.format(self.hack_name, self.phase)
		if os.path.exists(hack_phase):
			shutil.rmtree(hack_phase)
		os.mkdir(hack_phase)
		os.chdir(hack_phase)
		for name in self.name_list:
			with open(name, 'wt') as f:
				for function in self.projects_functions_list[self.name_list.index(name)]:
					print('{}'.format(function), file=f)
'''
if __name__ == '__main__':
	fe = extract_functions_javascript('spring2017-goldironhack', 1, 'input', 'output');
	fe.read_file("input/phase1")
	fe.extract()
	fe.output_to_file()
'''

