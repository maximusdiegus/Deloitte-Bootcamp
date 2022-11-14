from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def home():
    # if user_logged_in() == True:
    #     return redirect('http://my-app/game')
    # else:
    #     return 'This is a home page'
    return "Login Page"

@app.route('/Game')
def game():
    return "Game Page"

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



# app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# db = SQLAlchemy(app)


