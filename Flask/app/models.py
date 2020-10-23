#定义数据库结构,在已经封装好的ORM下定义数据库结构，每一张表的一行可以定义为一个类，通过定义多个类映射到多张表
from app import db
from datetime import datetime

class User(db.Model):#通过ORM将表user的元组灵活定义为一个类
    id=db.Column(db.INTEGER,primary_key=True)#主键
    username=db.Column(db.String(64),unique=True)
    email=db.Column(db.String(120),unique=True)
    password_hash=db.Column(db.String(128))
    posts=db.relationship("Post",backref="author",lazy="dynamic")
    '''User类有一个新的posts字段，用db.relationship初始化。这不是实际的数据库字段，而是用户和其动态之间关系的高级视图，因此
    它不在数据库图表中。对于一对多关系，db.relationship字段通常在“一”的这边定义，并用作访问“多”的便捷方式。因此，如果我有一个用户实例u，
    表达式u.posts将运行一个数据库查询，返回该用户发表过的所有动态。 db.relationship的第一个参数表示代表关系“多”的类。
    backref参数定义了代表“多”的类的实例反向调用“一”的时候的属性名称。这将会为用户动态添加一个属性post.author，
    调用它将返回给该用户动态的用户实例。 lazy参数定义了这种关系调用的数据库查询是如何执行的'''

    def __repr__(self):#调试时起作用,输入类的实例名，执行函数
        return "<User{}>".format(self.username)

class Post(db.Model):
    id=db.Column(db.INTEGER,primary_key=True)
    body=db.Column(db.String(140))
    timestamp=db.Column(db.DATETIME,index=True,default=datetime.utcnow)
    user_id=db.Column(db.INTEGER,db.ForeignKey("user.id"))

    def __repr__(self):
        return "<Post{}>".format(self.body)