from .list_public_events import ListPublicEvents
from .list_network_repository_events import ListNetworkRepositoryEvents
from .list_public_organization_events import ListPublicOrganizationEvents
from .list_repository_events import ListRepositoryEvents
from .list_user_events import ListUserEvents
from .list_user_organization_events import ListUserOrganizationEvents
from .list_a_user_events import ListAUserEvents
from .list_user_received_events import ListUserReceivedEvents
from .list_a_user_public_events import ListAUserPublicEvents


class Events(
    ListPublicEvents,
    ListNetworkRepositoryEvents,
    ListPublicOrganizationEvents,
    ListRepositoryEvents,
    ListUserEvents,
    ListUserOrganizationEvents,
    ListAUserEvents,
    ListUserReceivedEvents,
    ListAUserPublicEvents,

):
    pass
