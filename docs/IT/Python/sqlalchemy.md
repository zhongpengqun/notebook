# 插入数据
user1 = User(name='John', age=25)
user2 = User(name='Jane', age=30)
session.add_all([user1, user2])
session.commit()

