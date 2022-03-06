from .blocking import Blocking
from .followers import Followers
from .get_authenticated_user_info import GetAuthenticatedUserInfo


class Users(
    Blocking,
    Followers,
    GetAuthenticatedUserInfo,
):
    pass
