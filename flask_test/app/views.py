from flask import render_template, request, send_from_directory
from app import app
from .forms import LoginForm, FormulaForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Kate'} # placeholder for user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'WOOhoppoppo' 
        }
    ]
    return render_template('index.html',
                            title = 'HOME',
                            user = user,
                            posts = posts)

# this handles the login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title = 'Sign In',
                           form = form,
                           providers = app.config['OPENID_PROVIDERS'])

@app.route('/prop', methods=['GET', 'POST'])
def prop():
    form = FormulaForm()
    return render_template('prop.html', 
                           title = 'PROP',
                           form = form)


""" 
# this should handle the prop input form
@app.route('/login', methods=['GET', 'POST'])
def prop_in():
    prop_premise = FormulaForm()
    return render_template('login.html',
                            form = prop_premise)
"""

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('app/static', path)



