from github.scaffold import Scaffold
from github.types import GithubObject, Headers


class AuthenticateUser(Scaffold):
    def authenticate_user(self) -> bool:
        response = self.get_with_token(url=f'https://api.github.com/user')
        if response.ok:
            json_res = response.json()
            self.user = GithubObject._parse(json_res)
            self.headers = Headers._parse(dict(response.headers))
            self.is_authenticated = True
            return True
        else:
            self.is_authenticated = False
            # todo: raise error
            pass

        return False
