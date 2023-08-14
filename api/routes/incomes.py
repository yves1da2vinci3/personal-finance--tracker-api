from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import db
from models import Expense, Income

incomes = Blueprint("incomes", __name__)

@incomes.route("/", methods=["GET", "POST", "PUT", "DELETE"])
@jwt_required()
def incomes():
    """Handles requests for the incomes resource."""
    if request.method == "GET":
        incomes = db.session.query(Income).all()
        return jsonify([income.serialize() for income in incomes])
    elif request.method == "POST":
        data = request.json
        income = Income(name=data["name"], amount=data["amount"], date=data["date"])
        db.session.add(income)
        db.session.commit()
        return jsonify(income.serialize())
    elif request.method == "PUT":
        data = request.json
        income = db.session.query(Income).filter_by(id=data["id"]).first()
        income.name = data["name"]
        income.amount = data["amount"]
        income.date = data["date"]
        db.session.commit()
        return jsonify(income.serialize())
    elif request.method == "DELETE":
        id = request.json["id"]
        income = db.session.query(Income).filter_by(id=id).first()
        db.session.delete(income)
        db.session.commit()
        return jsonify({"message": "Income deleted"})

