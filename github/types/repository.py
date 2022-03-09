from dataclasses import dataclass
from typing import Optional, List

from .license import SimpleLicense
from .object import Object
from .repo_permissions import RepoPermissions
from .user import SimpleUser


@dataclass
class CodeOfConduct(Object):
    url: str
    key: str
    name: str
    html_url: str

    @staticmethod
    def _parse(obj: dict) -> Optional['CodeOfConduct']:
        if obj is None or not len(obj):
            return None

        return CodeOfConduct(
            url=obj.get('url', None),
            key=obj.get('key', None),
            name=obj.get('name', None),
            html_url=obj.get('html_url', None),
        )


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
    topics: Optional[List['str']]
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
    allow_rebase_merge: Optional['bool']
    template_repository: Optional['Repository']
    temp_clone_token: Optional['str']
    allow_squash_merge: Optional['bool']
    allow_auto_merge: Optional['bool']
    delete_branch_on_merge: Optional['bool']
    allow_merge_commit: Optional['bool']
    allow_forking: Optional['bool']
    subscribers_count: Optional['int']
    network_count: Optional['int']
    open_issues: int
    watchers: int
    master_branch: Optional['str']
    starred_at: Optional['str']

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
            topics=repo.get('topics', None),
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


@dataclass
class FullRepository(Object):
    """
    Full Repository
    """

    id: int
    node_id: str
    name: str
    full_name: str
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
    statuses_url: str
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
    watchers_count: int
    size: int
    default_branch: str
    open_issues_count: int
    is_template: Optional['bool']
    topics: Optional[List['str']]
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
    permissions: Optional['RepoPermissions']
    allow_rebase_merge: Optional['bool']
    template_repository: Optional['Repository']
    temp_clone_token: Optional['str']
    allow_squash_merge: Optional['bool']
    allow_auto_merge: Optional['bool']
    delete_branch_on_merge: Optional['bool']
    allow_merge_commit: Optional['bool']
    allow_forking: Optional['bool']
    subscribers_count: Optional['int']
    network_count: Optional['int']
    license: Optional['SimpleLicense']
    organization: Optional['SimpleUser']
    parent: Optional['Repository']
    source: Optional['Repository']
    forks: int
    master_branch: Optional['str']
    open_issues: int
    watchers: int
    anonymous_access_enabled: Optional['bool']
    code_of_conduct: Optional['CodeOfConduct']
    security_and_analysis: Optional['SecurityAndAnalysis']

    @staticmethod
    def _parse(repo: dict) -> Optional['FullRepository']:
        if repo is None or not len(repo):
            return None

        return FullRepository(
            id=repo.get('id', None),
            node_id=repo.get('node_id', None),
            name=repo.get('name', None),
            full_name=repo.get('full_name', None),
            owner=SimpleUser._parse(repo.get('owner', None)),
            private=repo.get('private', None),
            html_url=repo.get('html_url', None),
            description=repo.get('description', None),
            fork=repo.get('fork', None),
            url=repo.get('url', None),
            archive_url=repo.get('archive_url', None),
            assignees_url=repo.get('assignees_url', None),
            blobs_urls=repo.get('blobs_urls', None),
            branches_url=repo.get('branches_url', None),
            collaborators_url=repo.get('collaborators_url', None),
            comments_url=repo.get('comments_url', None),
            commits_url=repo.get('commits_url', None),
            compare_url=repo.get('compare_url', None),
            contents_url=repo.get('contents_url', None),
            contributors_url=repo.get('contributors_url', None),
            deployments_url=repo.get('deployments_url', None),
            downloads_url=repo.get('downloads_url', None),
            events_url=repo.get('events_url', None),
            forks_url=repo.get('forks_url', None),
            git_commits_url=repo.get('git_commits_url', None),
            git_refs_url=repo.get('git_refs_url', None),
            git_tags_url=repo.get('git_tags_url', None),
            git_url=repo.get('git_url', None),
            issue_comment_url=repo.get('issue_comment_url', None),
            issue_events_url=repo.get('issue_events_url', None),
            issues_url=repo.get('issues_url', None),
            keys_url=repo.get('keys_url', None),
            labels_url=repo.get('labels_url', None),
            languages_url=repo.get('languages_url', None),
            merges_url=repo.get('merges_url', None),
            milestones_url=repo.get('milestones_url', None),
            notifications_url=repo.get('notifications_url', None),
            pulls_url=repo.get('pulls_url', None),
            releases_url=repo.get('releases_url', None),
            ssh_url=repo.get('ssh_url', None),
            stargazers_url=repo.get('stargazers_url', None),
            statuses_url=repo.get('statuses_url', None),
            subscribers_url=repo.get('subscribers_url', None),
            subscription_url=repo.get('subscription_url', None),
            tags_url=repo.get('tags_url', None),
            teams_url=repo.get('teams_url', None),
            trees_url=repo.get('trees_url', None),
            clone_url=repo.get('clone_url', None),
            mirror_url=repo.get('mirror_url', None),
            hooks_url=repo.get('hooks_url', None),
            svn_url=repo.get('svn_url', None),
            homepage=repo.get('homepage', None),
            language=repo.get('language', None),
            forks_count=repo.get('forks_count', None),
            stargazers_count=repo.get('stargazers_count', None),
            watchers_count=repo.get('watchers_count', None),
            size=repo.get('size', None),
            default_branch=repo.get('default_branch', None),
            open_issues_count=repo.get('open_issues_count', None),
            is_template=repo.get('is_template', None),
            topics=repo.get('topics', None),
            has_issues=repo.get('has_issues', None),
            has_projects=repo.get('has_projects', None),
            has_wiki=repo.get('has_wiki', None),
            has_pages=repo.get('has_pages', None),
            has_downloads=repo.get('has_downloads', None),
            archived=repo.get('archived', None),
            disabled=repo.get('disabled', None),
            visibility=repo.get('visibility', None),
            pushed_at=repo.get('pushed_at', None),
            created_at=repo.get('created_at', None),
            updated_at=repo.get('updated_at', None),
            permissions=RepoPermissions._parse(repo.get('permissions', None)),
            allow_rebase_merge=repo.get('allow_rebase_merge', None),
            template_repository=Repository._parse(repo.get('template_repository', None)),
            temp_clone_token=repo.get('temp_clone_token', None),
            allow_squash_merge=repo.get('allow_squash_merge', None),
            allow_auto_merge=repo.get('allow_auto_merge', None),
            delete_branch_on_merge=repo.get('delete_branch_on_merge', None),
            allow_merge_commit=repo.get('allow_merge_commit', None),
            allow_forking=repo.get('allow_forking', None),
            subscribers_count=repo.get('subscribers_count', None),
            network_count=repo.get('network_count', None),
            license=SimpleLicense._parse(repo.get('license', None)),
            organization=SimpleUser._parse(repo.get('organization', None)),
            parent=Repository._parse(repo.get('parent', None)),
            source=Repository._parse(repo.get('source', None)),
            forks=repo.get('forks', None),
            master_branch=repo.get('master_branch', None),
            open_issues=repo.get('open_issues', None),
            watchers=repo.get('watchers', None),
            anonymous_access_enabled=repo.get('anonymous_access_enabled', None),
            code_of_conduct=CodeOfConduct._parse(repo.get('code_of_conduct', None)),
            security_and_analysis=SecurityAndAnalysis._parse(repo.get('security_and_analysis', None)),
        )


