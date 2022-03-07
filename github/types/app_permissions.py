from dataclasses import dataclass
from typing import Optional

from .object import Object


@dataclass
class AppPermissions(Object):
    """
    The set of permissions for the GitHub app
    """

    issues: Optional['str']
    checks: Optional['str']
    metadata: Optional['str']
    contents: Optional['str']
    deployments: Optional['str']

    @staticmethod
    def _parse(obj: dict) -> Optional['AppPermissions']:
        if obj is None or not len(obj):
            return None

        return AppPermissions(
            issues=obj.get('issues', None),
            checks=obj.get('checks', None),
            metadata=obj.get('metadata', None),
            contents=obj.get('contents', None),
            deployments=obj.get('deployments', None),
        )
