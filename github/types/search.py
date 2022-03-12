from dataclasses import dataclass
from typing import Optional, List

from .license import SimpleLicense
from .object import Object
from .repo_permissions import RepoPermissions
from .repository import MinimalRepository
from .user import SimpleUser


@dataclass
class SearchCodeResult(Object):
    total_count: Optional['int']
    incomplete_results: Optional['bool']
    items: Optional[List['CodeSearchResultItem']]

    @staticmethod
    def _parse(obj: dict) -> Optional['SearchCodeResult']:
        if obj is None or not len(obj):
            return None

        return SearchCodeResult(
            total_count=obj.get('total_count', None),
            incomplete_results=obj.get('incomplete_results', None),
            items=CodeSearchResultItem._parse_list(obj.get('items', None)),
        )


@dataclass
class CodeSearchResultItem(Object):
    """
    Code Search Result Item
    """
    name: Optional['str']
    path: Optional['str']
    sha: Optional['str']
    url: Optional['str']
    git_utl: Optional['str']
    html_url: Optional['str']
    repository: Optional['MinimalRepository']
    score: Optional['float']
    file_size: Optional['int']
    language: Optional['str']
    last_modified_at: Optional['str']
    line_numbers: Optional[List['str']]
    text_matches: Optional['SearchResultTextMatch']

    @staticmethod
    def _parse(obj: dict) -> Optional['CodeSearchResultItem']:
        if obj is None or not len(obj):
            return None

        return CodeSearchResultItem(
            name=obj.get('name', None),
            path=obj.get('path', None),
            sha=obj.get('sha', None),
            url=obj.get('url', None),
            git_utl=obj.get('git_utl', None),
            html_url=obj.get('html_url', None),
            repository=MinimalRepository._parse(obj.get('repository', None)),
            score=obj.get('score', None),
            file_size=obj.get('file_size', None),
            language=obj.get('language', None),
            last_modified_at=obj.get('last_modified_at', None),
            line_numbers=obj.get('line_numbers', None),
            text_matches=SearchResultTextMatch._parse(obj.get('text_matches', None)),
        )

    @staticmethod
    def _parse_list(result_items: list) -> Optional[List['CodeSearchResultItem']]:
        if type(result_items) != list:
            return []

        results: List['CodeSearchResultItem'] = []
        for result_dict in result_items:
            result = CodeSearchResultItem._parse(result_dict)
            if result_dict is not None and len(result_dict):
                results.append(result)
        return results


@dataclass
class SearchResultTextMatch(Object):
    """
    Search Result Text Match
    """
    object_url: Optional['str']
    object_type: Optional['str']
    property: Optional['str']
    fragment: Optional['str']
    matches: Optional[List['Match']]

    @staticmethod
    def _parse(obj: dict) -> Optional['SearchResultTextMatch']:
        if obj is None or not len(obj):
            return None

        return SearchResultTextMatch(
            object_url=obj.get('object_url', None),
            object_type=obj.get('object_type', None),
            property=obj.get('property', None),
            fragment=obj.get('fragment', None),
            matches=Match._parse_list(obj.get('matches', None)),
        )


@dataclass
class Match(Object):
    text: Optional['str']
    indices: Optional[List['int']]

    @staticmethod
    def _parse(obj: dict) -> Optional['Match']:
        if obj is None or not len(obj):
            return None

        return Match(
            text=obj.get('text', None),
            indices=obj.get('indices', None),
        )

    @staticmethod
    def _parse_list(matches_list: list) -> Optional[List['Match']]:
        if type(matches_list) != list:
            return []

        matches: List['Match'] = []
        for match_dict in matches_list:
            match = Match._parse(match_dict)
            if match_dict is not None and len(match_dict):
                matches.append(match)
        return matches


######################################################################################

@dataclass
class SearchRepositoriesResult(Object):
    total_count: Optional['int']
    incomplete_results: Optional['bool']
    items: Optional[List['RepoSearchResultItem']]

    @staticmethod
    def _parse(obj: dict) -> Optional['SearchRepositoriesResult']:
        if obj is None or not len(obj):
            return None

        return SearchRepositoriesResult(
            total_count=obj.get('total_count', None),
            incomplete_results=obj.get('incomplete_results', None),
            items=RepoSearchResultItem._parse_list(obj.get('items', None)),
        )


