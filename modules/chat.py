
from flask import Blueprint, render_template, g, url_for, request, redirect, session, Flask, copy_current_request_context, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle

from flask.helpers import flash
# from flask_login import LoginManager
# from flask_session import Session
import os

chat=Blueprint('chat', __name__)

routes = [{
  'name': 'forms',
  'url': '/form',
}, {
  'name': 'store',
  'url': '/store',
}]

@chat.route('/chat', methods=['POST', 'GET'])
def sessions():
    return render_template('chat.html', nav=routes)

