# auth.py

from flask import Blueprint, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from app import db
from app import jwt
from app import app
from models import User

auth = Blueprint("auth", __name__)




@auth.route("/register", methods=["POST"])
def register():
    """Registers a new user."""
    data = request.json
    username = data["username"]
    password = data["password"]

    if db.session.query(User).filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 409

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered"})

@auth.route("/login", methods=["POST"])
def login():
    """Logs in a user and returns a JWT token."""
    username = request.json["username"]
    password = request.json["password"]

    if not db.session.query(User).filter_by(username=username, password=password).first():
        return jsonify({"error": "Invalid username or password"}), 401

    user = db.session.query(User).filter_by(username=username).first()
    token = jwt.encode({"user_id": user.id}, app.config["JWT_SECRET_KEY"])

    return jsonify({"token": token})
