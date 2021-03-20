import os

from api.extensions import db
from config import allowed_extensions, upload_folder
from flask import (
                Blueprint, abort, 
                jsonify,
                request,
                Response
                )
from flask_jwt_extended import jwt_required
from werkzeug.utils import secure_filename

from .models import Content

blueprint = Blueprint(
    'core', 
    __name__, 
    template_folder='templates'
)
rotation_speed = 10000  # in miliseconds

def allowed_files(filename):
    return lambda f: '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@blueprint.route('/remove_content', methods=['POST'])
@jwt_required()
def remove_content():
    content_id = request.json.get('content_id')

    content = Content.query.filter_by(path=content_id)
    cont_object = content.first()

    if cont_object.type == 'file':
        os.remove(f'{upload_folder}/{cont_object.path}')
        content.delete()
    else:
        content.delete()

    db.session.commit()

    return Response(status=200)

@blueprint.route('/upload_file', methods=['POST'])
@jwt_required()
def upload_file():
    file = request.files.get('file')

    if file and allowed_files(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(upload_folder, filename))

        new_file = Content(type='file', path=filename)
        db.session.add(new_file)
        db.session.commit()
    else:
        return jsonify({'message' : 'file format invalid'}), 401

    return Response(status=200)

@blueprint.route('/upload_link', methods=['GET', 'POST'])
@jwt_required()
def upload_link():
    if request.method == 'POST':
        path = request.form.to_dict()['upload_link']
        new_link = Content(type='link', path=path)
        db.session.add(new_link)
        db.session.commit()
    else:
        abort(500, 'failed to upload link')