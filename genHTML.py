from jinja2 import FileSystemLoader, Environment
import os

CUR_PATH = os.path.realpath(__file__)
CUR_DIR = os.path.dirname(CUR_PATH)
TEMPLATES_DIR = os.path.join(CUR_DIR, 'templates')
EXCLUDE_TEMPS = ['base.html']
SITE_GLOBALS = {
	'email': 'umsevenmilecoding@gmail.com'
}

def render_from_template(directory, template_name, **kwargs):
	loader = FileSystemLoader(directory)
	env = Environment(loader=loader)
	template = env.get_template(template_name)
	return template.render(**kwargs)


templateNames = os.listdir(TEMPLATES_DIR)

for x in EXCLUDE_TEMPS:
	templateNames.remove(x)

for t in templateNames:
	html = render_from_template(TEMPLATES_DIR, t, **SITE_GLOBALS)
	with open(t, 'w') as f:
		f.write(html)