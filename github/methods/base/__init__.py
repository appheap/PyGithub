from .get_with_token import GetWithToken
from .post_with_token import PostWithToken


class Base(
    GetWithToken,
    PostWithToken,
):
    pass