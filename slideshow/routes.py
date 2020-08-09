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


# def get_links() -> list:
#     return db.Content.filter_by(type='link')

@bp.errorhandler(500)
def custom_500(error: dict):
    response = jsonify({'message': error})

@bp.route('/remove_image', methods=['GET', 'POST'])
def remove_image():
    name = request.form.to_dict()
    index = int(name['imageID']) - 1

    files = os.listdir(upload_folder)

    os.remove(f'{upload_folder}/{files[index]}')
    Content.query.filter_by(type='file', path=files[index]).delete()

    return redirect(url_for('core.setup'))

@bp.route('/remove_link', methods=['GET', 'POST'])
def remove_link():
    link = request.form.to_dict()
    Content.query.filter_by(type='link').delete()

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

    return render_template(
        'index.html',
        images=images,
        # links=[i[0] for i in get_links()],
        rotation_speed=rotation_speed
    )

@bp.route('/register', methods = ['GET', 'POST'])
def register():
    form = Register()

    if current_user.is_authenticated:
        return redirect(url_for('core.setup'))

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = User(username = 'Admin', password = hashed_password) # may allow multiple users in future  
        db.session.add(user)
        db.session.commit()

        print('admin password set')
        flash('admin password set') # currently not implemented
        return redirect(url_for('core.login'))

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