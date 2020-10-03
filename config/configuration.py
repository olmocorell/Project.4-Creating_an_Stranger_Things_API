import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

PORT = os.getenv("PORT")
DBURL = os.getenv("URL")

# Connect to the database

print(DBURL)
if not DBURL:
    raise ValueError("You should specify MONGODB_URL environment variable")


client = MongoClient(DBURL)
db = client.get_database()
coll_user = db['users']
coll_chat = db['chats']
coll_message = db['messages']
