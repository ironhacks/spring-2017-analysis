import os
import config
from bs4 import BeautifulSoup
import csv

class LibraryExtractor(object):
        def __init__(self):
                self.libraries = set()

        def getLibraryList(self, config):
                self.config = config
                curDir = os.getcwd()
                
                os.chdir(self.config.PHASE_DIRECTORY)
                #print("phase directory: " +self.config.PHASE_DIRECTORY)
                #path = os.getcwd()+'-output'
                #os.mkdir(path)
                for direct in os.listdir(os.getcwd()):
                        print(direct)
                        if os.path.isdir(direct):
                                studentname = direct.rsplit('-',1)[1]
                                print("Student name: "+studentname)
                                filep = os.path.join(direct, studentname+".csv" )
                                scriptfile = open(filep,"w")
                                for content in os.listdir(direct):
                                        print(content)
                                        if not os.path.isdir(content) and \
                                        (content.endswith(".html") or content.endswith(".htm")):
                                                filePath = os.path.join(direct, content)
                                                print(filePath)
                                                soup = BeautifulSoup(open(filePath,encoding="utf8",errors='ignore'), "html.parser")
                                                for scriptTag in soup.find_all('script'):
                                                        src = scriptTag.get('src')
                                                        print(src)
                                                        if src is not None and src != '':
                                                                self.libraries = self.libraries | {src, }
                                                                scriptfile.write(src+"\n")
                                scriptfile.close()
                os.chdir(curDir)

        def writeLibraryList(self, config):
                self.config = config
                with open(os.path.join(self.config.REPORTS_FOLDER, \
                        'libraries-list.csv'), 'w') as fout:
                        for library in self.libraries:
                                fout.write(library + '\n')
