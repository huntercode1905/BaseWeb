import redis
import os

# wKg4OGFiCAuAVO-EAAQmUzvQXlQ360.png


class Config(object):
    DEBUG = True
    SECRET_KEY = "%^$&#sdfafwerqaDFGSWEwerw"

    mysql_username = 'root'
    mysql_password = 'qwe123'
    mysql_addr = 'localhost'
    mysql_db = 'sisi_db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(
        mysql_username,
        mysql_password,
        mysql_addr,
        mysql_db
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # session相关
    SESSION_TYPE = 'redis'
    redis_for_session_host = '127.0.0.1'
    redis_for_session_port = 6379
    redis_for_session_db = 1
    # session有效时间: 单位：秒
    PERMANENT_SESSION_LIFETIME = 60*60*24

    # 是否对发送到浏览器上的session加密
    SESSION_USE_SIGNER = True
    #sessons是否长期有效，false，则关闭浏览器，session失效
    SESSION_PERMANENT = False
    # 保存在服务器的session的前缀
    SESSION_KEY_PREFIX = "session_for_sisi_"
    # session保存数据到rendis时启用的对象
    SESSION_REDIS = redis.StrictRedis(
        host=redis_for_session_host,
        port=redis_for_session_port,
        db=redis_for_session_db
    )

    # 验证码相关
    IMG_REDIS_HOST = '127.0.0.1'
    IMG_REDIS_PORT = 6379
    IMG_REDIS_DB = 2

    # 文件保存路径
    CKEDITOR_SERVE_LOCAL = True
    CKEDITOR_HEIGHT = 400
    CKEDITOR_LANGUAGE = 'zh-CN'
    CKEDITOR_FILE_UPLOADER = 'views.upload'
    CKEDITOR_ENABLE_CSRF = True
    UPLOADED_PATH = 'uploads'
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}
