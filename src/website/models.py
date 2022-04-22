from . import db
from datetime import datetime

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer, unique=True)
    password_hash = db.Column(db.String(500))
    orders = db.relationship("Order", backref="room", lazy="dynamic")

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"))
    name = db.Column(db.String(500))
    notes = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, default=datetime.now())
