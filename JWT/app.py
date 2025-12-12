import datetime 
from functools import wraps 

import flask 
import jwt 

app = flask.Flask(__name__)
JWT_SECRET = 'segredo'

def jwt_required(fn):
    @wraps(fn)
    def wrappend(*args, **kwargs):
        try:
            token = flask.request.headers.get('Authorization').split()[-1]
            # "Authorization" : 'Bearer !@#$%RUNgoo'
            decoded = jwt.decode(
                        token,
                        JWT_SECRET,
                        algorithms=['HS256']
            )
        except Exception as e:
            return flask.jsonify({
                    'NOK' : 'Token Inválido',
                })
        return fn(*args, **kwargs)
    return wrappend

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        # validaçao do formulario....
        username = flask.request.form.get('username')
        password = flask.request.form.get('passwd')
        # verificaçao coom a base de dados de usuario 
        credentialIsValid = username == 'fulano' and password == '4linux'

        if credentialIsValid:
            # gerar o token
            token = jwt.encode(
                    {
                        'username': username, 
                        'exp': datetime.datetime.utcnow() +
                            datetime.datetime(seconds=30)
                    },
                    JWT_SECRET,
                    algorithm='HS256')
            response = flask.request.get('https://localhost:5000/protegido', 
                        headers= {'Authorization' : f'Bearer {token}'})
            return flask.jsonify(response.json())

    return '''
        <form method="POST">
                <input type="text" name="username"> 
                <input type="password"  name="passwd">
                <input type="submit">
            </form>
        '''

@app.route('/protegido')
@jwt_required
def protegido():
    return flask.jsonify(
            {'mensagem': 'estou em uma area protegida'}
    )

