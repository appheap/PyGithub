from .list_blocked_users import ListBlockedUsers
from .is_user_blocked import IsUserBlocked


class Blocking(
    ListBlockedUsers,
    IsUserBlocked,

):
    pass
