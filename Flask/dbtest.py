from app import db
from app.models import User,Post

u=User(username="harbor666",email="1760577996@qq.com666",password_hash="fff")
db.session.add(u)
db.session.commit()

users=User.query.all()
for user in users:
    print(str(user.id)+":"+user.username)
