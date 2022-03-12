from github.scaffold import Scaffold
from github.types import Response, SearchTopicsResult


class SearchTopics(Scaffold):
    """
    Search topics
    """

    def search_topics(
            self,
            *,
            q: str,
            per_page: int = 100,
            page: int = 1,
    ) -> 'Response':
        """
       Find topics via various criteria. Results are sorted by best match.


        :param q: The query contains one or more search keywords and qualifiers.
        Qualifiers allow you to limit your search to specific areas of GitHub.
        The REST API supports the same qualifiers as GitHub.com.

        :param per_page:
            Results per page (max "100")
            Default: "30"

        :param page:
            Page number of the results to fetch.
            Default: "1"

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/search/topics',
            params={
                'q': q,
                'per_page': per_page,
                'page': page,
            }
        )

        if response.status_code == 200:
            return Response._parse(
                response=response,
                success=True,
                result=SearchTopicsResult._parse(response.json()),
            )
        elif response.status_code == 304:
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
