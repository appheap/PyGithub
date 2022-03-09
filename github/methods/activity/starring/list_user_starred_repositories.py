from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class ListUserStarredRepositories(Scaffold):
    """
    List repositories starred by a user
    """

    def list_user_starred_repositories(
            self,
            *,
            username: str,
            sort: str = 'created',
            direction: str = 'desc',
            per_page: int = 100,
            page: int = 1,
    ) -> 'Response':
        """
        Lists the people that have starred the repository.

        :param username: Username of the user

        :param sort: One of "created" (when the repository was starred) or "updated" (when it was last pushed to). Default: "created"

        :param direction: One of "asc" (ascending) or "desc" (descending). Default: "desc"

        :param per_page:
            Results per page (max "100")
            Default: "30"

        :param page:
            Page number of the results to fetch.
            Default: "1"

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/users/{username}/starred',
            params={
                'sort': sort,
                'direction': direction,
                'per_page': per_page,
                'page': page,
            },
            headers={
                'Accept': 'application/vnd.github.v3.star+json',
            }
        )

        if response.status_code == 200:
            return Response._parse(
                response=response,
                success=True,
                result=utils.parse_repositories_with_starred_at(response.json()),
            )
        elif response.status_code in (304, 401, 403,):
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
