import psycopg2

DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = 'fadzni'
DB_HOST = 'localhost' 
DB_PORT = '5432'

try:
    # Establish the connection
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT * from customer;")

    # Fetch the result
    db_version = cursor.fetchall()
    print(f"result: {db_version}")

    for i in db_version:
        print(i)

    # Close the cursor and connection
    cursor.close()
    conn.close()

except Exception as e:
    print(f"Error: {e}")