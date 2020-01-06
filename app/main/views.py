from app import db
from app.models import User,Notices,Blog,Commits
from flask import render_template, abort, flash, redirect, url_for
from sqlalchemy.sql.functions import current_user

from . import main
from .forms import ContactUs, BlogText, EditInfomation
import pymysql
pymysql.install_as_MySQLdb()

@main.route('/', methods=['GET', 'POST'])
def index():
    notice = Notices.query.order_by(Notices.ntime.desc()).first()
    blog = Blog.query.order_by(Blog.btime.desc()).all()#以列表形式返回的数据
    btext = []
    btime = []
    bau = []
    for i in blog:
        pass
    return render_template('index.html',notice=notice.ntext,blogs=blog)

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactUs()
    cname = form.name.data
    cemail = form.email.data
    cpasswd = form.passwd.data
    csugg = form.passwd.data
    return render_template('contact.html',form = form)

@main.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@main.route('/post', methods=['GET', 'POST'])
def post():
    form = BlogText()
    # if current_user.can(Permission.WRITE_ARTICLES)
    return render_template('post.html',form=form)

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(uname=username).first()
    if user is None:
        abort(404)
    return render_template('user.html',user=user)

#用户资料编辑表单（信息有错，回去改）
@main.route('/edit_info',methods=['GET','POST'])
def edit_info():
    form = EditInfomation()
    if form.validate_on_submit():
        user = User.query.filter_by(uname=form.uname.data).first()
        if user is not None and form.upasswd.data == user.upasswd:
            current_user.uname = form.name.data
            current_user.location = form.location.data
            current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', uname=current_user.username))
    form.name.data = current_user.uname
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)

#这里放一个管理员级别的资料编辑表单
@main.route('/edit_admin/<username>',methods=['GET','POST'])
def edit_admin(username):
    pass