@dataclass
class RepoSearchResultItem(Object):
    """
    Repo Search Result Item
    """
    id: Optional['int']
    node_id: Optional['str']
    name: Optional['str']
    full_name: Optional['str']
    owner: Optional['SimpleUser']
    private: Optional['bool']
    html_url: Optional['str']
    description: Optional['str']
    fork: Optional['bool']
    url: Optional['str']
    created_at: Optional['str']
    updated_at: Optional['str']
    pushed_at: Optional['str']
    homepage: Optional['str']
    size: Optional['int']
    stargazers_count: Optional['int']
    watchers_count: Optional['int']
    language: Optional['str']
    forks_count: Optional['int']
    open_issues_count: Optional['int']
    master_branch: Optional['str']
    default_branch: Optional['str']
    score: Optional['float']
    forks_url: Optional['str']
    keys_url: Optional['str']
    collaborators_url: Optional['str']
    teams_url: Optional['str']
    hooks_url: Optional['str']
    issue_events_url: Optional['str']
    events_url: Optional['str']
    assignees_url: Optional['str']
    branches_url: Optional['str']
    tags_url: Optional['str']
    blobs_url: Optional['str']
    git_tags_url: Optional['str']
    git_refs_url: Optional['str']
    trees_url: Optional['str']
    statuses_url: Optional['str']
    languages_url: Optional['str']
    stargazers_url: Optional['str']
    contributors_url: Optional['str']
    subscribers_url: Optional['str']
    subscription_url: Optional['str']
    commits_url: Optional['str']
    git_commits_url: Optional['str']
    comments_url: Optional['str']
    issue_comment_url: Optional['str']
    contents_url: Optional['str']
    compare_url: Optional['str']
    merges_url: Optional['str']
    archive_url: Optional['str']
    downloads_url: Optional['str']
    issues_url: Optional['str']
    pulls_url: Optional['str']
    milestones_url: Optional['str']
    notifications_url: Optional['str']
    labels_url: Optional['str']
    releases_url: Optional['str']
    deployments_url: Optional['str']
    git_url: Optional['str']
    ssh_url: Optional['str']
    clone_url: Optional['str']
    svn_url: Optional['str']
    forks: Optional['int']
    open_issues: Optional['int']
    watchers: Optional['int']
    topics: Optional[List['str']]
    mirror_url: Optional['str']
    has_issues: Optional['bool']
    has_projects: Optional['bool']
    has_pages: Optional['bool']
    has_wiki: Optional['bool']
    has_downloads: Optional['bool']
    archived: Optional['bool']
    disabled: Optional['bool']
    visibility: Optional['str']
    license: Optional['SimpleLicense']
    permissions: Optional['RepoPermissions']
    text_matches: Optional['SearchResultTextMatch']
    temp_clone_token: Optional['str']
    allow_merge_commit: Optional['bool']
    allow_squash_merge: Optional['bool']
    allow_rebase_merge: Optional['bool']
    allow_auto_merge: Optional['bool']
    delete_branch_on_merge: Optional['bool']
    allow_forking: Optional['bool']
    is_template: Optional['bool']

    @staticmethod
    def _parse(obj: dict) -> Optional['RepoSearchResultItem']:
        if obj is None or not len(obj):
            return None

        return RepoSearchResultItem(
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
            created_at=obj.get('created_at', None),
            updated_at=obj.get('updated_at', None),
            pushed_at=obj.get('pushed_at', None),
            homepage=obj.get('homepage', None),
            size=obj.get('size', None),
            stargazers_count=obj.get('stargazers_count', None),
            watchers_count=obj.get('watchers_count', None),
            language=obj.get('language', None),
            forks_count=obj.get('forks_count', None),
            open_issues_count=obj.get('open_issues_count', None),
            master_branch=obj.get('master_branch', None),
            default_branch=obj.get('default_branch', None),
            score=obj.get('score', None),
            forks_url=obj.get('forks_url', None),
            keys_url=obj.get('keys_url', None),
            collaborators_url=obj.get('collaborators_url', None),
            teams_url=obj.get('teams_url', None),
            hooks_url=obj.get('hooks_url', None),
            issue_events_url=obj.get('issue_events_url', None),
            events_url=obj.get('events_url', None),
            assignees_url=obj.get('assignees_url', None),
            branches_url=obj.get('branches_url', None),
            tags_url=obj.get('tags_url', None),
            blobs_url=obj.get('blobs_url', None),
            git_tags_url=obj.get('git_tags_url', None),
            git_refs_url=obj.get('git_refs_url', None),
            trees_url=obj.get('trees_url', None),
            statuses_url=obj.get('statuses_url', None),
            languages_url=obj.get('languages_url', None),
            stargazers_url=obj.get('stargazers_url', None),
            contributors_url=obj.get('contributors_url', None),
            subscribers_url=obj.get('subscribers_url', None),
            subscription_url=obj.get('subscription_url', None),
            commits_url=obj.get('commits_url', None),
            git_commits_url=obj.get('git_commits_url', None),
            comments_url=obj.get('comments_url', None),
            issue_comment_url=obj.get('issue_comment_url', None),
            contents_url=obj.get('contents_url', None),
            compare_url=obj.get('compare_url', None),
            merges_url=obj.get('merges_url', None),
            archive_url=obj.get('archive_url', None),
            downloads_url=obj.get('downloads_url', None),
            issues_url=obj.get('issues_url', None),
            pulls_url=obj.get('pulls_url', None),
            milestones_url=obj.get('milestones_url', None),
            notifications_url=obj.get('notifications_url', None),
            labels_url=obj.get('labels_url', None),
            releases_url=obj.get('releases_url', None),
            deployments_url=obj.get('deployments_url', None),
            git_url=obj.get('git_url', None),
            ssh_url=obj.get('ssh_url', None),
            clone_url=obj.get('clone_url', None),
            svn_url=obj.get('svn_url', None),
            forks=obj.get('forks', None),
            open_issues=obj.get('open_issues', None),
            watchers=obj.get('watchers', None),
            topics=obj.get('topics', None),
            mirror_url=obj.get('mirror_url', None),
            has_issues=obj.get('has_issues', None),
            has_projects=obj.get('has_projects', None),
            has_pages=obj.get('has_pages', None),
            has_wiki=obj.get('has_wiki', None),
            has_downloads=obj.get('has_downloads', None),
            archived=obj.get('archived', None),
            disabled=obj.get('disabled', None),
            visibility=obj.get('visibility', None),
            license=SimpleLicense._parse(obj.get('license', None)),
            permissions=RepoPermissions._parse(obj.get('permissions', None)),
            text_matches=SearchResultTextMatch._parse(obj.get('text_matches', None)),
            temp_clone_token=obj.get('temp_clone_token', None),
            allow_merge_commit=obj.get('allow_merge_commit', None),
            allow_squash_merge=obj.get('allow_squash_merge', None),
            allow_rebase_merge=obj.get('allow_rebase_merge', None),
            allow_auto_merge=obj.get('allow_auto_merge', None),
            delete_branch_on_merge=obj.get('delete_branch_on_merge', None),
            allow_forking=obj.get('allow_forking', None),
            is_template=obj.get('is_template', None),
        )

    @staticmethod
    def _parse_list(result_items: list) -> Optional[List['RepoSearchResultItem']]:
        if type(result_items) != list:
            return []

        results: List['RepoSearchResultItem'] = []
        for result_dict in result_items:
            result = RepoSearchResultItem._parse(result_dict)
            if result_dict is not None and len(result_dict):
                results.append(result)
        return results


