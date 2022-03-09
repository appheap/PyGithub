from github.scaffold import Scaffold
import requests
import json

class PostWithToken(Scaffold):
    def post_with_token(
            self,
            *,
            url: str,
            data: dict = None,
    ) -> 'requests.Response':
        response = requests.post(url, headers=self._default_headers, data=json.dumps(data))
        return response
