from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class ListNetworkRepositoryEvents(Scaffold):
    """
    List public events for a network of repositories
    """

    def list_network_repository_events(
            self,
            *,
            owner: str,
            repo: str,
            per_page: int = 100,
            page: int = None,
    ) -> 'Response':
        """
        List public events for a network of repositories

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
            url=f'https://api.github.com/networks/{owner}/{repo}/events',
            params={
                'per_page': per_page,
                'page': page,
            }
        )

        if response.status_code in (200, 304):
            return Response._parse(
                response=response,
                success=True,
                result=utils.parse_events(response.json()),
            )
        elif response.status_code in (301, 403, 404):
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
