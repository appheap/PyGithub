from typing import Optional, List

from .object import Object
from .github_error import GithubError


class GithubResponse(Object):
    def __init__(
            self,
            *,
            message: str = None,
            errors: Optional[List['GithubError']] = None,
    ):
        self.message = message
        self.errors = errors

    @staticmethod
    def _parse(response_dict: dict) -> Optional['GithubResponse']:
        if response_dict is None or not len(response_dict):
            return None

        error_dicts = response_dict.get('errors', None)
        errors = []
        if error_dicts:
            for error_dict in error_dicts:
                github_error = GithubError._parse(error_dict)
                if github_error:
                    errors.append(github_error)

        return GithubResponse(
            message=response_dict.get('message', None),
            errors=errors if len(errors) else None,
        )
