from flask import *
from os import listdir
from os.path import isfile, join
import os
import datetime

home = Blueprint('home', __name__)


@home.route('/', methods=['GET', 'POST'], subdomain='www')
@home.route('/', methods=['GET', 'POST'])
def main_route():

	data = {}

	if request.method == 'GET' and request.args:
		args = request.args
	
	return render_template('main/index.html', **data)