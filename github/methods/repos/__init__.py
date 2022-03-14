from .create_org_repository import CreateOrgRepository
from .get_a_repository import GetARepository
from .get_my_repositories import GetMyRepositories
from .list_organization_repositories import ListOrganizationRepositories
from .list_user_repositories import ListUserRepositories


class Repos(
    CreateOrgRepository,
    GetMyRepositories,
    GetARepository,
    ListUserRepositories,
    ListOrganizationRepositories,

):
    pass
