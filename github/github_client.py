from typing import Optional

from github.methods import Methods
from github.types import Headers, Object, PrivateUser
from .scaffold import Scaffold


class GithubClient(Methods, Scaffold, Object):
    username: Optional['str']
    token: Optional['str']

    user: Optional['PrivateUser']
    headers: Optional['Headers']
    _is_authenticated: bool
    _default_headers: dict
    _default_params: dict

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

        self._default_headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3.full+json',
        }
        self._default_params = {
            'i': ''
        }

        if self.auto_auth:
            self.authenticate_user()
