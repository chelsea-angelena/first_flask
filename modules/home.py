
from flask import Flask,Blueprint, render_template, g,  render_template, url_for, request, redirect, session
import os



routes = [{
  'name': 'home',
  'url': '/',
}, {
  'name': 'chat',
  'url': '/chat',
}]

home= Blueprint('home', __name__, template_folder='templates', static_folder='static')


@home.route('/')
def index():
    return render_template('index.html', nav=routes)