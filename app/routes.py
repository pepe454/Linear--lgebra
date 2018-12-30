from flask import render_template
from app import app 

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Danny'}
    return render_template('index.html', title="Danny's Matrix Calculator", user=user)