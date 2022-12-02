## 0x0F-python-object_relational_mapping

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

``mandatory tasks``

* [0-select_states.py]() -a script that lists all `states` from the database `hbtn_0e_0_usa`:

	* Your script should take 3 arguments: `mysql` `username`, `mysql` `password` and `database name` (no argument validation needed)
	* You must use the module `MySQLdb` (`import MySQLdb`)
	* Your script should connect to a MySQL server running on `localhost at` port `3306`
	* Results must be sorted in ascending order by `states.id`
	* Results must be displayed as they are in the example below
	* Your code should not be executed when imported

* [1-filter_states.py]() - a script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`:

	* Your script should take 3 arguments: `mysql` `username`, `mysql` `password` and `database` `name` (no argument validation needed)
	* You must use the module `MySQLdb` (`import MySQLdb`)
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* Results must be sorted in ascending order by `states.id`
	* Results must be displayed as they are in the example below
	* Your code should not be executed when imported

* [2-my_filter_states.py]() - a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.

	* Your script should take 4 arguments: `mysql` `username`, `mysql` `password`, `database name` and `state nam`e searched (no argument validation needed)
	* You must use the module `MySQLdb` (`import MySQLdb`)
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* You must use `format` to create the SQL query with the user input
	* Results must be sorted in ascending order by `states.id`
	* Results must be displayed as they are in the example below
	* Your code should not be executed when imported

* [3-my_safe_filter_states.py]() - a script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. But this time, write one that is safe from MySQL injections!

	* Your script should take 4 arguments: `mysql username`, `mysql password, database name` and `state name searched` (safe from MySQL injection)
	* You must use the module `MySQLdb` (`import MySQLdb`)
	* Your script should connect to a MySQL server running on `localhost at port` `3306`
	* Results must be sorted in ascending order by states.id
	* Results must be displayed as they are in the example below
	* Your code should not be executed when imported

* [4-cities_by_state.py]() - a script that lists all `cities` from the database `hbtn_0e_4_usa`

	* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
	* You must use the module MySQLdb (`import MySQLdb`)
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* Results must be sorted in ascending order by `cities.id`
	* You can use only `execute()` once
	* Results must be displayed as they are in the example below
	* Your code should not be executed when imported


* [5-filter_cities.py]() -  a script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`

	* Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` (SQL injection free!)
	* You must use the module MySQLdb (`import MySQLdb`)
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* Results must be sorted in ascending order by `cities.id`
	* You can use only `execute()` once
	* The results must be displayed as they are in the example below
	* Your code should not be executed when imported

* [model_state.py]() - a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`:

	* State `class`:
		* inherits from `Base`
		* links to the MySQL table `states`
		* class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
		* class attribute `name` that represents a column of a string with maximum 128 characters and can’t be null
	* You must use the module `SQLAlchemy`
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* WARNING: all classes who inherit from `Base` must be imported before calling `Base.metadata.create_all(engine)`

* [7-model_state_fetch_all.py]() - a script that lists all `State` objects from the database `hbtn_0e_6_usa`

	* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
	* You must use the module `SQLAlchemy`
	* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* Results must be sorted in ascending order by `states.id`
	* The results must be displayed as they are in the example below
	* Your code should not be executed when imported


* [8-model_state_fetch_first.py]() - a script that prints the first `State` object from the database `hbtn_0e_6_usa`

	* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
	* You must use the module `SQLAlchemy`
	* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* The state you display must be the first in `states.id`
	* You are not allowed to fetch all states from the database before displaying the result
	* The results must be displayed as they are in the example below
	* If the table `states` is empty, print `Nothing` followed by a new line
	* Your code should not be executed when imported


* [9-model_state_filter_a.py]() -a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`

	* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
	* You must use the module `SQLAlchemy`
	* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* Results must be sorted in ascending order by `states.id`
	* The results must be displayed as they are in the example below
	* Your code should not be executed when imported

* [10-model_state_my_get.py]() - a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`

Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name to search` (SQL injection free)
	* You must use the module `SQLAlchemy`
	* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* You can assume you have one record with the state name to search
	* Results must display the `states.id`
	* If no state has the name you searched for, display Not found
	* Your code should not be executed when imported
* [11-model_state_insert.py]() - a script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`

	* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
	* You must use the module `SQLAlchemy`
	* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* Print the new `states.id` after creation
	* Your code should not be executed when imported

* [12-model_state_update_id_2.py]() - a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`

	* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
	* You must use the module `SQLAlchemy`
	* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* Change the name of the `State` where `id = 2` to `New Mexico`
	* Your code should not be executed when imported

* [13-model_state_delete_a.py]() - a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`

	* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
	* You must use the module `SQLAlchemy`
	* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* Your code should not be executed when imported

* [model_city.py]() - a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`.

	* `City` class:
		* inherits from `Base` (imported from `model_state`)
		* links to the MySQL table `cities`
		* class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
		* class attribute `name` that represents a column of a string of 128 characters and can’t be null
		* class attribute `state_id` that represents a column of an integer, can’t be null and is a foreign key to `states.id`
	* You must use the module `SQLAlchemy`
* [14-model_city_fetch_by_state.py]() - a script `14-model_city_fetch_by_state.py` that prints all `City` objects from the database `hbtn_0e_14_usa`:

	* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
	* You must use the module `SQLAlchemy`
	* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* Results must be sorted in ascending order by `cities.id`
	* Results must be display as they are in the example below (`<state name>: (<city id>) <city name>`)
	* Your code should not be executed when imported
