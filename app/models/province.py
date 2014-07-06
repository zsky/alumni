#!/usr/bin/python
#coding: utf-8
from _base import db

class Province(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(32), nullable=False)

    alumnus = db.relationship('Alumnus', backref=db.backref('province', lazy='select'), lazy='dynamic')
