import jinja2
import os
import json
import time
from datetime import date
from jinja2 import Template
from collections import OrderedDict

# Returns the current date.
# https://docs.python.org/2/library/datetime.html
def today():
    d = date.fromtimestamp(time.time())
    return d.isoformat()

# https://github.com/TexAgg/Resume/blob/master/render.py#L31
latex_jinja_env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    comment_start_string = '\#{',
    comment_end_string = '}',
    line_statement_prefix = "-%",
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

with open('data/emojis.json') as data_file:
    # http://stackoverflow.com/a/6921760/5415895
    data = json.load(data_file, object_pairs_hook=OrderedDict)

sty_template = latex_jinja_env.get_template('templates/texmoji.template.sty')
sty_str = sty_template.render(
	today = today,
	data = data
)
with open("texmoji.sty", "w+") as f:
    f.write(sty_str)

tex_template = latex_jinja_env.get_template('templates/texmoji.template.tex')
tex_string = tex_template.render(
	today = today,
	data = data
)
with open("texmoji.tex", "w+") as f:
    f.write(tex_string)