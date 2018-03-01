import argparse
import os

# Create and handle command line arguments
parser = argparse.ArgumentParser(description='Kellogg Eye Web App')
parser.add_argument('-d', '--development', 
					action='store_true', # act like a flag
                    help='a flag for indicating the app will run for local development')
parser.add_argument('-u', default='devUser', type=str,
                    help='uniqname for the session (who you are signed in as)')
args = parser.parse_args()

# If app is run with development, fake a logged in user
USER = ''
if args.development and args.u:
    USER = args.u


env = dict(
	host = '0.0.0.0',
	port = 3000
)


STATIC_PATH = 'static'
CUR_PATH = os.path.realpath(__file__)
CUR_DIR = os.path.dirname(CUR_PATH)
TEMPLATES_DIR = os.path.join(CUR_DIR, 'templates')

FILE_PATHS = {

}

GLOBAL_JINJA = {
	'email': 'umsevenmilecoding@gmail.com',
	'github': 'https://github.com/SevenMileCoding',
	'phone': '(734) 531-9025'
}