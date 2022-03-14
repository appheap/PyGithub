from .create_organization_repository import CreateOrganizationRepository
from .get_a_repository import GetARepository
from .list_my_repositories import ListMyRepositories
from .list_organization_repositories import ListOrganizationRepositories
from .list_user_repositories import ListUserRepositories


class Repos(
    CreateOrganizationRepository,
    GetARepository,
    ListMyRepositories,
    ListUserRepositories,
    ListOrganizationRepositories,

):
    pass
