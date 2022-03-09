from github.scaffold import Scaffold
from github.types import Response, RepositorySubscription


class DeleteRepositorySubscription(Scaffold):
    """
    Delete a repository subscription
    """

    def delete_repository_subscription(
            self,
            *,
            owner: str,
            repo: str,
    ) -> 'Response':
        """
        Delete a repository subscription


        This endpoint should only be used to stop watching a repository. To control whether or not you wish to receive notifications from a repository, set the repository's subscription manually.

        :param owner: Username of the user

        :param repo: Name of the organization

        :return: 'Response'
        """
        response = self.delete_with_token(
            url=f'https://api.github.com/repos/{owner}/{repo}/subscription',
        )

        if response.status_code == 204:
            return Response._parse(
                response=response,
                success=True,
                result=True,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
