import psycopg2

conn = psycopg2.connect(database = "postgres", 
                        user = "postgres", 
                        password = "root", 
                        host = "localhost", 
                        port = "5432")
print ("Opened database successfully")

cur = conn.cursor()

cur.execute("SELECT id, coffee, price from cafe")
rows = cur.fetchall()
for row in rows:
   print ("ID = ", row[0])
   print ("COFFEE = ", row[1])
   print ("PRICE = ", row[2], "\n")

print ("Operation done successfully")
conn.close()