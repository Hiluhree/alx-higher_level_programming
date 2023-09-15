# 0x0F. Python - Object-relational mapping
## Resources

+ [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
+ [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/) (please don’t pay attention to `_mysql`)
+ [MySQLdb tutorial](https://www.mikusa.com/python-mysql-docs/index.html)
+ [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
+ [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
+ [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)
+ [Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
+ [Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
+ [10 common stumbling blocks for SQLAlchemy newbies](https://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
+ [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
+ [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/) (**Warning**: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)
+ [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)
+ [Python Virtual Environments: A primer](https://realpython.com/python-virtual-environments-a-primer/)

### More Info
**Install and activate venv**
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:

``$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate``

**Install MySQLdb module version 2.0.x**
For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04

``$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)``

**Install SQLAlchemy module version 1.4.x**
``$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'``

## Tasks
### 0. Get all states
+ [0-select_states.py](): a script that lists all ``states`` from the ``database hbtn_0e_0_usa:``

	+ Your script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name`` (no argument validation needed)
	+ You must use the module ``MySQLdb (import MySQLdb)``
	+ Your script should connect to a MySQL server running on ``localhost`` at port ``3306``
	+ Results must be sorted in ascending order by ``states.id``
	+ Results must be displayed as they are in the example below
	+ Your code should not be executed when imported
### 1. Filter states
+ [1-filter_states.py]():  a script that lists all ``states`` with a name starting with ``N`` (upper N) from the database ``hbtn_0e_0_usa``:

	+ Your script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name`` (no argument validation needed)
	+ You must use the module ``MySQLdb (import MySQLdb)``
	+ Your script should connect to a MySQL server running on ``localhost`` at port ``3306``
	+ Results must be sorted in ascending order by states.id
	+ Results must be displayed as they are in the example below
	+ Your code should not be executed when imported
### 2. Filter states by user input
+ [2-my_filter_states.py](): a script that takes in an argument and displays all values in the ``states`` table of ``hbtn_0e_0_usa`` where ``name`` matches the argument.

	+ Your script should take 4 arguments: ``mysql username``, ``mysql password``, ``database name`` and ``state name searched`` (no argument validation needed)
	+ You must use the module ``MySQLdb (import MySQLdb)``
	+ Your script should connect to a MySQL server running on ``localhost`` at port ``3306``
	+ You must use ``format`` to create the SQL query with the user input
	+ Results must be sorted in ascending order by ``states.id``
	+ Results must be displayed as they are in the example below
	+ Your code should not be executed when imported
### 3. SQL Injection...
+ [3-my_safe_filter_states.py](): a script that takes in arguments and displays all values in the ``states`` table of ``hbtn_0e_0_usa`` where ``name`` matches the argument. But this time, write one that is safe from MySQL injections!

	+ Your script should take 4 arguments: ``mysql username``, ``mysql password``, ``database name`` and ``state name searched`` (safe from MySQL injection)
	+ You must use the module ``MySQLdb (import MySQLdb)``
	+ Your script should connect to a MySQL server running on ``localhost`` at port ``3306``
	+ Results must be sorted in ascending order by ``states.id``
	+ Results must be displayed as they are in the example below
	+ Your code should not be executed when imported
### 4. Cities by states
+ [4-cities_by_state.py](): a script that lists all ``cities`` from the database ``hbtn_0e_4_usa``

	+ Your script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``
	+ You must use the module ``MySQLdb (import MySQLdb)``
	+ Your script should connect to a MySQL server running on ``localhost`` at port ``3306``
	+ Results must be sorted in ascending order by ``cities.id``
	+ You can use only ``execute()`` once
	+ Results must be displayed as they are in the example below
	+ Your code should not be executed when imported
### 5. All cities by state
+ [5-filter_cities.py](): a script that takes in the name of a state as an argument and lists all ``cities`` of that state, using the database ``hbtn_0e_4_usa``

	+ Your script should take 4 arguments: ``mysql username``, ``mysql password``, ``database name`` and ``state name`` (SQL injection free!)
	+ You must use the module ``MySQLdb (import MySQLdb)``
	+ Your script should connect to a MySQL server running on ``localhost`` at port ``3306``
	+ Results must be sorted in ascending order by ``cities.id``
	+ You can use only ``execute()`` once
	+ The results must be displayed as they are in the example below
	+ Your code should not be executed when imported
### 6. First state model
+ [model_state.py](): a python file that contains the class definition of a ``State`` and an instance ``Base = declarative_base()``:

+ ``State`` class:
	- inherits from ``Base`` [Tips](https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/basic_use.html)
	- links to the MySQL table ``states``
	- class attribute ``id`` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
	- class attribute ``name`` that represents a column of a string with maximum 128 characters and can’t be null
+ You must use the module ``SQLAlchemy``
+ Your script should connect to a MySQL server running on ``localhost`` at port ``3306``
+ **WARNING:** all classes who inherit from ``Base`` must be imported before calling ``Base.metadata.create_all(engine)``
### 7. All states via SQLAlchemy
+ [7-model_state_fetch_all.py]():  a script that lists all ``State`` objects from the database ``hbtn_0e_6_usa``

	+ Your script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``
	+ You must use the module ``SQLAlchemy``
	+ You must import ``State`` and ``Base`` from ``model_state - from model_state import Base, State``
	+ Your script should connect to a MySQL server running on ``localhost`` at port ``3306``
	+ Results must be sorted in ascending order by ``states.id``
	+ The results must be displayed as they are in the example below
	+ Your code should not be executed when imported
### 8. First state
+ [8-model_state_fetch_first.py](): a script that prints the first ``State`` object from the database ``hbtn_0e_6_usa``

	+ Your script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``
	+ You must use the module ``SQLAlchemy``
	+ You must import ``State`` and ``Base`` from ``model_state - from model_state import Base, State``
	+ Your script should connect to a MySQL server running on ``localhost`` at port ``3306``
	+ The state you display must be the first in ``states.id``
	+ You are not allowed to fetch all states from the database before displaying the result
	+ The results must be displayed as they are in the example below
	+ If the table ``states`` is empty, print ``Nothing`` followed by a new line
	+ Your code should not be executed when imported
### 9. Contains `a`
+ [9-model_state_filter_a.py](): a script that lists all ``State`` objects that contain the letter a from the database ``hbtn_0e_6_usa``

	+ Your script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``
	+ You must use the module ``SQLAlchemy``
	+ You must import ``State`` and ``Base`` from ``model_state - from model_state import Base, State``
	+ Your script should connect to a MySQL server running on ``localhost`` at port ``3306``
	+ Results must be sorted in ascending order by ``states.id``
	+ The results must be displayed as they are in the example below
	+ Your code should not be executed when imported
### 10. Get a state
+ [10-model_state_my_get.py](): a script that prints the ``State`` object with the ``name`` passed as argument from the database ``hbtn_0e_6_usa``

	+ Your script should take 4 arguments: ``mysql username``, ``mysql password``, ``database name`` and ``state name to search`` (SQL injection free)
	+ You must use the module ``SQLAlchemy``
	+ You must import ``State`` and ``Base`` from ``model_state - from model_state import Base, State``
	+ Your script should connect to a MySQL server running on ``localhost`` at port ``3306``
	+ You can assume you have one record with the state name to search
	+ Results must display the ``states.id``
	+ If no state has the name you searched for, display ``Not found``
	+ Your code should not be executed when imported
### 11. Add a new state
+ [11-model_state_insert.py](): a script that adds the ``State`` object “Louisiana” to the database ``hbtn_0e_6_usa``

	+ Your script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``
	+ You must use the module ``SQLAlchemy``
	+ You must import ``State`` and ``Base`` from ``model_state - from model_state import Base, State``
	+ Your script should connect to a MySQL server running on ``localhost`` at port ``3306``
	+ Print the new ``states.id`` after creation
	+ Your code should not be executed when imported
### 12. Update a state
+ [12-model_state_update_id_2.py](): a script that changes the name of a ``State`` object from the database ``hbtn_0e_6_usa``

	+ Your script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``
	+ You must use the module ``SQLAlchemy``
	+ You must import ``State`` and ``Base`` from ``model_state - from model_state import Base, State``
	+ Your script should connect to a MySQL server running on ``localhost`` at port ``3306``
	+ Change the name of the ``State`` where ``id = 2`` to ``New Mexico``
	+ Your code should not be executed when imported
### 13. Delete states
+ [13-model_state_delete_a.py](): a script that deletes all ``State`` objects with a name containing the letter a from the database ``hbtn_0e_6_usa``

	+ Your script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``
	+ You must use the module ``SQLAlchemy``
	+ You must import ``State`` and ``Base`` from ``model_state - from model_state import Base, State``
	+ Your script should connect to a MySQL server running on ``localhost`` at port ``3306``
	+ Your code should not be executed when imported
### 14. Cities in state
+ [model_city.py](): a Python file similar to ``model_state.py`` named ``model_city.py`` that contains the class definition of a ``City``.

	+ City class:
	- inherits from ``Base`` (imported from ``model_state``)
	- links to the MySQL table ``cities``
	- class attribute ``id`` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
	- class attribute ``name`` that represents a column of a string of 128 characters and can’t be null
	- class attribute ``state_id`` that represents a column of an integer, can’t be null and is a foreign key to ``states.id``
	+ You must use the module SQLAlchemy

+ [14-model_city_fetch_by_state.py](): a script ``14-model_city_fetch_by_state.py`` that prints all ``City`` objects from the database ``hbtn_0e_14_usa``:

	+ Your script should take 3 arguments: ``mysql username``, ``mysql password`` and ``database name``
	+ You must use the module ``SQLAlchemy``
	+ You must import ``State`` and ``Base`` from ``model_state - from model_state import Base, State``
	+ Your script should connect to a MySQL server running on ``localhost`` at port ``3306``
	+ Results must be sorted in ascending order by ``cities.id``
	+ Results must be display as they are in the example below (``<state name>: (<city id>) <city name>``)
	+ Your code should not be executed when imported
