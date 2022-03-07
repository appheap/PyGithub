from dataclasses import dataclass
from typing import Optional

from .object import Object


@dataclass
class Label(Object):
    id: int
    node_id: str
    url: str
    name: str
    description: str
    color: str
    default: bool

    @staticmethod
    def _parse(obj: dict) -> Optional['Label']:
        if obj is None or not len(obj):
            return None

        return Label(
            id=obj.get('id', None),
            node_id=obj.get('node_id', None),
            url=obj.get('url', None),
            name=obj.get('name', None),
            description=obj.get('description', None),
            color=obj.get('color', None),
            default=obj.get('default', None),
        )
