from app import app
from flask import render_template, request, redirect, Response, session
from helper_functions import getMimeType
from glorious_database import Database
import os
import json
import datetime

users = Database("users.json")
threads = Database("threads.json")
database_change_queue = []

@app.route('/')
def home():
	_items = []
	_threads = threads.data()
	for _t in _threads:
		_items.append(_threads[_t])
	return render_template('index.html', posts = _items)

@app.route('/post', methods = ['GET', 'POST'])
def post():
	if request.method == "POST":
		_title = request.form.get('post_title')
		_text = request.form.get('post_text')
		_now = datetime.datetime.today()
		_nows = _now.strftime("%A, %B %d, %Y, %H:%M:%S")
		_id = hash(_text + _nows)
		new_post = {
			'post_title':_title,
			'post_text':_text,
			'time':_nows,
			'replies':[],
			'id':_id
		}
		threads.insert(_id, new_post)
		return render_template('index.html')
	if request.method == "GET":
		return render_template('post.html')

@app.route('/reply/<thread>', methods = ['GET', 'POST'])
def reply(thread):
	if request.method == "POST":
		_text = request.form.get('reply_text')
		_time = datetime.datetime.today().strftime("%A, %B %d, %Y, %H:%M:%S")
		_thread = threads.data()[thread]
		_thread['replies'].append( {"time":_time, "text":_text} )
		threads.delete(thread)
		threads.insert(thread,_thread)
		return redirect("/",code=302)
	if request.method == "GET":
		return redirect("/",code=302)

@app.route('/edit/<page>', methods = ['GET', 'POST'])
def edit(page):
	if request.method == "GET":
		if session['username']:
			return Response(open(os.path.join(os.path.dirname(__file__)) + '/site/' + page).read(), mimetype='text/plain')
		else:
			return render_template('login.html')
	if request.method == "POST":
		if session['username']:
			_text = request.form.get('file_text')
			_filename = request.form.get('filename')
			_file = open(os.path.join(os.path.dirname(__file__)) + '/site/' + _filename, "w+")
			_file.write(_text)
			_file.close()
			return render_template(_filename)
		else:
			return render_template('login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == "GET":
		return render_template('login.html')
	if request.method == "POST":
		_user = request.form.get('username')
		_pass = request.form.get('pass')
		if users.data()[_user]['password'] == _pass:
			session['username'] = _user
			return render_template('index.html')
		else:
			return render_template('loginfailed.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
	if request.method == "POST":
		_username = request.form.get('username')
		_pass = request.form.get('pass')
		if(users.data().get(_username)):
			return render_template("postregister.html", success=False)
		else:
			users.insert(_username, {'password':_pass})
			return render_template("postregister.html", success=True)

	if request.method == "GET":
		return render_template("register.html")

@app.route('/all')
def all():
	_dir = os.path.join(os.path.dirname(__file__)) + '/site/'
	_docs = os.listdir(_dir)
	_pages = []
	for p in _docs:
		_ext = os.path.splitext(p)[1]
		if(_ext == ".html"):
			_pages.append(os.path.splitext(p)[0])
	return render_template('all.html', pages=_pages)

#Generic route (i.e., serving static files)
@app.route('/<content>')
def render_content(content):
	_file = os.path.join(os.path.dirname(__file__) + '/site/', content)
	return Response(open(_file).read(), mimetype=getMimeType(_file))

