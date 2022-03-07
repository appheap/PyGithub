from dataclasses import dataclass
from typing import Optional

from .integration import Integration
from .object import Object
from .reaction_rollup import ReactionRollup
from .user import SimpleUser


@dataclass
class IssueComment(Object):
    id: int
    node_id: str
    url: str
    body: str
    body_text: str
    body_html: str
    html_url: str
    user: Optional['SimpleUser']
    created_at: str
    updated_at: str
    issues_url: str
    author_association: Optional['str']
    performed_via_github_app: Optional['Integration']
    reactions: Optional['ReactionRollup']

    @staticmethod
    def _parse(obj: dict) -> Optional['IssueComment']:
        if obj is None or not len(obj):
            return None

        return IssueComment(
            id=obj.get('id', None),
            node_id=obj.get('node_id', None),
            url=obj.get('url', None),
            body=obj.get('body', None),
            body_text=obj.get('body_text', None),
            body_html=obj.get('body_html', None),
            html_url=obj.get('html_url', None),
            user=SimpleUser._parse(obj.get('user', None)),
            created_at=obj.get('created_at', None),
            updated_at=obj.get('updated_at', None),
            issues_url=obj.get('issues_url', None),
            author_association=obj.get('author_association', None),
            performed_via_github_app=Integration._parse(obj.get('performed_via_github_app', None)),
            reactions=ReactionRollup._parse(obj.get('reactions', None)),
        )
