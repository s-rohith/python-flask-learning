from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('public/index.html')


@app.route('/about')
def about():
    return """
    <h1 style = 'color: red;'> This is a RED h1 Heading </h1>
    <p>This is a lovely paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """
