from flask import redirect, url_for, flash
from app.comment.forms import CommentForm
from app.models import Comment
from app.urls import comment
from flask_login import current_user, login_required


# New Comment View
@login_required
@comment.route('new/<int:article_id>', methods=['POST'])
def new_comment(article_id):
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = Comment(body=comment_form.body.data,
                          user_id=current_user.id, article_id=article_id)
        comment.save()
        flash("Comment created successfully!")
    else:
        flash("Please fill the form with the correct details and try again")
    return redirect(url_for('article.detail', article_id=article_id))


# Update Comment View
@comment.route('/update/<int:article_id>/<int:comment_id>', methods=['POST'])
def update(article_id, comment_id):
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = Comment.query.filter(id=comment_id).first()
        comment.update()
        flash("Comment updated successfully")
    flash("Please fill the form with the correct details and try again")
    return redirect(url_for('article.detail', article_id=article_id))
