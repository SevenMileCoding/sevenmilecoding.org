from flask import *
from os import listdir
from os.path import isfile, join
import os
import config as C
import datetime

support = Blueprint('support', __name__)


@support.route('/support', methods=['GET', 'POST'])
def main_route():
	data = {}
	return render_template('main/support.html', **data)
