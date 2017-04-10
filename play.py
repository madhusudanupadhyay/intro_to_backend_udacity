import cgi
"""This is a cgi class"""

def escape_html(s):
    """The escape function"""
    return cgi.escape(s, quote=True)
print escape_html('"html, & = &amp;"')
