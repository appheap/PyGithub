from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class GetRepositorySubscription(Scaffold):
    """
    Get a repository subscription
    """

    def get_repository_subscription(
            self,
            *,
            owner: str,
            repo: str,
    ) -> 'Response':
        """
        Get a repository subscription

        :param owner: Username of the user

        :param repo: Name of the organization

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/repos/{owner}/{repo}/subscription',
        )

        if response.status_code == 200:
            # if you subscribe to the repository
            return Response._parse(
                response=response,
                success=True,
                result=utils.parse_repository_subscription(response.json()),
            )
        elif response.status_code == 404:
            # Not Found if you don't subscribe to the repository
            return Response._parse(
                response=response,
                success=True,
                result=False
            )
        elif response.status_code == 403:
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
