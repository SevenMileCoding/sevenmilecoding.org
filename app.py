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

STATIC_PATH = config.STATIC_PATH

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder=STATIC_PATH)

# Register the controllers
app.register_blueprint(blueprints.main.home)
app.register_blueprint(blueprints.main.info)
app.register_blueprint(blueprints.main.support)
app.register_blueprint(blueprints.learn.learn, subdomain='learn')
app.register_blueprint(blueprints.teach.teach, subdomain='teach')


app.config['SERVER_NAME'] = '7mc:' + str(config.env['port']) # so subdomains work

# add global variables to jinja templates
@app.context_processor
def inject_globals():
	return dict(**config.GLOBAL_JINJA)

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html')

# Listen on external IPs
if __name__ == '__main__':
	# listen on external IPs
	if len(sys.argv) > 1: # only arguments will be pased to development
		app.run(host=config.env['host'], port=config.env['port'], debug=True)
	else:
		app.run()

