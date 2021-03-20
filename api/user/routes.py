from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
from flask_jwt_extended import create_access_token, current_user, jwt_required
from werkzeug.security import generate_password_hash

from api.extensions import db, jwt

from .forms import RegisterForm, LoginForm, EditProfileForm
from .models import User

blueprint = Blueprint(
    'user', 
    __name__, 
    template_folder='templates', 
    url_prefix='/user/'
)

@jwt.user_identity_loader
def user_id_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    return User.query.filter_by(id=identity).one_or_none()

@blueprint.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()

    if user is None or not user.check_password(password):
        return jsonify('Incorrect username or password'), 401

    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token)

@blueprint.route('/register', methods=['POST'])
def register_user():
    pass

@blueprint.route('/test', methods=['GET'])
@jwt_required
def protected():
    return jsonify(
        id=current_user.id,
        full_name=current_user.full_name,
        username=current_user.username
    )