"""
MIT License

Copyright (c) 2019 Imran Mumtaz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import time

import pytest

from tests.helpers import get_delta_time, raise_value_error
from w8ing import wait


@pytest.mark.unit
@pytest.mark.until
def test_wait_until_condition_is_true():
    start_time = time.time()
    result = wait.until(lambda: True is True)
    end_time = time.time()

    assert result is True
    assert 0 <= get_delta_time(start_time, end_time) < 0.1


@pytest.mark.unit
@pytest.mark.until
def test_condition_should_timeout_and_return_false():
    start_time = time.time()
    result = wait.until(lambda: True is False, timeout=1)
    end_time = time.time()

    assert result is False
    assert 0 < get_delta_time(start_time, end_time) < 1.1


@pytest.mark.unit
@pytest.mark.until
def test_condition_becomes_true_after_some_time():
    counter = []
    start_time = time.time()
    result = wait.until(lambda: len(counter) == 10, call_each_try=lambda: counter.append("meow"), timeout=2)
    end_time = time.time()

    assert result is True
    assert 0.1 <= get_delta_time(start_time, end_time) < 1.1
    assert len(counter) == 10


@pytest.mark.unit
@pytest.mark.until
def test_exceptions_raised_without_declaring_any_to_catch():
    with pytest.raises(ValueError):
        assert wait.until(raise_value_error, timeout=1)


@pytest.mark.unit
@pytest.mark.until
def test_provide_1_exception_to_catch_returns_false():
    assert not wait.until(raise_value_error, catch_exceptions=(ValueError,), timeout=1)


@pytest.mark.unit
@pytest.mark.until
def test_provide_2_exceptions_to_catch_returns_true():
    assert not wait.until(raise_value_error, catch_exceptions=(TypeError, ValueError), timeout=1)
