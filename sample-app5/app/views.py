from app import app
from flask import Flask, make_response
from flask import render_template
import os, subprocess

def execute_command(cmd):
    pipe = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    out, error = pipe.communicate()
    if pipe.returncode == 0:
        return out, 200
    else:
        resp = make_response({'Error': 500, 'Message': 'Failed to execute a command or script in the python code'})
        resp.status_code = 500
        return resp
        
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
    my_resp.status_code = 546
    my_resp.mimetype = 'application/json'
    return my_resp, 200

@app.route('/list1', methods=["GET"])
def list_dir1():
    return execute_command('ls')   

@app.route('/list2', methods=["GET"])
def list_dir2():
    return execute_command('ls p')   


# Error Handling
@app.errorhandler(404)
def not_found_exception(error):
    return ({'Error': 404, 'Message': 'Requested URL not found'}), 404
