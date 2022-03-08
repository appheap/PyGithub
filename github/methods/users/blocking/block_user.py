from github.scaffold import Scaffold
from github.types import Response


class BlockUser(Scaffold):
    """
    Block a user
    """

    def block_user(
            self,
            *,
            username: str,
    ) -> 'Response':
        """
        Block a user


        :param username: Username of the user to be followed


        :return: 'Response'
        """
        response = self.put_with_token(
            url=f'https://api.github.com/user/blocks/{username}',
        )
        if response.status_code in (204, 304):
            # Status: 204 No Content
            # Status: 304 Not Modified => the person is already blocked by the authenticated user
            return Response._parse(
                response=response,
                success=True,
                description='the person is already blocked by the authenticated user' if response.status_code == 304 else None,
            )
        elif response.status_code in (404, 403, 401,422):
            #  Status: 422 Unprocessable Entity
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
