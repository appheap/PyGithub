from typing import Optional

import requests
from github import types


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
