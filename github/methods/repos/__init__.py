from .create_org_repository import CreateOrgRepository
from .get_a_repository import GetARepository
from .get_my_repositories import GetMyRepositories
from .get_user_repositories import GetUserRepositories
from .list_organization_repositories import ListOrganizationRepositories


class Repos(
    GetMyRepositories,
    GetUserRepositories,
    ListOrganizationRepositories,
    CreateOrgRepository,
    GetARepository,

):
    pass
