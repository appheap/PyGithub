from github.scaffold import Scaffold
from github.types import Response


class UnfollowUser(Scaffold):
    """
    Unfollow a user
    """

    def unfollow_user(
            self,
            *,
            username: str,
    ) -> 'Response':
        """
        Unfollow a user

        Unfollowing a user requires the user to be logged in and authenticated with basic auth or OAuth with the `user:follow` scope.


        :param username: Username of the user to be unfollowed


        :return: 'Response'
        """
        response = self.delete_with_token(
            url=f'https://api.github.com/user/following/{username}',
        )
        if response.status_code in (204, 304):
            # Status: 204 No Content
            # Status: 304 Not Modified => the person is already unfollowed by the authenticated user
            return Response._parse(
                response=response,
                success=True,
                description='the person is already unfollowed by the authenticated user',
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
