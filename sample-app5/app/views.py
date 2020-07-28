from app import app
from flask import Flask, make_response, Response, render_template
import os, subprocess, json

def execute_command(cmd):
    pipe = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    out, error = pipe.communicate()
    if pipe.returncode == 0:
        return out, 200
    else:
        resp = {'Error': 500, 'Message': 'Failed to execute a command or script in the python code'}
        return json.dumps(resp), 500

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

@app.route('/test', methods=["GET"])
def test():
    data = {}
    data['Status_code'] = 200
    data['output'] = 'hello'
    my_resp = make_response(data)
    my_resp.headers['warning'] = 'warning'
    my_resp.status_code = 546               # Custom status code
    my_resp.mimetype = 'application/json'
    return my_resp

@app.route('/list1', methods=["GET"])
def list_dir1():
    return execute_command('ls')


@app.route('/list2', methods=["GET"])
def list_dir2():
    return execute_command('ls p')   
    
