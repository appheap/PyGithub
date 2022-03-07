from .list_public_events import ListPublicEvents
from .list_network_repository_events import ListNetworkRepositoryEvents
from .list_public_organization_events import ListPublicOrganizationEvents
from .list_repository_events import ListRepositoryEvents
from .list_user_events import ListUserEvents


class Events(
    ListPublicEvents,
    ListNetworkRepositoryEvents,
    ListPublicOrganizationEvents,
    ListRepositoryEvents,
    ListUserEvents,

):
    pass
