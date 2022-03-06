from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class GetFollowing(Scaffold):
    """
    List the people the authenticated user follows
    """

    def get_following(
            self,
            *,
            per_page: int = 100,
            page: int = 1
    ) -> 'Response':
        """
        Lists the people who the authenticated user follows.


        :param per_page: Results per page (max 100) Default: 30

        :param page: Page number of the results to fetch. Default: 1

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/user/following',
            params={
                'per_page': per_page,
                'page': page,
            }
        )
        if response.status_code == 200:
            return Response._parse(
                response=response,
                success=True,
                result=utils.parse_simple_users(response.json()),
            )
        elif response.status_code in (304, 403, 401):
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
