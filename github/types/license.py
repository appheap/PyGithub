from dataclasses import dataclass
from typing import Optional

from .object import Object


@dataclass
class SimpleLicense(Object):
    """
    License Simple
    """

    key: str
    name: str
    url: str
    spdx_id: str
    node_id: str
    html_url: Optional['str'] = None

    @staticmethod
    def _parse(license_dict: dict):
        if not license_dict or not len(license_dict):
            return None

        return SimpleLicense(
            key=license_dict.get('key', None),
            name=license_dict.get('name', None),
            url=license_dict.get('url', None),
            spdx_id=license_dict.get('spdx_id', None),
            node_id=license_dict.get('node_id', None),
            html_url=license_dict.get('html_url', None),

        )
