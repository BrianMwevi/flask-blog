from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin')
auth = Blueprint('auth', __name__, url_prefix='/auth')
article = Blueprint('article', __name__, url_prefix='/articles')
comment = Blueprint('comment', __name__, url_prefix='/article/comment')
user = Blueprint('user', __name__, url_prefix='/user')
home = Blueprint('home',__name__, url_prefix='/')


from app.home import views
from app.auth import views
from app.profile import views
from app.article import views
from app.comment import views
