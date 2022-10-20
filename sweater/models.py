from flask_login import UserMixin
from sweater import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    debt = db.Column(db.NUMERIC, nullable=False)
    last_account = db.Column(db.NUMERIC, nullable=False)
    last_bill_of_the_month = db.Column(db.DATETIME, nullable=False)
    rate = db.Column(db.NUMERIC, nullable=False)

    condition_id = db.Column(db.Integer, db.ForeignKey('condition.id_condition'), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id_status'), nullable=False)
    payment_method_id = db.Column(db.Integer, db.ForeignKey('payment_method.id_payment_method'), nullable=False)
    payment_type_id = db.Column(db.Integer, db.ForeignKey('payment_type.id_payment_type'), nullable=False)


class Condition(db.Model):
    __tablename__ = 'condition'
    id_condition = db.Column(db.Integer, primary_key=True)
    list_condition = db.Column(db.String, nullable=False)
    cust_1 = db.relationship('Customer', backref='condition', lazy=True)


class Status(db.Model):
    __tablename__ = 'status'
    id_status = db.Column(db.Integer, primary_key=True)
    list_status = db.Column(db.String, nullable=False)
    cust_2 = db.relationship('Customer', backref='status', lazy=True)


class Payment_method(db.Model):
    __tablename__ = 'payment_method'
    id_payment_method = db.Column(db.Integer, primary_key=True)
    list_payment_method = db.Column(db.String, nullable=False)
    cust_3 = db.relationship('Customer', backref='payment_method', lazy=True)


class Payment_type(db.Model):
    __tablename__ = 'payment_type'
    id_payment_type = db.Column(db.Integer, primary_key=True)
    list_payment_type = db.Column(db.String, nullable=False)
    cust_4 = db.relationship('Customer', backref='payment_type', lazy=True)