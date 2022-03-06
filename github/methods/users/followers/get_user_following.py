from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class GetUserFollowing(Scaffold):
    """
    List the people a user follows
    """

    def get_user_following(
            self,
            *,
            username: str,
            per_page: int = 100,
            page: int = 1
    ) -> 'Response':
        """
        Lists the people who the specified user follows.


        :param username: Username of the user

        :param per_page: Results per page (max 100) Default: 30

        :param page: Page number of the results to fetch. Default: 1

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/users/{username}/following',
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
