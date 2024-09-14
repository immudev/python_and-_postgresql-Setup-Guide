# python_and_postgresql-Setup-Guide

## setup Python

### 1. Download Python:
- Go to the [official Python website](https://www.python.org/downloads/).
- Download the latest version of Python for your operating system.


### Run the Installer:
- Open the downloaded installer.
- Check the box that says "Add Python to PATH."
- Click "Install Now" to begin the installation process.


 ### Verify Installation:
- Open a command prompt or terminal.
- Type `python --version` (or `python3 --version` on some systems) and press Enter.
- Ensure that the version number is displayed, confirming that Python is installed.
- `pip` is usually included with Python. To check if it’s installed, type `pip --version` in the command prompt.


### Run the Installer pandas, psycopy2 & sqlalchemy:

#### pandas
To install pandas, follow these steps:
- Open a command prompt or terminal.
- Type `pip install pandas` and press Enter to download and install.


#### psycopy2
To install `psycopg2`, which is a popular PostgreSQL adapter for Python, follow these steps:
- Open a command prompt or terminal.
- Type `pip install psycopg2` and press Enter to download and install.

## connect python and postgresql
to find out your connection credentials
- open postgresql and select main database `postgres` and right click and select `properties`.
- open a connection tab in the properties panal
- it's show your connection credentials

```python
import psycopg2

# link the database connection credentials
conn = psycopg2.connect(
                        host = 'localhost', 
                        dbname = 'postgres', 
                        user = 'postgres',    # use your user
                        password = 'Admin',   # use your password
                        port = 5432
                        )

cur = conn.cursor()

# if you write a sql in the python use this method to create table, alter table, insert data & etc..
# cur.execute("""CREATE TABLE IF NOT EXISTS person (
            
#     id          INT PRIMARY KEY,
#     name        VARCHAR(150),
#     age         INT,
#     gender      VARCHAR(25)
# );
#  """)

conn.commit()

cur.close()
conn.close()
```


#### sqlalchemy
To install SQLAlchemy, follow these steps:
- Open a command prompt or terminal.
- Type `pip install sqlalchemy` and press Enter to download and install.


That’s it! Python should now be installed and ready for you to start coding.
