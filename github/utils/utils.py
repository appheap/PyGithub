from typing import Optional, Union, List
from urllib.parse import parse_qs
from urllib.parse import urlparse

import requests

from github import types


def parse_simple_users(users_dict: list) -> Optional[List['types.SimpleUser']]:
    if type(users_dict) != list:
        return []

    users: List['types.SimpleUser'] = []
    for user_dict in users_dict:
        user = types.SimpleUser._parse(user_dict)
        if user_dict is not None and len(user_dict):
            users.append(user)
    return users


def parse_repositories(repos_dict: list) -> Optional[List['types.Repository']]:
    if type(repos_dict) != list:
        return []

    repos: List['types.Repository'] = []
    for repo_dict in repos_dict:
        repo = types.Repository._parse(repo_dict)
        if repo_dict is not None and len(repo_dict):
            repos.append(repo)
    return repos


def parse_repository_subscription(repos_dict: list) -> Optional[List['types.RepositorySubscription']]:
    if type(repos_dict) != list:
        return []

    repos: List['types.RepositorySubscription'] = []
    for repo_dict in repos_dict:
        repo = types.RepositorySubscription._parse(repo_dict)
        if repo_dict is not None and len(repo_dict):
            repos.append(repo)
    return repos


def parse_repositories_with_starred_at(repos_dict: list) -> Optional[List['types.Repository']]:
    if type(repos_dict) != list:
        return []

    repos: List['types.Repository'] = []
    for res in repos_dict:
        _repo = res.get('repo')
        _repo['starred_at'] = res.get('starred_at', None)
        repo = types.Repository._parse(_repo)
        if _repo is not None and len(_repo):
            repos.append(repo)
    return repos


def parse_minimal_repositories(repos_dict: list) -> Optional[List['types.MinimalRepository']]:
    if type(repos_dict) != list:
        return []

    repos: List['types.Repository'] = []
    for repo_dict in repos_dict:
        repo = types.MinimalRepository._parse(repo_dict)
        if repo_dict is not None and len(repo_dict):
            repos.append(repo)
    return repos


def parse_emails(emails_dict: list) -> Optional[List['types.Email']]:
    if type(emails_dict) != list:
        return []

    emails: List['types.Email'] = []
    for email_dict in emails_dict:
        repo = types.Email._parse(email_dict)
        if email_dict is not None and len(email_dict):
            emails.append(repo)
    return emails


def parse_pages(pages_dict: list) -> Optional[List['types.Page']]:
    if type(pages_dict) != list:
        return []

    pages: List['types.Page'] = []
    for page_dict in pages_dict:
        repo = types.Page._parse(page_dict)
        if page_dict is not None and len(page_dict):
            pages.append(repo)
    return pages


def parse_labels(labels_dict: list) -> Optional[List[Union['str', 'types.Label']]]:
    if type(labels_dict) != list:
        return []

    events: List['types.Label'] = []
    for label_dict in labels_dict:
        if type(label_dict) == dict:
            label = types.Event._parse(label_dict)
            if label_dict is not None and len(label_dict):
                events.append(label)
        else:
            events.append(label_dict)
    return events


def parse_events(events_dict: list) -> Optional[List['types.Event']]:
    if type(events_dict) != list:
        return []

    events: List['types.Event'] = []
    for event_dict in events_dict:
        event = types.Event._parse(event_dict)
        if event_dict is not None and len(event_dict):
            events.append(event)
    return events


def parse_stargazers(stargazers_list: list) -> Optional[List['types.Stargazer']]:
    if type(stargazers_list) != list:
        return []

    stargazers: List['types.Stargazer'] = []
    for stargazer_dict in stargazers_list:
        stargazer = types.Stargazer._parse(stargazer_dict)
        if stargazer_dict is not None and len(stargazer_dict):
            stargazers.append(stargazer)
    return stargazers


def parse_last_page(response: requests.Response) -> int:
    try:
        url = response.links.get('last').get('url')
        parsed_url = urlparse(url)
        captured_value = parse_qs(parsed_url.query)
        last_page = int(captured_value.get('page')[0])
        return last_page
    except Exception as e:
        pass

    return -1
