from application import app, db
from application.models import User, Post
from application.forms import AddPost, UpdatePost
from flask import Flask, render_template, request, redirect, url_for
    
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/viewpost')
def viewpost():
    posts = Post.query.all()
    return render_template('viewpost.html', posts=posts)

@app.route('/addpost', methods=['GET','POST'])
def addpost():
    form = AddPost()
    if request.method == 'POST':
        newPost = Post(
            title = form.title.data,
            datePosted = form.datePosted,
            text = form.text.data
        )
        db.session.add(newPost)
        db.session.commit()
        return redirect(url_for('home', pid = newPost.id))
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

# @app.route('/updatepost', methods=['GET','POST'])
# def updatepost():
#     pid = 1
#     form = UpdatePost()
#     if request.method == 'POST':
#         post = Post.query.filter_by(id=pid).first()
#         post.title = form.title.data
#         post.titleDescription = form.titleDescription.data
#         post.text = form.text.data
#         db.session.commit()
#         return redirect(url_for('home'))
#     return render_template('updatepost.html', form=form)

# @app.route('/deletepost')
# def deletepost():
#     pid = 1
#     post = Post.query.filter_by(id=pid).first()
#     db.session.delete(post)
#     db.session.commit()
#     return redirect(url_for('home'))