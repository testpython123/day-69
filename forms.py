from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
from markupsafe import Markup


##WTForm
from wtforms.widgets import PasswordInput


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = EmailField("Email Field", validators=[DataRequired()])
    password = StringField("Password", widget=PasswordInput(hide_value=False), validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = EmailField("Email Field", validators=[DataRequired()])
    password = StringField("Password", widget=PasswordInput(hide_value=False), validators=[DataRequired()])
    submit = SubmitField("Logi in")


class CreateComment(FlaskForm):
    title = Markup('<strong>Comment</strong>')
    body = CKEditorField(title, validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
