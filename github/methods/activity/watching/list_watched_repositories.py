from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class ListWatchedRepositories(Scaffold):
    """
    List repositories watched by the authenticated user
    """

    def list_watched_repositories(
            self,
            *,
            per_page: int = 100,
            page: int = 1,
    ) -> 'Response':
        """
        Lists repositories the authenticated user is watching.

        :param per_page:
            Results per page (max "100")
            Default: "30"

        :param page:
            Page number of the results to fetch.
            Default: "1"

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/user/subscriptions',
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
        elif response.status_code in (304, 401, 403):
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
