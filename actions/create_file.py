from lib.base import BaseGithubAction
from github import GithubObject

__all__ = [
    'CreateFileAction'
]


class CreateFileAction(BaseGithubAction):
    def run(self, user, repo, path, message, content,
                    branch=GithubObject.NotSet,
                    committer=GithubObject.NotSet,
                    author=GithubObject.NotSet):

      user = self._client.get_user(user)
      repo = user.get_repo(repo)
      file = repo.create_file(path, message, content, branch, committer, author)

      return file
