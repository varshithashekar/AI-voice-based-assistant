import csv
import sqlite3
import webbrowser

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

# Create contacts table
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
#     id INTEGER PRIMARY KEY,
#     name VARCHAR(200),
#     mobile_no VARCHAR(255),
#     email VARCHAR(255) NULL
# )''')

# # Create web_command table
# cursor.execute('''CREATE TABLE IF NOT EXISTS web_command (
#     id INTEGER PRIMARY KEY,
#     name VARCHAR(200),
#     url VARCHAR(255)
# )''')

# # Create sys_command table
# cursor.execute('''CREATE TABLE IF NOT EXISTS sys_command (
#     id INTEGER PRIMARY KEY,
#     name VARCHAR(200),
#     path VARCHAR(255)
# )''')

# # Commit the changes
# con.commit()
# print("Tables created successfully!")

# # Close the connection
# con.close()


# query = "INSERT INTO web_command VALUES (null,'google','https://www.google.com/')"
# cursor.execute(query)
# con.commit()
# query = "INSERT INTO web_command VALUES (null,'youTube','https://www.youtube.com')"
# cursor.execute(query)
# con.commit()
# query = "INSERT INTO web_command VALUES (null,'snapchat','https://www.snapchat.com/')"
# cursor.execute(query)
# con.commit()
# query = "INSERT INTO web_command VALUES (null,'github','https://www.github.com/')"
# cursor.execute(query)
# con.commit()
# query = "INSERT INTO web_command VALUES (null,'hackerrank','https://www.hackerank.com/')"
# cursor.execute(query)
# # con.commit()
# query = "INSERT INTO web_command VALUES (null,'spotify','https://open.spotify.com')"
# cursor.execute(query)
# con.commit()
