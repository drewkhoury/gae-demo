from google.appengine.ext import ndb

class MyObject(ndb.Model):
    foo = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
