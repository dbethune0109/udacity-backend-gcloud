import os

import webapp2

form_html="""
<form>
<h2>Add A Food<h2>
<input type="text" name="food">
<button>Add</button>
</form>
"""

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class MainPage(Handler):
    def get(self):
        self.write("hello udacity!")

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