@dataclass
class MinimalRepository(Object):
    id: int
    node_id: str
    name: str
    full_name: str
    owner: 'SimpleUser'
    private: bool
    html_url: str
    description: str
    fork: bool
    url: str
    archive_url: str
    assignees_url: str
    blobs_url: str
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
    git_url: Optional['str']
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
    ssh_url: Optional['str']
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    clone_url: Optional['str']
    mirror_url: Optional['str']
    hooks_url: str
    svn_url: Optional['str']
    homepage: Optional['str']
    language: Optional['str']
    forks_count: Optional['int']
    stargazers_count: int
    watchers_count: Optional['int']
    size: Optional['int']
    default_branch: Optional['str']
    open_issues_count: Optional['int']
    is_template: Optional['bool']
    topics: List['str']
    has_issues: Optional['bool']
    has_projects: Optional['bool']
    has_wiki: Optional['bool']
    has_pages: Optional['bool']
    has_downloads: Optional['bool']
    archived: Optional['bool']
    disabled: Optional['bool']
    visibility: Optional['str']
    pushed_at: Optional['str']
    created_at: Optional['str']
    updated_at: Optional['str']
    permissions: Optional['RepoPermissions']
    role_name: Optional['str']
    template_repository: Optional['Repository']
    temp_clone_token: Optional['str']
    delete_branch_on_merge: bool
    subscribers_count: Optional['int']
    network_count: Optional['int']
    code_of_conduct: Optional['CodeOfConduct']
    license: Optional['SimpleLicense']
    forks: Optional['int']
    open_issues: Optional['int']
    watchers: Optional['int']
    allow_forking: Optional['bool']

    @staticmethod
    def _parse(obj: dict) -> Optional['MinimalRepository']:
        if obj is None or not len(obj):
            return None

        return MinimalRepository(
            id=obj.get('id', None),
            node_id=obj.get('node_id', None),
            name=obj.get('name', None),
            full_name=obj.get('full_name', None),
            owner=SimpleUser._parse(obj.get('owner', None)),
            private=obj.get('private', None),
            html_url=obj.get('html_url', None),
            description=obj.get('description', None),
            fork=obj.get('fork', None),
            url=obj.get('url', None),
            archive_url=obj.get('archive_url', None),
            assignees_url=obj.get('assignees_url', None),
            blobs_url=obj.get('blobs_url', None),
            branches_url=obj.get('branches_url', None),
            collaborators_url=obj.get('collaborators_url', None),
            comments_url=obj.get('comments_url', None),
            commits_url=obj.get('commits_url', None),
            compare_url=obj.get('compare_url', None),
            contents_url=obj.get('contents_url', None),
            contributors_url=obj.get('contributors_url', None),
            deployments_url=obj.get('deployments_url', None),
            downloads_url=obj.get('downloads_url', None),
            events_url=obj.get('events_url', None),
            forks_url=obj.get('forks_url', None),
            git_commits_url=obj.get('git_commits_url', None),
            git_refs_url=obj.get('git_refs_url', None),
            git_tags_url=obj.get('git_tags_url', None),
            git_url=obj.get('git_url', None),
            issue_comment_url=obj.get('issue_comment_url', None),
            issue_events_url=obj.get('issue_events_url', None),
            issues_url=obj.get('issues_url', None),
            keys_url=obj.get('keys_url', None),
            labels_url=obj.get('labels_url', None),
            languages_url=obj.get('languages_url', None),
            merges_url=obj.get('merges_url', None),
            milestones_url=obj.get('milestones_url', None),
            notifications_url=obj.get('notifications_url', None),
            pulls_url=obj.get('pulls_url', None),
            releases_url=obj.get('releases_url', None),
            ssh_url=obj.get('ssh_url', None),
            stargazers_url=obj.get('stargazers_url', None),
            statuses_url=obj.get('statuses_url', None),
            subscribers_url=obj.get('subscribers_url', None),
            subscription_url=obj.get('subscription_url', None),
            tags_url=obj.get('tags_url', None),
            teams_url=obj.get('teams_url', None),
            trees_url=obj.get('trees_url', None),
            clone_url=obj.get('clone_url', None),
            mirror_url=obj.get('mirror_url', None),
            hooks_url=obj.get('hooks_url', None),
            svn_url=obj.get('svn_url', None),
            homepage=obj.get('homepage', None),
            language=obj.get('language', None),
            forks_count=obj.get('forks_count', None),
            stargazers_count=obj.get('stargazers_count', None),
            watchers_count=obj.get('watchers_count', None),
            size=obj.get('size', None),
            default_branch=obj.get('default_branch', None),
            open_issues_count=obj.get('open_issues_count', None),
            is_template=obj.get('is_template', None),
            topics=obj.get('topics', None),
            has_issues=obj.get('has_issues', None),
            has_projects=obj.get('has_projects', None),
            has_wiki=obj.get('has_wiki', None),
            has_pages=obj.get('has_pages', None),
            has_downloads=obj.get('has_downloads', None),
            archived=obj.get('archived', None),
            disabled=obj.get('disabled', None),
            visibility=obj.get('visibility', None),
            pushed_at=obj.get('pushed_at', None),
            created_at=obj.get('created_at', None),
            updated_at=obj.get('updated_at', None),
            permissions=RepoPermissions._parse(obj.get('permissions', None)),
            role_name=obj.get('role_name', None),
            template_repository=Repository._parse(obj.get('template_repository', None)),
            temp_clone_token=obj.get('temp_clone_token', None),
            delete_branch_on_merge=obj.get('delete_branch_on_merge', None),
            subscribers_count=obj.get('subscribers_count', None),
            network_count=obj.get('network_count', None),
            code_of_conduct=CodeOfConduct._parse(obj.get('code_of_conduct', None)),
            license=SimpleLicense._parse(obj.get('license', None)),
            forks=obj.get('forks', None),
            open_issues=obj.get('open_issues', None),
            watchers=obj.get('watchers', None),
            allow_forking=obj.get('allow_forking', None),
        )


