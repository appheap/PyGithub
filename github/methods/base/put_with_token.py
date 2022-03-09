import requests

from github.scaffold import Scaffold


class PutWithToken(Scaffold):
    def put_with_token(
            self,
            *,
            url: str,
    ) -> 'requests.Response':
        response = requests.put(
            url,
            headers={
                **self._default_headers,
                'Content-Length': "0",
            },
        )
        return response
