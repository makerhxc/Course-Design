from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Length, Email,Regexp,EqualTo,AnyOf
from wtforms import ValidationError
from ..models import User

#用户登陆表单
class LoginForm(FlaskForm):
    uname = StringField('用户名:', validators=[DataRequired(),Length(1,10)])
    upasswd = PasswordField('密码:', validators=[DataRequired()])
    remember_me = BooleanField('记住我:')
    submit = SubmitField('点击登录')

#更改密码表单
class ChangePassForm(FlaskForm):
    uname = StringField('用户名:', validators=[DataRequired()])
    old_passwd = StringField('旧密码：',validators=[DataRequired()])
    upasswd = PasswordField('重置密码:', validators=[DataRequired()])
    upasswd2 = PasswordField('确认密码:', validators=[DataRequired()
        ,EqualTo('upasswd', message='两次密码不一致')])
    submit = SubmitField('确认重置')

#用户注册模块表单
class RegistrationForm(FlaskForm):
    uname = StringField('用户名：', validators=[DataRequired(),Length(1, 10, message="用户名长度不正确"),
                                        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                        'Usernames must have only letters, '
                                        'numbers, dots or underscores')])
    uemail = StringField('邮箱：', validators=[DataRequired(), Email(message="邮箱格式不正确")])
    upasswd = PasswordField('密码：', validators=[DataRequired(),Length(6,20,message='密码长度不得低于6位且不高于20位')])
    upasswd2 = PasswordField('确认密码：', validators=[EqualTo('upasswd', message='两次密码不一致')])
    usex = StringField('性别',validators=[AnyOf('男','女')])
    uschool = StringField('毕业院校：',default=' ')
    uword = TextAreaField('自我介绍：',default=' ')
    uhome = StringField('家乡所在地：',default=' ')
    submit = SubmitField('注册新帐号')

    def validate_email(self, field):
        if User.query.filter_by(uemail=field.data).first():
            raise ValidationError('邮箱已注册！')

    def validate_username(self, field):
        if User.query.filter_by(uname=field.data).first():
            raise ValidationError('用户名已注册！')

class WriteBlogForm(FlaskForm):
    btitle = StringField('博客标题：',validators=[DataRequired()])
    btext = TextAreaField('博客正文：',validators=[DataRequired()])
    submit = SubmitField('提交')

class WriteCommitForm(FlaskForm):
    ctext  = TextAreaField('评论内容:',validators=[DataRequired()])
    submit = SubmitField('评论')
