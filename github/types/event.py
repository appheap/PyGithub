from dataclasses import dataclass
from typing import Optional

from .actor import Actor
from .object import Object
from .payload import Payload
from .repository import Repo


@dataclass
class Event(Object):
    """
    Event
    """
    id: str
    type: str
    actor: Optional['Actor']
    repo: Optional['Repo']
    org: Optional['Actor']
    payload: Optional['Payload']
    public: bool
    created_at: str

    @staticmethod
    def _parse(obj: dict) -> Optional['Event']:
        if obj is None or not len(obj):
            return None

        return Event(
            id=obj.get('id', None),
            type=obj.get('type', None),
            actor=Actor._parse(obj.get('actor', None)),
            repo=Repo._parse(obj.get('repo', None)),
            org=Actor._parse(obj.get('org', None)),
            payload=Payload._parse(obj.get('payload', None)),
            public=obj.get('public', None),
            created_at=obj.get('created_at', None),
        )
