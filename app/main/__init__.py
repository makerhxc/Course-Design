#主页相关蓝本注册
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
