from flask import Blueprint, jsonify, request, Response
from flask_jwt_extended import create_access_token, jwt_required
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
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    return User.query.filter_by(id=identity).one_or_none()

@blueprint.route('/login', methods=['POST'])
def login():
    '''
    function to check whether a users credentials are correct and issue a new JWT token on login.
    '''

    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()

    if user is None or not user.check_password(password):
        return jsonify('Incorrect username or password'), 401

    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token)

@blueprint.route('/register', methods=['POST'])
def register_user():
    '''
    function to register a new user account.
    '''

    pass

@blueprint.route('/token_valid', methods=['GET'])
@jwt_required()
def token_valid():
    '''
    function to check whether a JWT token is valid.
    NOT IMPLEMENTED YET.
    '''

    return Response(status=200)

@blueprint.route('/logout', methods=['GET'])
@jwt_required()
def logout():
    '''
    function to blacklist JWT tokens on logout.
    NOT IMPLEMENTED YET.
    '''

    return Response(status=200)