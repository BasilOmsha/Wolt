# server.py
from flask import Flask
from Routes.routes import router as routes

app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
