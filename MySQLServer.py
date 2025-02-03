import mysql.connector

def create_database(mydb):
    try:
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as e:
        if e.errno == 1007:
            print("Database 'alx_book_store' already exists.") 
        else:
            print(f"Error creating database: {e}")


def main():
    try:
        mydb = mysql.connector.connect(
            host="local_host",
            user="root",
            password="n@t!1#10"
        )

        if mydb.is_connected():
            create_database(mydb)
            mydb.close()
        else:
            print("Failed to connect to MySQL server.")

    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL server: {err}")


if __name__ == "__main__":
    main()