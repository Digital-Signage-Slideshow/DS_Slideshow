from flask import render_template, request, redirect, url_for, flash, abort, \
    jsonify, Blueprint
from werkzeug.utils import secure_filename
from flask_login import login_required
import os

from config import upload_folder, allowed_extensions
from slideshow.extensions import db
from .models import Content

bp = Blueprint('core', __name__, template_folder='templates')

rotation_speed = 10000  # in miliseconds


def allowed_files(filename):
    return lambda f: '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


@bp.errorhandler(500)
def custom_500(error: dict):
    response = jsonify({'message': error})


@bp.route('/remove_content', methods=['GET', 'POST'])
def remove_content():
    if request.method == 'POST':
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
        file = request.files.get('file')

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


@bp.route('/')
@login_required
def index():
    return render_template('index.html')


@bp.route('/setup')
@login_required
def setup():
    global rotation_speed

    contents = Content.query.all()

    return render_template(
        'setup.html',
        contents=contents,
        rotation_speed=rotation_speed // 1000
    )


@bp.route('/slideshow')
def slideshow():
    print('called')
    images = os.listdir(upload_folder)
    links = db.session.query(Content).filter(Content.type == 'link')

    return render_template(
        'slideshow.html',
        images=images,
        links=[link.path for link in links],
        rotation_speed=rotation_speed,
    )
