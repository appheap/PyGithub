from github.scaffold import Scaffold
from github.types import Response


class FollowUser(Scaffold):
    """
    Follow a user
    """

    def follow_user(
            self,
            *,
            username: str,
    ) -> 'Response':
        """
        Follow a user

        Following a user requires the user to be logged in and authenticated with basic auth or OAuth with the `user:follow` scope.


        :param username: Username of the user to be followed


        :return: 'Response'
        """
        response = self.put_with_token(
            url=f'https://api.github.com/user/following/{username}',
        )
        if response.status_code in (204, 304):
            # Status: 204 No Content
            # Status: 304 Not Modified => the person is already followed by the authenticated user
            return Response._parse(
                response=response,
                success=True,
                description='the person is already followed by the authenticated user' if response.status_code == 304 else None,
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
