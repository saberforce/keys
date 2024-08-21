import rsa
import hashlib
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
@app.route("/")

def sayhi():

    return "hello worldly"





if __name__ == '__main__':
    app.run(debug=True)