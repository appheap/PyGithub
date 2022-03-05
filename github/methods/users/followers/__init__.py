from .get_followers import GetFollowers
from .get_following import GetFollowing
from .is_user_followed import IsUserFollowed

class Followers(
    GetFollowers,
    GetFollowing,
    IsUserFollowed,

):
    pass
