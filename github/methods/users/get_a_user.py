from github.scaffold import Scaffold
from github.types import Response, PublicUser, PrivateUser


class GetAUser(Scaffold):
    """
    Get a user
    """

    def get_a_user(
            self,
            *,
            username: str
    ) -> 'Response':
        """
        Provides publicly available information about someone with a GitHub account.

        :return: 'Response'
        """
        response = self.get_with_token(url=f'https://api.github.com/users/{username}')
        if response.status_code == 200:
            json_res = response.json()

            return Response._parse(
                response=response,
                success=True,
                result=PrivateUser._parse(json_res) if 'two_factor_authentication' in json_res.keys() \
                    else PublicUser._parse(json_res)
            )
        elif response.status_code == 404:
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
