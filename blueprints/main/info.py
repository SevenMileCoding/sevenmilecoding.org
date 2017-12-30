from flask import *
from os import listdir
from os.path import isfile, join
import os
import config as C
import datetime


info = Blueprint('info', __name__)


@info.route('/program', methods=['GET', 'POST'])
def program_route():

	data = {}

	if request.method == 'GET' and request.args:
		args = request.args
	
	return render_template('main/program.html', **data)





@info.route('/team', methods=['GET', 'POST'])
def members_route():

	data = {}

	if request.method == 'GET' and request.args:
		args = request.args
	
	return render_template('main/members.html', **data)
