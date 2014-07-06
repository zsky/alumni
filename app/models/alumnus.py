#!/usr/bin/python
#coding: utf-8
from _base import db

class Alumnus(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(32), nullable=False)
    # 1 ---------- male
    # 0 ---------- female
    # default is 1
    sex = db.Column(db.SmallInteger, nullable=False, default=1)
    born_t = db.Column(db.DateTime, nullable=False)
    # province
    province_id = db.Column(db.Integer, db.ForeignKey('province.id'), nullable=False)
    city = db.Column(db.String(32), nullable=False)
    tel = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    qq = db.Column(db.String(11), nullable=False)
    idcard = db.Column(db.String(18), nullable=False)
    # 学院
    college_id = db.Column(db.Integer, db.ForeignKey('college.id'), nullable=False)
    # 专业
    major = db.Column(db.String(255), nullable=False)
    # 班级
    classroom = db.Column(db.Strng(32), nullable=False)
    grade = db.Column(db.Integer(4), nullable=False)

    # optional
    workplace = db.Column(db.String(255))
    address = db.Column(db.String(255))
    zipcode = db.Column(db.String(6))
    phone = db.Column(db.String(11))
    experience = db.Column(db.String(65525))
    hobby = db.Column(db.String(255))
    honor = db.Column(db.String(255))
