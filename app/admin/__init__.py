#管理员模块蓝本
from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import views