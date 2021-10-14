from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
from flask_ckeditor import CKEditor
from config import Config
import redis
from flaskmain.utils.commons import ReConverter
import logging
from logging.handlers import  RotatingFileHandler  # 设置保存文件位置等信息


# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)
# 创建日志记录器， 指明保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logging.getLogger().addHandler(file_log_handler)

# 日志用法
"""
try:
    pass  # 需要用try的语句
except Exception as e:
    current_app.logger.error(e)
    flash("数据库链接错误联系管理员处理1") # or something else
    return redirect(url_for(''))  # 或者你要返回的东西
"""




db = SQLAlchemy()
ckeditor = CKEditor()

redis_store_for_image_code = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Session(app)
    CSRFProtect(app)

    global redis_store_for_image_code
    redis_store_for_image_code = redis.StrictRedis(
        host=Config.IMG_REDIS_HOST,
        port=Config.IMG_REDIS_PORT,
        db=Config.IMG_REDIS_DB
    )

    db.init_app(app)
    ckeditor.init_app(app)

    app.url_map.converters["re"] = ReConverter

    from .views import admin_views
    app.register_blueprint(admin_views, url_prefix="")
    return app
