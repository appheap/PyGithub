from .get_my_repositories import GetMyRepositories
from .get_user_repositories import GetUserRepositories


class Repos(
    GetMyRepositories,
    GetUserRepositories,

):
    pass
