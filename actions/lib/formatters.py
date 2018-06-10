from st2common.util import isotime

__all__ = [
    'repo_to_dict',
    'issue_to_dict',
    'label_to_dict',
    'user_to_dict'
]


def repo_to_dict(repo):
    return {
      "id": repo.id,
      "node_id": repo.node_id,
      "owner": user_to_dict(repo.owner),
      "name": repo.name,
      "full_name": repo.full_name,
      "description": repo.description,
      "private": repo.private,
      "fork": repo.fork,
      "url": repo.url,
      "html_url": repo.html_url,
      "archive_url": repo.archive_url,
      "assignees_url": repo.assignees_url,
      "blobs_url": repo.blobs_url,
      "branches_url": repo.branches_url,
      "clone_url": repo.clone_url,
      "collaborators_url": repo.collaborators_url,
      "comments_url": repo.comments_url,
      "commits_url": repo.commits_url,
      "compare_url": repo.compare_url,
      "contents_url": repo.contents_url,
      "contributors_url": repo.contributors_url,
      "deployments_url": repo.deployments_url,
      "downloads_url": repo.downloads_url,
      "events_url": repo.events_url,
      "forks_url": repo.forks_url,
      "git_commits_url": repo.git_commits_url,
      "git_refs_url": repo.git_refs_url,
      "git_tags_url": repo.git_tags_url,
      "git_url": repo.git_url,
      "hooks_url": repo.hooks_url,
      "issue_comment_url": repo.issue_comment_url,
      "issue_events_url": repo.issue_events_url,
      "issues_url": repo.issues_url,
      "keys_url": repo.keys_url,
      "labels_url": repo.labels_url,
      "languages_url": repo.languages_url,
      "merges_url": repo.merges_url,
      "milestones_url": repo.milestones_url,
      "mirror_url": repo.mirror_url,
      "notifications_url": repo.notifications_url,
      "pulls_url": repo.pulls_url,
      "releases_url": repo.releases_url,
      "ssh_url": repo.ssh_url,
      "stargazers_url": repo.stargazers_url,
      "statuses_url": repo.statuses_url,
      "subscribers_url": repo.subscribers_url,
      "subscription_url": repo.subscription_url,
      "svn_url": repo.svn_url,
      "tags_url": repo.tags_url,
      "teams_url": repo.teams_url,
      "trees_url": repo.trees_url,
      "homepage": repo.homepage,
      "language": repo.language,
      "forks_count": repo.forks_count,
      "stargazers_count": repo.stargazers_count,
      "watchers_count": repo.watchers_count,
      "size": repo.size,
      "default_branch": repo.default_branch,
      "open_issues_count": repo.open_issues_count,
      "topics": list(repo.topics),
      "has_issues": repo.has_issues,
      "has_wiki": repo.has_wiki,
      "has_pages": repo.has_pages,
      "has_downloads": repo.has_downloads,
      "archived": repo.archived,
      "pushed_at": repo.pushed_at,
      "created_at": repo.created_at,
      "updated_at": repo.updated_at,
      "permissions": repo.permissions,
      "allow_rebase_merge": repo.allow_rebase_merge,
      "allow_squash_merge": repo.allow_squash_merge,
      "allow_merge_commit": repo.allow_merge_commit,
      "subscribers_count": repo.subscribers_count,
      "network_count": repo.network_count,
      "has_projects": repo.has_projects
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
