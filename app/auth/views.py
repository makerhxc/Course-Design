from app import db
from flask_login import login_user, logout_user, login_required, current_user
from pymysql import NULL
from sqlalchemy import DateTime
from werkzeug.security import generate_password_hash
from wtforms import ValidationError

from . import auth
from flask import render_template, redirect, request, url_for, flash
from ..models import User, Blog, Commits
from .forms import LoginForm, RegistrationForm, ChangePassForm, WriteBlogForm,WriteCommitForm


#用户登陆路由接口
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        upasswd = form.upasswd.data
        user = User.query.filter_by(uname=form.uname.data).first()
        if user is not None and user.verify_password(form.upasswd.data):
            login_user(user, form.remember_me.data)
            # 这里有问题，重新开机，浏览器还保存上一次的用户
            return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('auth/login.html',form=form)


#用户注册
@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.usex.data == '男':
            usex=1
        else:
            usex=0
        user = User(uemail=form.uemail.data,
                    uname=form.uname.data,
                    upasswd=generate_password_hash(form.upasswd.data),
                    usex=usex,
                    uschool=form.uschool.data,
                    uword=form.uword.data,
                    uhome=form.uhome.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

#用户改密
@auth.route('/cha_passwd', methods=['GET', 'POST'])
def cha_passwd():
    form = ChangePassForm()
    if form.validate_on_submit():
        upasswd = form.old_passwd.data
        user = User.query.filter_by(uname= form.uname.data).first()
        if user is not None and upasswd==user.upasswd:
            user(upasswd=form.upasswd.data)
            db.session.add(user)
            db.session.commit()#这里可能有问题
            flash('改密成功')
            # login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index',name=form.uname.data))#进入主页面
        else:
            flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)

#用户登出系统
@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('您已登出')
    return redirect(url_for('main.index'))

#写博客
@auth.route('/writeblog', methods=['GET', 'POST'])
@login_required
def writeblog():
    form = WriteBlogForm()
    if form.validate_on_submit():
        bauid = current_user._get_current_object()
        btext = form.btext.data
        blog = Blog(bauid=bauid,btext=btext)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('auth/userpost.html',form=form)#写完博客应该回到个人页面，这里先用主页面替下


#写评论
@auth.route('/writecommit/<blogid>', methods=['GET', 'POST'])
@login_required
def writecommit(blogid):
    form = WriteCommitForm()
    if form.validate_on_submit():
        cau = current_user._get_current_object()
        ctext = form.ctext.data
        bid = blogid
        comm = Commits(bid=bid,ctext=ctext,cau=cau)
        db.session.add(comm)
        db.session.commit()
    return render_template('main.index')#发表评论后应回到博客页面，这里先空着