@dataclass
class Repo(Object):
    id: int
    name: str
    url: str

    @staticmethod
    def _parse(obj: dict) -> Optional['Repo']:
        if obj is None or not len(obj):
            return None

        return Repo(
            id=obj.get('id', None),
            name=obj.get('name', None),
            url=obj.get('url', None),
        )


@dataclass
class SecurityAndAnalysis(Object):
    advanced_security: Optional['AdvancedSecurity']
    secret_scanning: Optional['SecretScanning']

    @staticmethod
    def _parse(obj: dict) -> Optional['SecurityAndAnalysis']:
        if obj is None or not len(obj):
            return None

        return SecurityAndAnalysis(
            advanced_security=AdvancedSecurity._parse(obj.get('advanced_security', None)),
            secret_scanning=SecretScanning._parse(obj.get('secret_scanning', None)),
        )


@dataclass
class AdvancedSecurity(Object):
    enabled: bool

    @staticmethod
    def _parse(obj: dict) -> Optional['AdvancedSecurity']:
        if obj is None or not len(obj):
            return None
        return AdvancedSecurity(
            enabled=True if obj.get('status', None) == 'enabled' else False,
        )


@dataclass
class SecretScanning(Object):
    enabled: bool

    @staticmethod
    def _parse(obj: dict) -> Optional['SecretScanning']:
        if obj is None or not len(obj):
            return None
        return SecretScanning(
            enabled=True if obj.get('status', None) == 'enabled' else False,
        )


@dataclass
class RepositorySubscription(Object):
    """
    Repository invitations let you manage who you collaborate with.
    """
    subscribed: Optional['bool']
    ignored: Optional['bool']
    reason: Optional['str']
    created_at: Optional['str']
    url: Optional['str']
    repository_url: Optional['str']

    @staticmethod
    def _parse(obj: dict) -> Optional['RepositorySubscription']:
        if obj is None or not len(obj):
            return None

        return RepositorySubscription(
            subscribed=obj.get('subscribed', None),
            ignored=obj.get('ignored', None),
            reason=obj.get('reason', None),
            created_at=obj.get('created_at', None),
            url=obj.get('url', None),
            repository_url=obj.get('repository_url', None),
        )
