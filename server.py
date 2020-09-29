import os
import dotenv
from src.api import app
from src.config.configuration import PORT

app.run("0.0.0.0", PORT, debug=True) 
