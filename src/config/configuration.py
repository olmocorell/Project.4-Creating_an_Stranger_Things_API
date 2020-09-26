import os
import dotenv
env_path = os.path.join(os.path.dirname(__file__),'..', '.env')
dotenv.load_dotenv(dotenv_path=env_path)


# Connect to the database
dbURL = os.getenv('DB_URL')
print(dbURL)
if not dbURL:
    raise ValueError("You should specify MONGODB_URL environment variable")