from flask import Flas, request, jsonfiy, url_for, BluePrint
from api.models import db, User
import os
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


api = BluePrint("api", __name__)

app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

jwt = JWTManager(app)

@api.route("/token", methods = ["POST", "GET"])
