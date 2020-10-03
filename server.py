from config.configuration import PORT
from controllers import api_controllers
from app import app

app.run("0.0.0.0", PORT, debug=True) 