import mysql.connector
from mysql.connector import Error

try:
    # Establish the connection
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="bincom_test"
    )

    if mydb.is_connected():
        print("Successfully connected to the database")

    # Create a cursor object
    my_cursor = mydb.cursor()

    # Drop table if it already exists
    my_cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    # Create table
    sql = """
    CREATE TABLE EMPLOYEE (
        FNAME CHAR(20) NOT NULL,
        LNAME CHAR(20),
        AGE INT
    )
    """
    my_cursor.execute(sql)
    print("Table created successfully")

except Error as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    if my_cursor:
        my_cursor.close()
    if mydb.is_connected():
        mydb.close()
        print("MySQL connection is closed")
