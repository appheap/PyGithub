from dataclasses import dataclass
from typing import Optional

from .object import Object


@dataclass
class Headers(Object):
    allow_control_allow_origin: Optional['str']
    access_control_expose_headers: Optional['str']
    cache_control: Optional['str']
    content_encoding: Optional['str']
    content_security_policy: Optional['str']
    content_type: Optional['str']
    date: Optional['str']
    etag: Optional['str']
    last_modified: Optional['str']
    referrer_policy: Optional['str']
    server: Optional['str']
    strict_transport_security: Optional['str']
    transfer_encoding: Optional['str']
    vary: Optional['str']
    x_accepted_oauth_scopes: Optional['str']
    x_content_type_options: Optional['str']
    x_frame_options: Optional['str']
    x_github_media_type: Optional['str']
    x_github_request_id: Optional['str']
    x_oauth_scopes: Optional['str']
    x_ratelimit_limit: Optional['int']
    x_ratelimit_remaining: Optional['int']
    x_ratelimit_reset: Optional['int']
    x_ratelimit_resource: Optional['str']
    x_ratelimit_used: Optional['int']
    x_xss_protection: Optional['str']

    @staticmethod
    def _parse(headers: dict) -> Optional['Headers']:
        if headers is None or not len(headers):
            return None

        return Headers(
            allow_control_allow_origin=headers.get('Access-Control-Allow-Origin', None),
            access_control_expose_headers=headers.get('Access-Control-Expose-Headers', None),
            cache_control=headers.get('Cache-Control', None),
            content_encoding=headers.get('Content-Encoding', None),
            content_security_policy=headers.get('Content-Security-Policy', None),
            content_type=headers.get('Content-Type', None),
            date=headers.get('Date', None),
            etag=headers.get('ETag', None),
            last_modified=headers.get('Last-Modified', None),
            referrer_policy=headers.get('Referrer-Policy', None),
            server=headers.get('Server', None),
            strict_transport_security=headers.get('Strict-Transport-Security', None),
            transfer_encoding=headers.get('Transfer-Encoding', None),
            vary=headers.get('Vary', None),
            x_accepted_oauth_scopes=headers.get('X-Accepted-OAuth-Scopes', None),
            x_content_type_options=headers.get('X-Content-Type-Options', None),
            x_frame_options=headers.get('X-Frame-Options', None),
            x_github_media_type=headers.get('X-GitHub-Media-Type', None),
            x_github_request_id=headers.get('X-GitHub-Request-Id', None),
            x_oauth_scopes=headers.get('X-OAuth-Scopes', None),
            x_ratelimit_limit=int(headers.get('X-RateLimit-Limit', None)),
            x_ratelimit_remaining=int(headers.get('X-RateLimit-Remaining', None)),
            x_ratelimit_reset=int(headers.get('X-RateLimit-Reset', None)),
            x_ratelimit_resource=headers.get('X-RateLimit-Resource', None),
            x_ratelimit_used=int(headers.get('X-RateLimit-Used', None)),
            x_xss_protection=headers.get('X-XSS-Protection', None),
        )
