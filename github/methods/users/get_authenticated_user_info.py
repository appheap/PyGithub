from github.scaffold import Scaffold
from github.types import Headers, Response, PublicUser, PrivateUser


class GetAuthenticatedUserInfo(Scaffold):
    """
    Get the authenticated user
    """

    def get_authenticated_user_info(
            self,
    ) -> 'Response':
        """
        If the authenticated user is authenticated through basic authentication or OAuth with the user scope, then the response lists public and private profile information.

        If the authenticated user is authenticated through OAuth without the user scope, then the response lists only public profile information.

        :return: 'Response'
        """
        response = self.get_with_token(url=f'https://api.github.com/user')
        if response.status_code == 200:
            json_res = response.json()
            user = PrivateUser._parse(json_res) if 'two_factor_authentication' in json_res.keys() \
                else PublicUser._parse(json_res)

            headers = Headers._parse(dict(response.headers))
            return Response._parse(
                response=response,
                success=True,
                result=(user, headers)
            )
        elif response.status_code in (304, 401, 404,):
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
