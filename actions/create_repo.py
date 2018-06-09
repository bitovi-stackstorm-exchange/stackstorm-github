from lib.base import BaseGithubAction
from github import GithubObject
from lib.formatters import issue_to_dict

__all__ = [
    'CreateRepoAction'
]


"""
:calls: `POST /user/repos <http://developer.github.com/v3/repos>`_
:param name: string
:param description: string
:param homepage: string
:param private: bool
:param has_issues: bool
:param has_wiki: bool
:param has_downloads: bool
:param has_projects: bool
:param auto_init: bool
:param license_template: string
:param gitignore_template: string
:param allow_squash_merge: bool
:param allow_merge_commit: bool
:param allow_rebase_merge: bool
:rtype: :class:`github.Repository.Repository`
"""
class CreateRepoAction(BaseGithubAction):
    def run(self, user, repo, homepage, description):
        user = self._client.get_user(user)
        repo = user.get_repo(repo)

        if repo:
          return (False, "Repo " + repo + " already exists")

        repo = user.create_repo(repo, 
          description=description or GithubObject.NotSet, 
          homepage=homepage or GithubObject.NotSet,
          private=False
          # has_issues=github.GithubObject.NotSet,
          # has_wiki=github.GithubObject.NotSet, 
          # has_downloads=github.GithubObject.NotSet,
          # has_projects=github.GithubObject.NotSet, 
          # auto_init=github.GithubObject.NotSet, 
          # license_template=github.GithubObject.NotSet,
          # gitignore_template=github.GithubObject.NotSet, 
          # allow_squash_merge=github.GithubObject.NotSet,
          # allow_merge_commit=github.GithubObject.NotSet, 
          # allow_rebase_merge=github.GithubObject.NotSet
          )


        
        result = issue_to_dict(issue=repo)
        return result
