from typing import Optional

from .object import Object


class License(Object):

    def __init__(
            self,
            *,
            key: Optional['str'] = None,
            name: Optional['str'] = None,
            spdx_id: Optional['str'] = None,
            url: Optional['str'] = None,
            node_id: Optional['str'] = None,
    ):
        self.key = key
        self.name = name
        self.spdx_id = spdx_id
        self.url = url
        self.node_id = node_id

    @staticmethod
    def _parse(license: dict) -> Optional['License']:
        if license is None or not len(license):
            return None

        return License(
            key=license.get('key'),
            name=license.get('name'),
            spdx_id=license.get('spdx_id'),
            url=license.get('url'),
            node_id=license.get('node_id'),
        )
