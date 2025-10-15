"""hug/__init__.py

Everyone needs a hug every once in a while. Even API developers. Hug aims to make developing Python driven APIs as
simple as possible, but no simpler.

Hug's Design Objectives:

- Make developing a Python driven API as succint as a written definition.
- The framework should encourage code that self-documents.
- It should be fast. Never should a developer feel the need to look somewhere else for performance reasons.
- Writing tests for APIs written on-top of Hug should be easy and intuitive.
- Magic done once, in an API, is better then pushing the problem set to the user of the API.
- Be the basis for next generation Python APIs, embracing the latest technology.

Copyright (C) 2016  Timothy Edmund Crosley

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

"""

from falcon import *

from hug import (
    directives,
    exceptions,
    format,
    input_format,
    introspect,
    middleware,
    output_format,
    redirect,
    route,
    test,
    transform,
    types,
    use,
    validate,
)
from hug._version import current
from hug.api import API
from hug.decorators import (
    context_factory,
    default_input_format,
    default_output_format,
    delete_context,
    directive,
    extend_api,
    middleware_class,
    reqresp_middleware,
    request_middleware,
    response_middleware,
    startup,
    wraps,
)
from hug.route import (
    call,
    cli,
    connect,
    delete,
    exception,
    get,
    get_post,
    head,
    http,
    local,
    not_found,
    object,
    options,
    patch,
    post,
    put,
    sink,
    static,
    trace,
)
from hug.types import create as type

# The following imports must be imported last; in particular, defaults to have access to all modules
from hug import authentication  # isort:skip
from hug import development_runner  # isort:skip
from hug import defaults  # isort:skip

try:  # pragma: no cover - defaulting to uvloop if it is installed
    import uvloop
    import asyncio

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except (ImportError, AttributeError):
    pass

__version__ = current

from hug import _compat  # isort:skip

# NOTE(vytas): Hug often instantiates Falcon exceptions by passing title and description via
#   positional arguments. Support for this was dropped in Falcon 4.0, see more here:
#   https://falcon.readthedocs.io/en/stable/changes/4.0.0.html#breaking-changes.
#
#   Since hug is re-exporting everything from Falcon, we partially reduce the damage for existing
#   apps by shimming the re-exported exceptions corresponding to the most-popular HTTP status codes
#   to accept title and description as positional arguments (like it is 2019 again).

HTTPBadRequest = _compat._allow_title_descr_posargs(HTTPBadRequest)  # noqa: F405
HTTPUnauthorized = _compat._allow_title_descr_posargs(HTTPUnauthorized)  # noqa: F405
HTTPForbidden = _compat._allow_title_descr_posargs(HTTPForbidden)  # noqa: F405
HTTPNotFound = _compat._allow_title_descr_posargs(HTTPNotFound)  # noqa: F405
HTTPGone = _compat._allow_title_descr_posargs(HTTPGone)  # noqa: F405
HTTPInternalServerError = _compat._allow_title_descr_posargs(HTTPInternalServerError)  # noqa: F405
HTTPServiceUnavailable = _compat._allow_title_descr_posargs(HTTPServiceUnavailable)  # noqa: F405
