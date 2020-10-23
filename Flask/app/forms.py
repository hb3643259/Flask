from flask_wtf import FlaskForm #引入表单验证模块
from wtforms import StringField,BooleanField,PasswordField,SubmitField #引入不同域
from wtforms.validators import DataRequired #数据检查模块，检查是否为空

#创建一个login类生成表单,继承flask_wtf的Flask_Form类
class LoginForm(FlaskForm):
    username=StringField("username",validators=[DataRequired()]) #validators列表对输入框进行多种限制
    password=PasswordField("password",validators=[DataRequired()])
    remember_me=BooleanField("Remember me")
    submit=SubmitField("Sign In")
    #之后便携登陆模版文件，创建登陆界面
