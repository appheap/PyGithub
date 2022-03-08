from github.scaffold import Scaffold
from github.types import Response


class UnblockUser(Scaffold):
    """
    Unlock a user
    """

    def unblock_user(
            self,
            *,
            username: str,
    ) -> 'Response':
        """
        Unblock a user


        :param username: Username of the user to be followed


        :return: 'Response'
        """
        response = self.delete_with_token(
            url=f'https://api.github.com/user/blocks/{username}',
        )
        if response.status_code in (204, 304):
            # Status: 204 No Content
            # Status: 304 Not Modified => the person is already unblocked by the authenticated user
            return Response._parse(
                response=response,
                success=True,
                description='the person is already unblocked by the authenticated user' if response.status_code == 304 else None,
            )
        elif response.status_code in (404, 403, 401):
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
