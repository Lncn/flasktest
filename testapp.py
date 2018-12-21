from flask import Flask
app = Flask(__name__)

@app.route('/')
def root_index():
    return "Hello, Lincoln! This is returned by the app root!"

@app.route('/static')
def show_static():
    return 'This is a static thing'

@app.route('/user/<username>')
def show_user(username):
    # <username> can be any arbitrary string
    return 'User %s' % username

@app.route('/string/<string:string>')
def print_string(string):
    # <string> can be any arbitrary string (without slashes)
    return "String '%s'" % string

@app.route('/int/<int:integer>')
def show_integer(integer):
    # <integer> can only be an integer
    return 'Integer %d' % integer

@app.route('/float/<float:fl>')
def show_float(fl):
    # <fl> can only be a float
    return 'Float %f' % fl

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # <subpath> can have show the subpath after /path/
    return 'Subpath %s' % subpath

@app.route('/uuid/<uuid:u>')
def show_uuid(u):
    # What is this? 
    return 'UUID %s' % subpath
