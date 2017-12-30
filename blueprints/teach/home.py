from flask import *
from os import listdir
from os.path import isfile, join
import os
import datetime

teach = Blueprint('teach', __name__)


@teach.route('/', methods=['GET', 'POST'])
def main_route():
	data = {}

	if request.method == 'GET' and request.args:
		args = request.args
	
	return render_template('teach/index.html', **data)
