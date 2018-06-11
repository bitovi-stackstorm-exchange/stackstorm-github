from lib.base import BaseGithubAction
from github import GithubObject
from lib.formatters import file_to_dict

__all__ = [
    'CreateFileAction'
]


class CreateFileAction(BaseGithubAction):
    def run(self, user, repo, path, message, content,
                    branch=github.GithubObject.NotSet,
                    committer=github.GithubObject.NotSet,
                    author=github.GithubObject.NotSet):

        user = self._client.get_user(user)
        repo = user.get_repo(repo)
        file = repo.create_file(path, message, content, branch, committer, author)
                    
        result = file.raw_data
        return result
