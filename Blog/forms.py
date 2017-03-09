from wtforms_alchemy import ModelForm
from models import User, Post, Tag


class UserForm(ModelForm):
    class Meta:
        model = User


class PostForm(ModelForm):
    class Meta:
        model = Post
        include = ['user_id']
        exclude = ['slug']


class TagForm(ModelForm):
    class Meta:
        model = Tag
