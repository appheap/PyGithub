from dataclasses import dataclass

from .object import Object

RESPONSES = {
    -1: 'Unknown Error',
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
class Response(Object):
    code: int
    description: str

    @staticmethod
    def _parse(code: int = -1):
        if RESPONSES.get(code, None):
            return Response(
                code=code,
                description=RESPONSES[code]
            )
        else:
            return Response(
                code=-1,
                description=RESPONSES[-1]
            )

    @staticmethod
    def _parse_unknown(status_code: int, message: str) -> 'Response':
        return Response(
            code=status_code,
            description=message
        )
