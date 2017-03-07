from wtforms_alchemy import ModelForm
from models import User, Post, Tag

#Формы готовы, но пока нигде не используются

class UserForm(ModelForm):
    class Meta:
        model = User


class PostForm(ModelForm):
    class Meta:
        model = Post
        include = ['user_id']


class TagForm(ModelForm):
    class Meta:
        model = Tag
