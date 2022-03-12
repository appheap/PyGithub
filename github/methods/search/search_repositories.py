from github.scaffold import Scaffold
from github.types import Response, SearchRepositoriesResult


class SearchRepositories(Scaffold):
    """
    Search repositories
    """

    def search_repositories(
            self,
            *,
            q: str,
            sort: str = None,
            order: str = 'desc',
            per_page: int = 100,
            page: int = 1,
    ) -> 'Response':
        """
       Find repositories via various criteria.


        :param q: The query contains one or more search keywords and qualifiers.
        Qualifiers allow you to limit your search to specific areas of GitHub.
        The REST API supports the same qualifiers as GitHub.com.

        :param sort: Sorts the results of your query. Can only be "indexed", which indicates how recently a file has been indexed by the GitHub search infrastructure.
        Default: "best match"

        :param order: Determines whether the first search result returned is the highest number of matches ("desc") or lowest number of matches ("asc").
        This parameter is ignored unless you provide sort.
        Default: "desc"

        :param per_page:
            Results per page (max "100")
            Default: "30"

        :param page:
            Page number of the results to fetch.
            Default: "1"

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/search/repositories',
            params={
                'q': q,
                'sort': sort,
                'order': order,
                'per_page': per_page,
                'page': page,
            }
        )

        if response.status_code == 200:
            return Response._parse(
                response=response,
                success=True,
                result=SearchRepositoriesResult._parse(response.json()),
            )
        elif response.status_code in (304, 503, 422):
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
