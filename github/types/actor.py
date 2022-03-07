from dataclasses import dataclass
from typing import Optional

from .object import Object


@dataclass
class Actor(Object):
    id: int
    login: str
    display_login: str
    gravatar_id: Optional['str']
    url: str
    avatar_id: Optional['str']

    @staticmethod
    def _parse(obj: dict) -> Optional['Actor']:
        if obj is None or not len(obj):
            return None

        return Actor(
            id=obj.get('id', None),
            login=obj.get('login', None),
            display_login=obj.get('display_login', None),
            gravatar_id=obj.get('gravatar_id', None),
            url=obj.get('url', None),
            avatar_id=obj.get('avatar_id', None),
        )
