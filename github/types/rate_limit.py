from dataclasses import dataclass
from typing import Optional

from .object import Object


@dataclass
class RateLimit(Object):
    """
    Rate Limit
    """
    limit: Optional['int']
    remaining: Optional['int']
    reset: Optional['int']
    used: Optional['int']

    @staticmethod
    def _parse(obj: dict) -> Optional['RateLimit']:
        if obj is None or not len(obj):
            return None

        return RateLimit(
            limit=obj.get('limit', None),
            remaining=obj.get('remaining', None),
            reset=obj.get('reset', None),
            used=obj.get('used', None),
        )


@dataclass
class Resources(Object):
    core: Optional['RateLimit']
    graphql: Optional['RateLimit']
    search: Optional['RateLimit']
    source_import: Optional['RateLimit']
    integration_manifest: Optional['RateLimit']
    code_scanning_upload: Optional['RateLimit']
    actions_runner_registration: Optional['RateLimit']
    scim: Optional['RateLimit']

    @staticmethod
    def _parse(obj: dict) -> Optional['Resources']:
        if obj is None or not len(obj):
            return None

        return Resources(
            core=RateLimit._parse(obj.get('core', None)),
            graphql=RateLimit._parse(obj.get('graphql', None)),
            search=RateLimit._parse(obj.get('search', None)),
            source_import=RateLimit._parse(obj.get('source_import', None)),
            integration_manifest=RateLimit._parse(obj.get('integration_manifest', None)),
            code_scanning_upload=RateLimit._parse(obj.get('code_scanning_upload', None)),
            actions_runner_registration=RateLimit._parse(obj.get('actions_runner_registration', None)),
            scim=RateLimit._parse(obj.get('scim', None)),
        )


@dataclass
class RateLimitOverview(Object):
    """
    Rate Limit Overview
    """
    resources: Optional['Resources']

    @staticmethod
    def _parse(obj: dict) -> Optional['RateLimitOverview']:
        if obj is None or not len(obj):
            return None

        return RateLimitOverview(
            resources=Resources._parse(obj.get('resources', None))
        )
