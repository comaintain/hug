from collections.abc import Mapping
from typing import Any, type_check_only

from _typeshed import Incomplete
from falcon.testing import StartResponseMock

from hug.api import API

@type_check_only
class _MockResponse(StartResponseMock):
    headers: list[tuple[str, str]]
    headers_dict: Mapping[str, str]
    status: str
    exc_info: tuple[object, object, object] | None

    data: Any
    content_type: str

def call(
    method: str,
    api_or_module: API | object,
    url: str,
    body: str | object = "",
    headers: Mapping[str, str] | None = None,
    params: Mapping[str, object] | None = None,
    query_string: str = "",
    scheme: str = "http",
    host: str = ...,
    **kwargs,
) -> _MockResponse: ...
def connect(
    api_or_module: API | object,
    url: str,
    body: str | object = "",
    headers: Mapping[str, str] | None = None,
    params: Mapping[str, object] | None = None,
    query_string: str = "",
    scheme: str = "http",
    host: str = ...,
    **kwargs,
) -> _MockResponse: ...

delete = connect
get = connect
head = connect
options = connect
patch = connect
post = connect
put = connect
trace = connect

def cli(
    method, *args, api: Incomplete | None = None, module: Incomplete | None = None, **arguments
): ...
