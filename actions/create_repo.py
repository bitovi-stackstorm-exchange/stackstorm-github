from lib.base import BaseGithubAction
from github import GithubObject, GithubException
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
      repo_instance = None

      try:
        user.get_repo(repo)
      except GithubException as e:
        repo_instance = user.create_repo(repo, 
          description=description or GithubObject.NotSet, 
          homepage=homepage or GithubObject.NotSet,
          private=False,
          has_issues=GithubObject.NotSet,
          has_wiki=GithubObject.NotSet, 
          has_downloads=GithubObject.NotSet,
          has_projects=GithubObject.NotSet, 
          auto_init=GithubObject.NotSet, 
          license_template=GithubObject.NotSet,
          gitignore_template=GithubObject.NotSet, 
          allow_squash_merge=GithubObject.NotSet,
          allow_merge_commit=GithubObject.NotSet, 
          allow_rebase_merge=GithubObject.NotSet
          )
      else:
        return (False, "Repo " + repo + " already exists")

      result = vars(repo_instance)
      return result
