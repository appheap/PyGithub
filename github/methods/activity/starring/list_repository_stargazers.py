from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class ListRepositoryStargazers(Scaffold):
    """
    List organization events for the authenticated user
    """

    def list_repository_stargazers(
            self,
            *,
            owner: str,
            repo: str,
            per_page: int = 100,
            page: int = 1,
    ) -> 'Response':
        """
        Lists the people that have starred the repository.

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
            url=f'https://api.github.com/repos/{owner}/{repo}/stargazers',
            params={
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
                result=utils.parse_stargazers(response.json()),
            )
        elif response.status_code == 422:
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
