from application import app, db
from application.models import User, Post
from flask import Flask, render_template, request, redirect, url_for
    
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/viewpost')
def viewpost():
    return render_template('viewpost.html')

@app.route('/addpost')
def addpost():
    return render_template('addpost.html')
