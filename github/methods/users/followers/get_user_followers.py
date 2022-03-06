from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class GetUserFollowers(Scaffold):
    """
    List followers of a user
    """

    def get_user_followers(
            self,
            *,
            username: str,
            per_page: int = 100,
            page: int = 1
    ) -> 'Response':
        """
        Lists the people following the specified user.


        :param username: Username of the user

        :param per_page: Results per page (max 100) Default: 30

        :param page: Page number of the results to fetch. Default: 1

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/users/{username}/followers',
            params={
                'per_page': per_page,
                'page': page,
            }
        )
        if response.status_code == 200:
            return Response._parse(
                response=response,
                success=True,
                result=utils.parse_simple_users(response.json())
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
