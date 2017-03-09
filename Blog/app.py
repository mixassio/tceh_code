from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__,template_folder='templates')
app.config.from_object(config)
db = SQLAlchemy(app=app)


@app.route('/create/<tag>')
def create_tag(tag):
    from models import Tag
    print(tag)
    new_tag = Tag(title=tag)
    db.session.add(new_tag)
    db.session.commit()
    return 'done'


@app.route('/create/post/', methods=['GET', 'POST'])
def create_post():
    from models import Post
    from forms import PostForm

    if request.method == 'POST':
        form = PostForm(request.form)
    if form.validate():
        post = Post(**form.data)
        db.session.add(post)
        db.session.commit()
    return 'done'


@app.route('/all_post')
def all_post():
    sel = db.session.query(Post).all()
    return render_template('all_post.txt', posts=sel)

if __name__ == '__main__':
    from models import db, Post, User, Tag, Tags
    db.create_all()
    app.run()
