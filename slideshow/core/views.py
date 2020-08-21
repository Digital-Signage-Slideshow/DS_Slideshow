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
        Content.query.filter_by(type='file', path=filename).delete()
        db.session.commit()

    return redirect(url_for('core.setup'))


@bp.route('/remove_link', methods=['GET', 'POST'])
def remove_link():
    link = request.form.get('link')
    Content.query.filter_by(type='link', path=link).delete()
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

    contents = Content.query.all()

    # images = os.listdir(upload_folder)
    # links = db.session.query(Content).filter(Content.type == 'link')

    return render_template(
        'core/setup.html',
        contents=contents,
        # images=images,
        # links=links,
        rotation_speed=rotation_speed // 1000
    )


@bp.route('/')
def slideshow():
    images = os.listdir(upload_folder)
    links = db.session.query(Content).filter(Content.type == 'link')

    return render_template(
        'core/index.html',
        images=images,
        links=[link.path for link in links],
        rotation_speed=rotation_speed,
    )
