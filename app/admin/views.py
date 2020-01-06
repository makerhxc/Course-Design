from app import db
from app.models import Blog
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, redirect, url_for, request
from flask_wtf import form

from .forms import UserInfo, NoticeInfo, Commit, BlogText

from . import admin

@admin.route('/getalluser',methods=['GET','POST'])
def getalluser():
    pass

#文章页面
@admin.route('/getbestblog',methods=['GET','POST'])
def getbestblog():
    userform = UserInfo()
    return render_template('admin/back-article.html',changeuserform=userform)

#评论页面
@admin.route('/getbestcommit',methods=['GET','POST'])
def getbestcommit():
    userform = UserInfo()
    return render_template('admin/back-comment.html',changeuserform=userform)

#管理主页面
@admin.route('/adminindex',methods=['GET','POST'])
def adminindex():
    userform = UserInfo()
    return render_template('admin/back-index.html',changeuserform=userform)

#管理公告
@admin.route('/getnotice',methods=['GET','POST'])
def getnotice():
    userform = UserInfo()
    return render_template('admin/back-notice.html',changeuserform=userform)

#增加文章
@admin.route('/userpost',methods=['GET','POST'])
def userpost():
    userform = UserInfo()
    blogtext = BlogText()
    if blogtext.validate_on_submit():
        blog = Blog(bauid=current_user, btext=blogtext.btext.data,
                    bpra=0, bheadline=blogtext.bheadline.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('admin/back-add-article.html',changeuserform=userform)

#增加公告
@admin.route('/addnotice',methods=['GET','POST'])
def addnotice():
    notice = NoticeInfo()
    userform = UserInfo()
    if form.validate_on_submit():
        notice = NoticeInfo(ntext=notice.ntext.data,nauid=current_user.__name__)
        db.session.add(notice)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('admin/back-add-notice.html',changeuserform=userform)



#增加评论
@admin.route('/addcommit',methods=['GET','POST'])
def addcommit():
    commit = Commit()
    userform = UserInfo()
    if form.validate_on_submit():
        commit = NoticeInfo(ntext=commit.ntext.data,nauid=current_user.__name__)
        db.session.add(commit)
        db.session.commit()
        return redirect(url_for('main.post'))
    return render_template('main/contact.html')