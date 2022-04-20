from flask import Blueprint, render_template, flash

views = Blueprint("views", __name__)

@views.route("/")
def root():
    return render_template("index.html")
