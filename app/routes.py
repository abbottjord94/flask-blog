from app import app
from flask import render_template

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
