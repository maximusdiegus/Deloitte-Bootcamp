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
        email = db.Column(db.String(50), nullable=False)
        password = db.Column(db.String(50), nullable=False)
        Games = db.relationship('Game', backref='user')
    
    class Game(db.Model):
        GameId = db.Column(db.Integer, primary_key=True)
        Data = db.Column(db.JSON, nullable=False)
        UserId = db.Column(db.Integer, db.ForeignKey('User.UserId'), nullable=False)

    with app.app_context():
        db.create_all()  