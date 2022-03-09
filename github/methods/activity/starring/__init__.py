from .list_repository_stargazers import ListRepositoryStargazers
from .list_starred_repositories import ListStarredRepositories
from .is_repository_starred_by_me import IsRepositoryStarredByMe
from .star_repository import StarRepository
from .unstar_repository import UnstarRepository
from .list_user_starred_repositories import ListUserStarredRepositories


class Starring(
    ListRepositoryStargazers,
    ListStarredRepositories,
    IsRepositoryStarredByMe,
    StarRepository,
    UnstarRepository,
    ListUserStarredRepositories,

):
    pass
