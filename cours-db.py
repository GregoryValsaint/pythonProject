from os import getenv

from mysql import connector
import params
from dotenv import load_dotenv
load_dotenv()

print(getenv("DB_NAME"))


db = connector.connect(
    host="localhost",
    database=getenv("DB_NAME"),
    user=getenv("DB_USER"),
    password=getenv("DB_PASS")
)

cursor = db.cursor(dictionary=True)

#
# cursor = db.cursor()
# username="shinoby"
# first_name="Grégory"
# last_name="Valsaint"
#
# cursor.execute("INSERT INTO user (username, first_name, last_name) VALUES (%s, %s, %s)",(username,first_name,last_name))

# cursor.execute("INSERT INTO user (username, first_name, last_name) VALUES (%(username)s, %(user_first_name)s, %(user_last_name)s)",
#                {'user_username': username,"user_first_name": first_name,"user_last_name": last_name}
#             )

#pour récupérer qu'un seul champ de tous les utilisateur
# cursor.execute("SELECT * FROM user ")
#
# while True:
#     user = cursor.fetchone()
#     if user == None:
#         break
#     else:
#         print(user['username'])

#pour récupérer qu'un seul champ de tous les utilisateur
query = "SELECT username FROM user WHERE id = %(id)s"

cursor.execute(query, {"id":3})

user = cursor.fetchone()
print(user['username'])


db.commit()

