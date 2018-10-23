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
    # 用户和评论一对多关联
    user_comment = db.relationship('Comment',backref='user',lazy='dynamic')

    def __repr__(self):
        return 'user : %s'%self.name

class News(db.Model):
    '''
    新闻表
    '''
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text)

    # 外键
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    type_id = db.Column(db.Integer,db.ForeignKey('type.id'))

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
    content = db.Column(db.Text,nullable=False)

    # 外键
    parent_id = db.Column(db.Integer,db.ForeignKey('comment.id'))
    news_id = db.Column(db.Integer,db.ForeignKey('news.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    # 自关联
    parent = db.relationship('Comment',remote_side=[id])

    def __repr__(self):
        return 'comment : %d'%self.id

class Type(db.Model):
    '''
    分类表
    '''
    __tablename__ = 'type'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=False)

    # 新闻分类一对多关系
    type_news = db.relationship('News',backref='type',lazy='dynamic')

    def __repr__(self):
        return 'type : %s'%self.name