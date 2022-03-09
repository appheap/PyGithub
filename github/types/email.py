from dataclasses import dataclass
from typing import Optional

from .object import Object


@dataclass
class Email(Object):
    email: str
    primary: bool
    verified: bool
    visibility: Optional['str']

    @staticmethod
    def _parse(obj: dict) -> Optional['Email']:
        if obj is None or not len(obj):
            return None

        return Email(
            email=obj.get('email', None),
            primary=obj.get('primary', None),
            verified=obj.get('verified', None),
            visibility=obj.get('visibility', None),
        )
