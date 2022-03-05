from .get_followers import GetFollowers
from .get_following import GetFollowing
from .is_user_followed import IsUserFollowed
from .follow_user import FollowUser
from .unfollow_user import UnfollowUser
from .get_user_followers import GetUserFollowers
from .get_user_following import GetUserFollowing
from .is_target_user_followed_by_user import IsTargetUserFollowedByUser


class Followers(
    GetFollowers,
    GetFollowing,
    IsUserFollowed,
    FollowUser,
    UnfollowUser,
    GetUserFollowers,
    GetUserFollowing,
    IsTargetUserFollowedByUser,

):
    pass
