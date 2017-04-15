#!/usr/bin/env python
"""
This is docstring
"""
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import jinja2

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

TEMPLATE_DIR = os.curdir
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

# Parent Class with simple rendering functions

class Handler(webapp.RequestHandler):
    """This is magic"""
    def write(self, *a, **kw):
        """Magical get"""
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        """Using render function"""
        temp = JINJA_ENV.get_template(template)
        return temp.render(params)

    def render(self, template, **kw):
        """Cool Render Function"""
        self.write(self.render_str(template, **kw))


# Handler class for handling shopping list items

class MSHandler(Handler):
    """This is magic"""
    def get(self):
        """Magical get"""
        items = self.request.get_all("food")
        self.render("shopping_list.html", items=items)

# FizzBuzz class for nothing at all

class FizzBuzzHandler(Handler):
    """This is to calculate the fizzbuzz numbers and redirect to the webapp"""
    def get(self):
        """To get the number as request parameter"""
        n = self.request.get('n', 0)
        if n:
            n = int(n)
            self.render("fizzbuzz.html", n=n)

def main():
    """Another Docstring"""
    application = webapp.WSGIApplication([('/', MSHandler),
                                          ('/fizzbuzz', FizzBuzzHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
