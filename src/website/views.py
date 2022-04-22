from flask import Blueprint, render_template, flash, request
from . import db
from .models import Order

views = Blueprint("views", __name__)

@views.route("/")
def root():
    return render_template("index.html")

@views.route("/place", methods=["POST"])
def place():
    room = request.form.get("room")
    order = request.form.get("order")
    notes = request.form.get("notes")
    if room and room != "" and order and order != "":
        if notes and notes != "":
            new_order = Order(room_id=room, name=order, notes=notes)
        else:
            new_order = Order(room_id=room, name=order, notes="0")
        db.session.add(new_order)
        db.session.commit()
    flash("Successfully placed order", "success")
    return render_template("room_host.html", room_code=room)

@views.route("/delete", methods=["POST"])
def delete():
    id = request.form.get("id")
    order = Order.query.get(id)
    room_id = request.form.get("room")
    if order and order != "":
        db.session.delete(order)
        db.session.commit()
        flash("Successfully deleted order", "success")
    return render_template("room_receiver.html", room_code=room_id, orders=Order.query.filter_by(room_id=room_id).all())