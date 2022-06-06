# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")

@app.route('/DWFA/')
def dashboard():
    return render_template("DWFA.html")

@app.route('/tools/')
def tools():
    return render_template("tools.html")

@app.route('/contact/')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()