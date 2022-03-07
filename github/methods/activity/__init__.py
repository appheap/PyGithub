from .events import Events
from .feeds import Feeds
from .notifications import Notifications
from .starring import Starring
from .watching import Watching


class Activity(
    Events,
    Feeds,
    Notifications,
    Starring,
    Watching,
):
    pass
