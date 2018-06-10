from st2common.util import isotime

__all__ = [
    'repo_to_dict',
    'issue_to_dict',
    'label_to_dict',
    'user_to_dict'
]


def repo_to_dict(repo):
    return {
      "id": repo.get('id', None),
      "node_id": repo.get('node_id', None),
      "owner": user_to_dict(repo.get('owner', None)),
      "name": repo.get('name', None),
      "full_name": repo.get('full_name', None),
      "description": repo.get('description', None),
      "private": repo.get('private', None),
      "fork": repo.get('fork', None),
      "url": repo.get('url', None),
      "html_url": repo.get('html_url', None),
      "archive_url": repo.get('archive_url', None),
      "assignees_url": repo.get('assignees_url', None),
      "blobs_url": repo.get('blobs_url', None),
      "branches_url": repo.get('branches_url', None),
      "clone_url": repo.get('clone_url', None),
      "collaborators_url": repo.get('collaborators_url', None),
      "comments_url": repo.get('comments_url', None),
      "commits_url": repo.get('commits_url', None),
      "compare_url": repo.get('compare_url', None),
      "contents_url": repo.get('contents_url', None),
      "contributors_url": repo.get('contributors_url', None),
      "deployments_url": repo.get('deployments_url', None),
      "downloads_url": repo.get('downloads_url', None),
      "events_url": repo.get('events_url', None),
      "forks_url": repo.get('forks_url', None),
      "git_commits_url": repo.get('git_commits_url', None),
      "git_refs_url": repo.get('git_refs_url', None),
      "git_tags_url": repo.get('git_tags_url', None),
      "git_url": repo.get('git_url', None),
      "hooks_url": repo.get('hooks_url', None),
      "issue_comment_url": repo.get('issue_comment_url', None),
      "issue_events_url": repo.get('issue_events_url', None),
      "issues_url": repo.get('issues_url', None),
      "keys_url": repo.get('keys_url', None),
      "labels_url": repo.get('labels_url', None),
      "languages_url": repo.get('languages_url', None),
      "merges_url": repo.get('merges_url', None),
      "milestones_url": repo.get('milestones_url', None),
      "mirror_url": repo.get('mirror_url', None),
      "notifications_url": repo.get('notifications_url', None),
      "pulls_url": repo.get('pulls_url', None),
      "releases_url": repo.get('releases_url', None),
      "ssh_url": repo.get('ssh_url', None),
      "stargazers_url": repo.get('stargazers_url', None),
      "statuses_url": repo.get('statuses_url', None),
      "subscribers_url": repo.get('subscribers_url', None),
      "subscription_url": repo.get('subscription_url', None),
      "svn_url": repo.get('svn_url', None),
      "tags_url": repo.get('tags_url', None),
      "teams_url": repo.get('teams_url', None),
      "trees_url": repo.get('trees_url', None),
      "homepage": repo.get('homepage', None),
      "language": repo.get('language', None),
      "forks_count": repo.get('forks_count', None),
      "stargazers_count": repo.get('stargazers_count', None),
      "watchers_count": repo.get('watchers_count', None),
      "size": repo.get('size', None),
      "default_branch": repo.get('default_branch', None),
      "open_issues_count": repo.get('open_issues_count', None),
      "topics": list(repo.get('topics', None)),
      "has_issues": repo.get('has_issues', None),
      "has_wiki": repo.get('has_wiki', None),
      "has_pages": repo.get('has_pages', None),
      "has_downloads": repo.get('has_downloads', None),
      "archived": repo.get('archived', None),
      "pushed_at": repo.get('pushed_at', None),
      "created_at": repo.get('created_at', None),
      "updated_at": repo.get('updated_at', None),
      "permissions": repo.get('permissions', None),
      "allow_rebase_merge": repo.get('allow_rebase_merge', None),
      "allow_squash_merge": repo.get('allow_squash_merge', None),
      "allow_merge_commit": repo.get('allow_merge_commit', None),
      "subscribers_count": repo.get('subscribers_count', None),
      "network_count": repo.get('network_count', None),
      "has_projects": repo.get('has_projects', None)
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
