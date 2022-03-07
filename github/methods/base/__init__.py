from .get_with_token import GetWithToken
from .post_with_token import PostWithToken
from .put_with_token import PutWithToken
from .delete_with_token import DeleteWithToken
from .patch_with_token import PatchWithToken


class Base(
    GetWithToken,
    PostWithToken,
    PutWithToken,
    DeleteWithToken,
    PatchWithToken,
):
    pass
