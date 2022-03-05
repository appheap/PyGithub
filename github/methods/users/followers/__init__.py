from .get_followers import GetFollowers
from .get_following import GetFollowing
from .is_user_followed import IsUserFollowed
from .follow_user import FollowUser
from .unfollow_user import UnfollowUser
from .get_user_followers import GetUserFollowers
from .get_user_following import GetUserFollowing


class Followers(
    GetFollowers,
    GetFollowing,
    IsUserFollowed,
    FollowUser,
    UnfollowUser,
    GetUserFollowers,
    GetUserFollowing,

):
    pass
