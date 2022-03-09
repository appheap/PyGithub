from github.scaffold import Scaffold
import requests


class GetWithToken(Scaffold):
    def get_with_token(
            self,
            *,
            url: str,
            params: dict = None,
    ) -> 'requests.Response':
        params = {
            **self._default_params,
            **params
        } if params and len(params) else self._default_params

        response = requests.get(url, headers=self._default_headers, params=params)
        return response
