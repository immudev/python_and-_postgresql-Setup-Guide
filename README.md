# python_and_postgresql-Setup-Guide

## Project Overview

**Project Title**: Retail Sales Analysis  
**Level**: Beginner  
**Database**: `retail_sales`

## Project Structure

### 1. Download Python:
- Go to the [official Python website](https://www.python.org/downloads/).
- Download the latest version of Python for your operating system.


### 2. Run the Installer:
- Open the downloaded installer.
- Check the box that says "Add Python to PATH."
- Click "Install Now" to begin the installation process.


 ### 3. Verify Installation:
- Open a command prompt or terminal.
- Type `python --version` (or `python3 --version` on some systems) and press Enter.
- Ensure that the version number is displayed, confirming that Python is installed.
- `pip` is usually included with Python. To check if it’s installed, type `pip --version` in the command prompt.


### 4. Run the Installer pandas, psycopy2 & sqlalchemy:

#### 1. pandas
To install pandas, follow these steps:
- Open a command prompt or terminal.
- Type `pip install pandas` and press Enter to download and install.


#### 2. psycopy2
To install `psycopg2`, which is a popular PostgreSQL adapter for Python, follow these steps:
- Open a command prompt or terminal.
- Type `pip install psycopg2` and press Enter to download and install.

### 3. connect python and postgresql
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


#### 4. sqlalchemy
To install SQLAlchemy, follow these steps:
- Open a command prompt or terminal.
- Type `pip install sqlalchemy` and press Enter to download and install.


## load dataset in postgres database
- Open the vscode or any python editer
- write a given code to load the database. code given below.

```python
# import pandas and sqlalchemy for load dataset in portgresql
import pandas as pd
from sqlalchemy import create_engine


# creating SQL Alchemy engine object to connect severs
# can you use your database connection postgresql://username:password@localhost/database
# this database connection is mine z
conn_string = 'postgresql://postgres:Admin@localhost/painting_p004'
db = create_engine(conn_string)


# Initializing connection to the databse
conn = db.connect()

# list the csv file to load in the database
files = ['canvas_size', 'image_link', 'museum_hours', 'museum', 'product_size', 'subject', 'work']

# create a for lop to rreperate porcess untile the files end 
for file in files:

    # load the dataframe as df into the database 
    df = pd.read_csv(f"C:\\Users\\smohe\\OneDrive\\Desktop\\SQL\\projects\\project_004\\dataset\\{file}.csv")
    # the 'if_exists' can be 'fail' 'replace' or 'append' if exists is check the talble already exists or not if exists this step replace a table
    df.to_sql(file, con=conn, if_exists='replace', index=False)


# after click run button its take few sec to load dataset in database 
# after conplete the process you go to the databse refresh and check your databse 
```


That’s it! Python should now be installed and ready for you to explore.
