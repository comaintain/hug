"""tests/test_full_request.py.

Test cases that rely on a command being ran against a running hug server

Copyright (C) 2016 Timothy Edmund Crosley

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

import platform
import socket
import sys
import time
from pathlib import Path
from subprocess import Popen

import pytest
import requests

from .constants import TEST_DIRECTORY

test_module_file = Path(TEST_DIRECTORY) / "module_full_request.py"


@pytest.mark.skipif(
    platform.python_implementation() == "PyPy", reason="Can't run hug CLI from travis PyPy"
)
@pytest.mark.skipif(sys.platform == "win32", reason="CLI not currently testable on Windows")
def test_hug_post():
    assert test_module_file.exists()

    port = 33333
    hug_server = Popen(["hug", "-f", str(test_module_file), "-p", str(port)])
    try:
        wait_until_port_is_open(hug_server, port)

        result = requests.post(f"http://127.0.0.1:{port}/test", {"data": "here"}, timeout=5)
        assert result.status_code == 200, result.text
        assert result.json() == {"message": "ok"}
    finally:
        hug_server.kill()


def wait_until_port_is_open(process: Popen, port: int, host: str = "127.0.0.1", timeout: float = 5):
    start_time = time.time()
    while True:
        try:
            exit_code = process.poll()
            if exit_code is not None:
                raise RuntimeError(f"Server failed to start with exit code {exit_code}")

            with socket.create_connection((host, port), timeout=1):
                return
        except OSError as ex:
            if time.time() - start_time >= timeout:
                raise TimeoutError(
                    f"Timeout waiting for port {port} on host {host} to open"
                ) from ex

            time.sleep(0.05)
