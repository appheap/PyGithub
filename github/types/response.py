from dataclasses import dataclass
from typing import Optional, List, Union, Container

import requests

from .github_error import GithubError
from .object import Object

STATUS_CODES_MAPPING = {
    -1: 'Unknown Error',
    200: 'OK',
    204: 'No Content',
    301: 'Moved permanently',
    304: 'Not modified',
    401: 'Requires authentication',
    403: 'Forbidden',
    404: 'Not Found',
    415: 'Preview header missing',
    422: 'Validation failed',
    503: 'Service unavailable',
    1: 'Resource not found',
    2: 'Validation failed',
    3: 'Bad Request',
    4: 'Accepted',
    5: 'Preview header missing',
    6: 'Not modified',
    7: 'Gone',
}


@dataclass
class Response(Object):
    success: bool
    status_code: int
    reason: Optional['str']
    message: Optional['str']
    errors: Optional[List['GithubError']]

    result: Optional[Union['object', 'Object', List['Object'], Container[Union['Object', 'object']]]]
    description: Optional['str']

    @staticmethod
    def _parse(
            response: 'requests.Response',

            success: bool,
            description: Optional['str'] = None,
            result: Optional[Union['object', 'Object', List['Object'], Container[Union['Object', 'object']]]] = None,
    ):
        try:
            response_dict = response.json()
        except Exception as e:
            response_dict = None
        errors_dict = response_dict.get('errors', None) if type(response_dict) == dict else None

        errors = []
        if errors_dict is not None:
            for error_dict in errors_dict:
                github_error = GithubError._parse(error_dict)
                if github_error:
                    errors.append(github_error)

        message = getattr(response, 'message', None)
        status_code = response.status_code

        if message is not None:
            if STATUS_CODES_MAPPING.get(status_code, None) == message:
                return Response(
                    status_code=status_code,
                    message=STATUS_CODES_MAPPING[status_code],
                    reason=response.reason,
                    errors=errors if len(errors) else None,

                    result=result,
                    description=description,
                    success=success,
                )
            else:
                return Response(
                    status_code=status_code,
                    message=message,
                    reason=response.reason,
                    errors=errors if len(errors) else None,

                    result=result,
                    description=description,
                    success=success,
                )
        else:
            if STATUS_CODES_MAPPING.get(status_code, None):
                return Response(
                    status_code=status_code,
                    message=STATUS_CODES_MAPPING[status_code],
                    reason=response.reason,
                    errors=errors if len(errors) else None,

                    result=result,
                    description=description,
                    success=success,
                )
            else:
                return Response(
                    status_code=-1,
                    message=STATUS_CODES_MAPPING[-1],
                    reason=response.reason,
                    errors=errors if len(errors) else None,

                    result=result,
                    description=description,
                    success=success,
                )
