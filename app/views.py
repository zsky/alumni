from flask import render_template, redirect, request
from app import app
from datetime import datetime
import pdb


@app.route('/pages')
def pages():
    return render_template("pages.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/list_type1')
def list_type1():
    return render_template("list_type1.html")

@app.route('/regions')
def regions():
    return render_template("regions.html")

@app.route('/editor')
def editor():
    return render_template("editor.html")

@app.route('/editor_content', methods=["post"])
def editor_content():
    print 'content'
    print request.form['content']
    return request.form['content']


