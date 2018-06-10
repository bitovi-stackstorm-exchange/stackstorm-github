from st2common.util import isotime

__all__ = [
    'repo_to_dict',
    'issue_to_dict',
    'label_to_dict',
    'user_to_dict'
]


def repo_to_dict(repo):
    return {
      "id": repo.get('github_type', None),
      "node_id": repo.get('github_type', None),
      "owner": user_to_dict(repo.get('github_type', None)),
      "name": repo.get('github_type', None),
      "full_name": repo.get('github_type', None),
      "description": repo.get('github_type', None),
      "private": repo.get('github_type', None),
      "fork": repo.get('github_type', None),
      "url": repo.get('github_type', None),
      "html_url": repo.get('github_type', None),
      "archive_url": repo.get('github_type', None),
      "assignees_url": repo.get('github_type', None),
      "blobs_url": repo.get('github_type', None),
      "branches_url": repo.get('github_type', None),
      "clone_url": repo.get('github_type', None),
      "collaborators_url": repo.get('github_type', None),
      "comments_url": repo.get('github_type', None),
      "commits_url": repo.get('github_type', None),
      "compare_url": repo.get('github_type', None),
      "contents_url": repo.get('github_type', None),
      "contributors_url": repo.get('github_type', None),
      "deployments_url": repo.get('github_type', None),
      "downloads_url": repo.get('github_type', None),
      "events_url": repo.get('github_type', None),
      "forks_url": repo.get('github_type', None),
      "git_commits_url": repo.get('github_type', None),
      "git_refs_url": repo.get('github_type', None),
      "git_tags_url": repo.get('github_type', None),
      "git_url": repo.get('github_type', None),
      "hooks_url": repo.get('github_type', None),
      "issue_comment_url": repo.get('github_type', None),
      "issue_events_url": repo.get('github_type', None),
      "issues_url": repo.get('github_type', None),
      "keys_url": repo.get('github_type', None),
      "labels_url": repo.get('github_type', None),
      "languages_url": repo.get('github_type', None),
      "merges_url": repo.get('github_type', None),
      "milestones_url": repo.get('github_type', None),
      "mirror_url": repo.get('github_type', None),
      "notifications_url": repo.get('github_type', None),
      "pulls_url": repo.get('github_type', None),
      "releases_url": repo.get('github_type', None),
      "ssh_url": repo.get('github_type', None),
      "stargazers_url": repo.get('github_type', None),
      "statuses_url": repo.get('github_type', None),
      "subscribers_url": repo.get('github_type', None),
      "subscription_url": repo.get('github_type', None),
      "svn_url": repo.get('github_type', None),
      "tags_url": repo.get('github_type', None),
      "teams_url": repo.get('github_type', None),
      "trees_url": repo.get('github_type', None),
      "homepage": repo.get('github_type', None),
      "language": repo.get('github_type', None),
      "forks_count": repo.get('github_type', None),
      "stargazers_count": repo.get('github_type', None),
      "watchers_count": repo.get('github_type', None),
      "size": repo.get('github_type', None),
      "default_branch": repo.get('github_type', None),
      "open_issues_count": repo.get('github_type', None),
      "topics": list(repo.get('github_type', None)),
      "has_issues": repo.get('github_type', None),
      "has_wiki": repo.get('github_type', None),
      "has_pages": repo.get('github_type', None),
      "has_downloads": repo.get('github_type', None),
      "archived": repo.get('github_type', None),
      "pushed_at": repo.get('github_type', None),
      "created_at": repo.get('github_type', None),
      "updated_at": repo.get('github_type', None),
      "permissions": repo.get('github_type', None),
      "allow_rebase_merge": repo.get('github_type', None),
      "allow_squash_merge": repo.get('github_type', None),
      "allow_merge_commit": repo.get('github_type', None),
      "subscribers_count": repo.get('github_type', None),
      "network_count": repo.get('github_type', None),
      "has_projects": repo.get('github_type', None)
    }


def issue_to_dict(issue):
    result = {}

    author = user_to_dict(issue.user)
    assignee = user_to_dict(issue.assignee)
    closed_by = user_to_dict(issue.closed_by)

    if issue.pull_request:
        is_pull_request = True
    else:
        is_pull_request = False

    result['id'] = issue.id
    result['repository'] = issue.repository.name
    result['author'] = author
    result['assign'] = assignee
    result['title'] = issue.title
    result['body'] = issue.body
    result['url'] = issue.html_url
    result['state'] = issue.state
    result['is_pull_request'] = is_pull_request

    if issue.labels:
        labels = [label_to_dict(label) for label in issue.labels]
    else:
        labels = []

    result['labels'] = labels

    # Note: We convert it to a serialize type (string)
    if issue.created_at:
        created_at = isotime.format(issue.created_at)
    else:
        created_at = None

    if issue.closed_at:
        closed_at = isotime.format(issue.closed_at)
    else:
        closed_at = None

    result['created_at'] = created_at
    result['closed_at'] = closed_at
    result['closed_by'] = closed_by
    return result


def label_to_dict(label):
    result = {}

    result['name'] = label.name
    result['color'] = label.color
    result['url'] = label.url

    return result


def user_to_dict(user):
    if not user:
        return None

    result = {}
    result['name'] = user.name
    result['login'] = user.login
    return result


def team_to_dict(team):
    if not team:
        return None

    result = {}
    result['id'] = team.id
    result['name'] = team.name
    result['members_count'] = team.members_count
    return result
