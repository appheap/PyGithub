from dataclasses import dataclass
from typing import Optional

from .object import Object


@dataclass
class RepoPermissions(Object):
    admin: bool
    pull: bool
    triage: Optional['bool']
    push: bool
    maintain: Optional['bool']

    @staticmethod
    def _parse(permissions: dict) -> Optional['RepoPermissions']:
        if permissions is None or not len(permissions):
            return None

        return RepoPermissions(
            admin=permissions.get('admin'),
            maintain=permissions.get('maintain', None),
            push=permissions.get('push'),
            triage=permissions.get('triage', None),
            pull=permissions.get('pull'),
        )
