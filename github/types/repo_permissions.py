from typing import Optional

from .object import Object


class RepoPermissions(Object):

    def __init__(
            self,
            *,
            admin: Optional['str'] = None,
            maintain: Optional['str'] = None,
            push: Optional['str'] = None,
            triage: Optional['str'] = None,
            pull: Optional['str'] = None,

    ):
        self.admin = admin
        self.maintain = maintain
        self.push = push
        self.triage = triage
        self.pull = pull

    @staticmethod
    def _parse(permissions: dict):
        if permissions is None or not len(permissions):
            return None

        return RepoPermissions(
            admin=permissions.get('admin', None),
            maintain=permissions.get('maintain', None),
            push=permissions.get('push', None),
            triage=permissions.get('triage', None),
            pull=permissions.get('pull', None),
        )
