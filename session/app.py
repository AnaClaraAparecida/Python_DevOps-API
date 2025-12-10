from functools import wraps 

import flask 

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = "!@#%FACEBUGG"

def login_required(function):
    @wraps(function)
    def wrappend(*args, **kwaegs):
        # logica de validaçao da sessao
        if flask.session.get('authorized') is None:
            return flask.redirect(flask.url_for('login'))
        return function(*args, **kwargs)
    return wrappend

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        # logica de processamento do form
        ## fulano | 4linux 
        username = flask.request.form.get('username')
        password = flask.request.form.get('passwd')
        credentialIsValid = username == "fulano" and password == "4linux"

        if credentialIsValid:
            flask.session['authorized'] = True
            return flask.redirect(flask.url_for('protegida'))

    return '''
        <form method="POST">
            <input type="text" name="username">
            <input type="password" name="passwd">

    '''

@app.route("/protegida")
@login_required 
def protegida():
    return "Esta é uma area protegida"

@app.route("/logout")
def logout():
    del flask.session['authorized']
    return flask.redirect('/login')
