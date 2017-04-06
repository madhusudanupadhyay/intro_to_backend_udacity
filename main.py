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
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

form = """
<h1>Form</h1>
<form method="post" action="/testform">
    Name: <input name="name">
    <br>
    <br>
    <input type="submit">
</form>

"""


class MainHandler(webapp.RequestHandler):
    """DocString for everything"""
    def get(self):
        """Docstring for method"""
        self.response.out.write(form)

class TestHandler(webapp.RequestHandler):
    """DocString for everything"""
    def post(self):
        """
        Docstring for method
        """
        name = self.request.get("name")
        self.response.out.write(name)

        # self.response.headers['Content-Type'] = 'text/plain'
        # self.response.out.write(self.request)


def main():
    """Another Docstring"""
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/testform', TestHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
