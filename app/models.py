from app import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)
    password=db.Column(db.String(100),nullable=False)
class Transaction(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    date=db.Column(db.DateTime,nullable=False)
    day=db.Column(db.String(100),nullable=False)
    expense_purpose=db.Column(db.String(100),nullable=True)
    amount=db.Column(db.Float,nullable=False)
