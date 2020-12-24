from flask_wtf import FlaskForm  # 从flask_wtf包中导入FlaskForm类
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField  # 导入这些类
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError, Length

# 登录
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


# 注册表单
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    password2 = StringField('Password2', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Register-注册')

    # 验证用户名是否存在
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first
        if user is not None:
            raise ValidationError("Please use a  differnce username")

    # 验证email名是否存在
    def validate_username(self, username):
        user = User.query.filter_by(email=username.mail).first
        if user is not None:
            raise ValidationError("Please use a  differnce email")


# 编辑个人主页表单
class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About_me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    # 验证用户名
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')
