from github.scaffold import Scaffold
import requests
import json


class PutWithToken(Scaffold):
    def put_with_token(
            self,
            *,
            url: str,
    ) -> 'requests.Response':
        response = requests.put(
            url,
            headers={
                **self._headers,
                'Content-Length': "0",
            },
        )
        return response