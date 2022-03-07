from dataclasses import dataclass
from typing import Optional

from .object import Object


@dataclass
class PullRequest(Object):
    merged_at: Optional['str']
    diff_url: Optional['str']
    html_url: Optional['str']
    patch_url: Optional['str']
    url: Optional['str']

    @staticmethod
    def _parse(obj: dict) -> Optional['PullRequest']:
        if obj is None or not len(obj):
            return None

        return PullRequest(
            merged_at=obj.get('merged_at', None),
            diff_url=obj.get('diff_url', None),
            html_url=obj.get('html_url', None),
            patch_url=obj.get('patch_url', None),
            url=obj.get('url', None),
        )
