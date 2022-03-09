from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class IsRepositoryStarredByMe(Scaffold):
    """
    Check if a repository is starred by the authenticated user
    """

    def is_repository_starred_by_me(
            self,
            *,
            owner: str,
            repo: str,
            per_page: int = 100,
            page: int = 1,
    ) -> 'Response':
        """
        Check if a repository is starred by the authenticated user

        :param owner: Username of the user

        :param repo: Name of the repository

        :param per_page:
            Results per page (max "100")
            Default: "30"

        :param page:
            Page number of the results to fetch.
            Default: "1"

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/user/starred/{owner}/{repo}',
            params={
                'per_page': per_page,
                'page': page,
            },
        )

        if response.status_code == 204:
            # Response if this repository is starred by you
            return Response._parse(
                response=response,
                success=True,
                result=True,
            )
        elif response.status_code == 404:
            return Response._parse(
                response=response,
                success=True,
                result=False,
            )
        elif response.status_code in (304, 401, 403):
            # Not Found if this repository is not starred by you
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
