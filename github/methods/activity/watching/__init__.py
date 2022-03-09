from .delete_repository_subscription import DeleteRepositorySubscription
from .get_repository_subscription import GetRepositorySubscription
from .list_repository_watchers import ListRepositoryWatchers
from .list_user_watched_repositories import ListUserWatchedRepositories
from .list_watched_repositories import ListWatchedRepositories
from .set_repository_subscription import SetRepositorySubscription


class Watching(
    DeleteRepositorySubscription,
    GetRepositorySubscription,
    ListRepositoryWatchers,
    ListUserWatchedRepositories,
    ListWatchedRepositories,
    SetRepositorySubscription,

):
    pass
