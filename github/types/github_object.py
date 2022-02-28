from typing import Optional

from .object import Object


class GithubObject(Object):

    def __init__(
            self,
            *,
            login: Optional['str'] = None,
            id: Optional['str'] = None,
            node_id: Optional['str'] = None,
            avatar_id: Optional['str'] = None,
            gravatar_id: Optional['str'] = None,
            url: Optional['str'] = None,
            html_url: Optional['str'] = None,
            followers_url: Optional['str'] = None,
            following_url: Optional['str'] = None,
            gists_url: Optional['str'] = None,
            starred_url: Optional['str'] = None,
            subscriptions_url: Optional['str'] = None,
            organizations_url: Optional['str'] = None,
            repos_url: Optional['str'] = None,
            events_url: Optional['str'] = None,
            received_events_url: Optional['str'] = None,
            type: Optional['str'] = None,
            site_admin: Optional['str'] = None,
            name: Optional['str'] = None,
            company: Optional['str'] = None,
            blog: Optional['str'] = None,
            location: Optional['str'] = None,
            email: Optional['str'] = None,
            hireable: Optional['str'] = None,
            bio: Optional['str'] = None,
            twitter_username: Optional['str'] = None,
            public_repos: Optional['int'] = None,
            public_gists: Optional['int'] = None,
            followers: Optional['str'] = None,
            following: Optional['str'] = None,
            created_at: Optional['str'] = None,
            updated_at: Optional['str'] = None,
            private_gists: Optional['str'] = None,
            total_private_repos: Optional['int'] = None,
            owned_private_repos: Optional['str'] = None,
            disk_usage: Optional['str'] = None,
            collaborators: Optional['str'] = None,
            two_factor_authentication: Optional['bool'] = None,
    ):
        self.login = login
        self.id = id
        self.node_id = node_id
        self.avatar_id = avatar_id
        self.gravatar_id = gravatar_id
        self.url = url
        self.html_url = html_url
        self.followers_url = followers_url
        self.following_url = following_url
        self.gists_url = gists_url
        self.starred_url = starred_url
        self.subscriptions_url = subscriptions_url
        self.organizations_url = organizations_url
        self.repos_url = repos_url
        self.events_url = events_url
        self.received_events_url = received_events_url
        self.type = type
        self.site_admin = site_admin
        self.name = name
        self.company = company
        self.blog = blog
        self.location = location
        self.email = email
        self.hireable = hireable
        self.bio = bio
        self.twitter_username = twitter_username
        self.public_repos = public_repos
        self.public_gists = public_gists
        self.followers = followers
        self.following = following
        self.created_at = created_at
        self.updated_at = updated_at
        self.private_gists = private_gists
        self.total_private_repos = total_private_repos
        self.owned_private_repos = owned_private_repos
        self.disk_usage = disk_usage
        self.collaborators = collaborators
        self.two_factor_authentication = two_factor_authentication
        # self.plan=None

    @staticmethod
    def _parse(user: dict) -> Optional['GithubObject']:
        if user is None or not len(user):
            return None

        return GithubObject(
            login=user.get('login', None),
            id=user.get('id', None),
            node_id=user.get('node_id', None),
            avatar_id=user.get('avatar_id', None),
            gravatar_id=user.get('gravatar_id', None),
            url=user.get('url', None),
            html_url=user.get('html_url', None),
            followers_url=user.get('followers_url', None),
            following_url=user.get('following_url', None),
            gists_url=user.get('gists_url', None),
            starred_url=user.get('starred_url', None),
            subscriptions_url=user.get('subscriptions_url', None),
            organizations_url=user.get('organizations_url', None),
            repos_url=user.get('repos_url', None),
            events_url=user.get('events_url', None),
            received_events_url=user.get('received_events_url', None),
            type=user.get('type', None),
            site_admin=user.get('site_admin', None),
            name=user.get('name', None),
            company=user.get('company', None),
            blog=user.get('blog', None),
            location=user.get('location', None),
            email=user.get('email', None),
            hireable=user.get('hireable', None),
            bio=user.get('bio', None),
            twitter_username=user.get('twitter_username', None),
            public_repos=user.get('public_repos', None),
            public_gists=user.get('public_gists', None),
            followers=user.get('followers', None),
            following=user.get('following', None),
            created_at=user.get('created_at', None),
            updated_at=user.get('updated_at', None),
            private_gists=user.get('private_gists', None),
            total_private_repos=user.get('total_private_repos', None),
            owned_private_repos=user.get('owned_private_repos', None),
            disk_usage=user.get('disk_usage', None),
            collaborators=user.get('collaborators', None),
            two_factor_authentication=user.get('two_factor_authentication', None),
        )
