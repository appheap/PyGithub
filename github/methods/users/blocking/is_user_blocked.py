from github.scaffold import Scaffold
from github.types import Response


class IsUserBlocked(Scaffold):
    """
    Check if a user is blocked by the authenticated user
    """

    def is_user_blocked(
            self,
            *,
            username: str,
    ) -> 'Response':
        """
        Check if a user is blocked by the authenticated user


        :param username: Username of the user to be checked


        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/user/blocks/{username}',
        )
        if response.status_code == 204:
            # Status: 204 No Content
            return Response._parse(
                response=response,
                success=True,
                result=True,
                description='the person is followed by the authenticated user'
            )
        elif response.status_code == 404:
            # if the person is not blocked by the authenticated user
            return Response._parse(
                response=response,
                success=True,
                result=False,
                description='the person is not followed by the authenticated user'
            )
        elif response.status_code in (304, 403, 401,):
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
