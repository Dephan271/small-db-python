import psycopg2

connection = psycopg2.connect(host='localhost', port='5432', database='postgres', user='postgres', password='root')

print ("Opened database successfully")

cursor = connection.cursor()

altering_table = '''ALTER TABLE cafe 
ALTER COLUMN price TYPE VARCHAR(100);
'''
cursor.execute(altering_table)
connection.commit()
print("Table altered successfully in PostgreSQL ")
cursor.close()
connection.close()
print("PostgreSQL connection is closed")