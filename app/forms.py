from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class ThreadForm(FlaskForm):
	title = StringField('thread-title', validators=[DataRequired(), Length(min=2, max=300)])
	body = StringField('thread-body', validators=[DataRequired()])
	submit = SubmitField('Post')
