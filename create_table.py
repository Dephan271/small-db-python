import psycopg2

connection = psycopg2.connect(host ='localhost',
                            port ='5432',
                            database ="postgres",
                            user = "postgres",
                            password = 'root')
cursor = connection.cursor()
create_table = '''CREATE TABLE cafe
            (ID SERIAL PRIMARY KEY,
            COFFEE VARCHAR(100),
            PRICE FLOAT);'''
cursor.execute(create_table)
connection.commit()
print("Table created successfully in PostgreSQL ")

cursor.close()
connection.close()
print("PostgreSQL connection is closed")
       