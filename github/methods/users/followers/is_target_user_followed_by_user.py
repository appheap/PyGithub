from typing import Tuple, Union

from github.scaffold import Scaffold
from github.types import Response


class IsTargetUserFollowedByUser(Scaffold):
    """
    Check if a user follows another user
    """

    def is_target_user_followed_by_user(
            self,
            *,
            username: str,
            target_user: str,
    ) -> Tuple['bool', Union['bool', 'Response']]:
        """
        Check if a user follows another user


        :param username: Username of the user to be checked
        :param target_user: Username of the target to be checked


        :return: Tuple['bool', Union['bool', 'Response']]
        """
        response = self.get_with_token(
            url=f'https://api.github.com/users/{username}/following/{target_user}',
        )
        if response.status_code == 204:
            # Status: 204 No Content => the user follows the target user
            return True, True
        elif response.status_code == 404:
            # Status: 404 Not Found => the user does not follow the target user
            return True, False
        else:
            return False, Response._parse(response.status_code, response.json(), getattr(response, 'message', None))
