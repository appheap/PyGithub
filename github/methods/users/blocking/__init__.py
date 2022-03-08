from .list_blocked_users import ListBlockedUsers
from .is_user_blocked import IsUserBlocked
from .block_user import BlockUser
from .unblock_user import UnblockUser


class Blocking(
    ListBlockedUsers,
    IsUserBlocked,
    BlockUser,
    UnblockUser,

):
    pass
