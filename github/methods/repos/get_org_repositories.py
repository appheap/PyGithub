from typing import List, Optional, Union, Tuple

from github.scaffold import Scaffold
from github.types import Repository, Response


class GetOrgRepositories(Scaffold):
    """
    List organization repositories
    """

    def get_org_repositories(
            self,
            *,
            organization: str = None,
            type: str = 'all',
            sort: str = 'updated',
            direction: str = 'desc',
            per_page: int = 100,
            page: int = None,
    ) -> Tuple[bool, Union[List['Repository'], 'Response']]:
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

        :return: Tuple[bool, Union[List['Repository'], 'Response']]
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

        repos: List[Repository] = []
        if response.status_code == 200:
            for repo_dict in response.json():
                repo = Repository._parse(repo_dict)
                if repo_dict is not None and len(repo_dict):
                    repos.append(repo)
            return True, repos
        elif response.status_code == 404:
            return False, Response._parse(404)
        else:
            return False, Response._parse_unknown(
                status_code=response.status_code,
                message=response.json().get('message'),
            )
