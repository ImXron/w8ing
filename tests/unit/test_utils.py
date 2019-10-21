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

from w8ing import utils
from w8ing.utils import call_if_callable


@pytest.mark.unit
def test_is_callable_true_case():
    utils.is_callable(lambda: True)


@pytest.mark.unit
def test_is_callable_false_case():
    with pytest.raises(AssertionError):
        utils.is_callable("meow")


@pytest.mark.unit
def test_can_get_time_and_type_is_float():
    time = utils.get_time()
    assert time
    assert isinstance(time, float)


def test_call_if_callable():
    string = "cat nip"

    def make_string(string):
        return string

    assert call_if_callable(lambda: make_string("cat nip")) == string


def test_call_if_callable_gets_a_non_callable():
    with pytest.raises(TypeError):
        call_if_callable("boots and cat")
