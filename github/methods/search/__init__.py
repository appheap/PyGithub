from .search_code import SearchCode
from .search_repositories import SearchRepositories
from .search_topics import SearchTopics


class Search(
    SearchCode,
    SearchRepositories,
    SearchTopics,
):
    pass
