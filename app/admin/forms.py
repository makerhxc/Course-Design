from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,IntegerField,TextAreaField
from wtforms.validators import DataRequired, Email, AnyOf


class BlogText(FlaskForm):
    blog = TextAreaField('我的想法:', validators=[DataRequired()])
    submit = SubmitField('发表')

class UserInfo(FlaskForm):
    uname = StringField('姓名：',default=' ')
    uemail = StringField('邮箱:',default='  ')
    usex = StringField('性别', validators=[AnyOf('男', '女')])
    uschool = StringField('毕业院校：', default=' ')
    uword = TextAreaField('自我介绍：', default=' ')
    uhome = StringField('家乡所在地：', default=' ')
    upasswd = PasswordField('请输入密码后提交：')
    submit = SubmitField('立即提交')

class NoticeInfo(FlaskForm):
    ntext = StringField('公告内容：',validators=[DataRequired()])
    submit = SubmitField('立即提交')

class Commit(FlaskForm):
    ctext = StringField('评论内容：',validators=[DataRequired()])
    submit = SubmitField('立即评论')

class BlogText(FlaskForm):
    bmainword = StringField('博客关键字:',validators=[DataRequired()])
    bheadline = StringField('博客标题：',validators=[DataRequired()])
    btext = TextAreaField('我的想法:', validators=[DataRequired()])
    submit = SubmitField('发表')