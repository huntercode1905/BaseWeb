class Config(object):
    DEBUG = True
    SECRET_KEY = "12434566HGFDSD*&^%"

    mysql_name = 'root'
    mysql_password = 'qwe123'
    mysql_address = '127.0.0.1'
    mysql_port = 3306
    mysql_database_name = 'shop_001'
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
        mysql_name,
        mysql_password,
        mysql_address,
        mysql_port,
        mysql_database_name
    )
    # 设置mysql的错误跟踪信息显示, 默认为false,就是显示
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 打印每次模型操作对应的SQL语句
    # SQLALCHEMY_ECHO = True
