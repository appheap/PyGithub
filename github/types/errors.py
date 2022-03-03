from dataclasses import dataclass

from .object import Object

RESPONSES = {
    -1: 'Unknown Error',
    422: 'Validation failed',
    304: 'Not modified',
    403: 'Forbidden',
    401: 'Requires authentication',
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
