import os
import jinja2
import re, string
import datamodels
import cgi

class Validation():

    def strip_to_alpha(self, string):
        pattern = re.compile('[^a-zA-Z]')
        return pattern.sub('', string)


    def strip_to_num(self, string):
        pattern = re.compile('[^0-9]')
        return pattern.sub('', string)


class Templates():

  def render(self, tpl_path, context=''):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)
