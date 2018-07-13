from flask import Flask, render_template
from src.common.database import Database

__author__ = 'mjd'


app = Flask(__name__)
app.config.from_object('src.config')
app.secret_key = "123"


@app.before_first_request
def init_db():
    Database.initialize()


@app.route('/')
def home():
    return render_template('home.jinja2')

from src.models.users.views import user_blueprint
from src.models.wines.views import wine_blueprint
from src.models.blogs.views import blog_blueprint
from src.models.posts.views import post_blueprint
app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(wine_blueprint, url_prefix="/wines")
app.register_blueprint(blog_blueprint, url_prefix="/blogs")
app.register_blueprint(post_blueprint, url_prefix="/posts")
