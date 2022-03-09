from dataclasses import dataclass
from typing import Optional

from .object import Object
from .user import SimpleUser


@dataclass
class Stargazer(Object):
    starred_at: str
    user: 'SimpleUser'

    @staticmethod
    def _parse(obj: dict) -> Optional['Stargazer']:
        if obj is None or not len(obj):
            return None

        return Stargazer(
            starred_at=obj.get('starred_at', None),
            user=SimpleUser._parse(obj.get('user', None)),
        )
