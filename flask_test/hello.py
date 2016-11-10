#!/usr/bin/python


from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def hello():
    return "Hello World!"
"""
if __name__ == "__main__":
    app.run()

"""

@app.route('/prop')
def prop():
        return 'PRORP!'



@app.route('/prop/')
def index(name=None):
        return render_template('index.html', name=name)



"""
@app.route('/prop', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        # run prop
    if request.method == 'GET':
        # show the data entry form



"""
