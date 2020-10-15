from flask import render_template
from . import main
from .events import values


@main.route('/')
def index():
    return render_template('index.html',**values)

