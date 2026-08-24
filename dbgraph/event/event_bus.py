import queue
import threading

from dbgraph.event.event import Event
from dbgraph.event.event_handler import EventHandler


class EventBus:
    """Store events in a queue and manage a background thread to distribute events"""

    def __init__(self) -> None:
        self.queue = queue.Queue()
        self.handlers: dict[type[Event], set[EventHandler]] = {}
        self._thread: threading.Thread | None = None
        self._stop_event = threading.Event()

    def subscribe(self, event_type: type[Event], handler: EventHandler):
        """Subscribe a handler to specific type of event"""
        if event_type in self.handlers:
            self.handlers[event_type].add(handler)
        else:
            self.handlers[event_type] = {handler}

    def unsubscribe(self, event_type: type[Event], handler: EventHandler):
        """Unsubscribe a handler from listening to specific event type"""
        self.handlers[event_type].remove(handler)

    def publish(self, event: Event):
        """Push an event into the event queue"""
        self.queue.put(event)

    def _dispatch(self):
        """Get the latest event and let the appropriate handler process it"""
        event = self.queue.get()
        for handler in self.handlers[type(event)]:
            handler.handle(event)

    def _run(self):
        """Run the event loop"""
        while not self._stop_event.is_set():
            try:
                self._dispatch()
            except queue.Empty:
                continue

    def start(self):
        """Start the event background thread"""
        if self._thread is not None and self._thread.is_alive():
            return
        self._stop_event.clear()
        self._thread = threading.Thread(
            target=self._run, name="dbgraph-event-bus", daemon=True
        )
        self._thread.start()

    def stop(self):
        """Stop the event background thread"""
        self._stop_event.set()
        if self._thread is not None:
            self._thread.join()
            self._thread = None
