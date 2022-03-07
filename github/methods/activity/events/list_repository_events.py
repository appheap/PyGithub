from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class ListRepositoryEvents(Scaffold):
    """
    List repository events
    """

    def list_repository_events(
            self,
            *,
            owner: str,
            repo: str,
            per_page: int = 100,
            page: int = None,
    ) -> 'Response':
        """
        List repository events

        :param owner:

        :param repo:

        :param per_page:
            Results per page (max "100")
            Default: "30"

        :param page:
            Page number of the results to fetch.
            Default: "1"

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/repos/{owner}/{repo}/events',
            params={
                'per_page': per_page,
                'page': page,
            }
        )

        if response.status_code == 200:
            return Response._parse(
                response=response,
                success=True,
                result=utils.parse_events(response.json()),
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