######################################################################################
@dataclass
class SearchTopicsResult(Object):
    total_count: Optional['int']
    incomplete_results: Optional['bool']
    items: Optional[List['TopicSearchResultItem']]

    @staticmethod
    def _parse(obj: dict) -> Optional['SearchTopicsResult']:
        if obj is None or not len(obj):
            return None

        return SearchTopicsResult(
            total_count=obj.get('total_count', None),
            incomplete_results=obj.get('incomplete_results', None),
            items=TopicSearchResultItem._parse_list(obj.get('items', None)),
        )


@dataclass
class TopicSearchResultItem(Object):
    """
    Topic Search Result Item
    """
    name: Optional['str']
    display_name: Optional['str']
    short_description: Optional['str']
    description: Optional['str']
    created_by: Optional['str']
    released: Optional['str']
    created_at: Optional['str']
    updated_at: Optional['str']
    featured: Optional['bool']
    curated: Optional['bool']
    score: Optional['float']
    repository_count: Optional['int']
    logo_url: Optional['str']
    text_matches: Optional['SearchResultTextMatch']
    related: Optional[List['RelatedObject']]
    aliases: Optional[List['AliasObject']]

    @staticmethod
    def _parse(obj: dict) -> Optional['TopicSearchResultItem']:
        if obj is None or not len(obj):
            return None

        return TopicSearchResultItem(
            name=obj.get('name', None),
            display_name=obj.get('display_name', None),
            short_description=obj.get('short_description', None),
            description=obj.get('description', None),
            created_by=obj.get('created_by', None),
            released=obj.get('released', None),
            created_at=obj.get('created_at', None),
            updated_at=obj.get('updated_at', None),
            featured=obj.get('featured', None),
            curated=obj.get('curated', None),
            score=obj.get('score', None),
            repository_count=obj.get('repository_count', None),
            logo_url=obj.get('logo_url', None),
            text_matches=SearchResultTextMatch._parse(obj.get('text_matches', None)),
            related=RelatedObject._parse_list(obj.get('related', None)),
            aliases=AliasObject._parse_list(obj.get('aliases', None)),
        )

    @staticmethod
    def _parse_list(result_items: list) -> Optional[List['TopicSearchResultItem']]:
        if type(result_items) != list:
            return []

        results: List['TopicSearchResultItem'] = []
        for result_dict in result_items:
            result = TopicSearchResultItem._parse(result_dict)
            if result_dict is not None and len(result_dict):
                results.append(result)
        return results


