from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

jwt = JWTManager(app)


if __name__ == "__main__":
    app.run(debug=True)
