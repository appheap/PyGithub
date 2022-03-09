from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class ListUserOrganizationEvents(Scaffold):
    """
    List organization events for the authenticated user
    """

    def list_user_organization_events(
            self,
            *,
            username: str,
            org: str,
            per_page: int = 100,
            page: int = 1,
    ) -> 'Response':
        """
        This is the user's organization dashboard. You must be authenticated as the user to view this.

        :param username: Username of the user

        :param org: Name of the organization

        :param per_page:
            Results per page (max "100")
            Default: "30"

        :param page:
            Page number of the results to fetch.
            Default: "1"

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/users/{username}/events/orgs/{org}',
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
