from github.scaffold import Scaffold
import requests


class GetWithToken(Scaffold):
    def get_with_token(
            self,
            *,
            url: str,
            params: dict = None,
            headers: dict = None,
    ) -> 'requests.Response':
        params = {
            **self._default_params,
            **params
        } if params and len(params) else self._default_params

        if headers is None or not len(headers):
            response = requests.get(url, headers=self._default_headers, params=params)
        else:
            new_headers = self._default_headers.copy()
            new_headers.update(headers)
            response = requests.get(url, headers=new_headers, params=params)

        return response
