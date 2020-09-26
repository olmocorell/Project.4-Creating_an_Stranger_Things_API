import os
import dotenv
from src.api import app
dotenv.load_dotenv()



app.run("0.0.0.0", os.getenv("PUERTO"), debug=True)
