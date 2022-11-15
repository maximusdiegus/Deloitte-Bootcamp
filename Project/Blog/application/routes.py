from application import app, db
from application.models import User, Post
from application.forms import AddPost, UpdatePost, SelectUser, AddUser, EditUser
from flask import Flask, render_template, request, redirect, url_for

@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    form = SelectUser()
    if request.method == 'POST':
        user = User.query.filter_by(username = form.username.data, password = form.password.data).first()
        if user:
            return redirect(url_for('home'))
            
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form = AddUser()
    if request.method == 'POST':
        newUser = User(
            username = form.username.data,
            password = form.password.data
        )
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/edituser', methods=['GET','POST'])
def edituser():
    form = EditUser()
    if request.method == 'POST':
        user = User.query.filter_by(username = form.username, password = form.password).first()
        user.username = form.username.data
        user.password = form.password
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('edituser.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/viewpost')
def viewpost():
    posts = Post.query.all()
    userForm = SelectUser()
    user = User.query.filter_by(username = userForm.username.data, password = userForm.password.data)
    
    return render_template('viewpost.html', posts=posts, user=user)

@app.route('/addpost', methods=['GET','POST'])
def addpost():
    form = AddPost()
    userForm = SelectUser()
    user = User.query.filter_by(username = userForm.username.data, password = userForm.password.data)
    
    if request.method == 'POST':
        newPost = Post(
            title = form.title.data,
            datePosted = form.datePosted,
            text = form.text.data,
            user_id = user.id
        )
        db.session.add(newPost)
        db.session.commit()
        return redirect(url_for('viewpost', pid = newPost.id))
    return render_template('addpost.html', form=form)

@app.route('/updatepost/<int:pid>', methods=['GET','POST'])
def updatepost(pid):
    form = UpdatePost()
    if request.method == 'POST':
        post = Post.query.filter_by(id=pid).first()
        post.title = form.title.data
        post.datePosted = form.datePosted
        post.text = form.text.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('updatepost.html', form=form)

@app.route('/deletepost/<int:pid>')
def deletepost(pid):
    post = Post.query.filter_by(id=pid).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))