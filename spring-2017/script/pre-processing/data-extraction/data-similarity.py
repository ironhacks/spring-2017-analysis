import os
import csv
import shutil
import hashlib
import subprocess


# basic information
hackname = "spring2017-unal-goldironhack"
phase_number = 4;
data_directory = "input"
home_directory = os.getcwd()
output_directory = "output"

# list
list_all_phase = list()
list_dataset_key = list()
list_dataset_value = list()
list_user_name = list()
list_samephase_similarity = list()
list_crossphase_similarity = list()

def init():
	os.chdir(home_directory)
	with open("data_list.csv") as data_list_file:
		data_list_reader = csv.reader(data_list_file)
		for data in data_list_reader:
			list_dataset_key.append(data[0].strip())
			list_dataset_value.append(data[1].strip())
	for root, dirs, files in os.walk(data_directory):
		for directory in dirs:
			if directory == ".git":
				shutil.rmtree(os.path.join(root, directory))
		for file in files:
			if file.endswith('.zip'):
				subprocess.call(["unzip", '-o', os.path.join(root, file), '-d', root])
				os.remove(os.path.join(root, file))
	for directory in os.listdir(os.path.join(data_directory, hackname + "-phase1")):
		list_user_name.append(directory)
	#print(list_user_name)
def extract_dataset():
	for phase in range(1, phase_number + 1):
		# phase level: contain all in a phase
		phase_list = list()
		os.chdir(home_directory)
		os.chdir(os.path.join(data_directory, hackname + "-phase" + str(phase)))
		directory_list = []
		for directory in list_user_name:
			print(directory)
			# project level: contain all in a project
			project_list = list()
			for root, dirs, files in os.walk(directory):
				for file in files:
					if file.endswith(".csv"):
						project_list.append(get_MD5(os.path.join(root, file)))
					if file.endswith((".js", "html", "htm")):
						try:
							f = open(os.path.join(root, file), "r")
							file_content = f.read()
							for data in list_dataset_key:
								if file_content.find(data) > -1:
									project_list.append(data)
						except Exception:
							pass
						if f != None:
							f.close()
						
			phase_list.append(project_list)
			print(project_list)
		list_all_phase.append(phase_list)
		print("{}{}".format("extrect finished: phase", phase))

def similarity_calculation(list_a, list_b):
	common = [val for val in list_a if val in list_b]
	if (len(list_a) + len(list_b))  == 0:
		return 1
	return (len(common)/(len(list_a) + len(list_b) + len(common)))

def samephase_similarity():
	for phase in list_all_phase:
		# phase level list
		phase_list = list()
		for project in phase:
			# project level list
			project_list = list()
			for other_project in phase:
				project_list.append(similarity_calculation(project, other_project))
			phase_list.append(project_list)
			print(project_list)
		print(phase_list)
		list_samephase_similarity.append(phase_list)
		print("{}{}".format("finished same phase similarity", list_all_phase.index(phase)))

def crossphase_similarity():
	for phase in list_all_phase[0:-1]:
		# phase level list
		phase_list = list()
		for project in phase:
			# project level list
			project_list = list()
			for other_project in list_all_phase[list_all_phase.index(phase) + 1]:
				project_list.append(similarity_calculation(project, other_project))
			phase_list.append(project_list)
		list_crossphase_similarity.append(phase_list)
		print("{}{}".format("finished cross phase similarity", list_all_phase.index(phase)))

def output():
	# for the same phase
	os.chdir(home_directory)
	if os.path.exists(output_directory):
		shutil.rmtree(output_directory)
	os.mkdir(output_directory)
	os.chdir(output_directory)
	for phase in list_samephase_similarity:
		filename = hackname + "-phase" + str(list_samephase_similarity.index(phase) + 1) + "-samephase-data-similarity.csv"
		with open(filename, 'w') as fout:
			writer = csv.writer(fout, delimiter=',', quotechar='"')
			writer.writerow([""] + list_user_name)
			for user in list_user_name:
				writer.writerow([user] + phase[list_user_name.index(user)])

	for phase in list_crossphase_similarity:
		filename = hackname + "-phase" + str(list_crossphase_similarity.index(phase) + 1) + "-" + str(list_crossphase_similarity.index(phase) + 2) + "-crosshase-data-similarity.csv"
		with open(filename, 'w') as fout:
			writer = csv.writer(fout, delimiter=',', quotechar='"')
			writer.writerow([""] + list_user_name)
			for user in list_user_name:
				writer.writerow([user] + phase[list_user_name.index(user)])

def get_MD5(file):
	m = hashlib.md5()
	f = open(file, "rb")
	maxbuf = 8192

	while 1:
		buf = f.read(maxbuf)
		if not buf:
			break
		m.update(buf)
	f.close()
	return m.hexdigest()


if __name__ == '__main__':
	init()
	extract_dataset()
	#samephase_similarity()
	#crossphase_similarity()
	#output()
