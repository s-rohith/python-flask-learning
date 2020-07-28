from app import app
from flask import Flask, make_response, Response, render_template, request
import os, subprocess, json

@app.route('/', methods=["GET"])
def index():
    return render_template('public/index.html')

@app.route('/about', methods=["GET"])
def about():
    return """
    <h1 style = 'color: red;'> This is a RED h1 Heading </h1>
    <p>This is a lovely paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """

@app.route("/qs") # query using for loop
def qs():
    args = request.args
    
    for k, v in args.items():
        print(f"{k}: {v}")
    
    return "Query received!"

@app.route("/query") # query using if statement
def query_string():
    args = request.args
    if "process" in args:
        process_name = args.get("process")
    
    if "action" in args:
        action_name = args.get("action")

    print(process_name, action_name)
    
    return "Query received!"