"""
Main entry point for the Flask application.

This module initializes the Flask app, sets up the database, 
registers routes, and starts the application.
"""

from flask import Flask
from database.db_setup import init_db
from routes import register_routes

app = Flask(__name__)

init_db(app)

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