@dataclass
class RelatedObject(Object):
    id: Optional['int']
    name: Optional['str']
    topic_id: Optional['int']
    relation_type: Optional['str']

    @staticmethod
    def _parse(obj: dict) -> Optional['RelatedObject']:
        if obj is None or not len(obj):
            return None

        return RelatedObject(
            id=obj.get('id', None),
            name=obj.get('name', None),
            topic_id=obj.get('topic_id', None),
            relation_type=obj.get('relation_type', None),
        )

    @staticmethod
    def _parse_list(result_items: list) -> Optional[List['RelatedObject']]:
        if type(result_items) != list:
            return []

        results: List['RelatedObject'] = []
        for result_dict in result_items:
            result = RelatedObject._parse(result_dict)
            if result_dict is not None and len(result_dict):
                results.append(result)
        return results


@dataclass
class AliasObject(Object):
    id: Optional['int']
    name: Optional['str']
    topic_id: Optional['int']
    relation_type: Optional['str']

    @staticmethod
    def _parse(obj: dict) -> Optional['AliasObject']:
        if obj is None or not len(obj):
            return None

        return AliasObject(
            id=obj.get('id', None),
            name=obj.get('name', None),
            topic_id=obj.get('topic_id', None),
            relation_type=obj.get('relation_type', None),
        )

    @staticmethod
    def _parse_list(result_items: list) -> Optional[List['AliasObject']]:
        if type(result_items) != list:
            return []

        results: List['AliasObject'] = []
        for result_dict in result_items:
            result = AliasObject._parse(result_dict)
            if result_dict is not None and len(result_dict):
                results.append(result)
        return results


######################################################################################

@dataclass
class SearchUsersResult(Object):
    total_count: Optional['int']
    incomplete_results: Optional['bool']
    items: Optional[List['RepoSearchResultItem']]

    @staticmethod
    def _parse(obj: dict) -> Optional['SearchUsersResult']:
        if obj is None or not len(obj):
            return None

        return SearchUsersResult(
            total_count=obj.get('total_count', None),
            incomplete_results=obj.get('incomplete_results', None),
            items=UserSearchResultItem._parse_list(obj.get('items', None)),
        )


