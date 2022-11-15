from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired
from datetime import datetime

class AddPost(FlaskForm):
    title = StringField('Title', validators=[DataRequired(message="The title cannot be left blank")])
    datePosted = datetime.now()
    text = StringField('Your post topic. ', validators=[DataRequired(message="The text cannot be left blank")])
    submit = SubmitField('Add post to your blog')
    
class UpdatePost(FlaskForm):
    title = StringField('Title', validators=[DataRequired(message="The title cannot be left blank")])
    datePosted = datetime.now()
    text = StringField('Your post topic. ', validators=[DataRequired(message="The text cannot be left blank")])
    submit = SubmitField('Update post')
    
class AddUser(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired(message="The the username cannot be left blank")])
    password = StringField('Password: ', validators=[DataRequired(message="The password cannot be left blank")])
    submit = SubmitField('Add user')
    
class EditUser(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired(message="The the username cannot be left blank")])
    password = StringField('Password: ', validators=[DataRequired(message="The password cannot be left blank")])
    submit = SubmitField('Update user')
     
class SelectUser(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired(message="The the username cannot be left blank")])
    password = StringField('Password: ', validators=[DataRequired(message="The password cannot be left blank")])
    submit = SubmitField('Login') 