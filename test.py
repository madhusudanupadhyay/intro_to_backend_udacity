"""
    Not wasting time now
"""

MONTHS = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

MONTH_ABBS = dict((month[0:3].lower(), month) for month in MONTHS)

def valid_month(month):
    """
    Return month string if its valid
    """
    if month:
        short_month = month[:3].lower()
        return MONTH_ABBS.get(short_month)


# print valid_month('December')
# print valid_month('Decembcdasdaser')
# print valid_month('december')
# print valid_month('decd1ember')
print valid_month('xyz')
