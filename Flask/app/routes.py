from app import app
from flask import render_template,flash,redirect,url_for # 用于给模版（template）传递动态参数
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():#主页的视图函数
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login',methods=["GET","POST"])#methods提供提交表单的方法
def login():#login页的视图函数
    form=LoginForm()
    #对表单进行处理或检查
    if form.validate_on_submit():#get请求会直接返回false，post请求会运行LoginForm中设置的检查器
        flash("request from user {} ,remember_me {} ".format(form.username.data,form.remember_me.data))#向用户显示消息
        redirect(url_for("index"))#重定向到主页,让主页显示用户的消息
    return render_template("login.html",title="Sign In",form=form)

