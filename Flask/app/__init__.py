from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__) #__init__.py中的内容表示该包暴露在外的内容，即其他地方可以引用的包内容
app.config.from_object(Config)#为Flask添加配置信息

db=SQLAlchemy(app)#为app flask对象创建数据库对象
migrate=Migrate(app,db)#为app flask对象以及数据库对象db添加数据迁移引擎

from app import routes,models
