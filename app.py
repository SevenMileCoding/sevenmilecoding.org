try:
	from flask import Flask
except ModuleNotFoundError as e:
	print(e)
	print('Make sure to run: pip install -r module-reqs.txt')

from flask import Flask, render_template
import blueprints
import config
import sys
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--development', 
					action='store_true', # act like a flag
                    help='a flag for indicating the app will run for local development')
args = parser.parse_args()

STATIC_PATH = config.STATIC_PATH

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder=STATIC_PATH)

# Register the controllers
app.register_blueprint(blueprints.main.home)
app.register_blueprint(blueprints.main.info)
app.register_blueprint(blueprints.main.support)
app.register_blueprint(blueprints.learn.home, subdomain='learn')
app.register_blueprint(blueprints.teach.home, subdomain='teach')


# Subdomain setup
serverName = 'sevenmilecoding.org'
if args.development:
	serverName = '7mc:' + str(config.env['port']) # so subdomains work on local machine
app.config['SERVER_NAME'] = serverName

# add global variables to jinja templates
@app.context_processor
def inject_globals():
	return dict(**config.GLOBAL_JINJA)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('main/404.html')

# Listen on external IPs
if __name__ == '__main__':
	# listen on external IPs
	if args.development: # only arguments will be pased to development
		app.run(host=config.env['host'], port=config.env['port'], debug=True)
	else:
		app.run()

