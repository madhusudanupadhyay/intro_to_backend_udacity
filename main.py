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
<form method="post">
    When is your Birthday?
    <br>
    <label>Date
    <input type="text" name="date">
    </label>
    <label>Month
    <input type="text" name="month">
    </label>
    <label>Year
    <input type="text" name="year">
    </label>


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

    def post(self):
        """Post Handler"""
        self.response.out.write('Wow, One more fuckup!!!')



def main():
    """Another Docstring"""
    application = webapp.WSGIApplication([('/', MainHandler)], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
