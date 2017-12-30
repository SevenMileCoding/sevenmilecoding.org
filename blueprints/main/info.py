from flask import *
from os import listdir
from os.path import isfile, join
import os
import config as C
import datetime


info = Blueprint('info', __name__)


@info.route('/grade', methods=['GET', 'POST'])
def main_route():

	gradeView = True
	data = {}

	if request.method == 'GET' and request.args:
		args = request.args
		imgId = args['p']
		print('\nLoading view for', imgId, '\n')
		data = getPageData(imgId)
	
	return render_template('base.html', **data)





@info.route('/getUser', methods=['GET', 'POST'])
def get_user_route():
	rForm = request.form
	if request.form['caller'] == 'exportGrade':
		user = util.get_current_user()
		return jsonify({'user': user})
	else: return jsonify({'user':'error'})
