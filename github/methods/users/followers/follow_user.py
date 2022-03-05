from typing import Tuple, List, Union

from github.scaffold import Scaffold
from github.types import SimpleUser, Response


class FollowUser(Scaffold):
    """
    Follow a user
    """

    def follow_user(
            self,
            *,
            username: str,
    ) -> Tuple['bool', Union['bool', 'Response']]:
        """
        Follow a user

        Following a user requires the user to be logged in and authenticated with basic auth or OAuth with the `user:follow` scope.


        :param username: Username of the user to be followed


        :return: Tuple['bool', Union['bool', 'Response']]
        """
        response = self.put_with_token(
            url=f'https://api.github.com/user/following/{username}',
        )
        if response.status_code in (204, 304):
            # Status: 204 No Content
            # Status: 304 Not Modified => the person is already followed by the authenticated user
            return True, True
        elif response.status_code in (404, 403, 401):
            return False, Response._parse(response.status_code, response.json(), getattr(response, 'message', None))
        else:
            return False, Response._parse(response.status_code, response.json(), getattr(response, 'message', None))