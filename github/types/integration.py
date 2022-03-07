from dataclasses import dataclass
from typing import Optional, List

from .app_permissions import AppPermissions
from .object import Object
from .user import SimpleUser


@dataclass
class Integration(Object):
    """
    GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    id: str
    slug: Optional['str']
    node_id: Optional['str']
    owner: Optional['SimpleUser']
    name: Optional['str']
    description: Optional['str']
    external_url: Optional['str']
    html_url: Optional['str']
    created_at: Optional['str']
    updated_at: Optional['str']
    permissions: Optional['AppPermissions']
    events: Optional[List['str']]
    installation_count: Optional['int']
    client_id: Optional['str']
    client_secret: Optional['str']
    webhook_secret: Optional['str']
    pem: Optional['str']

    @staticmethod
    def _parse(obj: dict) -> Optional['Integration']:
        if obj is None or not len(obj):
            return None

        return Integration(
            id=obj.get('id', None),
            slug=obj.get('slug', None),
            node_id=obj.get('node_id', None),
            owner=SimpleUser._parse(obj.get('owner', None)),
            name=obj.get('name', None),
            description=obj.get('description', None),
            external_url=obj.get('external_url', None),
            html_url=obj.get('html_url', None),
            created_at=obj.get('created_at', None),
            updated_at=obj.get('updated_at', None),
            permissions=AppPermissions._parse(obj.get('permissions', None)),
            events=obj.get('events', None),
            installation_count=obj.get('installation_count', None),
            client_id=obj.get('client_id', None),
            client_secret=obj.get('client_secret', None),
            webhook_secret=obj.get('webhook_secret', None),
            pem=obj.get('pem', None),
        )
