from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class ListRepositoryWatchers(Scaffold):
    """
    List watchers
    """

    def list_repository_watchers(
            self,
            *,
            owner: str,
            repo: str,
            per_page: int = 100,
            page: int = 1,
    ) -> 'Response':
        """
        Lists the people watching the specified repository.

        :param owner: Username of the user

        :param repo: Name of the organization

        :param per_page:
            Results per page (max "100")
            Default: "30"

        :param page:
            Page number of the results to fetch.
            Default: "1"

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/repos/{owner}/{repo}/subscribers',
            params={
                'per_page': per_page,
                'page': page,
            },
        )

        if response.status_code == 200:
            return Response._parse(
                response=response,
                success=True,
                result=utils.parse_simple_users(response.json()),
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
