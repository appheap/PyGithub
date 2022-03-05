from .get_authenticated_user_info import GetAuthenticatedUserInfo
from .followers import Followers


class Users(
    GetAuthenticatedUserInfo,
    Followers,
):
    pass
