
# Python Primer

### This is a Jupyter Notebook
You can write Python code and it will execute. You can write the typical 'hello world' program like this:

```python
print('hello world')
```

You can execute by pressing shift-enter. Try it! You can also click the Run button in the toolbar.


```python
print('hello world')
```

### You can do a lot more than just print "hello world"

This is a fully functioning Python3 interpreter so you can write functions and objects like in the next box.

Try printing the 21st Fibonacci number below instead of the 11th. You can add caching if you want to practice coding in Python.


```python
def fib(n):
    if n in (0,1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))
```

### Imports

You already have unit tests that are written for you.
Your task is to make them pass.
We can import various modules to make our experience using Jupyter more pleasant.
This way, making everything work will be a lot easier.

```python
# import everything and define a test runner function
from importlib import reload
from helper import run_test

import helper
```

### A few things you should remember in Python3

Strings and bytes are now different

```python
s = 'hello world'
b = b'hello world'
```

These may look the same but the 'b' prefix means that one is bytes. Basically, the on-disk characters on the system are bytes and the actual symbols in unicode are strings. A good explanation of the difference is [here](http://www.diveintopython3.net/strings.html).


```python
s = 'hello world'
b = b'hello world'

print(s==b) # False

# You convert from string to bytes this way:

hello_world_bytes = s.encode('ascii')
print(hello_world_bytes == b) # True

# You convert from bytes to string this way:

hello_world_string = b.decode('ascii')
print(hello_world_string == s) # True
```

### Test Driven Exercise

Below is test driven exercise. The tests being run are in the `test/index_test.py` file. Again, if you want to see the code you can click on the Octocat icon on the tool bar. Your job on these Test Driven Exercises is to get the tests to pass.

In order to do this, you'll have to write the methods below. So go ahead and implement the `bytes_to_str` and `str_to_bytes functions`. Once you're done, run the blue Run Test button. Try it now!

### (Getting Help)

If you can't get this, there is a `solution.ipynb` notebook on GitHub (click the Octocat GitHub button near the Run Test button to see the repository) with complete answers.


```python
def bytes_to_str(b, encoding='ascii'):
    '''Returns a string version of the bytes'''
    pass


def str_to_bytes(s, encoding='ascii'):
    '''Returns a bytes version of the string'''
    pass
```
