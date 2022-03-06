from flask import Flask, copy_current_request_context, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle
from flask.helpers import flash
# from flask_login import LoginManager
from flask_session import Session
import os
from flask_socketio import SocketIO, emit, send, disconnect
from config import Config

db=SQLAlchemy()
sess=Session()

def init_app():
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object(Config)
    app.secret_key=os.urandom(12)

    css = Bundle('static/css/*.css', filters='postcss', output='dist/css/main.css')
    assets = Environment()
    assets.register('css', css)

    assets.init_app(app)

    db.init_app(app)
    # TODO
    # login_manager.init_app(app)
    sess.init_app(app)

    # Add bp's
    with app.app_context():

        from modules import chat
        from modules import home


        app.register_blueprint(chat.chat)
        app.register_blueprint(home.home)

        db.create_all()
        return app

app=init_app()
socketio=SocketIO(app)

# socketio for chat
def messageReceived():
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

@socketio.on('my_event', namespace='/test')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
        {'data': message['data'], 'count': session['receive_count']})


@socketio.on('my_broadcast_event', namespace='/test')
def test_broadcast_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
        {'data': message['data'], 'count': session['receive_count']},
        broadcast=True)


@socketio.on('disconnect_request', namespace='/test')
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()

    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
        {'data': 'Disconnected!', 'count': session['receive_count']},
        callback=can_disconnect)


if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0')
