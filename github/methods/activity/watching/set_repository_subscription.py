from github.scaffold import Scaffold
from github.types import Response, RepositorySubscription


class SetRepositorySubscription(Scaffold):
    """
    Set a repository subscription
    """

    def set_repository_subscription(
            self,
            *,
            owner: str,
            repo: str,
            subscribed: bool = True,
            ignored: bool = True,
    ) -> 'Response':
        """
        Set a repository subscription

        If you would like to watch a repository, set subscribed to true. If you would like to ignore notifications made within a repository, set ignored to true. If you would like to stop watching a repository, delete the repository's subscription completely.

        :param owner: Username of the user

        :param repo: Name of the organization

        :param subscribed: Determines if notifications should be received from this repository.

        :param ignored: Determines if all notifications should be blocked from this repository.

        :return: 'Response'
        """
        response = self.put_with_token(
            url=f'https://api.github.com/repos/{owner}/{repo}/subscription',
            params={
                'subscribed': subscribed,
                'ignored': ignored,
            }
        )

        if response.status_code == 200:
            return Response._parse(
                response=response,
                success=True,
                result=RepositorySubscription._parse(response.json()),
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
