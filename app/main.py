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

app = Flask(__name__)

conn = psycopg2.connect(
        host="movie-project.cc10tszik781.us-east-1.rds.amazonaws.com",
        database="movies",
        user=os.environ.get('DB_USERNAME'),
        password=os.environ.get('DB_PASSWORD'))

# Open a cursor to perform database operations
cur = conn.cursor()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/recs", methods=["GET", "POST"])
def get_recs():

    if request.method == 'POST':
        cluster = request.form.get('cluster')
        for movie in cluster:
            print(movie)
        
        year = request.form.get('year')
        year_1 = year.split(",")[0]
        year_2 = year.split(",")[1]
        for movie in year:
            print(movie)

        rating = request.form.get('rating')
        rating_1 = rating.split(",")[0]
        rating_2 = rating.split(",")[1]
        for movie in rating:
            print(movie)

        query = f"""
        SELECT title
        FROM full_table
        WHERE cluster = {cluster}
            and year BETWEEN {year_1} and {year_2}
            and rating BETWEEN {rating_1} and {rating_2}
            ORDER BY RANDOM();
        """

        cur.execute(query)

        data = cur.fetchmany(2)
        for title in data:
            print(title)

        return render_template('recs.html', data = data)

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