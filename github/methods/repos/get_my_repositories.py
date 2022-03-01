from typing import List, Optional

from github.scaffold import Scaffold
from github.types import Repository


class GetMyRepositories(Scaffold):
    def get_my_repositories(
            self,
            *,
            visibility: str = None,
            affiliation: str = None,
            type: str = None,
            sort: str = None,
            direction: str = None,
            per_page: int = 100,
            page: int = None,
            since: str = None,
            before: str = None,
    ) -> Optional[List['Repository']]:
        """
        Lists repositories that the authenticated user has explicit permission (:read, :write, or :admin) to access.

        :param visibility:
            Can be one of "all", "public", or "private". Note: For GitHub AE, can be one of "all", "internal", or "private". Default: "all"

        :param affiliation:
            Comma-separated list of values. Can include:
            * owner: Repositories that are owned by the authenticated user.
            * collaborator: Repositories that the user has been added to as a collaborator.
            * organization_member: Repositories that the user has access to through being a member of an organization.
            This includes every repository on every team that the user is on.
            Default: owner,collaborator,organization_member

        :param type:
            Can be one of "all", "owner", "public", "private", "member". Note: For
            GitHub AE, can be one of "all", "owner", "internal", "private", "member". Default: "all"
            Will cause a 422 error if used in the same request as visibility or affiliation.
            Will cause a 422 error if used in the same request as visibility or affiliation.
            Default: "all"

        :param sort:
            Can be one of "created", "updated", "pushed", "full_name".
            Default: "full_name"

        :param direction:
            Can be one of "asc" or "desc". Default: "asc" when using "full_name", otherwise "desc"

        :param per_page:
            Results per page (max "100")
            Default: "30"

        :param page:
            Page number of the results to fetch.
            Default: "1"

        :param since:
            Only show notifications updated after the given time. This is a timestamp in `ISO 8601` format: `YYYY-MM-DDTHH:MM:SSZ`.

        :param before:
            Only show notifications updated before the given time. This is a timestamp in `ISO 8601` format: `YYYY-MM-DDTHH:MM:SSZ`.

        :return: List[`types.Repository`]
        """
        response = self.get_with_token(
            url='https://api.github.com/user/repos',
            params={
                'visibility': visibility if visibility else 'all',
                'affiliation': affiliation,
                'type': type,
                'sort': sort if sort else 'updated',
                'direction': direction if direction else 'dsc',
                'per_page': per_page if per_page else 100,
                'page': page if page else 1,
                'since': since,
                'before': before,
            }
        )

        repos: List[Repository] = []
        if response.ok:
            for repo_dict in response.json():
                repo = Repository._parse(repo_dict)
                if repo_dict is not None and len(repo_dict):
                    repos.append(repo)

        return repos