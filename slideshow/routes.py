from flask import render_template, request, redirect, url_for, flash, abort, jsonify
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from slideshow import app
import os
from slideshow import database

rotation_speed = 10000 # in miliseconds
upload_folder = f'{os.path.dirname(__file__)}/static/images/slideshow_images'
allowed_extensions = ['png', 'jpg', 'jpeg']

allowed_files = lambda filename : '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def get_links() -> list:
    return database.Content.filter_by(type = 'link')

@app.errorhandler(500)
def custom_500(error : dict):
    response = jsonify({'message' : error})

@app.route('/remove_image', methods = ['GET', 'POST'])
def remove_image():
    name = request.form.to_dict()
    index = int(name['imageID']) - 1

    files = os.listdir(upload_folder)

    os.remove(f'{upload_folder}/{files[index]}')
    database.query.filter_by(type = 'file', path = files[index]).delete()

    return redirect('/setup')

@app.route('/remove_link', methods = ['GET', 'POST'])
def remove_link():
    link = request.form.to_dict()
    database.query.filter_by(type = 'link', path = path).delete()

    return redirect('/setup')

@app.route('/alter_rotation_speed', methods = ['GET', 'POST'])
def alter_rotation_speed():
    global rotation_speed

    try:
        rotation_speed = float(request.form.to_dict()['alter_rotation_speed']) * 1000
    except Exception as e:
        flash('Please enter a number')

    return redirect('/setup')

@app.route('/upload_file', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect('/setup')

        file = request.files['file']
    else:
        abort(500, 'failed to upload file')

    if file and allowed_files(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(upload_folder, filename))

        new_file = Content(type = 'file', path = filename, priority = priority)
        database.session.add(new_file)
        database.session.commit()

    return redirect('/setup')

@app.route('/upload_link', methods = ['GET', 'POST'])
def upload_link():
    if request.method == 'POST':
        path = request.form.to_dict()['upload_link']
    else:
        abort(500, 'failed to upload link')

    new_link = Content(type = 'link', path = path, priority = priority)
    database.session.add(new_link)
    database.session.commit()

    return redirect(url_for('main.setup'))

@app.route('/setup')
# @login_required
def setup():
    global rotation_speed

    images = os.listdir(upload_folder)

    return render_template(
        'setup.html', 
        images = images, 
        links = [i[0] for i in get_links()], 
        rotation_speed = rotation_speed // 1000
    )

@app.route('/')
def slideshow():
    images = os.listdir(upload_folder)

    return render_template(
        'index.html', 
        images = images, 
        links = [i[0] for i in get_links()],
        rotation_speed = rotation_speed
    )