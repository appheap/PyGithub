from typing import Optional

import requests

from github import types
from github.types import Response


class Scaffold:
    user: Optional['types.PrivateUser']
    headers: Optional['types.Headers']
    _is_authenticated: bool
    _default_headers: dict
    _default_params: dict

    def __init__(self):
        pass

    def get_with_token(
            self,
            *,
            url: str,
            params: dict = None,
            headers: dict = None,
    ) -> 'requests.Response':
        pass

    def post_with_token(
            self,
            *,
            url: str,
            data: dict = None,
    ) -> 'requests.Response':
        pass

    def put_with_token(
            self,
            *,
            url: str,
            data: dict = None,
            params: dict = None,
    ) -> 'requests.Response':
        pass

    def delete_with_token(
            self,
            *,
            url: str,
            data: dict = None,
    ) -> 'requests.Response':
        pass

    def patch_with_token(
            self,
            *,
            url: str,
            data: dict = None,
    ) -> 'requests.Response':
        pass

    def get_authenticated_user_info(
            self,
    ) -> 'Response':
        pass
