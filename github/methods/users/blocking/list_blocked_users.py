from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class ListBlockedUsers(Scaffold):
    """
    List users blocked by the authenticated user
    """

    def list_blocked_users(
            self,
    ) -> 'Response':
        """
        List the users you've blocked on your personal account.


        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/user/blocks',
        )
        if response.status_code == 200:
            return Response._parse(
                response=response,
                success=True,
                result=utils.parse_simple_users(response.json()),
            )
        elif response.status_code in (304, 404, 403, 401, 415):
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
