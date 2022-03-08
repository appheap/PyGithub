from typing import List

from github.scaffold import Scaffold
from github.types import Response


class DeleteEmails(Scaffold):
    """
    Delete an email address for the authenticated user
    """

    def delete_emails(
            self,
            *,
            emails: List['str'],
    ) -> 'Response':
        """
        This endpoint is accessible with the `user` scope.

        :param emails: 	Required. Email addresses associated with the GitHub user account.

        :return: 'Response'
        """
        response = self.delete_with_token(
            url=f'https://api.github.com/user/emails',
            data={
                'emails': emails,
            }
        )
        if response.status_code in (204, 304):
            # Status: 204 No Content
            # Status: 304 Not Modified
            return Response._parse(
                response=response,
                success=True,
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
