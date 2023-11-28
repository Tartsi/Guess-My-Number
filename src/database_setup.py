import sqlite3

"""
This module sets up the database for the app
"""

DATABASE_NAME = 'database.db'

# CREATING A DATABASE WILL ALWAYS RESET A PRE-EXISTING DATABASE OF THE SAME NAME!


def create_datebase():

    try:

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        with open('schema.sql', 'r') as file:
            script = file.read()

        cursor.executescript(script)

        conn.commit()
        conn.close()
        print("Database created successfully")

    except Exception as error:
        print("Error creating database: ", error)
        return False


if __name__ == "__main__":
    create_datebase()
