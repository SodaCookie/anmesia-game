"""Defines the System interface and Message class"""

class Message(object):
    """Simple class used to construct Message objects"""

    def __init__(self, mtype, *args):
        self.mtype = mtype
        self.args = args


class System(object):
    """Interface for creating a new system in the Game"""

    def __init__(self, name, system):
        """Initialize a new System"""
        super().__init__()
        self.queue = [] # Message queue
        self.system = system
        self.name = name

    def init(self, entities):
        """Override. Called at the start of the game"""
        pass

    def update(self, delta, entities):
        """Override. Called every game cycle by default will execute messages
        to function calls."""
        messages = self.flush_messages()
        for message in messages:
            getattr(self, "message_%s" % message.mtype)(
                entities, *message.args)

    def quit(self, entities):
        """Override. Called at the end of the game"""
        pass

    def flush_messages(self):
        """Returns all the messages passed to the system"""
        old_queue = self.queue
        self.queue = []
        return old_queue

    def message(self, message):
        """Passes a message to the system"""
        self.queue.append(message)