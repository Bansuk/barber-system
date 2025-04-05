"""
Main entry point for the Flask application.

This module initializes the Flask app, sets up the database, 
registers routes, and starts the application.
"""

from flask import Flask
from flask_smorest import Api
from database.db_setup import init_db
from routes import register_routes

app = Flask(__name__)
app.config['API_TITLE'] = "Barber System"
app.config['API_VERSION'] = "1.0"
app.config['OPENAPI_VERSION'] = "3.0.2"
app.config['OPENAPI_URL_PREFIX'] = "/api/docs"
app.config['OPENAPI_SWAGGER_UI_PATH'] = "/swagger-ui"
app.config['OPENAPI_SWAGGER_UI_URL'] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

init_db(app)

register_routes(api)

if __name__ == "__main__":
    app.run(debug=True)
