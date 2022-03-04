from dataclasses import dataclass
from typing import Optional, List

from .object import Object

RESPONSES = {
    -1: 'Unknown Error',
    301: 'Moved permanently',
    422: 'Validation failed',
    304: 'Not modified',
    401: 'Requires authentication',
    403: 'Forbidden',
    404: 'Not Found',
    1: 'Resource not found',
    2: 'Validation failed',
    3: 'Bad Request',
    4: 'Accepted',
    5: 'Preview header missing',
    6: 'Not modified',
    7: 'Gone',
}


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


@dataclass
class Response(Object):
    code: int
    description: str
    errors: Optional[List['GithubError']]

    @staticmethod
    def _parse(status_code: int, response_dict: dict, message: str):
        errors_dict = response_dict.get('errors', None)

        errors = []
        if errors_dict:
            for error_dict in errors_dict:
                github_error = GithubError._parse(error_dict)
                if github_error:
                    errors.append(github_error)

        if message is not None:
            if RESPONSES.get(status_code, None) == message:
                return Response(
                    code=status_code,
                    description=RESPONSES[status_code],
                    errors=errors if len(errors) else None,
                )
            else:
                return Response(
                    code=status_code,
                    description=message,
                    errors=errors if len(errors) else None,
                )
        else:
            if RESPONSES.get(status_code, None):
                return Response(
                    code=status_code,
                    description=RESPONSES[status_code],
                    errors=errors if len(errors) else None,
                )
            else:
                return Response(
                    code=-1,
                    description=RESPONSES[-1],
                    errors=errors if len(errors) else None,
                )
