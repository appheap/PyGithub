from .search_code import SearchCode
from .search_repositories import SearchRepositories
from .search_topics import SearchTopics
from .search_users import SearchUsers
from .search_lables import SearchLabels


class Search(
    SearchCode,
    SearchRepositories,
    SearchTopics,
    SearchUsers,
    SearchLabels,
):
    pass
