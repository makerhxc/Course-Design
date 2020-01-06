# from flask import current_app
# from wtforms.validators import EqualTo
from datetime import datetime

from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin,AnonymousUserMixin   #用于认证用户
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer#令牌加密，需要确认后才能注册，用于确认用户

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(20), unique=True, index=True)
    uemail = db.Column(db.String(20), unique=True, index=True)
    upasswd = db.Column(db.String(128))
    usex = db.Column(db.Integer,nullable=True ,default=1)
    uschool = db.Column(db.String(20),nullable=True)
    uword = db.Column(db.String(255),nullable=True)
    uhome = db.Column(db.String(255),nullable=True)
    uregtime = db.Column(db.DateTime(), default=datetime.utcnow)
    uid_bau = db.relationship('Blog',backref='baid')
    uid_cau = db.relationship('Commits',backref='ucau')

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):#密码不可读
        raise AttributeError('密码无法读出')

    @password.setter
    def password(self, password):
        self.upasswd = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.upasswd, password)

    #加载用户的回调函数
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def get_id(self):
        return self.uid


class Blog(db.Model):
    __tablename__ = 'blogs'
    bid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    bauid = db.Column(db.Integer, db.ForeignKey('users.uid'))
    btext = db.Column(db.String(64))
    bpra = db.Column(db.Integer, nullable=True)  # 点赞数
    btime = db.Column(db.DateTime(), default=datetime.utcnow)
    bheadline = db.Column(db.String(64),nullable=True)
    bid_cbid = db.relationship('Commits', backref='bcid')


class Commits(db.Model):
    __tablename__ = 'commits'
    cid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    bid = db.Column(db.Integer, db.ForeignKey('blogs.bid'))
    ctext = db.Column(db.String(255))
    cau =  db.Column(db.Integer, db.ForeignKey('users.uid'))
    ctime = db.Column(db.DateTime(),default=datetime.utcnow)

class Notices(db.Model):
    __tablename__ = 'notices'
    nid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    ntext = db.Column(db.String(64))
    ntime = db.Column(db.DateTime(),default=datetime.utcnow)
    nauid = db.Column(db.Integer)
