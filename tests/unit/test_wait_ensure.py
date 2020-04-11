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

import pytest

from tests.conftest import get_delta_time, raise_value_error, get_time
from w8ing import wait


@pytest.mark.ensure
@pytest.mark.unit
def test_ensure_condition_stays_true_until_timeout():
    start_time = get_time()
    result = wait.ensure(lambda: True is True, timeout=2)
    end_time = get_time()

    assert result is True
    assert 1.9 <= get_delta_time(start_time, end_time) < 2.1


@pytest.mark.ensure
@pytest.mark.unit
def test_condition_does_not_stay_true_and_returns_before_timeout():
    counter = []
    start_time = get_time()
    result = wait.ensure(
        lambda: len(counter) < 5, call_each_try=lambda: counter.append("kitty"), retry_time=0.1, timeout=1
    )
    end_time = get_time()

    assert result is False
    assert 0 < get_delta_time(start_time, end_time) < 0.51


@pytest.mark.ensure
@pytest.mark.unit
def test_call_on_retry_removes_items_from_a_list_and_ensure_that_the_list_is_not_empty():
    counter = ["meow"] * 11
    start_time = get_time()
    result = wait.ensure(lambda: len(counter) > 0, call_each_try=lambda: counter.pop(), retry_time=0.1, timeout=1)
    end_time = get_time()

    assert result is True
    assert 0.9 <= get_delta_time(start_time, end_time) < 1.1
    assert len(counter) == 1


@pytest.mark.ensure
@pytest.mark.unit
def test_exceptions_raised_without_declaring_any_to_catch():
    with pytest.raises(ValueError):
        assert wait.ensure(raise_value_error, timeout=1)


@pytest.mark.ensure
@pytest.mark.unit
def test_provide_1_exception_to_catch_returns_true():
    assert wait.ensure(raise_value_error, catch_exceptions=(ValueError,), timeout=1) is None


@pytest.mark.ensure
@pytest.mark.unit
def test_provide_2_exceptions_to_catch_returns_true():
    assert wait.ensure(raise_value_error, catch_exceptions=(TypeError, ValueError), timeout=1) is None
