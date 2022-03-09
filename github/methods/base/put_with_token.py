import json

import requests

from github.scaffold import Scaffold


class PutWithToken(Scaffold):
    def put_with_token(
            self,
            *,
            url: str,
            data: dict = None,
            params: dict = None,
    ) -> 'requests.Response':
        response = requests.put(
            url,
            headers={
                **self._default_headers,
                'Content-Length': "0",
            },
            data=json.dumps(data) if data else None,
            params=params,
        )
        return response
