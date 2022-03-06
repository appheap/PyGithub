from github.scaffold import Scaffold
from github.types import Response


class IsUserFollowed(Scaffold):
    """
    Check if a person is followed by the authenticated user
    """

    def is_user_followed(
            self,
            *,
            username: str,
    ) -> 'Response':
        """
        Check if a person is followed by the authenticated user


        :param username: Username of the user to be checked


        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/user/following/{username}',
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
            # if the person is not followed by the authenticated user
            return Response._parse(
                response=response,
                success=True,
                result=False,
                description='the person is not followed by the authenticated user'
            )
        elif response.status_code in (304, 403, 401):
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
