from flask import session, redirect, url_for, flash
import functools
from werkzeug.routing import BaseConverter
import re



def login_require(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if session.get("id") is not None:
            return func(*args, **kwargs)
        else:
            flash("请登录后，再访问该网页")
            return redirect(url_for("views.login"))
    return inner


# 自定义万能转换器（用正则表达式匹配）
class ReConverter(BaseConverter):
    def init(self, url_map, regex):
        # 调用父类的初始化方法
        super(ReConverter, self).init(url_map)
        # 保存正则表达式
        self.regex = regex


# 检查是否含有特殊字符
def is_string_validate(str):
    sub_str = re.sub(r'！@#￥%……&×;；=', "", str)
    if len(str) == len(sub_str):
        # 说明合法
        return False
    else:
        # 不合法
        return True


def get_text_plain(html_text):
    from bs4 import BeautifulSoup
    bs = BeautifulSoup(html_text, 'html.parser')
    return bs.get_text()
