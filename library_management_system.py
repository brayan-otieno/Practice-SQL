import mysql.connector
from mysql.connector import Error

# Function to connect to the MySQL database
def connect_to_db():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="yourusername",  # Replace with your MySQL username
            password="yourpassword",  # Replace with your MySQL password
            database="library"
        )
        if mydb.is_connected():
            print("Connected to the database.")
        return mydb
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to add a new book to the library
def add_book(title, author, isbn):
    try:
        mydb = connect_to_db()
        if mydb:
            mycursor = mydb.cursor()
            sql = "INSERT INTO books (title, author, isbn) VALUES (%s, %s, %s)"
            val = (title, author, isbn)
            mycursor.execute(sql, val)
            mydb.commit()
            print(f"{mycursor.rowcount} record(s) inserted.")
            mycursor.close()
            mydb.close()
    except Error as e:
        print(f"Error: {e}")

# Function to search for books by title
def search_books_by_title(title):
    try:
        mydb = connect_to_db()
        if mydb:
            mycursor = mydb.cursor()
            sql = "SELECT * FROM books WHERE title LIKE %s"
            val = ("%" + title + "%",)  # Use wildcard to match partial titles
            mycursor.execute(sql, val)
            results = mycursor.fetchall()
            
            if results:
                print(f"Books found with title '{title}':")
                for row in results:
                    print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, ISBN: {row[3]}")
            else:
                print(f"No books found with title '{title}'.")
            mycursor.close()
            mydb.close()
    except Error as e:
        print(f"Error: {e}")

# Function to list all books in the library
def list_all_books():
    try:
        mydb = connect_to_db()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM books")
            results = mycursor.fetchall()
            
            if results:
                print("All books in the library:")
                for row in results:
                    print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, ISBN: {row[3]}")
            else:
                print("No books found in the library.")
            mycursor.close()
            mydb.close()
    except Error as e:
        print(f"Error: {e}")

# Function to delete a book by its ID
def delete_book(book_id):
    try:
        mydb = connect_to_db()
        if mydb:
            mycursor = mydb.cursor()
            sql = "DELETE FROM books WHERE id = %s"
            val = (book_id,)
            mycursor.execute(sql, val)
            mydb.commit()
            print(f"{mycursor.rowcount} record(s) deleted.")
            mycursor.close()
            mydb.close()
    except Error as e:
        print(f"Error: {e}")

# Example usage of the functions

# Add books
add_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
add_book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

# Search for books by title
search_books_by_title("Gatsby")

# List all books
list_all_books()

# Delete a book by ID (use the correct ID)
delete_book(1)

# List all books again after deletion
list_all_books()
