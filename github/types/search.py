from dataclasses import dataclass
from typing import Optional, List

from .object import Object
from .repository import MinimalRepository
from github.utils import utils


@dataclass
class SearchCodeResult(Object):
    total_count: Optional['int']
    incomplete_results: Optional['bool']
    items: Optional[List['CodeSearchResultItem']]

    @staticmethod
    def _parse(obj: dict) -> Optional['SearchCodeResult']:
        if obj is None or not len(obj):
            return None

        return SearchCodeResult(
            total_count=obj.get('total_count', None),
            incomplete_results=obj.get('incomplete_results', None),
            items=obj.get('items', None),
        )


@dataclass
class CodeSearchResultItem(Object):
    """
    Code Search Result Item
    """
    name: Optional['str']
    path: Optional['str']
    sha: Optional['str']
    url: Optional['str']
    git_utl: Optional['str']
    html_url: Optional['str']
    repository: Optional['MinimalRepository']
    score: Optional['float']
    file_size: Optional['int']
    language: Optional['str']
    last_modified_at: Optional['str']
    line_numbers: Optional[List['str']]
    text_matches: Optional['SearchResultTextMatch']

    @staticmethod
    def _parse(obj: dict) -> Optional['CodeSearchResultItem']:
        if obj is None or not len(obj):
            return None

        return CodeSearchResultItem(
            name=obj.get('name', None),
            path=obj.get('path', None),
            sha=obj.get('sha', None),
            url=obj.get('url', None),
            git_utl=obj.get('git_utl', None),
            html_url=obj.get('html_url', None),
            repository=MinimalRepository._parse(obj.get('repository', None)),
            score=obj.get('score', None),
            file_size=obj.get('file_size', None),
            language=obj.get('language', None),
            last_modified_at=obj.get('last_modified_at', None),
            line_numbers=obj.get('line_numbers', None),
            text_matches=SearchResultTextMatch._parse(obj.get('text_matches', None)),
        )


@dataclass
class SearchResultTextMatch(Object):
    """
    Search Result Text Match
    """
    object_url: Optional['str']
    object_type: Optional['str']
    property: Optional['str']
    fragment: Optional['str']
    matches: Optional[List['Match']]

    @staticmethod
    def _parse(obj: dict) -> Optional['SearchResultTextMatch']:
        if obj is None or not len(obj):
            return None

        return SearchResultTextMatch(
            object_url=obj.get('object_url', None),
            object_type=obj.get('object_type', None),
            property=obj.get('property', None),
            fragment=obj.get('fragment', None),
            matches=utils.parse_matches(obj.get('matches', None)),
        )


@dataclass
class Match(Object):
    text: Optional['str']
    indices: Optional[List['int']]

    @staticmethod
    def _parse(obj: dict) -> Optional['Match']:
        if obj is None or not len(obj):
            return None

        return Match(
            text=obj.get('text', None),
            indices=obj.get('indices', None),
        )
