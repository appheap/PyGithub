from typing import Optional, Tuple

from github.scaffold import Scaffold
from github.types import GithubObject, Headers


class GetMyInfo(Scaffold):
    def get_my_info(self) -> Tuple[Optional['GithubObject'], Optional['Headers']]:
        response = self.get_with_token(url=f'https://api.github.com/user')
        if response.ok:
            json_res = response.json()
            user = GithubObject._parse(json_res)
            headers = Headers._parse(dict(response.headers))
            return user, headers

        return None, None
