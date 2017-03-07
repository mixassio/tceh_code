from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app=app)

#Здесь пока нет логики, идет проверка на добавление записей в базу
#Всё загружается, но сервер выдаёт какую-то ошибку, не понял пока
@app.route('/')
def posts():
    from models import Post, User, Tag, Tags
    user = User(name='ivan', email='ivan@mail.ru')
    post = Post(title='kak ya provel etim letom', content='ochen horosho provel', is_visible=True, user_id=1)
    tag = Tag(title='kitchen')
    postteg = Tags(tag_id=2, post_id=2)
    print(post.title, post.slug)
    db.session.add(tag)
    db.session.add(user)
    db.session.add(post)
    db.session.add(postteg)
    db.session.commit()

if __name__ == '__main__':
    from models import db, Post, User, Tag, Tags
    db.create_all()
    app.run()
