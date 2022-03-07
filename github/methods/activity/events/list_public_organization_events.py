from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class ListPublicOrganizationEvents(Scaffold):
    """
    List public organization events
    """

    def list_public_organization_events(
            self,
            *,
            organization: str,
            per_page: int = 100,
            page: int = None,
    ) -> 'Response':
        """
        List public organization events

        :param organization:

        :param per_page:
            Results per page (max "100")
            Default: "30"

        :param page:
            Page number of the results to fetch.
            Default: "1"

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/orgs/{organization}/events',
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
