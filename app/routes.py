from app import app
from flask import render_template, request

items = [
	{
		'author': "Jordan Abbott",
		'text': "Epstein Didn't Kill Himself"
	},
	{
		'author': "Jordan Abbott",
		'text': "All hail our mightly robot overlords"
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
		print(request.form.get('post_title'))
		print(request.form.get('post_text'))
		return render_template('post.html')
	if request.method == "GET":
		return render_template('post.html')
