from flask import Flask, flash, request
from .views import views
from .auth import auth

app = Flask(__name__)

app.register_blueprint(views)
app.register_blueprint(auth, url_prefix="/auth")

app.run(host="0.0.0.0", port=8080, debug=True)