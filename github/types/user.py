from dataclasses import dataclass
from typing import Optional

from .object import Object


@dataclass
class SimpleUser(Object):
    """
    Simple User
    """

    name: Optional['str']
    email: Optional['str']
    login: str
    id: str
    node_id: str
    avatar_id: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: str
    starred_at: Optional['str']

    @staticmethod
    def _parse(simple_user_dict: dict):
        if not simple_user_dict or not len(simple_user_dict):
            return None

        return SimpleUser(
            name=simple_user_dict.get('name', None),
            email=simple_user_dict.get('email', None),
            login=simple_user_dict.get('login'),
            id=simple_user_dict.get('id'),
            node_id=simple_user_dict.get('node_id'),
            avatar_id=simple_user_dict.get('avatar_id'),
            gravatar_id=simple_user_dict.get('gravatar_id'),
            url=simple_user_dict.get('url'),
            html_url=simple_user_dict.get('html_url'),
            followers_url=simple_user_dict.get('followers_url'),
            following_url=simple_user_dict.get('following_url'),
            gists_url=simple_user_dict.get('gists_url'),
            starred_url=simple_user_dict.get('starred_url'),
            subscriptions_url=simple_user_dict.get('subscriptions_url'),
            organizations_url=simple_user_dict.get('organizations_url'),
            repos_url=simple_user_dict.get('repos_url'),
            events_url=simple_user_dict.get('events_url'),
            received_events_url=simple_user_dict.get('received_events_url'),
            type=simple_user_dict.get('type'),
            site_admin=simple_user_dict.get('site_admin'),
            starred_at=simple_user_dict.get('starred_at', None),
        )


@dataclass
class PrivateUser(Object):
    """
    Private User
    """
    login: str
    id: int
    node_id: str
    avatar_id: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool
    name: str
    company: str
    blog: str
    location: str
    email: str
    hireable: bool
    bio: str
    twitter_username: Optional['str']
    public_repos: int
    public_gists: int
    followers: int
    following: int
    created_at: str
    updated_at: str
    private_gists: int
    total_private_repos: int
    owned_private_repos: int
    disk_usage: int
    collaborators: int
    two_factor_authentication: bool
    plan: Optional['Plan']
    suspended_at: Optional['str']
    business_plus: Optional['bool']
    ldap_dn: Optional['str']

    @staticmethod
    def _parse(obj: dict) -> Optional['PrivateUser']:
        if obj is None or not len(obj):
            return None

        return PrivateUser(
            login=obj.get('login', None),
            id=obj.get('id', None),
            node_id=obj.get('node_id', None),
            avatar_id=obj.get('avatar_id', None),
            gravatar_id=obj.get('gravatar_id', None),
            url=obj.get('url', None),
            html_url=obj.get('html_url', None),
            followers_url=obj.get('followers_url', None),
            following_url=obj.get('following_url', None),
            gists_url=obj.get('gists_url', None),
            starred_url=obj.get('starred_url', None),
            subscriptions_url=obj.get('subscriptions_url', None),
            organizations_url=obj.get('organizations_url', None),
            repos_url=obj.get('repos_url', None),
            events_url=obj.get('events_url', None),
            received_events_url=obj.get('received_events_url', None),
            type=obj.get('type', None),
            site_admin=obj.get('site_admin', None),
            name=obj.get('name', None),
            company=obj.get('company', None),
            blog=obj.get('blog', None),
            location=obj.get('location', None),
            email=obj.get('email', None),
            hireable=obj.get('hireable', None),
            bio=obj.get('bio', None),
            twitter_username=obj.get('twitter_username', None),
            public_repos=obj.get('public_repos', None),
            public_gists=obj.get('public_gists', None),
            followers=obj.get('followers', None),
            following=obj.get('following', None),
            created_at=obj.get('created_at', None),
            updated_at=obj.get('updated_at', None),
            private_gists=obj.get('private_gists', None),
            total_private_repos=obj.get('total_private_repos', None),
            owned_private_repos=obj.get('owned_private_repos', None),
            disk_usage=obj.get('disk_usage', None),
            collaborators=obj.get('collaborators', None),
            two_factor_authentication=obj.get('two_factor_authentication', None),
            plan=Plan._parse(obj.get('plan', None)),
            suspended_at=obj.get('suspended_at', None),
            business_plus=obj.get('business_plus', None),
            ldap_dn=obj.get('ldap_dn', None),
        )


@dataclass
class PublicUser(Object):
    """
    Public User
    """
    login: str
    id: int
    node_id: str
    avatar_id: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool
    name: str
    company: str
    blog: str
    location: str
    email: str
    hireable: bool
    bio: str
    twitter_username: Optional['str']
    public_repos: int
    public_gists: int
    followers: int
    following: int
    created_at: str
    updated_at: str
    plan: Optional['Plan']
    suspended_at: Optional['str']
    private_gists: Optional['int']
    total_private_repos: Optional['int']
    owned_private_repos: Optional['int']
    disk_usage: Optional['int']
    collaborators: Optional['int']

    @staticmethod
    def _parse(obj: dict) -> Optional['PublicUser']:
        if obj is None or not len(obj):
            return None

        return PublicUser(
            login=obj.get('login', None),
            id=obj.get('id', None),
            node_id=obj.get('node_id', None),
            avatar_id=obj.get('avatar_id', None),
            gravatar_id=obj.get('gravatar_id', None),
            url=obj.get('url', None),
            html_url=obj.get('html_url', None),
            followers_url=obj.get('followers_url', None),
            following_url=obj.get('following_url', None),
            gists_url=obj.get('gists_url', None),
            starred_url=obj.get('starred_url', None),
            subscriptions_url=obj.get('subscriptions_url', None),
            organizations_url=obj.get('organizations_url', None),
            repos_url=obj.get('repos_url', None),
            events_url=obj.get('events_url', None),
            received_events_url=obj.get('received_events_url', None),
            type=obj.get('type', None),
            site_admin=obj.get('site_admin', None),
            name=obj.get('name', None),
            company=obj.get('company', None),
            blog=obj.get('blog', None),
            location=obj.get('location', None),
            email=obj.get('email', None),
            hireable=obj.get('hireable', None),
            bio=obj.get('bio', None),
            twitter_username=obj.get('twitter_username', None),
            public_repos=obj.get('public_repos', None),
            public_gists=obj.get('public_gists', None),
            followers=obj.get('followers', None),
            following=obj.get('following', None),
            created_at=obj.get('created_at', None),
            updated_at=obj.get('updated_at', None),
            plan=Plan._parse(obj.get('plan', None)),
            suspended_at=obj.get('suspended_at', None),
            private_gists=obj.get('private_gists', None),
            total_private_repos=obj.get('total_private_repos', None),
            owned_private_repos=obj.get('owned_private_repos', None),
            disk_usage=obj.get('disk_usage', None),
            collaborators=obj.get('collaborators', None),
        )


@dataclass
class Plan(Object):
    collaborators: int
    name: str
    space: int
    private_repos: int

    @staticmethod
    def _parse(obj: dict) -> Optional['Plan']:
        if obj is None or not len(obj):
            return None

        return Plan(
            collaborators=obj.get('collaborators', None),
            name=obj.get('name', None),
            space=obj.get('space', None),
            private_repos=obj.get('private_repos', None),
        )
