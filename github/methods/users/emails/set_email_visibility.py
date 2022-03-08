from github.scaffold import Scaffold
from github.types import Response


class SetEmailVisibility(Scaffold):
    """
    Set primary email visibility for the authenticated user
    """
    _options = [
        "public",
        "private"
    ]

    def set_email_visibility(
            self,
            *,
            visibility: str,
    ) -> 'Response':
        """
        Sets the visibility for your primary email addresses.


        :param visibility: Required. Denotes whether an email is publicly visible.


        :return: 'Response'
        """
        if visibility not in self._options:
            raise ValueError('visibility value should be one of these values:' + str(self._options))

        response = self.patch_with_token(
            url=f'https://api.github.com/user/email/visibility',
            data={
                'visibility': visibility
            }
        )
        if response.status_code in (200, 204):
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
