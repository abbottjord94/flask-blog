from flask import Flask, render_template, url_for
app = Flask(__name__, template_folder='site')
from app import routes

if __name__ == '__main__':
	app.run(debug=True)
