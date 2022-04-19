from flask import Blueprint, render_template, request

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        room_code = request.form.get("room")
        pw = request.form.get("password")
        # TODO: Check room and password hash

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        room_code = 0 # TODO: Randomize room code
        pw = request.form.get("password")
        # TODO: Add room and pasword hash to the database