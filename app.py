from crypt import methods
from flask import Flask, url_for, render_template, redirect, json, jsonify, request
from flask_pymongo import PyMongo
import pymysql
import random

import os

from config import awskey

app = Flask(__name__)


# conn = pymysql.connect(
#         host= 'movie-project.cc10tszik781.us-east-1.rds.amazonaws.com', 
#         port = 5432,
#         user = 'postgres', 
#         password = awskey,
#         db = 'movie-project',
#         )

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/recs", methods=["GET", "POST"])
def get_recs():

    return jsonify('sample_table')

@app.route("/about", methods=["GET", "POST"])
def goto_about():
    return render_template('about.html')

@app.route("/code", methods=["GET", "POST"])
def goto_code():
    return render_template('code.html')

@app.route("/bios", methods=["GET", "POST"])
def goto_bios():
    return render_template('bios.html')

if __name__ == "__main__":
    app.run(debug=True)