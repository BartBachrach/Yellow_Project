from crypt import methods
from flask import Flask, url_for, render_template, redirect, json, jsonify, request
from flask_pymongo import PyMongo
import random
import requests

import os

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/recs", methods=["GET", "POST"])
def get_recs():
    return(request.form)

@app.route("/about", methods=["GET", "POST"])
def goto_about():
    return(request.form)

@app.route("/code", methods=["GET", "POST"])
def goto_code():
    return(request.form)

@app.route("/bios", methods=["GET", "POST"])
def goto_bios():
    return(request.form)

def load_and_get_stats(body: dict) -> dict:
    chars = mongo.db.collectionname

    chars.update_one({body}. {'$inc':{'displayed': 1}})

    return chars.find()

if __name__ == "__main__":
    app.run(debug=True)