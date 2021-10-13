from flask import Blueprint, render_template
from flask_wtf.csrf import generate_csrf


admin_views = Blueprint("views", __name__)

from . import index, passport, image_codes



# 404
@admin_views.app_errorhandler(404)
def handler_404_error(error):
    context = {
        'title': "错误页面"
    }
    return render_template('admin/404.html', error=error, context=context)


# 504




# scrf_token
@admin_views.after_request
def after_request_add_csrf_token(response):
    csrf_token = generate_csrf()
    response.set_cookie("csrf_token", csrf_token)
    return response
