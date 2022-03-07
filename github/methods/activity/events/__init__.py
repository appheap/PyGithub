from .list_public_events import ListPublicEvents
from .list_network_repository_events import ListNetworkRepositoryEvents


class Events(
    ListPublicEvents,
    ListNetworkRepositoryEvents,

):
    pass
