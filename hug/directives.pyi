from _typeshed import Incomplete

from hug.api import API

class Timer:
    start: float
    round_to: int
    def __init__(self, round_to: int | None = None, **kwargs) -> None: ...
    def __float__(self) -> float: ...
    def __int__(self) -> int: ...

module = object
api = API
api_version = Incomplete
documentation = str
session = Incomplete
user = Incomplete
cors = str

class CurrentAPI:
    api_version: Incomplete
    api: API
    def __getattr__(self, name): ...
