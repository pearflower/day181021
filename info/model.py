from . import db

class User(db.Model):
    '''
    用户表
    '''
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    age = db.Column(db.Integer,default=0)

    # 用户和新闻一对多关联
    user_news = db.relationship('News',backref='user',lazy='dynamic')

    def __repr__(self):
        return 'user : %s'%self.name

class News(db.Model):
    '''
    新闻表
    '''
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(300))

    # 外键
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    # 新闻和评论一对多关联
    news_comment = db.relationship('Comment',backref='news',lazy='dynamic')

    def __repr__(self):
        return 'news : %s' % self.title


class Comment(db.Model):
    '''
    评论表
    '''
    __tablename__ = 'comment'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(100),nullable=False)

    # 外键
    news_id = db.Column(db.Integer,db.ForeignKey('news.id'))

    def __repr__(self):
        return 'comment : %s'%self.content