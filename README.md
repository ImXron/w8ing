```
██╗    ██╗ █████╗ ██╗███╗   ██╗ ██████╗ 
██║    ██║██╔══██╗██║████╗  ██║██╔════╝ 
██║ █╗ ██║╚█████╔╝██║██╔██╗ ██║██║  ███╗
██║███╗██║██╔══██╗██║██║╚██╗██║██║   ██║
╚███╔███╔╝╚█████╔╝██║██║ ╚████║╚██████╔╝
 ╚══╝╚══╝  ╚════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
```

[![Build Status](https://travis-ci.com/ImXron/w8ing.svg?branch=master)](https://travis-ci.com/ImXron/w8ing)
[![codecov](https://codecov.io/gh/ImXron/w8ing/branch/master/graph/badge.svg)](https://codecov.io/gh/ImXron/w8ing)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)
[![image](https://img.shields.io/pypi/v/w8ing.svg)](https://python.org/pypi/w8ing)
[![image](https://img.shields.io/pypi/pyversions/w8ing.svg)](https://python.org/pypi/w8ing)
___

**_W8ing_** is (as the great Kenneth Reitz would say) waiting and or polling **_for humans_**.

Get it? The **_8_** replaces the **_ait_** in **_waiting_** :wink: :woman_shrugging:.

Let **_W8ing_** help you nuke all your hard calls to `time.sleep()` and make your tests less flakey :metal:.
___
    
## Install
Install via pip (highly recommend installing within a [Pipenv](https://github.com/pypa/pipenv)):
```
pip3 install w8ing
```

## Usages

Wait **_until_** some condition is true:
```python
from w8ing import wait

# This example uses an imaginary function that doesn't immediately give us the value we want.
result = wait.until(lambda: get_cat_treats(8) == 8)

# By default, this wait will return whether or not the condition was true or not.
result
True
```

Wait **_until_** an http request is valid:
```python
import requests
from w8ing import wait

# You can even specify the timeout and retry delay.
response = wait.until(lambda: requests.get("http://www.google.com"), retry_time=1, timeout=15)

# By default a successful response (codes 2XX) object is truthy.
response
<Response [200]>
```

Wait **_until_** a serial device becomes available and catch any associated exceptions (for you hardware people):

```python
import serial
from w8ing import wait

# If successful, you'll get a pyserial object back, otherwise you'll get None!
serial_port = wait.until(
    lambda: serial.Serial('/dev/ttyUSB0'), catch_exceptions=(SerialException,), retry_time=1, timeout=30
)

# If it doesn't open you can make a nice assert so your co-workers love you.
assert serial_port, "Unable to open serial port! Did you even plug it in??"

# Otherwise, continue!
serial_port.read(10).decode()
"boots and cats"
```

You can also call another function each loop!
```python
from w8ing import wait

cat_treats = []

# The call_each_try function gets called each time the condition gets evaluated, 
result = wait.until(lambda: len(cat_treats) > 8, call_each_try=lambda: cat_treats.append("treat"), retry_time=0.5)

result
True

# The cat will be pleased, very pleased.
```

### But wait, there's more!

What if you need to **_ensure_** that some condition remains true?? Got you covered fam:

```python
from w8ing import wait

cat_nip = ["cat nip"] * 10

# Set retry delay to 0 so we can evaluate the condition as fast as possible! 
result = wait.ensure(lambda: len(cat_nip) > 5, call_each_try=lambda: cat_nip.pop(), retry_time=0, timeout=2)

result
True

# The cat will get extra intoxicated by this high quality cat nip, good job.
```
**Note:** Due to computing power and other operating system processes, it is possible that the **condition** could
 flicker to false and back to true before being able to catch it! 

## Contribute
Feel free to open an issue and once you get a green light, submit a PR!

All PRs will receive respectful and constructive feedback.