import os
#将配置参数信息封装到一个类中，之后可以直接在该类中添加必要的参数信息

basedir=os.path.abspath(os.path.dirname(__file__))#数据库的顶级目录信息
class Config(object):
    #SECRET_KEY信息用于Flask_wtf模块生成令牌或密钥，防止CSRF攻击
    SECRET_KEY=os.environ.get('SECRET_KEY') or "you-will-never-guess"

    #添加数据库配置，开发时使用轻量级的SQLite，部署在服务器中使用MySQL，不用改变代码
    #默认数据库地址
    SQLALCHEMY_DATABASE_URL=os.environ.get("DATABASE_URL") or "sqlite:///"+os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False#不向应用发送消息

