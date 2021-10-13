from . import admin_views
from flaskmain.utils.commons import login_require
from flaskmain.models import User
from flask import render_template, current_app, send_from_directory, request, url_for
from flaskmain.forms import ArticleForm
from werkzeug.utils import secure_filename
from flask_ckeditor import upload_success, upload_fail
import os



@admin_views.route("/index")
@admin_views.route("/")
@login_require
def index():
    context = {
        "title": "首页"
    }
    return render_template('admin/base.html', context=context)

# 基础信息
@admin_views.route("/base_information")
@login_require
def base_information():
    context = {
        "title": "网站基本信息"
    }
    return render_template('admin/base_information.html', context=context)


# 文件 ---> 包 ----> 库 ---> 框架
# 发布内容
@admin_views.route('/articles')
@login_require
def articles():
    """

    params:
    return:
    """
    context = {
        "title": "文章列表"
    }
    return render_template('admin/articles.html', context=context)


# 添加文章
@admin_views.route('/add_article', methods=['GET', 'POST'])
@login_require
def add_article():
    form = ArticleForm()
    context = {
        "title": "添加文章"
    }
    if request.method == 'POST' and form.validate_on_submit():
        title = request.form.get('title')
        content = request.form.get('content')
        print("title = ", title)
        print("content = ", content)
    return render_template('admin/add_articles.html', context=context, form=form)

# 文章列表
@admin_views.route('/article')
@login_require
def article():
    pass


# @admin_views.route('/files/<path:filename>')
# def uploaded_files(filename):
#     path = '/the/uploaded/directory'
#     return send_from_directory(path, filename)

@admin_views.route('/files/<path:filename>')
@login_require
def uploaded_files(filename):
    path = os.path.join(current_app.static_folder, 'upload')
    return send_from_directory(path, filename)

@admin_views.route('/upload', methods=['POST'])
@login_require
def upload():
    f = request.files.get('upload')  # 获取上传图片文件对象
    # Add more validations here
    # if secure_filename(f.filename):
    #     return upload_fail(message='文件名字不正确！')
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:  # 验证文件类型示例
        return upload_fail(message='Image only!')  # 返回upload_fail调用
    f.save(os.path.join(os.path.join(current_app.static_folder, 'upload'), f.filename))
    url = url_for('views.uploaded_files', filename=f.filename)
    return upload_success(url=url) # 返回upload_success调用



# @app.route('/files/<path:filename>')
# def uploaded_files(filename):
#     path = '/the/uploaded/directory'
#     return send_from_directory(path, filename)
#
#
# @app.route('/upload', methods=['POST'])
# def upload():
#     f = request.files.get('upload')  # 获取上传图片文件对象
#     # Add more validations here
#     if extension not in ['jpg', 'gif', 'png', 'jpeg']:  # 验证文件类型示例
#         return upload_fail(message='Image only!')  # 返回upload_fail调用
#     f.save(os.path.join('/the/uploaded/directory', f.filename))
#     url = url_for('uploaded_files', filename=f.filename)
#     return upload_success(url=url) # 返回upload_success调用
