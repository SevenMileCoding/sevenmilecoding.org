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

@teach.route('/cal', methods=['GET', 'POST'])
@teach.route('/sched', methods=['GET', 'POST'])
@teach.route('/schedule', methods=['GET', 'POST'])
def schedule_route():
	data = {}

	if request.method == 'GET' and request.args:
		args = request.args
	
	return render_template('teach/schedule.html', **data)


@teach.route('/resources')
def resources_route():
	return render_template('teach/resources.html')