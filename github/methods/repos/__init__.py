from .get_my_repositories import GetMyRepositories
from .get_user_repositories import GetUserRepositories
from .get_org_repositories import GetOrgRepositories
from .create_org_repository import CreateOrgRepository


class Repos(
    GetMyRepositories,
    GetUserRepositories,
    GetOrgRepositories,
    CreateOrgRepository,

):
    pass
