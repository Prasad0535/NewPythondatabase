import sqlite3
from sqlite3 import Error

# Function to create a connection to the SQLite database
def create_connection(database_file):
    conn = None
    try:
        conn = sqlite3.connect(database_file)
        print(f"Connected to the database: SQLite {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
    return conn

# Function to create the 'Registration' table
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Table created successfully")
    except Error as e:
        print(e)

# Function to create a new record in the 'Registration' table
def create_record(conn, name, email, dob):
    sql = ''' INSERT INTO Registration(Name, Email, DateOfBirth)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (name, email, dob))
    conn.commit()
    return cur.lastrowid

# Function to retrieve all records from the 'Registration' table
def read_records(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Registration")
    rows = cur.fetchall()
    return rows

# Function to update an existing record in the 'Registration' table
def update_record(conn, id, name, email, dob):
    sql = ''' UPDATE Registration
              SET Name = ? ,
                  Email = ? ,
                  DateOfBirth = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (name, email, dob, id))
    conn.commit()

# Function to delete a record from the 'Registration' table
def delete_record(conn, id):
    sql = 'DELETE FROM Registration WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

# Main function
def main():
    database = r"registration.db"  # SQLite database file

    # Create a database connection
    # conn = create_connection(database)
    # Create a database connection
    conn = create_connection(r"registration.db")

    if conn is not None:
        # Create 'Registration' table
        create_table(conn, """
                                    CREATE TABLE IF NOT EXISTS Registration (
                                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        Name TEXT NOT NULL,
                                        Email TEXT NOT NULL,
                                        DateOfBirth DATE
                                    );
                                """)

        # Example usage: Create a record
        create_record(conn, "John Doe", "john@example.com", "1990-01-01")
        
        # Example usage: Retrieve all records
        records = read_records(conn)
        print("All Records:")
        for record in records:
            print(record)
        
        # Example usage: Update a record
        update_record(conn, 1, "Jane Doe", "jane@example.com", "1995-05-05")
        update_record(conn, 2,"Prasad Sonawane","prasadsonawane101@gmail.com","2002-01-02" )
        # Example usage: Delete a record
        delete_record(conn, 1)

        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
