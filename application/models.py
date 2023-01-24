"""Data models."""
from flask_login import UserMixin
from datetime import datetime
from . import db


class Product(db.Model):

    __tablename__   = 'products'
    product_id      = db.Column(db.String(200), primary_key=True)
    date_created    = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Product %r>' % self.product_id


class Location(db.Model):
    __tablename__   = 'locations'
    location_id     = db.Column(db.String(200), primary_key=True)
    date_created    = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Location %r>' % self.location_id


class ProductMovement(db.Model):

    __tablename__   = 'productmovements'
    movement_id     = db.Column(db.Integer, primary_key=True)
    product_id      = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    qty             = db.Column(db.Integer)
    from_location   = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    to_location     = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    movement_time   = db.Column(db.DateTime, default=datetime.utcnow)

    product         = db.relationship('Product', foreign_keys=product_id)
    fromLoc         = db.relationship('Location', foreign_keys=from_location)
    toLoc           = db.relationship('Location', foreign_keys=to_location)

    def __repr__(self):
        return '<ProductMovement %r>' % self.movement_id


class User(UserMixin, db.Model):
    """User account model"""

    __tablename__   = 'usr'
    id              = db.Column(db.Integer, primary_key=True)
    username        = db.Column(db.String(100), nullable=False, unique=True)
    password        = db.Column(db.String(200), nullable=False, unique=False)


    def __repr__(self):
        return '<User {}>'.format(self.username)

