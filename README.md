
# This is a Jupyter Notebook
You can write Python code and it will execute. You can write the typical 'hello world' program like this:

```python
print('hello world')
```

You can execute by pressing shift-enter. Try it! You can also click the Run button in the toolbar.


```python
print('hello world')
```

    hello world


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

### Test Driven Exercise

There is a test driven exercise. The tests are in the `test/index_test.py` file. Again, if you want to see the code you can click on the Octocat icon on the tool bar. Your job is to get the tests to pass.

In order to do this, you'll have to write the methods below. So go ahead and implement the `bytes_to_str` and `str_to_bytes functions`. Once you're done run the Run Test button. Try it now!


```python
def bytes_to_str(b, encoding='ascii'):
    '''Returns a string version of the bytes'''
    pass


def str_to_bytes(s, encoding='ascii'):
    '''Returns a bytes version of the string'''
    pass
```

### Getting Help

If you can't get this, there's a solution branch on GitHub with complete answers in the `index.ipynb` file which you can use to get the answers.

### Useful Python 3 Idioms

You can reverse a list by using `[::-1]`:

```python
a = [1, 2, 3, 4, 5]
print(a[::-1]) # [5, 4, 3, 2, 1]
```

Also works on both strings and bytes:

```python
s = 'hello world'
print(s[::-1]) # 'dlrow olleh'
b = b'hello world'
print(b[::-1]) # b'dlrow olleh'
```

Indexing bytes will get you the numerical value:

```python
print(b'&'[0]) # 38 since & charcter #38
```

You can do the reverse by using bytes:

```python
print(bytes([38])) # b'&'
```


```python
a = [1, 2, 3, 4, 5]
print(a[::-1]) # [5, 4, 3, 2, 1]

s = 'hello world'
print(s[::-1]) # 'dlrow olleh'
b = b'hello world'
print(b[::-1]) # b'dlrow olleh'

print(b'&'[0]) # 38 since & charcter #38

print(bytes([38])) # b'&'
```

### Python Tricks

Here is how we convert binary to/from hex:


```python
print(b'hello world'.hex())
print(bytes.fromhex('68656c6c6f20776f726c64'))
```

### Exercise

Reverse this hex dump: `b010a49c82b4bc84cc1dfd6e09b2b8114d016041efaf591eca88959e327dd29a`

Hint: you'll want to turn this into binary data, reverse and turn it into hex again


```python
# Exercise 2

h = 'b010a49c82b4bc84cc1dfd6e09b2b8114d016041efaf591eca88959e327dd29a'

# convert to binary (bytes.fromhex)
# reverse ([::-1])
# convert to hex()
```

### Modular Arithmetic

If you don't remember Modular Arithmetic, it's this function on python

```python
39 % 12
```

The result is 3 because that is the remainder after division (39 / 12 == 3 + 3/12).

Some people like to call it "wrap-around" math. If it helps, think of modular arithmetic like a clock:

![clock](http://latex.artofproblemsolving.com/f/4/d/f4daa2601de14fddf3d8441e16cc322a25e85354.png)

Think of taking the modulo as asking the question "what hour will it be 39 hours from now?"

If you're still confused, please take a look at [this](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic) article.


```python
print(39 % 12)
```

### Exercise

Find the modulo 19 of these numbers:

* 99
* \\(456 \cdot 444\\)
* \\(9^{77}\\)

(note python uses ** to do exponentiation)


```python
# Exercise 3

prime = 19
# 99
# 456*444
# 9**77
```

### Converting from bytes to int and back

Converting from bytes to integer requires learning about Big and Little Endian encoding. Essentially any number greater than 255 can be encoded in two ways, with the "Big End" going first or the "Little End" going first.

Normal human reading is from the "Big End". For example 123 is read as 100 + 20 + 3. Some computer systems encode integers with the "Little End" first.

A number like 500 is encoded this way in Big Endian:

0x01f4 (256 + 244)

But this way in Little Endian:

0xf401 (244 + 256)

In Python we can convert an integer to big or little endian using a built-in method:

```python
n = 1234567890
big_endian = n.to_bytes(4, 'big')  # b'\x49\x96\x02\xd2'
little_endian = n.to_bytes(4, 'little')  # b'\xd2\x02\x96\x49'
```

We can also convert from bytes to an integer this way:

```python
big_endian = b'\x49\x96\x02\xd2'
n = int.from_bytes(big_endian, 'big')  # 1234567890
little_endian = b'\xd2\x02\x96\x49'
n = int.from_bytes(little_endian, 'little')  # 1234567890
```


```python
n = 1234567890
big_endian = n.to_bytes(4, 'big')
little_endian = n.to_bytes(4, 'little')

print(big_endian.hex())
print(little_endian.hex())

print(int.from_bytes(big_endian, 'big'))
print(int.from_bytes(little_endian, 'little'))
```

### Test Driven Exercise

Convert the following:

 * 8675309 to 8 bytes in big endian
 * interpret ```b'\x11\x22\x33\x44\x55'``` as a little endian integer


```python
# Exercise 4.1

n = 8675309
# print n in 8 big endian bytes

little_endian = b'\x11\x22\x33\x44\x55'
# print little endian in decimal

def little_endian_to_int(bytes):
    '''little_endian_to_int takes byte sequence as a little-endian number.
    Returns an integer'''
    # use the from_bytes method of int
    pass

def int_to_little_endian(n, length):
    '''endian_to_little_endian takes an integer and returns the little-endian
    byte sequence of length'''
    # use the to_bytes method of n
    pass
```
