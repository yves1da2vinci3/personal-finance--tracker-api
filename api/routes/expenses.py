# expenses.py

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import db
from models import Expense

expenses = Blueprint("expenses", __name__)

@expenses.route("/", methods=["GET", "POST", "PUT", "DELETE"])
@jwt_required()
def expenses():
    """Handles requests for the expenses resource."""
    if request.method == "GET":
        expenses = db.session.query(Expense).all()
        return jsonify([expense.serialize() for expense in expenses])
    elif request.method == "POST":
        data = request.json
        expense = Expense(name=data["name"], amount=data["amount"], date=data["date"])
        db.session.add(expense)
        db.session.commit()
        return jsonify(expense.serialize())
    elif request.method == "PUT":
        data = request.json
        expense = db.session.query(Expense).filter_by(id=data["id"]).first()
        expense.name = data["name"]
        expense.amount = data["amount"]
        expense.date = data["date"]
        db.session.commit()
        return jsonify(expense.serialize())
    elif request.method == "DELETE":
        id = request.json["id"]
        expense = db.session.query(Expense).filter_by(id=id).first()
        db.session.delete(expense)
        db.session.commit()
        return jsonify({"message": "Expense deleted"})

