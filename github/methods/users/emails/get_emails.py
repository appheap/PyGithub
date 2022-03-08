from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class GetEmails(Scaffold):
    """
    List email addresses for the authenticated user
    """

    def get_emails(
            self,
            *,
            per_page: int = 100,
            page: int = 1
    ) -> 'Response':
        """
        Lists all of your email addresses, and specifies which one is visible to the public. This endpoint is accessible with the `user:email` scope.


        :param per_page: Results per page (max 100) Default: 30

        :param page: Page number of the results to fetch. Default: 1

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/user/emails',
            params={
                'per_page': per_page,
                'page': page,
            }
        )
        if response.status_code == 200:
            return Response._parse(
                response=response,
                success=True,
                result=utils.parse_emails(response.json()),
            )
        elif response.status_code in (304, 403, 401, 404):
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
