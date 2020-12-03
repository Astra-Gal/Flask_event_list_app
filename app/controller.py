from flask import render_template, request
from app import app
from app.models.event import Event
from app.models.event_list import *

@app.route('/')
def index():
    
    return render_template('index.html', events=events)