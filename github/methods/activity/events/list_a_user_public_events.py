from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class ListAUserPublicEvents(Scaffold):
    """
    List public events received by a user

    """

    def list_a_user_public_events(
            self,
            *,
            username: str,
            per_page: int = 100,
            page: int = 1,
    ) -> 'Response':
        """
        List public events received by a user

        :param username: Username of the user

        :param per_page:
            Results per page (max "100")
            Default: "30"

        :param page:
            Page number of the results to fetch.
            Default: "1"

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/users/{username}/received_events/public',
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
