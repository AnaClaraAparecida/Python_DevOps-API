import logging.config
import flask

from routes.hello import blueprint as hello

logging.config.fileConfig('logging.ini')

app = flask.Flask(__name__)
app.register_blueprint(hello)

@app.route("/")
def index():
    app.logger.debug(f" {__name__}: Mensagem de DEBUG")
    app.logger.info(f" {__name__}: Mensagem de INFO")
    app.logger.warning(f" {__name__}: Mensagem de WARNING")
    app.logger.error(f" {__name__}: Mensagem de ERROR")
    app.logger.critical(f" {__name__}: Mensagem de CRITICAL")
    return flask.jsonify({
        'message': 'teste de log no flask'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')
