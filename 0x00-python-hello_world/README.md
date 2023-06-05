# 0x00. Python - Hello, World
## Resources
+ [The Python tutorial](https://docs.python.org/3/tutorial/index.html)(only the first three chapters below)
+ [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
+ [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
+ [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html) (Read up until “3.1.2. Strings” included)
+ [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
+ [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
+ [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

### Tasks
+ Task 0: [Run Python file](https://github.com/Hiluhree/alx-higher_level_programming/blob/master/0x00-python-hello_world/0-run): A Shell script that runs a Python script.

	- The Python file name will be saved in the environment variable ``$PYFILE``
+ Task 1: [Run inline](https://github.com/Hiluhree/alx-higher_level_programming/blob/master/0x00-python-hello_world/1-run_inline): A Shell script that runs Python code.

	- The Python code will be saved in the environment variable ``$PYCODE``
+ Task 2: [Hello, print](https://github.com/Hiluhree/alx-higher_level_programming/blob/master/0x00-python-hello_world/2-print.py): A Python script that prints exactly ``"Programming is like building a multilingual puzzle, followed by a new line``.

	- Use the function ``print``
+ Task 3: [Print integer](https://github.com/Hiluhree/alx-higher_level_programming/blob/master/0x00-python-hello_world/3-print_number.py): Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable ``number``, followed ``by Battery street``, followed by a new line.

	+ You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py)
	+ The output of the script should be:
		- the``number``, followed by ``Battery street``,
		- followed by a new line
	+ You are not allowed to cast the variable ``number`` into a string
	+ Your code must be 3 lines long
	+ You have to use f-strings [tips](https://realpython.com/python-f-strings/)
+ Task 4: [Print float](https://github.com/Hiluhree/alx-higher_level_programming/blob/master/0x00-python-hello_world/4-print_float.py): Complete the source code in order to print the float stored in the variable ``number`` with a precision of 2 digits.

	+ You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py)
	+ The output of the program should be:
		- ``Float:``, followed by the float with only 2 digits
		- followed by a new line
	+ You are not allowed to cast ``number`` to string
	+ You have to use f-strings
+ Task 5: [Print string](https://github.com/Hiluhree/alx-higher_level_programming/blob/master/0x00-python-hello_world/5-print_string.py): Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable ``str``, followed by its first 9 characters.

	+ You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py)
	+ The output of the program should be:
		- 3 times the value of ``str``
		- followed by a new line
		- followed by the 9 first characters of ``str``
		- followed by a new line
	+ You are not allowed to use any loops or conditional statement
	+ Your program should be maximum 5 lines long
+ Task 6: [Play with strings](https://github.com/Hiluhree/alx-higher_level_programming/blob/master/0x00-python-hello_world/6-concat.py): Complete this [source code to print](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py) ``Welcome to Holberton School!``

	+ You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py)
	+ You are not allowed to use any loops or conditional statements.
	+ You have to use the variables ``str1`` and ``str2`` in your new line of code
	+ Your program should be exactly 5 lines long
+ Task 7: [ Copy - Cut - Paste](https://github.com/Hiluhree/alx-higher_level_programming/blob/master/0x00-python-hello_world/7-edges.py): Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)

	+ You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)
	+ You are not allowed to use any loops or conditional statements
	+ Your program should be exactly 8 lines long
	+ ``word_first_3`` should contain the first 3 letters of the variable ``word``
	+ ``word_last_2`` should contain the last 2 letters of the variable ``word``
	+ ``middle_word`` should contain the value of the variable ``word`` without the first and last letters
+ Task 8: [Create a new sentence](https://github.com/Hiluhree/alx-higher_level_programming/blob/master/0x00-python-hello_world/8-concat_edges.py): Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py) to print object-oriented programming with Python, followed by a new line.

	+ You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py)
	+ You are not allowed to use any loops or conditional statements
	+ Your program should be exactly 5 lines long
	+ You are not allowed to create new variables
	+  You are not allowed to use string literals
+ Task 9: [Easter Egg](https://github.com/Hiluhree/alx-higher_level_programming/blob/master/0x00-python-hello_world/9-easter_egg.py): A Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

	+ The script should be maximum 98 characters long (please check with ``wc -m 9-easter_egg.py``)
+ Task 10: [Linked list cycle](https://github.com/Hiluhree/alx-higher_level_programming/blob/master/0x00-python-hello_world/10-check_cycle.c):
#### Technical interview preparation:

	+ You are not allowed to google anything
	+ Whiteboard first
	+ This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.
A function in C that checks if a singly linked list has a cycle in it.

	+ Prototype: ``int check_cycle(listint_t *list);``
	+ Return: ``0`` if there is no cycle, ``1`` if there is a cycle
#### Requirements:

	+ Only these functions are allowed: ``write``, ``printf``, ``putchar``, ``puts``, ``malloc``, ``free``
+ Task 11: [Hello, write](https://github.com/Hiluhree/alx-higher_level_programming/blob/master/0x00-python-hello_world/100-write.py)
A Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

	+ Use the function ``write`` from the ``sys`` module
	+ You are not allowed to use ``print``
	+ Your script should print to ``stderr``
	+ Your script should exit with the status code ``1``
+ Task 12: [Compile](https://github.com/Hiluhree/alx-higher_level_programming/blob/master/0x00-python-hello_world/101-compile): A script that compiles a Python script file.

	+ The Python file name will be stored in the environment variable ``$PYFILE``

	+ The output filename has to be ``$PYFILEc`` (ex: ``export PYFILE=my_main.py`` => output filename:``my_main.pyc``)
+ Task 13: [ByteCode -> Python #1](https://github.com/Hiluhree/alx-higher_level_programming/blob/master/0x00-python-hello_world/102-magic_calculation.py):
A Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
```
3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
