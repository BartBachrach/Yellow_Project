from crypt import methods
from flask import Flask, url_for, render_template, redirect, json, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/data", methods=["GET", "POST"])
def get_data():
    return(request.form)

if __name__ == "__main__":
    app.run(debug=True)