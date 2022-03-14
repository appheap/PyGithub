from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class ListUserRepositories(Scaffold):
    """
    List repositories for a user
    """

    def list_user_repositories(
            self,
            *,
            username: str = None,
            type: str = 'all',
            sort: str = 'updated',
            direction: str = 'desc',
            per_page: int = 100,
            page: int = None,
    ) -> 'Response':
        """
        Lists public repositories for the specified user. Note: For GitHub AE, this endpoint will list internal repositories for the specified user.

        :param username:
            Username of the User

        :param type:
            Can be one of "all", "owner", "member".
            Default: "owner"

        :param sort:
            Can be one of "created", "updated", "pushed", "full_name".
            Default: "full_name"

        :param direction:
            Can be one of "asc" or "desc". Default: "asc" when using "full_name", otherwise "desc"

        :param per_page:
            Results per page (max "100")
            Default: "30"

        :param page:
            Page number of the results to fetch.
            Default: "1"

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/users/{username}/repos',
            params={
                'type': type,
                'sort': sort,
                'direction': direction,
                'per_page': per_page,
                'page': page,
            }
        )

        if response.status_code == 200:
            return Response._parse(
                response=response,
                success=True,
                result=utils.parse_repositories(response.json())
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
