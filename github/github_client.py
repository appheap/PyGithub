from typing import Optional

from github.methods import Methods
from github.types import GithubObject, Headers, Object
from .scaffold import Scaffold


class GithubClient(Methods, Scaffold, Object):
    username: Optional['str']
    token: Optional['str']

    user: Optional['GithubObject']
    headers: Optional['Headers']
    _is_authenticated: bool

    def __init__(
            self,
            *,
            login: str = None,
            token: str = None,

            auto_auth: bool = True,
    ) -> None:
        super().__init__()

        self.username = login
        self.token = token

        self.auto_auth = auto_auth
        self._is_authenticated = False

        self._headers = {
            'Authorization': f'token {self.token}',
        }
        self._default_params = {
            'i': ''
        }
