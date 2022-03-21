import os
import shutil
import subprocess

import extract_functions_javascript
from github_clone import GithubCloner


class main(object):
    def __init__(self, organization_name, repo_name_prefix, hack, number_phase, input_folder, output):
        self.organization_name = organization_name
        self.repo_name_prefix = repo_name_prefix
        self.hack_name = '{}-{}'.format(hack, organization_name)
        self.number_phase = number_phase
        self.home_dir = os.getcwd()
        self.input_folder = input_folder
        self.output = output
        self.access_token = os.environ.get('GITHUB_ACCESS_TOKEN')
        if not self.access_token:
            raise Exception("You must get an access token from github and set it on the command line, e.g.:\nexport GITHUB_ACCESS_TOKEN=<token_from_github>")

    def git_clone(self):
        input_dir = os.path.join(os.getcwd(), self.input_folder)
        shutil.rmtree(input_dir, ignore_errors=True)
        os.mkdir(input_dir)

        gc = GithubCloner(self.access_token, self.repo_name_prefix)
        repos = gc.get_repos_for_org_and_repo_name(self.organization_name)
        gc.clone_repos(repos, self.input_folder)

    def extract_functions(self):
        # calculateSamePhaseSimilarity
        # self.similarity.writeMatrixToFile(similarityDict, self.cfg.REPORTS_FOLDER,
        #        filePrefix, i)
        # i is phase
        for phase in range(1, self.number_phase + 1):
            fe = extract_functions_javascript.extract_functions_javascript(self.hack_name, phase, self.input_folder, self.output)
            fe.read_file('{}-phase{}'.format(self.hack_name, phase))
            fe.extract()
            fe.output_to_file()
            os.chdir(self.home_dir)


if __name__ == '__main__':
    input_folder = 'data'
    organization_name = 'goldironhack'
    repo_name_prefix = 'IH-Project-2017'
    hack = 'spring2017'

    m = main(organization_name, repo_name_prefix, hack, 5, input_folder, 'output')

    # Clone repositories from GitHub
    m.git_clone()  # You can comment out this line once you've cloned, for speed

    m.extract_functions()
