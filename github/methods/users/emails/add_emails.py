from typing import List

from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class AddEmails(Scaffold):
    """
    Add an email address for the authenticated user
    """

    def add_emails(
            self,
            *,
            emails: List['str'],
    ) -> 'Response':
        """
        This endpoint is accessible with the `user` scope.

        :param emails: 	Required. Adds one or more email addresses to your GitHub account.
        Must contain at least one email address.
        Note: Alternatively, you can pass a single email address or an array of emails addresses directly, but we recommend that you pass an object using the emails key.


        :return: 'Response'
        """
        response = self.post_with_token(
            url=f'https://api.github.com/user/emails',
            data={
                'emails': emails,
            }
        )
        if response.status_code in (201, 304):
            # Status: 201 Created
            # Status: 304 Not Modified
            return Response._parse(
                response=response,
                success=True,
                result=utils.parse_emails(response.json()),
            )
        elif response.status_code in (404, 403, 401, 422):
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
