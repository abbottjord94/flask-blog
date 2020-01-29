from app import app
from flask import render_template, request, Response
from helper_functions import getMimeType
import os

items = [
	{
		'id':"a431f",
		'author': "Jordan Abbott",
		'text': "Epstein Didn't Kill Himself",
		'replies': [
			{
				'text':"yes indeed"
			},
			{
				'text':"hillary did it"
			}
		]
	},
	{
		'id':"r53fg",
		'author': "Jordan Abbott",
		'text': "All hail our mightly robot overlords",
		'replies': [
			{
				'text':"no"
			},
			{
				'text':"all hail calculotron"
			}
		]
	}
]

@app.route('/')
def home():
	return render_template('index.html', posts=items)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/post', methods = ['GET', 'POST'])
def post():
	if request.method == "POST":
		title = request.form.get('post_title')
		text = request.form.get('post_text')
		new_post = {
			'title':title,
			'text':text
		}
		print(new_post)
		return render_template('post.html')
	if request.method == "GET":
		return render_template('post.html')

#Generic route (i.e., serving static files)
@app.route('/<content>')
def render_content(content):
	file = os.path.join(os.path.dirname(__file__) + '/site/', content)
	return Response(open(file).read(), mimetype=getMimeType(file))
