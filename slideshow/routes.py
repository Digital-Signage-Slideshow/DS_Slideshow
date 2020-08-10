from flask import render_template, request, redirect, url_for, flash, abort, \
    jsonify, Blueprint
from werkzeug.utils import secure_filename
from flask_login import login_user, login_required, current_user, logout_user, login_required
import os

from .extensions import db, bcrypt, login_manager, session
from .forms import Register, Login
from .models import User, Content

rotation_speed = 10000  # in miliseconds
upload_folder = f'{os.path.dirname(__file__)}/static/images/slideshow_images'
allowed_extensions = ['png', 'jpg', 'jpeg']

bp = Blueprint('core', __name__, template_folder='templates')

def allowed_files(filename):
    return lambda f: '.' in filename and filename.rsplit('.', 1)[
        1].lower() in allowed_extensions

@bp.errorhandler(500)
def custom_500(error: dict):
    response = jsonify({'message': error})

@bp.route('/remove_image', methods=['GET', 'POST'])
def remove_image():
    if request.method == 'POST':
        filename = request.form.get('image_id')

        os.remove(f'{upload_folder}/{filename}')
        Content.query.filter_by(type='file', path = filename).delete()
        db.session.commit()

    return redirect(url_for('core.setup'))

@bp.route('/remove_link', methods=['GET', 'POST'])
def remove_link():
    link = request.form.get('link')
    Content.query.filter_by(type = 'link', path = link).delete()
    db.session.commit()

    return redirect(url_for('core.setup'))

@bp.route('/alter_rotation_speed', methods=['GET', 'POST'])
def alter_rotation_speed():
    global rotation_speed

    try:
        rotation_speed = float(
            request.form.to_dict()['alter_rotation_speed']) * 1000
    except Exception as e:
        flash('Please enter a number')

    return redirect(url_for('core.setup'))

@bp.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        # priority =
        if 'file' not in request.files:
            return redirect(url_for('core.setup'))
        if file and allowed_files(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_folder, filename))

            new_file = Content(type='file', path=filename)
            db.session.add(new_file)
            db.session.commit()
    else:
        abort(500, 'failed to upload file')

    return redirect(url_for('core.setup'))

@bp.route('/upload_link', methods=['GET', 'POST'])
def upload_link():
    if request.method == 'POST':
        path = request.form.to_dict()['upload_link']
        new_link = Content(type='link', path=path)
        db.session.add(new_link)
        db.session.commit()
    else:
        abort(500, 'failed to upload link')

    return redirect(url_for('core.setup'))

@bp.route('/setup')
@login_required
def setup():
    global rotation_speed

    images = os.listdir(upload_folder)
    links = db.session.query(Content).filter(Content.type == 'link')

    return render_template(
        'setup.html',
        images = images,
        links = links,
        rotation_speed = rotation_speed // 1000
    )

@bp.route('/')
def slideshow():
    images = os.listdir(upload_folder)
    links = db.session.query(Content).filter(Content.type == 'link')

    return render_template(
        'index.html',
        images = images,
        links = [link.path for link in links],
        rotation_speed = rotation_speed,
    )

@bp.route('/register', methods = ['GET', 'POST'])
def register():
    print('function called')
    form = Register()

    if current_user.is_authenticated:
        print('user already logged in')
        return redirect(url_for('core.setup'))

    if form.validate_on_submit():
        print('form valid')
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = User(username = 'Admin', password = hashed_password) # may allow multiple users in future  
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('core.login'))
    elif form.errors.get('password') == ['active_password']:
        flash('there is already an active admin password set, please <a href = "/login">login</a> instead')

    return render_template('register.html', form = form)

@bp.route('/login', methods = ['GET', 'POST'])
def login():
    form = Login()

    if current_user.is_authenticated:
        return redirect(url_for('core.setup'))

    if form.validate_on_submit():
        user = User.query.filter_by(id = 1).first()
        
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            return redirect(url_for('core.setup'))
        else:
            flash('Login unsuccesful, please check password')

    return render_template('login.html', form = form)

@bp.route('/logout', methods = ['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('core.login'))