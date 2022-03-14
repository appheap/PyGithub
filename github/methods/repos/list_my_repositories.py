from github.scaffold import Scaffold
from github.types import Response
from github.utils import utils


class ListMyRepositories(Scaffold):
    """
    List repositories for the authenticated user
    """

    def list_my_repositories(
            self,
            *,
            visibility: str = 'all',
            affiliation: str = None,
            type: str = None,
            sort: str = 'updated',
            direction: str = 'desc',
            per_page: int = 100,
            page: int = None,
            since: str = None,
            before: str = None,
    ) -> 'Response':
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

        :return: 'Response'
        """
        response = self.get_with_token(
            url='https://api.github.com/user/repos',
            params={
                'visibility': visibility,
                'affiliation': affiliation,
                'type': type,
                'sort': sort,
                'direction': direction,
                'per_page': per_page,
                'page': page,
                'since': since,
                'before': before,
            }
        )

        if response.status_code == 200:
            return Response._parse(
                response=response,
                success=True,
                result=utils.parse_repositories(response.json()),
            )
        elif response.status_code in (304, 401, 403, 422,):
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
