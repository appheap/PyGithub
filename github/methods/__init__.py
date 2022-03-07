from .activity import Activity
from .auth import Auth
from .base import Base
from .organizations import Organizations
from .repos import Repos
from .search import Search
from .users import Users


class Methods(
    Activity,
    Auth,
    Base,
    Organizations,
    Repos,
    Search,
    Users

):
    pass
