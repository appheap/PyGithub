from dataclasses import dataclass
from typing import Optional

from .object import Object
from .user import SimpleUser


@dataclass
class Milestone(Object):
    url: Optional['str']
    html_url: Optional['str']
    labels_url: Optional['str']
    id: Optional['int']
    node_id: Optional['str']
    number: Optional['int']
    state: Optional['str']
    title: Optional['str']
    description: Optional['str']
    creator: Optional['SimpleUser']
    open_issues: Optional['int']
    closed_issues: Optional['int']
    created_at: Optional['str']
    updated_at: Optional['str']
    closed_at: Optional['str']
    due_on: Optional['str']

    @staticmethod
    def _parse(obj: dict) -> Optional['Milestone']:
        if obj is None or not len(obj):
            return None

        return Milestone(
            url=obj.get('url', None),
            html_url=obj.get('html_url', None),
            labels_url=obj.get('labels_url', None),
            id=obj.get('id', None),
            node_id=obj.get('node_id', None),
            number=obj.get('number', None),
            state=obj.get('state', None),
            title=obj.get('title', None),
            description=obj.get('description', None),
            creator=obj.get('creator', None),
            open_issues=obj.get('open_issues', None),
            closed_issues=obj.get('closed_issues', None),
            created_at=obj.get('created_at', None),
            updated_at=obj.get('updated_at', None),
            closed_at=obj.get('closed_at', None),
            due_on=obj.get('due_on', None),
        )
