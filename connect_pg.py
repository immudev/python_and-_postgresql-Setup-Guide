import psycopg2

conn = psycopg2.connect(
                        host = 'localhost', 
                        dbname = 'postgres', 
                        user = 'postgres', 
                        password = 'Admin', 
                        port = 5432
                        )



cur = conn.cursor()

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