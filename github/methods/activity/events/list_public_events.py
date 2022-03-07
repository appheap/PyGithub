from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class ListPublicEvents(Scaffold):
    """
    List public events
    """

    def list_public_events(
            self,
            *,
            per_page: int = 100,
            page: int = None,
    ) -> 'Response':
        """
        We delay the public events feed by five minutes, which means the most recent event returned by the public events API actually occurred at least five minutes ago.

        :param per_page:
            Results per page (max "100")
            Default: "30"

        :param page:
            Page number of the results to fetch.
            Default: "1"

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/events',
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
        elif response.status_code in (403, 503):
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
