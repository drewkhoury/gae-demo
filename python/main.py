# third party imports
####################################
import cgi
import urllib
import webapp2

import json
from google.appengine.api import mail

# custom imports
####################################
import helpers
import datamodels




class helloClass(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write( helpers.Templates().render('pages/index.html.j2' ) )


class requirements(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write( helpers.Templates().render('pages/requirements.html.j2' ) )


class localenv(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write( helpers.Templates().render('pages/local-env.html.j2' ) )


class deploy(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write( helpers.Templates().render('pages/deploy.html.j2' ) )


class AddObjectAction(webapp2.RequestHandler):
    def post(self):

        foo = self.request.get('foo')

        foo_safe = helpers.Validation().strip_to_alpha(foo)

        my_object = datamodels.MyObject(
            foo=foo_safe)
        my_object.put()

        self.response.write( '<b>' + foo_safe + '</b> has been added to the datasore (<a href="http://localhost:8000/datastore?kind=MyObject" target="_blank">local datastore</a> | <a href="https://console.cloud.google.com/datastore/entities/query?kind=MyObject" target="_blank">online datastore</a>). <a href="/">go back</a>' )


app = webapp2.WSGIApplication([
    ('/', helloClass),
    ('/requirements', requirements),
    ('/local-env', localenv),
    ('/deploy', deploy),
    ('/object/add', AddObjectAction),
])
