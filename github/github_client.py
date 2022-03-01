from typing import Optional

from github.methods import Methods
from github.types import GithubObject, Headers, Object
from .scaffold import Scaffold


class GithubClient(Methods, Scaffold, Object):
    username: Optional['str']
    token: Optional['str']

    user: Optional['GithubObject']
    headers: Optional['Headers']

    def __init__(self, *, login: str = None, token: str = None) -> None:
        super().__init__()

        self.username = login
        self.token = token

        self._headers = {
            'Authorization': f'token {self.token}',
        }
        self._default_params = {
            'i': ''
        }

        self._init_user()

    def _init_user(self):
        users, headers = self.get_my_info()
        if users and headers:
            self.users = users
            self.headers = headers
        else:
            # todo: raise error
            pass
