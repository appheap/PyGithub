from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class ListUsers(Scaffold):
    """
    List users
    """

    def list_users(
            self,
            *,
            since: int = None,
            per_page: int = 100
    ) -> 'Response':
        """
        Lists all users, in the order that they signed up on GitHub. This list includes personal user accounts and organization accounts.


        Note: Pagination is powered exclusively by the since parameter. Use the Link header to get the URL for the next page of users.

        :param since: A user ID. Only return users with an ID greater than this ID.

        :param per_page: Results per page (max 100) Default: 30

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/users',
            params={
                'since': since,
                'per_page': per_page,
            }
        )
        if response.status_code == 200:

            return Response._parse(
                response=response,
                success=True,
                result=utils.parse_simple_users(response.json()),
            )
        elif response.status_code == 304:
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
