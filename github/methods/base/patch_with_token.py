import json

import requests

from github.scaffold import Scaffold


class PatchWithToken(Scaffold):
    def patch_with_token(
            self,
            *,
            url: str,
            data: dict = None,
    ) -> 'requests.Response':
        response = requests.patch(
            url,
            headers=self._default_headers,
            data=json.dumps(data)
        )
        return response
