from . import db

class User(db.Model):
    '''
    用户表
    '''
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    age = db.Column(db.Integer,default=0)
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
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return 'news : %s' % self.title