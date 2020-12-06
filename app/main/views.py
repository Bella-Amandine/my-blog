from flask import render_template, redirect, url_for, abort
from .. import db
from . import main
from ..models import Blog, Comment
from flask_login import login_required, current_user
from .forms import BlogRegistrationForm, CommentForm

@main.route("/", methods = ["GET"])
def index():

    #Get all blogs
    all_blogs = Blog.display_all_blogs()

    return render_template('main/index.html', all_blogs = all_blogs)

@main.route('/blog/new', methods = ['GET', 'POST'])
@login_required
def save_new_blog():

    form = BlogRegistrationForm()

    if form.validate_on_submit():
        new_blog = Blog(blog_message = form.blog_message.data, writer_id = current_user.id)
        new_blog.create_blog()

        return redirect(url_for('main.index'))

    return render_template('main/new-blog.html', blog_form = form)

@main.route('/blog/<int:id>', methods = ['GET', 'POST'])
@login_required
def update_blog(id):

    form = BlogRegistrationForm()

    if form.validate_on_submit():
        blog_to_update = Blog.get_single_blog(id)
        if blog_to_update is not None:
            blog_to_update.update_blog(id, form.blog_message.data)
            # blog_to_update.blog_message = form.blog_message.data
            # db.session.add(blog_to_update)
            # db.session.commit()
            return redirect(url_for('main.index'))
        else :
            abort(404)

    return render_template('main/update-blog.html', blog_form = form)

@main.route('/blog/delete/<int:id>', methods = ['GET'])
@login_required
def delete_blog(id):
    Blog.delete_blog(id)
    return redirect(url_for('main.index'))

@main.route('/blog/comment/<int:id>', methods = ['GET', 'POST'])
def add_comment(id):

    form = CommentForm()
    if form.validate_on_submit():
        blog = Blog.get_single_blog(id)
        if blog is not None:
            comment = Comment(user_name = form.user_name.data, comment_message = form.comment.data, blog_id = id)
            comment.create_comment()

            return redirect(url_for('main.index'))

        else :
            abort(404)
    
    return render_template('main/comment-form.html', comment_form = form)
