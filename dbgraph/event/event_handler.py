from abc import ABC, abstractmethod

from dbgraph.event.event import Event


class EventHandler(ABC):
    """Interface for event handler"""

    @abstractmethod
    def handle(self, event: Event):
        """Handle the event"""
