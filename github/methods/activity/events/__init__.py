from .list_public_events import ListPublicEvents
from .list_network_repository_events import ListNetworkRepositoryEvents
from .list_public_organization_events import ListPublicOrganizationEvents
from .list_repository_events import ListRepositoryEvents


class Events(
    ListPublicEvents,
    ListNetworkRepositoryEvents,
    ListPublicOrganizationEvents,
    ListRepositoryEvents,

):
    pass
