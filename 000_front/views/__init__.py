from flask import Blueprint


# 生成蓝图类
views = Blueprint('views', __name__)


from . import index
