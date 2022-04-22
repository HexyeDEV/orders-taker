from flask import Blueprint, render_template, request, flash
import random
from .models import Room, Order
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        room_code = request.form.get("room")
        pw = request.form.get("password")
        room = db.session.query(Room).filter_by(code=room_code).first()
        if room is None or room == "" or not check_password_hash(room.password_hash, pw):
            flash("Invalid room code or password", "error")
            return render_template("login.html")
        else:
            flash("Successfully logged in", "success")
            room_type = request.form.get("type")
            if room_type == "host":
                return render_template("room_host.html", room_code=room_code)
            elif room_type == "receiver":
                orders = db.session.query(Order).filter_by(room_id=room_code).all()
                return render_template("room_receiver.html", room_code=room_code, orders=orders)

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        room_code = random.randint(10000, 999999)
        while room_code in db.session.query(Room.code).all():
            room_code = random.randint(10000, 999999)
        return render_template("register.html", room_code=room_code)
    else:
        room_code = int(request.form.get("room"))
        pw = request.form.get("password")
        if room_code != None and room_code != "" and pw != None and pw != "" and not room_code in db.session.query(Room.code).all():
            db.session.add(Room(code=room_code, password_hash=generate_password_hash(pw)))
            db.session.commit()
            flash("Successfully registered", "success")
            return render_template("room_host.html", room_code=room_code)
        else:
            flash("Invalid room code or password", "error")
            return render_template("register.html")