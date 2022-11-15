from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app

if input("This will erase the database first. Are you sure you want to continue? (Y/N): ") == "Y":

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tictactoe.db'
    db = SQLAlchemy(app)
    with app.app_context():
        db.drop_all()

    class User(db.Model):
        UserId = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(50), nullable=False)
        password = db.Column(db.String(50), nullable=False)
        Games = db.relationship('Game', backref='user')
    
    class Post(db.Model):
        PostId = db.Column(db.Integer, primary_key=True)
        Title = db.Column(db.String(50), nullable=False)
        TitleDescription = db.Column(db.String(50), nullable=False)
        Text = db.Column(db.String(1000), nullable=False)
        UserId = db.Column(db.Integer, db.ForeignKey('User.UserId'), nullable=False)

    with app.app_context():
        db.create_all() 