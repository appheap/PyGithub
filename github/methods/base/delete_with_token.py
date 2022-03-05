from github.scaffold import Scaffold
import requests
import json


class DeleteWithToken(Scaffold):
    def delete_with_token(
            self,
            *,
            url: str,
    ) -> 'requests.Response':
        response = requests.delete(
            url,
            headers=self._headers
        )
        return response
