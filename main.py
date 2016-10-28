import jinja2
import os
import json
import time
from datetime import date
from jinja2 import Template

# https://github.com/TexAgg/Resume/blob/master/render.py#L31
latex_jinja_env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    #comment_start_string = '\#{',
    #comment_end_string = '}',
    line_statement_prefix = "-%",
    #line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

sty_template = latex_jinja_env.get_template('templates/texmoji.template.sty')
sty_str = sty_template.render()
with open("texmoji.sty", "w+") as f:
    f.write(sty_str)

tex_template = latex_jinja_env.get_template('templates/texmoji.template.tex')
tex_string = tex_template.render()
with open("texmoji.tex", "w+") as f:
    f.write(tex_string)