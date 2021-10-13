from . import views
from flask import render_template



@views.route("/index")
@views.route("/")
def index():
    context = {
        "title": "首页"
    }
    return render_template("index.html", context=context)


@views.route("/detail")
def detial():
    context = {
        "title": "分类页"
    }
    return render_template("detail.html", context=context)



@views.route('/oindex')
def oindex():
    context = {
        "title": "分类页"
    }
    return render_template('Oindex.html', context=context)




@views.route('/odetail')
def odetail():
    return render_template('Odetail.html')
