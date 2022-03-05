from typing import Optional, Tuple, Union

from github.scaffold import Scaffold
from github.types import GithubObject, Headers, Response, PublicUser, PrivateUser


class GetAuthenticatedUserInfo(Scaffold):
    """
    Get the authenticated user
    """

    def get_authenticated_user_info(
            self,
    ) -> Tuple[bool, Union[Tuple[Union['PublicUser', 'PrivateUser'], Optional['Headers']], 'Response']]:
        """
        If the authenticated user is authenticated through basic authentication or OAuth with the user scope, then the response lists public and private profile information.

        If the authenticated user is authenticated through OAuth without the user scope, then the response lists only public profile information.

        :return: Tuple[bool, Union[Tuple[Optional['GithubObject'], Optional['Headers']], 'Response']]
        """
        response = self.get_with_token(url=f'https://api.github.com/user')
        if response.status_code == 200:
            json_res = response.json()
            user = PrivateUser._parse(json_res) if 'two_factor_authentication' in json_res.keys() \
                else PublicUser._parse(json_res)

            headers = Headers._parse(dict(response.headers))
            return True, (user, headers)
        elif response.status_code == 304:
            return False, Response._parse(response.status_code, response.json(), getattr(response, 'message', None))
        elif response.status_code == 401:
            return False, Response._parse(response.status_code, response.json(), getattr(response, 'message', None))
        elif response.status_code == 404:
            return False, Response._parse(response.status_code, response.json(), getattr(response, 'message', None))
        else:
            return False, Response._parse(response.status_code, response.json(), getattr(response, 'message', None))
