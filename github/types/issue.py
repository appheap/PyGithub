from dataclasses import dataclass
from typing import Optional, List, Union

from .object import Object
from .user import SimpleUser
from .label import Label
from .milestone import Milestone
from .pull_request import PullRequest
from .integration import Integration
from .repository import Repository
from .reaction_rollup import ReactionRollup
from github.utils import utils


@dataclass
class Issue(Object):
    """
    Issues are a great way to keep track of tasks, enhancements, and bugs for your projects.
    """
    id: int
    node_id: str
    url: str
    repository_url: Optional['str']
    labels_url: Optional['str']
    comments_url: Optional['str']
    events_url: Optional['str']
    html_url: Optional['str']
    number: Optional['int']
    state: Optional['str']
    title: Optional['str']
    body: Optional['str']
    user: Optional['SimpleUser']
    labels: Optional[List[Union['str', 'Label']]]
    assignee: Optional['SimpleUser']
    assignees: Optional[List['SimpleUser']]
    milestone: Optional['Milestone']
    locked: Optional['bool']
    active_lock_reason: Optional['str']
    comments: Optional['int']
    pull_request: Optional['PullRequest']
    closed_at: Optional['str']
    created_at: Optional['str']
    updated_at: Optional['str']
    draft: Optional['bool']
    closed_by: Optional['SimpleUser']
    body_html: Optional['str']
    body_text: Optional['str']
    timeline_url: Optional['str']
    repository: Optional['Repository']
    performed_via_github_app: Optional['Integration']
    author_association: Optional['str']
    reactions: Optional['ReactionRollup']

    @staticmethod
    def _parse(obj: dict) -> Optional['Issue']:
        if obj is None or not len(obj):
            return None

        return Issue(
            id=obj.get('id', None),
            node_id=obj.get('node_id', None),
            url=obj.get('url', None),
            repository_url=obj.get('repository_url', None),
            labels_url=obj.get('labels_url', None),
            comments_url=obj.get('comments_url', None),
            events_url=obj.get('events_url', None),
            html_url=obj.get('html_url', None),
            number=obj.get('number', None),
            state=obj.get('state', None),
            title=obj.get('title', None),
            body=obj.get('body', None),
            user=SimpleUser._parse(obj.get('user', None)),
            labels=utils.parse_labels(obj.get('labels', None)),
            assignee=SimpleUser._parse(obj.get('assignee', None)),
            assignees=utils.parse_simple_users(obj.get('assignees', None)),
            milestone=Milestone._parse(obj.get('milestone', None)),
            locked=obj.get('locked', None),
            active_lock_reason=obj.get('active_lock_reason', None),
            comments=obj.get('comments', None),
            pull_request=PullRequest._parse(obj.get('pull_request', None)),
            closed_at=obj.get('closed_at', None),
            created_at=obj.get('created_at', None),
            updated_at=obj.get('updated_at', None),
            draft=obj.get('draft', None),
            closed_by=SimpleUser._parse(obj.get('closed_by', None)),
            body_html=obj.get('body_html', None),
            body_text=obj.get('body_text', None),
            timeline_url=obj.get('timeline_url', None),
            repository=Repository._parse(obj.get('repository', None)),
            performed_via_github_app=Integration._parse(obj.get('performed_via_github_app', None)),
            author_association=obj.get('author_association', None),
            reactions=ReactionRollup._parse(obj.get('reactions', None)),
        )
