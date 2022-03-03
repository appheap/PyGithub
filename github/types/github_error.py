from typing import Optional

from .object import Object


class GithubError(Object):
    def __init__(
            self,
            *,
            resource: str = None,
            code: str = None,
            field: str = None,
            message: str = None,
    ):
        self.resource = resource
        self.code = code
        self.field = field
        self.message = message

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
