# -*- coding: utf-8 -*-
# Written by Harry Lees

# Dependancies Below
from flask import Flask, render_template, request, redirect, url_for, flash
import os
import sqlite3
from werkzeug.utils import secure_filename

slideshowTime = 10000 # variable to control amount of time slides are shown for - miliseconds
uploadFolder = 'static/images/slideshowImages' # variable to control where the images that are uploaded will be stored
allowedExtensions = ['png', 'jpg', 'jpeg']

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = uploadFolder

@app.route('/removeImage', methods = ['GET', 'POST'])
def removeImage():
	name = request.form.to_dict()
	index = int(name['imageID']) - 1
	files = os.listdir(uploadFolder)

	os.remove(f'{uploadFolder}/{files[index]}')
	return redirect('/setup')

@app.route('/removeLink', methods = ['GET', 'POST'])
def removeLink():
	link = request.form.to_dict()
	index = int(link['linkID']) - 1

	with sqlite3.connect('linkDatabase.db') as connection:
		cursor = connection.execute('select * from links')

		for i, row in enumerate(cursor):
			if i == index:
				connection.execute(f'delete from links where path = \'{row[0]}\';')

	return redirect('/setup')

@app.route('/alterRotationSpeed', methods = ['GET', 'POST'])
def alterRotationSpeed():
	global slideshowTime

	try:
		slideshowTime = int(request.form.to_dict()['alterRotationSpeed'])*1000
	except Exception as e:
		flash('Please enter a number')

	return redirect('/setup')

@app.route('/uploadFile', methods = ['GET', 'POST'])
def uploadFile():
	if request.method == 'POST':
		if 'file' not in request.files: # check to see whether a file was uploaded
			return redirect('/setup')

		file = request.files['file']
	else:
		return '<p style = \'font-family: Verdana, Geneva; font-size: 12px;\'>Error, failed to upload file.</p>'

	if file.filename == '': # check that the file has a title
		return redirect('/setup')

	if file and allowedFiles(file.filename): # check that the files extension is valid
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

	return redirect('/setup')


@app.route('/uploadLink', methods = ['GET', 'POST'])
def uploadLink():
	if request.method == 'POST':
		uploadedLink = request.form.to_dict()['linkUpload']
	else:
		return '<p style = \'font-family: Verdana, Geneva; font-size: 12px;\'>Error, failed to upload link.</p>'

	with sqlite3.connect('linkDatabase.db') as connection:
		connection.execute('create table if not exists links(\'path\' text primary key)')
		connection.execute(f'insert into links values(\'{uploadedLink}\')')

	return redirect('/setup')

@app.route('/setup')
def returnSetup():
	global slideshowTime

	images = os.listdir(uploadFolder) # reads all of the images in the images folder

	with sqlite3.connect('linkDatabase.db') as connection:
		cursor = connection.execute('select * from links')
		links = cursor.fetchall()

	return render_template('setup.html', images = images, links = [i[0] for i in links], rotationSpeed = slideshowTime//1000)

def allowedFiles(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowedExtensions

@app.route('/')
def returnIndex():
	images = os.listdir(uploadFolder) # reads all of the images in the images folder

	with sqlite3.connect('linkDatabase.db') as connection:
		cursor = connection.execute('select * from links')
		links = cursor.fetchall()

	return render_template('index.html', images = images, slideshowTime = slideshowTime, links = [i[0] for i in links])

try:
	if __name__ == '__main__':
		app.run(host = '0.0.0.0', debug = True, port = 5001)

		with sqlite3.connect('linkDatabase.db') as connection:
			connection.execute('create table if not exists links(\'path\' text primary key)')

except Exception as e:
	print('Error: ', e)
	print('shutting down...')
