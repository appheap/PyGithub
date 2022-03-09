from github.scaffold import Scaffold
from github.types import Response


class UnstarRepository(Scaffold):
    """
    Unstar a repository for the authenticated user
    """

    def unstar_repository(
            self,
            *,
            owner: str,
            repo: str,
    ) -> 'Response':
        """
        Unstar a repository for the authenticated user

        :param owner: Username of the user

        :param repo: Name of the repository

        :return: 'Response'
        """
        response = self.delete_with_token(
            url=f'https://api.github.com/user/starred/{owner}/{repo}',
        )

        if response.status_code in (204, 304):
            return Response._parse(
                response=response,
                success=True,
                result=True,
            )
        elif response.status_code in (401, 403, 404):
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
