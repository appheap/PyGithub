from typing import Optional

from .object import Object


class Headers(Object):
    def __init__(
            self,
            *,
            allow_control_allow_origin: Optional['str'] = None,
            access_control_expose_headers: Optional['str'] = None,
            cache_control: Optional['str'] = None,
            content_encoding: Optional['str'] = None,
            content_security_policy: Optional['str'] = None,
            content_type: Optional['str'] = None,
            date: Optional['str'] = None,
            etag: Optional['str'] = None,
            last_modified: Optional['str'] = None,
            referrer_policy: Optional['str'] = None,
            server: Optional['str'] = None,
            strict_transport_security: Optional['str'] = None,
            transfer_encoding: Optional['str'] = None,
            vary: Optional['str'] = None,
            x_accepted_oauth_scopes: Optional['str'] = None,
            x_content_type_options: Optional['str'] = None,
            x_frame_options: Optional['str'] = None,
            x_github_media_type: Optional['str'] = None,
            x_github_request_id: Optional['str'] = None,
            x_oauth_scopes: Optional['str'] = None,
            x_ratelimit_limit: Optional['int'] = None,
            x_ratelimit_remaining: Optional['int'] = None,
            x_ratelimit_reset: Optional['int'] = None,
            x_ratelimit_resource: Optional['str'] = None,
            x_ratelimit_used: Optional['int'] = None,
            x_xss_protection: Optional['str'] = None,
    ) -> None:
        self.allow_control_allow_origin = allow_control_allow_origin
        self.access_control_expose_headers = access_control_expose_headers
        self.cache_control = cache_control
        self.content_encoding = content_encoding
        self.content_security_policy = content_security_policy
        self.content_type = content_type
        self.date = date
        self.etag = etag
        self.last_modified = last_modified
        self.referrer_policy = referrer_policy
        self.server = server
        self.strict_transport_security = strict_transport_security
        self.transfer_encoding = transfer_encoding
        self.vary = vary
        self.x_accepted_oauth_scopes = x_accepted_oauth_scopes
        self.x_content_type_options = x_content_type_options
        self.x_frame_options = x_frame_options
        self.x_github_media_type = x_github_media_type
        self.x_github_request_id = x_github_request_id
        self.x_oauth_scopes = x_oauth_scopes
        self.x_ratelimit_limit = x_ratelimit_limit
        self.x_ratelimit_remaining = x_ratelimit_remaining
        self.x_ratelimit_reset = x_ratelimit_reset
        self.x_ratelimit_resource = x_ratelimit_resource
        self.x_ratelimit_used = x_ratelimit_used
        self.x_xss_protection = x_xss_protection

    @staticmethod
    def _parse(headers: dict):
        if headers is None or not len(headers):
            return

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
