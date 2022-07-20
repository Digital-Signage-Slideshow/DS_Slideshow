from flask import render_template, request, redirect, url_for, flash, jsonify, Blueprint
from werkzeug.utils import secure_filename
from flask_login import login_required
import os

from slideshow.extensions import db
from slideshow.utils import allowed_file_extensions, get_file_extension, generate_uuid
from .models import Content

from config import UPLOAD_FOLDER

bp = Blueprint('core', __name__, template_folder='templates')

rotation_speed = 10000  # in miliseconds
upload_folder = UPLOAD_FOLDER


@bp.errorhandler(500)
def custom_500(error: dict):
    response = jsonify({'message': error})


@bp.get('/')
@login_required
def index():
    """
    Displays the index page.
    """
    return render_template('index.html')


@bp.get('/login')
def login():
    """
    Displays the login page.
    """
    return redirect(url_for('user.login'))


@bp.get('/register')
def register():
    """
    Displays the register page.
    """
    return redirect(url_for('user.register'))


@bp.get('/setup')
@login_required
def setup():
    """
    Displays the setup page.
    """
    contents = Content.query.all()
    return render_template('setup.html', contents=contents, rotation_speed=rotation_speed // 1000)


@bp.get('/slideshow')
def slideshow():
    """
    Displays the slideshow page.
    """
    contents = Content.query.filter_by(active=True).all()

    return render_template(
        'slideshow.html',
        contents=contents,
        rotation_speed=rotation_speed,
    )


@bp.post('/alter_rotation_speed')
def alter_rotation_speed():
    """
    Changes the rotation speed of the slideshow.
    """
    global rotation_speed

    try:
        rotation_speed = float(
            request.form.to_dict()['alter_rotation_speed']) * 1000
    except Exception as e:
        flash('Please enter a number')

    return redirect(url_for('core.setup'))


@bp.post('/upload_file/')
@login_required
def upload_file():
    """
    Uploads a file to the server.
    """
    file = request.files['file']

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    if file and allowed_file_extensions(file.filename):
        # Upload the file to the uploads folder
        file_ext = get_file_extension(file.filename)
        filename = secure_filename(generate_uuid() + '.' + file_ext)
        file.save(os.path.join(upload_folder, filename))
        flash('File uploaded successfully')

        # Create a new content object
        content = Content(type='file', path=filename)
        db.session.add(content)
        db.session.commit()

        return redirect(url_for('core.setup'))


@bp.post('/remove_content')
@login_required
def remove_content():
    """
    Removes a content object from the server.
    Removes the file from the uploads' folder.
    """
    content_id = request.form.get('content_id')
    content = Content.query.filter_by(path=content_id)
    cont_object = content.first()

    if cont_object.type == 'file':
        os.remove(f'{upload_folder}/{cont_object.path}')
        content.delete()
    else:
        content.delete()
    db.session.commit()
    return redirect(url_for('core.setup'))


@bp.post('/upload_link')
@login_required
def upload_link():
    """
    Adds a link to the database.
    """
    link = request.form.to_dict()['upload_link']

    if link:
        # Create a new content object
        content = Content(type='link', path=link)
        db.session.add(content)
        db.session.commit()

        return redirect(url_for('core.setup'))
    else:
        flash('Please enter a link')
        return redirect(url_for('core.setup'))
