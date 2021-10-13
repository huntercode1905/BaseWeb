from . import admin_views
from flask import render_template, session, redirect, url_for, request, current_app,flash
from flaskmain.forms import AdminUserForm
from flaskmain.utils.commons import is_string_validate
from .image_codes import get_image_number
from flaskmain.models import User
import re


@admin_views.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('id') is not None:
        return redirect(url_for('views.index'))
    form = AdminUserForm()
    if request.method == "POST" and form.validate_on_submit():
        print("0"*30)
        username = request.form.get('username')
        password = request.form.get('password')
        imagenumber = request.form.get('imagenumber')
        uuid = request.form.get('uuid')
        print("1"*30)
        if not all([username, password, imagenumber, uuid]):
            flash("参数不完整")
            return render_template('admin/login.html', form=form)
        print("2"*30)
        if not re.search(r'([a-zA-Z0-9]{36})', uuid):
            flash("提取验证码失败，你想干嘛？")
            return render_template('admin/login.html', form=form)
        print("3"*30)
        if imagenumber.lower() != get_image_number(uuid).lower():
            flash("验证码错误")
            return render_template('admin/login.html', form=form)
        print("4"*30)
        if is_string_validate(username):
            flash("用户名不能包含特殊字符")
            return render_template('admin/login.html', form=form)
        print("5"*30)
        try:
            user = User.query.filter_by(username=username).first()
        except Exception as e:
            current_app.logger.error(e)
            flash("数据库链接错误联系管理员处理1")
            return render_template('admin/login.html', form=form)
        print("6"*30)
        if user is None or not user.check_password(password):
            flash("用户名或者密码错误")
            return render_template('admin/login.html', form=form)
        print("session")
        session["id"] = user.id
        session["username"] = user.username
        return redirect(url_for('views.index'))
    return render_template('admin/login.html', form=form)


@admin_views.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('views.login'))
