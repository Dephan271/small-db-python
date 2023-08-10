import psycopg2
connection = psycopg2.connect(host='localhost', port='5432', database='postgres', user='postgres', password='root')
cursor = connection.cursor()

def choose(num):
    #dict
    types = {
        1: ("ice latte", 2),
        2: ("ice cappuccino", 2),
        3: ("hot latte", 2),
        4: ("hot cappuccino", 2)
    }

    total = 0
    multiple_coffee=[]
    records_to_insert = []

    for i in num:
        if i in types:
            coffee_type, price = types[i]
            quantity = int(input(f"How many {coffee_type}s do you want? "))
            print(f"You buy {quantity} {coffee_type}s, which will be {quantity * price}")
            total += quantity * price 

            multiple_coffee.append(coffee_type)
            
            total = f"{total} $"


    #insert value into list 
    records_to_insert.append((multiple_coffee, total))
    print(f"The total will be {total}")

    #insert value into table
    postgres_insert_query = "INSERT INTO cafe(COFFEE, PRICE) VALUES (%s, %s)"

    try:
        #Execute
        cursor.executemany(postgres_insert_query, records_to_insert)
        connection.commit()
        print("Records inserted successfully!")
        #Exception for Error
    except Exception as e:
        print("Error:", e)
        connection.rollback()
#close
    cursor.close()
    connection.close()


# Menu
print("Welcome to the cafe")
print('''Menu:
1. Ice Latte        $2
2. Ice Cappuccino   $2
3. Hot Latte        $2
4. Hot Cappuccino   $2
''')
numbers = input("Choose a cafe (separate each number by a space for multiple choices): ").split()
#To make everything in the list is an INT and not a string
choose(list(map(int, numbers)))
