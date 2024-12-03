from flask import Flask
from routes import book_bp
from flask_smorest import Api
from db import db
import os

# Initialize Flask App
app = Flask(__name__)

# Configuration
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Book Store API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///books.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize Extensions
api = Api(app)
db.init_app(app)

# Register Blueprint
api.register_blueprint(book_bp)

# Database Setup
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, port=5001)
