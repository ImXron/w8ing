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

██╗    ██╗ █████╗ ██╗███╗   ██╗ ██████╗
██║    ██║██╔══██╗██║████╗  ██║██╔════╝
██║ █╗ ██║╚█████╔╝██║██╔██╗ ██║██║  ███╗
██║███╗██║██╔══██╗██║██║╚██╗██║██║   ██║
╚███╔███╔╝╚█████╔╝██║██║ ╚████║╚██████╔╝
 ╚══╝╚══╝  ╚════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝

TODO:
    * Option to have a call parameter (like condition) and another to take that value and see if it's True.
        * function=lambda: 1+1, check_expression=lambda x: x == 2.
    * Tox?
"""
import time
from typing import Any, Callable, Tuple, Type, Optional

from w8ing import utils
from w8ing.utils import call_if_callable

_RETRY_TIME: float = 0.1
_TIMEOUT: float = 5.0


def ensure(
    condition: Callable,
    catch_exceptions: Tuple[Type[Exception], ...] = tuple(),
    call_each_try: Optional[Callable] = None,
    retry_time: float = _RETRY_TIME,
    timeout: float = _TIMEOUT,
) -> Any:
    """
    Waits and ensures that a condition remains true for a given amount of time.

    NOTE:
        There is still a chance that your condition could be false for a fraction of a second!
        This will depending on computing power, OS operations, etc.
        Recommend setting retry to 0 if timing is critical for you.

    :param condition: The condition to ensure remains true, throughout the timeout.
    :param call_each_try: Optional callable to execute upon the start of each loop / retry.
    :param catch_exceptions: Optional exceptions to catch during each loop.
    :param retry_time: How often to evaluate the condition's expression.
    :param timeout: Max timeout for evaluating the condition's expression.
    :return: Returns a bool depending on the outcome of the condition or a return value from the condition.
    """
    utils.is_callable(condition)
    call_if_callable(lambda: utils.is_callable(condition))
    result = None
    start_time = utils.get_time()
    while utils.get_time() - start_time < timeout:
        try:
            call_if_callable(call_each_try)
            result = condition()

            if not result:
                return result

            time.sleep(retry_time)
        except catch_exceptions:
            time.sleep(retry_time)

    return result


def until(
    condition: Callable,
    call_each_try: Optional[Callable] = None,
    catch_exceptions: Tuple[Type[Exception], ...] = tuple(),
    retry_time: float = _RETRY_TIME,
    timeout: float = _TIMEOUT,
) -> Any:
    """
    Waits until a certain condition is met.

    :param condition: The condition to wait until true, throughout the timeout.
    :param call_each_try: Optional callable to execute upon the start of each loop / retry.
    :param catch_exceptions: Optional exceptions to catch during each loop.
    :param retry_time: How often to evaluate the condition's expression.
    :param timeout: Max timeout for evaluating the condition's expression.
    :return: Returns a bool depending on the outcome of the condition or a return value from the condition.
    """
    utils.is_callable(condition)
    call_if_callable(lambda: utils.is_callable(condition))
    result = None
    start_time = utils.get_time()
    while utils.get_time() - start_time < timeout:
        try:
            call_if_callable(call_each_try)
            result = condition()

            if result:
                return result

            time.sleep(retry_time)

        except catch_exceptions:
            time.sleep(retry_time)

    return result
