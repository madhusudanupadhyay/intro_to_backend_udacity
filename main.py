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
    <br>
    <label>Date
    <input type="text" name="date" value="%(date)s">
    </label>
    <label>Month
    <input type="text" name="month" value="%(month)s">
    </label>
    <label>Year
    <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color:red">
        <p>
            %(error)s
        </p>
    </div>

    <br>
    <br>
    <input type="submit">
</form>
"""
MONTHS = {'mar': 'March', 'feb': 'February', 'aug': 'August',
          'sep': 'September', 'apr': 'April', 'jun': 'June',
          'jul': 'July', 'jan': 'January', 'may': 'May',
          'nov': 'November', 'dec': 'December', 'oct': 'October'}

def valid_date(date):
    """For validity of day"""
    if date and date.isdigit():
        date = int(date)
        if date > 0 and date < 32:
            return date
        else:
            return None
    else:
        return None

def valid_year(year):
    """For validity of Year"""
    if year and year.isdigit():
        year = int(year)
        if year >= 1900 and year <= 2020:
            return year
        else:
            return None
    else:
        return None

def valid_month(month):
    """For validity of month"""
    if month:
        month_short = (month[:3]).lower()
        month_new = MONTHS.get(month_short)
        return month_new
    else:
        return None



class MainHandler(webapp.RequestHandler):
    """DocString for everything"""

    def write_form(self, error='', date='', month='', year=''):
        """ERRORS"""
        self.response.out.write(form %{"error":error,
                                       "date":date,
                                       "month":month,
                                       "year":year})

    def get(self):
        """Docstring for method"""
        self.write_form()

    def post(self):
        """Post Handler"""
        user_date = self.request.get('date')
        user_month = self.request.get('month')
        user_year = self.request.get('year')

        date = valid_date(user_date)
        month = valid_month(user_month)
        year = valid_year(user_year)


        if date and month and year:
            self.response.out.write('<img src="http://www.businessofapps.com/wp-content/uploads/2016/09/225008LOGO-1.jpg" style="width:100px;" >'+ '<br>' + '<a href="/">Go Back</a>')
        elif not (date and month and year):
            self.write_form(' Invalid Inputs ', user_date, user_month, user_year)
        # elif not month:
        #     self.write_form(' Invalid month ', user_month, user_date, user_year)
        # elif not year:
        #     self.write_form(' Invalid year ', user_year, user_date, user_month)




def main():
    """Another Docstring"""
    application = webapp.WSGIApplication([('/', MainHandler)], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
