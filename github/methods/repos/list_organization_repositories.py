from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class ListOrganizationRepositories(Scaffold):
    """
    List organization repositories
    """

    def list_organization_repositories(
            self,
            *,
            organization: str = None,
            type: str = 'all',
            sort: str = 'updated',
            direction: str = 'desc',
            per_page: int = 100,
            page: int = None,
    ) -> 'Response':
        """
        Lists repositories for the specified organization.

        :param organization:
            Name of the Organization

        :param type:
            Specifies the types of repositories you want returned. Can be one of "all", "public", "private", "forks", "sources", "member", "internal".
            Note: For GitHub AE, can be one of "all", "private", "forks", "sources", "member", "internal".
            Default: "all".
            If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+, type can also be internal.
            However, the internal value is not yet supported when a GitHub App calls this API with an installation access token.

        :param sort:
            Can be one of "created", "updated", "pushed", "full_name".
            Default: "created"

        :param direction:
            Can be one of "asc" or "desc". Default: when using "full_name": "asc", otherwise "desc"

        :param per_page:
            Results per page (max "100")
            Default: "30"

        :param page:
            Page number of the results to fetch.
            Default: "1"

        :return: 'Response'
        """
        response = self.get_with_token(
            url=f'https://api.github.com/orgs/{organization}/repos',
            params={
                'type': type,
                'sort': sort,
                'direction': direction,
                'per_page': per_page,
                'page': page,
            }
        )

        if response.status_code == 200:
            return Response._parse(
                response=response,
                success=True,
                result=utils.parse_minimal_repositories(response.json()),
            )
        elif response.status_code == 404:
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
