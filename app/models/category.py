#!/usr/bin/python
#coding: utf-8
from _base import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
