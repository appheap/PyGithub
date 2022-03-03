from dataclasses import dataclass
from typing import Optional

from github.types import Object


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
