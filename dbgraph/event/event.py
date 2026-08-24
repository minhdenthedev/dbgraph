from dataclasses import dataclass


@dataclass
class Event:
    """Base event used in DBGraph"""

    message: str


@dataclass
class ProgressEvent(Event):
    """Event with progress"""

    target: float
    current: float

    def get_percentage(self) -> float:
        """Return the progress of the task in percentage"""
        return self.current / self.target
