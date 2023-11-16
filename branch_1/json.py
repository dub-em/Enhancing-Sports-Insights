import json
import psycopg2

# PostgreSQL database connection parameters
connection_params = {
    "host": "testtech.postgres.database.azure.com",
    "port": "5432",
    "database": "postgres",
    "user": "testtech",
    "password": "George9042"
}

# Read JSON file
with open("dwsample2-json.json", "r") as file:
    json_data = json.load(file)
json_string = json.dumps(json_data)
# Connect to PostgreSQL
connection = psycopg2.connect(**connection_params)
cursor = connection.cursor()

create_query = '''CREATE TABLE IF NOT EXISTS json_data (
    id SERIAL PRIMARY KEY,
    data JSONB
);'''
cursor.execute(create_query)
# Insert JSON data into the table
insert_query = "INSERT INTO json_data (data) VALUES (%s);"
cursor.execute(insert_query, (json_string,))

select_query = "SELECT * FROM json_data;"
cursor.execute(select_query)

# Fetch all rows
rows = cursor.fetchall()

# Print the fetched data
for row in rows:
    print(row)
# Commit and close connection
connection.commit()
cursor.close()
connection.close()