@dataclass
class UserSearchResultItem(Object):
    """
    User Search Result Item
    """
    login: Optional['str']
    id: Optional['int']
    node_id: Optional['str']
    avatar_url: Optional['str']
    gravatar_url: Optional['str']
    url: Optional['str']
    html_url: Optional['str']
    followers_url: Optional['str']
    subscriptions_url: Optional['str']
    organizations_url: Optional['str']
    repos_url: Optional['str']
    received_events_url: Optional['str']
    type: Optional['str']
    score: Optional['float']
    following_url: Optional['str']
    gists_url: Optional['str']
    starred_url: Optional['str']
    events_url: Optional['str']
    public_repos: Optional['int']
    public_gists: Optional['int']
    followers: Optional['int']
    following: Optional['int']
    created_at: Optional['str']
    updated_at: Optional['str']
    name: Optional['str']
    bio: Optional['str']
    email: Optional['str']
    location: Optional['str']
    site_admin: Optional['bool']
    hireable: Optional['bool']
    text_matches: Optional['SearchResultTextMatch']
    blog: Optional['str']
    company: Optional['str']
    suspended_at: Optional['str']

    @staticmethod
    def _parse(obj: dict) -> Optional['UserSearchResultItem']:
        if obj is None or not len(obj):
            return None

        return UserSearchResultItem(
            login=obj.get('login', None),
            id=obj.get('id', None),
            node_id=obj.get('node_id', None),
            avatar_url=obj.get('avatar_url', None),
            gravatar_url=obj.get('gravatar_url', None),
            url=obj.get('url', None),
            html_url=obj.get('html_url', None),
            followers_url=obj.get('followers_url', None),
            subscriptions_url=obj.get('subscriptions_url', None),
            organizations_url=obj.get('organizations_url', None),
            repos_url=obj.get('repos_url', None),
            received_events_url=obj.get('received_events_url', None),
            type=obj.get('type', None),
            score=obj.get('score', None),
            following_url=obj.get('following_url', None),
            gists_url=obj.get('gists_url', None),
            starred_url=obj.get('starred_url', None),
            events_url=obj.get('events_url', None),
            public_repos=obj.get('public_repos', None),
            public_gists=obj.get('public_gists', None),
            followers=obj.get('followers', None),
            following=obj.get('following', None),
            created_at=obj.get('created_at', None),
            updated_at=obj.get('updated_at', None),
            name=obj.get('name', None),
            bio=obj.get('bio', None),
            email=obj.get('email', None),
            location=obj.get('location', None),
            site_admin=obj.get('site_admin', None),
            hireable=obj.get('hireable', None),
            text_matches=SearchResultTextMatch._parse(obj.get('text_matches', None)),
            blog=obj.get('blog', None),
            company=obj.get('company', None),
            suspended_at=obj.get('suspended_at', None),
        )

    @staticmethod
    def _parse_list(result_items: list) -> Optional[List['UserSearchResultItem']]:
        if type(result_items) != list:
            return []

        results: List['UserSearchResultItem'] = []
        for result_dict in result_items:
            result = UserSearchResultItem._parse(result_dict)
            if result_dict is not None and len(result_dict):
                results.append(result)
        return results


######################################################################################

@dataclass
class LabelSearchResult(Object):
    total_count: Optional['int']
    incomplete_results: Optional['bool']
    items: Optional[List['LabelSearchResultItem']]

    @staticmethod
    def _parse(obj: dict) -> Optional['LabelSearchResult']:
        if obj is None or not len(obj):
            return None

        return LabelSearchResult(
            total_count=obj.get('total_count', None),
            incomplete_results=obj.get('incomplete_results', None),
            items=LabelSearchResultItem._parse_list(obj.get('items', None)),
        )


@dataclass
class LabelSearchResultItem(Object):
    """
    Label Search Result Item
    """
    id: Optional['int']
    node_id: Optional['str']
    url: Optional['str']
    name: Optional['str']
    color: Optional['str']
    is_default: Optional['bool']
    description: Optional['str']
    score: Optional['float']
    text_matches: Optional['SearchResultTextMatch']

    @staticmethod
    def _parse(obj: dict) -> Optional['LabelSearchResultItem']:
        if obj is None or not len(obj):
            return None

        return LabelSearchResultItem(
            id=obj.get('id', None),
            node_id=obj.get('node_id', None),
            url=obj.get('url', None),
            name=obj.get('name', None),
            color=obj.get('color', None),
            is_default=obj.get('default', None),
            description=obj.get('description', None),
            score=obj.get('score', None),
            text_matches=SearchResultTextMatch._parse(obj.get('text_matches', None)),
        )

    @staticmethod
    def _parse_list(result_items: list) -> Optional[List['LabelSearchResultItem']]:
        if type(result_items) != list:
            return []

        results: List['LabelSearchResultItem'] = []
        for result_dict in result_items:
            result = LabelSearchResultItem._parse(result_dict)
            if result_dict is not None and len(result_dict):
                results.append(result)
        return results
