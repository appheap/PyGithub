from dataclasses import dataclass
from typing import Optional, List

from github.utils import utils
from .issue import Issue
from .issue_comment import IssueComment
from .object import Object
from .page import Page


@dataclass
class Payload(Object):
    action: str
    issue: Optional['Issue']
    comment: Optional['IssueComment']
    pages: Optional[List['Page']]

    @staticmethod
    def _parse(obj: dict) -> Optional['Payload']:
        if obj is None or not len(obj):
            return None

        payload = Payload(
            action=obj.get('action', None),
            issue=Issue._parse(obj.get('issue', None)),
            comment=IssueComment._parse(obj.get('comment', None)),
            pages=utils.parse_pages(obj.get('pages', None)),
        )
        if payload.action is None and payload.comment is None and not len(payload.pages) and payload.issue is None:
            return None
        
        return payload
