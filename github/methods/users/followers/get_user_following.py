from typing import Tuple, List, Union

from github.scaffold import Scaffold
from github.types import SimpleUser, Response


class GetUserFollowing(Scaffold):
    """
    List the people a user follows
    """

    def get_user_following(
            self,
            *,
            username: str,
            per_page: int = 100,
            page: int = 1
    ) -> Tuple['bool', Union[List['SimpleUser'], 'Response']]:
        """
        Lists the people who the specified user follows.


        :param username: Username of the user

        :param per_page: Results per page (max 100) Default: 30

        :param page: Page number of the results to fetch. Default: 1

        :return: Tuple['bool', Union[List['SimpleUser'], 'Response']]
        """
        response = self.get_with_token(
            url=f'https://api.github.com/users/{username}/following',
            params={
                'per_page': per_page,
                'page': page,
            }
        )
        if response.status_code == 200:
            users = []
            for user_dict in response.json():
                user = SimpleUser._parse(user_dict)
                if user_dict is not None and len(user_dict):
                    users.append(user)
            return True, users
        else:
            return False, Response._parse(response.status_code, response.json(), getattr(response, 'message', None))
