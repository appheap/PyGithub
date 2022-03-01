from typing import List, Optional

from github.scaffold import Scaffold
from github.types import Repository


class GetUserRepositories(Scaffold):
    """
    List repositories for a user
    """

    def get_user_repositories(
            self,
            *,
            username: str = None,
            type: str = 'all',
            sort: str = 'updated',
            direction: str = 'desc',
            per_page: int = 100,
            page: int = None,
    ) -> Optional[List['Repository']]:
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

        :return: List[`types.Repository`]
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

        repos: List[Repository] = []
        if response.ok:
            for repo_dict in response.json():
                repo = Repository._parse(repo_dict)
                if repo_dict is not None and len(repo_dict):
                    repos.append(repo)

        return repos