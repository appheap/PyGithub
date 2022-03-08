from .set_email_visibility import SetEmailVisibility
from .get_emails import GetEmails
from .add_emails import AddEmails
from .delete_emails import DeleteEmails
from .get_public_emails import GetPublicEmails


class Emails(
    SetEmailVisibility,
    GetEmails,
    AddEmails,
    DeleteEmails,
    GetPublicEmails,

):
    """
    Management of email addresses via the API requires that you authenticate through basic auth, or through OAuth with a correct scope for the endpoint.
    """
    pass
