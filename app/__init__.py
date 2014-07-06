#!/usr/bin/python
#coding: utf-8
from flask import Flask

def create_app():
    app = Flask(__name__)

    return app


app = create_app()
from app import views


