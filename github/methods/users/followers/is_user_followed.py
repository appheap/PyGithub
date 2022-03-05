from typing import Tuple, List, Union

from github.scaffold import Scaffold
from github.types import SimpleUser, Response


class IsUserFollowed(Scaffold):
    """
    Check if a person is followed by the authenticated user
    """

    def is_user_followed(
            self,
            *,
            username: str,
    ) -> Tuple['bool', Union['bool', 'Response']]:
        """
        Check if a person is followed by the authenticated user


        :param username: Username of the user to be checked


        :return: Tuple['bool', Union['bool', 'Response']]
        """
        response = self.get_with_token(
            url=f'https://api.github.com/user/following/{username}',
        )
        if response.status_code == 204:
            # Status: 204 No Content
            return True, True
        elif response.status_code == 404:
            # if the person is not followed by the authenticated user
            return True, False
        elif response.status_code in (304, 403, 401):
            return False, Response._parse(response.status_code, response.json(), getattr(response, 'message', None))
        else:
            return False, Response._parse(response.status_code, response.json(), getattr(response, 'message', None))
