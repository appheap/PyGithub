from dataclasses import dataclass
from typing import Optional

from .object import Object


@dataclass
class GithubError(Object):
    resource: str
    code: str
    field: str
    message: str

    @staticmethod
    def _parse(error_dict: dict) -> Optional['GithubError']:
        if error_dict is None or not len(error_dict):
            return None

        return GithubError(
            resource=error_dict.get('resource', None),
            code=error_dict.get('code', None),
            field=error_dict.get('field', None),
            message=error_dict.get('message', None),
        )
