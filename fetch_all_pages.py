import pymysql  # Install this library if not already present: pip install pymysql

# Database connection details (replace with your actual values)
host = ""
user = ""
password = ""
database = ""  # Replace with the name of your database

# Connect to the database
try:
    connection = pymysql.connect(
        host=host, user=user, password=password, database=database
    )
except Exception as e:
    print("Error connecting to database:", e)
    exit()

# Create a cursor object
cursor = connection.cursor()

# Select rows from the database
query = "SELECT page_title, page_touched, old_text FROM tech_revision,tech_page,tech_text WHERE tech_revision.rev_id=tech_page.page_latest AND tech_text.old_id=tech_revision.rev_id LIMIT 10;"
try:
    cursor.execute(query)
    rows = cursor.fetchall()

    # Print all rows
    for row in rows:
        print(row[0])

except Exception as e:
    print("Error reading data from database:", e)
    exit()


# Close the cursor and database connection
cursor.close()
connection.close()
