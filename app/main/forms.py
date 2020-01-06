from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,IntegerField,TextAreaField
from wtforms.validators import DataRequired, Email, Length, Regexp, AnyOf
from sqlalchemy.sql.functions import current_user


class ContactUs(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    email = StringField('Email Address:', validators=[Email()])
    passwd = IntegerField('Phone Number:', validators=[DataRequired()])
    suggest = TextAreaField('Suggest:', validators=[DataRequired()])
    submit = SubmitField('Send')

class BlogText(FlaskForm):
    blog = TextAreaField('我的想法:', validators=[DataRequired()])
    submit = SubmitField('发表')

class EditInfomation(FlaskForm):
    uname = StringField('用户名：', validators=[DataRequired(), Length(1, 10, message="用户名长度不正确"),
                                            Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                   'Usernames must have only letters, '
                                                   'numbers, dots or underscores')])
    uemail = StringField('邮箱：', validators=[DataRequired(), Length(1, 15, message="邮箱长度不正确"), Email(message="邮箱格式不正确")])
    upasswd = PasswordField('密码：', validators=[DataRequired()])
    usex = StringField('性别',validators=[AnyOf('男','女')])
    uschool = StringField('毕业院校：')
    uword = TextAreaField('自我介绍：')
    uhome = StringField('家乡所在地：')
    submit = SubmitField('提交更改')