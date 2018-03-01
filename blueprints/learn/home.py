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


@learn.route('/calendar')
def calendar_route():

	data = {}

	if request.method == 'GET' and request.args:
		args = request.args

	return render_template('learn/calendar.html')



@learn.route('/tutorials')
def tutorials_route():

	data = {}

	if request.method == 'GET' and request.args:
		args = request.args

	return render_template('learn/tutorials.html')


@learn.route('/activities')
def activities_route():

	data = {}

	if request.method == 'GET' and request.args:
		args = request.args

	return render_template('learn/activities.html')


@learn.route('/resources')
def resources_route():

	data = {}

	if request.method == 'GET' and request.args:
		args = request.args

	return render_template('learn/resources.html')