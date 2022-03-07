from .list_public_events import ListPublicEvents
from .list_network_repository_events import ListNetworkRepositoryEvents
from .list_public_organization_events import ListPublicOrganizationEvents


class Events(
    ListPublicEvents,
    ListNetworkRepositoryEvents,
    ListPublicOrganizationEvents,

):
    pass
