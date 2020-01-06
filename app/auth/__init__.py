#注册用户模块蓝本
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views