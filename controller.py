# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, flash, abort, jsonify
import os
import sqlite3
from werkzeug.utils import secure_filename

__author__ = 'Harry Lees'
__date__ = '05.08.2020'

rotation_speed = 10000 # in miliseconds
upload_folder = 'static/images/slideshowImages'
allowed_extensions = ['png', 'jpg', 'jpeg']

app = Flask(__name__)

allowed_files = lambda filename : '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def get_links() -> tuple:
	with sqlite3.connect('link_database.db') as connection:
		cursor = connection.execute('SELECT * FROM links')
		return cursor.fetchall()

@app.errorhandler(500)
def custom_500(error : dict):
	response = jsonify({'message' : error.description['message']})

@app.route('/remove_image', methods = ['GET', 'POST'])
def remove_image():
	name = request.form.to_dict()
	index = int(name['imageID']) - 1

	files = os.listdir(upload_folder)

	os.remove(f'{upload_folder}/{files[index]}')
	return redirect('/setup')

@app.route('/remove_link', methods = ['GET', 'POST'])
def remove_link():
	link = request.form.to_dict()
	index = int(link['linkID']) - 1

	with sqlite3.connect('link_database.db') as connection:
		cursor = connection.cursor()

		data = cursor.execute('SELECT * FROM LINKS')
		path_name = list(data.fetchall())[index][0]

		cursor.execute('DELETE FROM LINKS WHERE path = ?', [path_name])

	return redirect('/setup')

@app.route('/alter_rotation_speed', methods = ['GET', 'POST'])
def alter_rotation_speed():
	global rotation_speed

	try:
		rotation_speed = float(request.form.to_dict()['alterRotationSpeed']) * 1000
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

	return redirect('/setup')

@app.route('/upload_link', methods = ['GET', 'POST'])
def upload_link():
	if request.method == 'POST':
		link = request.form.to_dict()['linkUpload']
	else:
		abort(500, 'failed to upload link')

	with sqlite3.connect('link_database.db') as connection:
		connection.execute('INSERT INTO links VALUES(?)', [link])

	return redirect('/setup')

@app.route('/setup')
def return_setup():
	global rotation_speed

	images = os.listdir(upload_folder)

	return render_template(
		'setup.html', 
		images = images, 
		links = [i[0] for i in get_links()], 
		rotation_speed = rotation_speed // 1000
	)

@app.route('/')
def return_index():
	images = os.listdir(upload_folder)

	return render_template(
		'index.html', 
		images = images, 
		links = [i[0] for i in get_links()],
		rotation_speed = rotation_speed
	)

if __name__ == '__main__':
	app.run(host = '0.0.0.0', debug = True, port = 5000)

	with sqlite3.connect('link_database.db') as connection:
		connection.execute("CREATE TABLE IF NOT EXISTS links('path' TEXT PRIMARY KEY)")
