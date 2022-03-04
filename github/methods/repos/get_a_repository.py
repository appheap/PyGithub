from typing import Union

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
    ) -> Union['FullRepository', 'Response']:
        """
        The "parent" and "source" objects are present when the repository is a fork.
        "parent" is the repository this repository was forked from, "source" is the ultimate source for the network.

        :return: Union['Repository', 'Response']
        """
        response = self.get_with_token(
            url=f'https://api.github.com/repos/{owner}/{repo}',
        )

        if response.status_code == 200:
            return FullRepository._parse(response.json())
        elif response.status_code == 301:
            return Response._parse(response.status_code, response.json(), getattr(response, 'message', None))
        elif response.status_code == 403:
            return Response._parse(response.status_code, response.json(), getattr(response, 'message', None))
        elif response.status_code == 404:
            return Response._parse(response.status_code, response.json(), getattr(response, 'message', None))
        else:
            return Response._parse(response.status_code, response.json(), getattr(response, 'message', None))
