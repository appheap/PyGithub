from dataclasses import dataclass
from typing import Optional

from .object import Object


@dataclass
class ReactionRollup(Object):
    url: str
    total_count: int
    plus_one: int
    minus_one: int
    laugh: int
    confused: int
    heart: int
    hooray: int
    eyes: int
    rocket: int

    @staticmethod
    def _parse(obj: dict) -> Optional['ReactionRollup']:
        if obj is None or not len(obj):
            return None

        return ReactionRollup(
            url=obj.get('url', None),
            total_count=obj.get('total_count', None),
            plus_one=obj.get('plus_one', None),
            minus_one=obj.get('minus_one', None),
            laugh=obj.get('laugh', None),
            confused=obj.get('confused', None),
            heart=obj.get('heart', None),
            hooray=obj.get('hooray', None),
            eyes=obj.get('eyes', None),
            rocket=obj.get('rocket', None),
        )
