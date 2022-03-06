from typing import Optional

from github.types import SimpleUser, List, Repository, MinimalRepository


def parse_simple_users(users_dict: dict) -> Optional[List['SimpleUser']]:
    if type(users_dict) != dict:
        return []

    users: List['SimpleUser'] = []
    for user_dict in users_dict:
        user = SimpleUser._parse(user_dict)
        if user_dict is not None and len(user_dict):
            users.append(user)
    return users


def parse_repositories(repos_dict: dict) -> Optional[List['Repository']]:
    if type(repos_dict) != dict:
        return []

    repos: List['Repository'] = []
    for repo_dict in repos_dict:
        repo = Repository._parse(repo_dict)
        if repo_dict is not None and len(repo_dict):
            repos.append(repo)
    return repos


def parse_minimal_repositories(repos_dict: dict) -> Optional[List['MinimalRepository']]:
    if type(repos_dict) != dict:
        return []

    repos: List['Repository'] = []
    for repo_dict in repos_dict:
        repo = MinimalRepository._parse(repo_dict)
        if repo_dict is not None and len(repo_dict):
            repos.append(repo)
    return repos
