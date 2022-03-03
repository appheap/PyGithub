from dataclasses import dataclass
from typing import Optional, List

from .license import SimpleLicense
from .object import Object
from .repo_permissions import RepoPermissions
from .user import SimpleUser


@dataclass
class Repository(Object):
    """
    A git repository
    """

    id: int
    node_id: str
    name: str
    full_name: str
    license: SimpleLicense
    organization: Optional['SimpleUser']
    forks: int
    permissions: Optional['RepoPermissions']
    owner: SimpleUser
    private: bool
    html_url: str
    description: str
    fork: str
    url: str
    archive_url: str
    assignees_url: str
    blobs_urls: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    downloads_url: str
    events_url: str
    forks_url: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    notifications_url: str
    pulls_url: str
    releases_url: str
    ssh_url: str
    stargazers_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    clone_url: str
    mirror_url: str
    hooks_url: str
    svn_url: str
    homepage: str
    language: str
    forks_count: int
    stargazers_count: int
    statuses_url: str
    watchers_count: int
    size: int
    default_branch: str
    open_issues_count: int
    is_template: Optional['bool']
    topics: List['str']
    has_issues: bool
    has_projects: bool
    has_wiki: bool
    has_pages: bool
    has_downloads: bool
    archived: bool
    disabled: bool
    visibility: Optional['str']
    pushed_at: str
    created_at: str
    updated_at: str
    allow_rebase_merge: Optional['int']
    template_repository: Optional['int']
    temp_clone_token: Optional['int']
    allow_squash_merge: Optional['int']
    allow_auto_merge: Optional['int']
    delete_branch_on_merge: Optional['int']
    allow_merge_commit: Optional['int']
    allow_forking: Optional['bool']
    subscribers_count: Optional['int']
    network_count: Optional['int']
    open_issues: int
    watchers: int
    master_branch: Optional['int']
    starred_at: Optional['int']

    @staticmethod
    def _parse(repo: dict) -> Optional['Repository']:
        if repo is None or not len(repo):
            return None

        return Repository(
            id=repo.get('id'),
            node_id=repo.get('node_id'),
            name=repo.get('name'),
            full_name=repo.get('full_name'),
            license=SimpleLicense._parse(repo.get('license')),
            organization=SimpleUser._parse(repo.get('organization', None)),
            forks=repo.get('forks'),
            permissions=RepoPermissions._parse(repo.get('permissions', None)),
            owner=SimpleUser._parse(repo.get('owner')),
            private=repo.get('private'),
            html_url=repo.get('html_url'),
            description=repo.get('description'),
            fork=repo.get('fork'),
            url=repo.get('url'),
            archive_url=repo.get('archive_url'),
            assignees_url=repo.get('assignees_url'),
            blobs_urls=repo.get('blobs_urls'),
            branches_url=repo.get('branches_url'),
            collaborators_url=repo.get('collaborators_url'),
            comments_url=repo.get('comments_url'),
            commits_url=repo.get('commits_url'),
            compare_url=repo.get('compare_url'),
            contents_url=repo.get('contents_url'),
            contributors_url=repo.get('contributors_url'),
            deployments_url=repo.get('deployments_url'),
            downloads_url=repo.get('downloads_url'),
            events_url=repo.get('events_url'),
            forks_url=repo.get('forks_url'),
            git_commits_url=repo.get('git_commits_url'),
            git_refs_url=repo.get('git_refs_url'),
            git_tags_url=repo.get('git_tags_url'),
            git_url=repo.get('git_url'),
            issue_comment_url=repo.get('issue_comment_url'),
            issue_events_url=repo.get('issue_events_url'),
            issues_url=repo.get('issues_url'),
            keys_url=repo.get('keys_url'),
            labels_url=repo.get('labels_url'),
            languages_url=repo.get('languages_url'),
            merges_url=repo.get('merges_url'),
            milestones_url=repo.get('milestones_url'),
            notifications_url=repo.get('notifications_url'),
            pulls_url=repo.get('pulls_url'),
            releases_url=repo.get('releases_url'),
            ssh_url=repo.get('ssh_url'),
            stargazers_url=repo.get('stargazers_url'),
            subscribers_url=repo.get('subscribers_url'),
            subscription_url=repo.get('subscription_url'),
            tags_url=repo.get('tags_url'),
            teams_url=repo.get('teams_url'),
            trees_url=repo.get('trees_url'),
            clone_url=repo.get('clone_url'),
            mirror_url=repo.get('mirror_url'),
            hooks_url=repo.get('hooks_url'),
            svn_url=repo.get('svn_url'),
            homepage=repo.get('homepage'),
            language=repo.get('language'),
            forks_count=repo.get('forks_count'),
            stargazers_count=repo.get('stargazers_count'),
            statuses_url=repo.get('statuses_url'),
            watchers_count=repo.get('watchers_count'),
            size=repo.get('size'),
            default_branch=repo.get('default_branch'),
            open_issues_count=repo.get('open_issues_count'),
            is_template=repo.get('is_template', None),
            topics=repo.get('topics'),
            has_issues=repo.get('has_issues'),
            has_projects=repo.get('has_projects'),
            has_wiki=repo.get('has_wiki'),
            has_pages=repo.get('has_pages'),
            has_downloads=repo.get('has_downloads'),
            archived=repo.get('archived'),
            disabled=repo.get('disabled'),
            visibility=repo.get('visibility', None),
            pushed_at=repo.get('pushed_at'),
            created_at=repo.get('created_at'),
            updated_at=repo.get('updated_at'),
            allow_rebase_merge=repo.get('allow_rebase_merge', None),
            template_repository=repo.get('template_repository', None),
            temp_clone_token=repo.get('temp_clone_token', None),
            allow_squash_merge=repo.get('allow_squash_merge', None),
            allow_auto_merge=repo.get('allow_auto_merge', None),
            delete_branch_on_merge=repo.get('delete_branch_on_merge', None),
            allow_merge_commit=repo.get('allow_merge_commit', None),
            allow_forking=repo.get('allow_forking', None),
            subscribers_count=repo.get('subscribers_count', None),
            network_count=repo.get('network_count', None),
            open_issues=repo.get('open_issues'),
            watchers=repo.get('watchers'),
            master_branch=repo.get('master_branch', None),
            starred_at=repo.get('starred_at', None),
        )
