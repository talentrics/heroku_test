from flask import Flask 
from flask import url_for

app = Flask(__name__)

from app import views
from app import admin_views