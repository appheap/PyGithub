from github.scaffold import Scaffold
from github.types import Response, RateLimitOverview


class GetRateLimitStatus(Scaffold):
    """
    Get rate limit status for the authenticated user
    """

    def get_rate_limit_status(self) -> 'Response':
        """
        Get rate limit status for the authenticated user
        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/rate_limit',
        )

        if response.status_code == 200:
            return Response._parse(
                response=response,
                success=True,
                result=RateLimitOverview._parse(response.json())
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
