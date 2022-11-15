from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
class UserInfo(FlaskForm):
    userName = StringField()
    passWord = StringField()

@app.route('/')
def home():
    
    
    # if user_logged_in() == True:
    #     return redirect('http://my-app/game')
    # else:
    #     return 'This is a home page'
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/termsandprivacy')
def termsandprivacy():
    return render_template('termsandprivacy.html')


@app.route('/Game')
def game():
    return "Game Page"

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



# app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# db = SQLAlchemy(app)


