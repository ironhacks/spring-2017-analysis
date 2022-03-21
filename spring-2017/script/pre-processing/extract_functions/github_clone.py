import os
import re
import shutil
import subprocess
from github import Github


class GithubCloner:

    def __init__(self, access_token, repo_name_prefix):
        # Initialize using an access token
        self.access_token = access_token
        self.gh = Github(access_token)
        self.repo_name_prefix = repo_name_prefix
        self.phase_re = 'phase\d+'
        url_re = '{}-\S+_{}'.format(self.repo_name_prefix, self.phase_re)
        self.repo_urlpattern = re.compile(url_re)
        self.phase_pattern = re.compile(self.phase_re)

    def get_repos_for_org_and_repo_name(self, organization_name):
        org = self.gh.get_organization(organization_name)
        repo_clone_urls = []
        #i = 0
        for repo in org.get_repos():
            # e.g. IH-Project-2017-Fastlaw_webapp_phase5
            if self.repo_urlpattern.match(repo.name):
                repo_clone_urls.append(repo)
                #i += 1
                #if i > 3:
                #    break
        return repo_clone_urls

    def clone_repo(self, repo, repo_dir):
        domain = 'github.com'
        domain_with_token = '{}@{}'.format(self.access_token, domain)
        repo_url_with_token = repo.clone_url.replace(domain, domain_with_token)
        phase_name = self.phase_pattern.search(repo.clone_url)[0]
        phase_dir = '{}-{}'.format(self.repo_name_prefix, phase_name)
        clone_dir = os.path.join(repo_dir, phase_dir, repo.name)
        args = [
            "git",
            "clone",
            repo_url_with_token,
            clone_dir,
        ]
        subprocess.check_call(args)

    def clone_repos(self, repos, repo_dir):
        i = 0
        for repo in repos:
            self.clone_repo(repo, repo_dir)
