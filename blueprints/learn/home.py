from flask import *
from os import listdir
from os.path import isfile, join
import os
import datetime

learn = Blueprint('learn', __name__)


@learn.route('/')
def main_route():

	data = {}

	if request.method == 'GET' and request.args:
		args = request.args

	return render_template('learn/index.html')