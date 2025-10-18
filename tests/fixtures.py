"""Defines fixtures that can be used to streamline tests and / or define dependencies"""

from collections import namedtuple
from itertools import count

import pytest

import hug

Routers = namedtuple("Routers", ["http", "local", "cli"])

# Counter for generating unique API IDs
_api_counter = count()


class TestAPI(hug.API):
    pass


def _generate_api_id():
    """Generate a unique API ID using the counter."""
    return "fake_api_{}".format(next(_api_counter))


@pytest.fixture
def hug_api():
    """Defines a dependency for and then includes a uniquely identified hug API for a single test case"""
    api = TestAPI(_generate_api_id())
    api.route = Routers(
        hug.routing.URLRouter().api(api),
        hug.routing.LocalRouter().api(api),
        hug.routing.CLIRouter().api(api),
    )
    return api


@pytest.fixture
def hug_api_error_exit_codes_enabled():
    """
    Defines a dependency for and then includes a uniquely identified hug API
    for a single test case with error exit codes enabled.
    """
    return TestAPI(_generate_api_id(), cli_error_exit_codes=True)


@pytest.fixture
def loop():
    """Create a new event loop for each test."""
    import asyncio

    l = asyncio.new_event_loop()
    asyncio.set_event_loop(l)
    yield l
    l.close()
