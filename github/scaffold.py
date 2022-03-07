from typing import Optional, Tuple, Union

import requests
from github import types
from github.types import GithubObject, Headers, Response


class Scaffold:
    user: Optional['types.GithubObject']
    headers: Optional['types.Headers']
    _is_authenticated: bool

    def __init__(self):
        pass

    def get_with_token(
            self,
            *,
            url: str,
            params: dict = None,
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
    ) -> Tuple[bool, Union[Tuple[Optional['GithubObject'], Optional['Headers']], 'Response']]:
        pass
