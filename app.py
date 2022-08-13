from crypt import methods
from pkgutil import get_data
from unittest import result
from flask import Flask, url_for, render_template, redirect, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import psycopg2.extras
import random
import os

from sqlalchemy.sql import func

from config import DB_USERNAME, DB_PASSWORD

app = Flask(__name__)

conn = psycopg2.connect(
        host="movie-project.cc10tszik781.us-east-1.rds.amazonaws.com",
        database="movies",
        user=DB_USERNAME,
        password=DB_PASSWORD)

# Open a cursor to perform database operations
cur = conn.cursor()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/recs", methods=["GET", "POST"])
def get_recs():

    cluster = request.form.get('class')
    for movie in cluster:
        print(movie)
    
    age = request.form.get('year')
    for movie in age:
        print(movie)

    rating = request.form.get('rating')
    for movie in rating:
        print(rating)

    query = '''SELECT title FROM sample_table
    WHERE
    class=cluster
    AND
    year=age
    AND
    rating=rating;
    '''

    cur.execute(query)

    return render_template(get_recs)

    # cur.execute(query)
    # data = cur.fetchall()
    # for sample in data:
    #     print(sample)

    # return (request.form)

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

    # IF exampleSelect1 = Science Fiction, filter table to * WHERE class = 1
        # exampleSelect1 = Suspenseful, filter to * WHERE class = 0
        # exampleSelect1 = Animated, filter to * WHERE class = 2
        # exampleSelect1 = Critically Acclaimed, filter to * WHERE class = 4
        # exampleSelect1 = I'm feeling lucky!, filter to * WHERE class = 3

    # THEN IF exampleSelect2 = 2022 - 2010, filter to * WHERE year >=2010
                #exampleSelect2 = 2010 - 2000, filter to * WHERE year <= 2010 and >= 2000
                #exampleSelect2 = 2000 - 1980, filter to * WHERE year <= 2000 and >= 1980
                #exampleSelect2 = 1980 - 1960, filter to * WHERE year <= 1980 and >= 1960
                #exampleSelect2 = 1959 or older, filter to * WHERE year <= 1959
    
    # THEN IF exampleSelect3 = Yes - Show me only 4 stars and above.
                # exampleSelect3 = A little bit - Show me only 3 stars and above.
                # exampleSelect3 = No - Show me anything.     