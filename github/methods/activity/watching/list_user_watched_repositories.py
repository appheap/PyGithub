from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class ListUserWatchedRepositories(Scaffold):
    """
    List repositories watched by a user
    """

    def list_user_watched_repositories(
            self,
            *,
            username: str,
            per_page: int = 100,
            page: int = 1,
    ) -> 'Response':
        """
        Lists repositories a user is watching.

        :param username: Username of the user

        :param per_page:
            Results per page (max "100")
            Default: "30"

        :param page:
            Page number of the results to fetch.
            Default: "1"

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/users/{username}/subscriptions',
            params={
                'per_page': per_page,
                'page': page,
            },
        )

        if response.status_code == 200:
            return Response._parse(
                response=response,
                success=True,
                result=utils.parse_minimal_repositories(response.json()),
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
