#定义数据库结构,在已经封装好的ORM下定义数据库结构，每一张表的一行可以定义为一个类，通过定义多个类映射到多张表
from app import db

class User(db.Model):#通过ORM将表user的元组灵活定义为一个类
    id=db.Column(db.INTEGER,primary_key=True)#主键
    username=db.Column(db.String(64),unique=True)
    email=db.Column(db.String(120),unique=True)
    password_hash=db.Column(db.String(128))

    def __repr__(self):#调试时起作用,输入类的实例名，执行函数
        return "<User{}>".format(self.username)
