from .get_followers import GetFollowers
from .get_following import GetFollowing
from .is_user_followed import IsUserFollowed
from .follow_user import FollowUser
from .unfollow_user import UnfollowUser


class Followers(
    GetFollowers,
    GetFollowing,
    IsUserFollowed,
    FollowUser,
    UnfollowUser,

):
    pass
