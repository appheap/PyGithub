from .list_a_user_events import ListAUserEvents
from .list_a_user_public_events import ListAUserPublicEvents
from .list_network_repository_events import ListNetworkRepositoryEvents
from .list_public_events import ListPublicEvents
from .list_public_organization_events import ListPublicOrganizationEvents
from .list_repository_events import ListRepositoryEvents
from .list_user_events import ListUserEvents
from .list_user_organization_events import ListUserOrganizationEvents
from .list_user_received_events import ListUserReceivedEvents


class Events(
    ListAUserEvents,
    ListAUserPublicEvents,
    ListNetworkRepositoryEvents,
    ListPublicEvents,
    ListPublicOrganizationEvents,
    ListRepositoryEvents,
    ListUserEvents,
    ListUserOrganizationEvents,
    ListUserReceivedEvents,
):
    pass
