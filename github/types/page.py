from dataclasses import dataclass
from typing import Optional

from .object import Object


@dataclass
class Page(Object):
    page_name: str
    title: str
    summary: str
    action: str
    sha: str
    html_url: str

    @staticmethod
    def _parse(obj: dict) -> Optional['Page']:
        if obj is None or not len(obj):
            return None

        return Page(
            page_name=obj.get('page_name', None),
            title=obj.get('title', None),
            summary=obj.get('summary', None),
            action=obj.get('action', None),
            sha=obj.get('sha', None),
            html_url=obj.get('html_url', None),
        )
