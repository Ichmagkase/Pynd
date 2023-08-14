import sqlite3
import csv
import sys
import os

# Check for proper usage
if len(sys.argv) != 3:
    print("Invalid function call: Requires 2 parameters (python csvtodb.py [new .db name (excluding .db)] [.csv file])")
    exit()

# Create an SQLite database or connect to an existing one
database_file = (sys.argv[1] + '.db')
conn = sqlite3.connect(database_file)
cursor = conn.cursor()

# Create a table to hold the CSV data (if it doesn't exist already)
table_name = sys.argv[1]
create_table_query = """
    CREATE TABLE IF NOT EXISTS {} (
        name TEXT,
        type TEXT,
        dmg INTEGER,
        desc TEXT

    )
""".format(table_name)
cursor.execute(create_table_query)

# Read the CSV file and insert data into the SQLite table
csv_file = sys.argv[2]
with open(csv_file, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip the header row if it exists in the CSV file
    for row in csv_reader:
        insert_query = "INSERT INTO {} (name, type, dmg, desc) VALUES (?, ?, ?, ?)".format(table_name)
        cursor.execute(insert_query, (row[0], row[1], row[2], row[3]))

# Prompt the user
prompt = input(f"Would you like to delete {sys.argv[2]}? Y/n ")
if prompt.lower() == 'y':
    os.remove(sys.argv[2])

prompt = input(f"Would you like to move {database_file} to databases? Y/n ")

if prompt.lower() == 'y':
    os.rename(database_file, f'databases\{database_file}')

# Commit the changes and close the connection
conn.commit()
conn.close()