import json

import requests

from github.scaffold import Scaffold


class DeleteWithToken(Scaffold):
    def delete_with_token(
            self,
            *,
            url: str,
            data: dict = None,
    ) -> 'requests.Response':
        response = requests.delete(
            url,
            headers=self._default_headers,
            data=json.dumps(data) if data else None
        )
        return response
