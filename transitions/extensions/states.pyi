from ..core import MachineError as MachineError, State as State, listify as listify
from typing import Any

_LOGGER: Any

class Tags(State):
    tags: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __getattr__(self, item): ...

class Error(Tags):
    def __init__(self, *args, **kwargs) -> None: ...
    def enter(self, event_data) -> None: ...

class Timeout(State):
    dynamic_methods: Any
    timeout: Any
    _on_timeout: Any
    runner: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def enter(self, event_data): ...
    def exit(self, event_data): ...
    def _process_timeout(self, event_data) -> None: ...
    @property
    def on_timeout(self): ...
    @on_timeout.setter
    def on_timeout(self, value) -> None: ...

class Volatile(State):
    volatile_cls: Any
    volatile_hook: Any
    initialized: bool
    def __init__(self, *args, **kwargs) -> None: ...
    def enter(self, event_data) -> None: ...
    def exit(self, event_data) -> None: ...

def add_state_features(*args): ...

class VolatileObject: ...