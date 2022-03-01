from .auth import Auth
from .base import Base
from .repos import Repos
from .users import Users


class Methods(
    Auth,
    Base,
    Repos,
    Users

):
    pass
