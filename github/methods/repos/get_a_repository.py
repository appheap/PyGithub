from github.scaffold import Scaffold
from github.types import Response, FullRepository


class GetARepository(Scaffold):
    """
    Get a repository
    """

    def get_a_repository(
            self,
            *,
            owner: str,
            repo: str,
    ) -> 'Response':
        """
        The "parent" and "source" objects are present when the repository is a fork.
        "parent" is the repository this repository was forked from, "source" is the ultimate source for the network.

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/repos/{owner}/{repo}',
        )

        if response.status_code == 200:
            return Response._parse(
                response=response,
                success=True,
                result=FullRepository._parse(response.json())
            )
        elif response.status_code in (301, 403, 404):
            return Response._parse(
                response=response,
                success=False,
            )
