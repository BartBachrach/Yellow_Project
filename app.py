from crypt import methods
from flask import Flask, url_for, render_template, redirect, json, jsonify, request
import random
import os

#from config import awskey

import psycopg2

conn = psycopg2.connect(
        host="movie-project.cc10tszik781.us-east-1.rds.amazonaws.com",
        database="movies",
        user="#",
        password="#")

# Open a cursor to perform database operations
cur = conn.cursor()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/recs", methods=["GET", "POST"])
def get_recs():
    query = '''SELECT * FROM sample_table;
    '''

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

    cur.execute(query)
    data = cur.fetchall()
    for sample in data:
        print(sample)

    return (request.form)

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