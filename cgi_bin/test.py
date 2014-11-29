#!/usr/bin/python
import cgi, cgitb

form = cgi.FieldStorage()

fname = form.getvalue('fname')
lname = form.getvalue('lname')

print "Content-Type: text/html"
print
print """
<html>
<body>
<h2>Hellow!!</h2>
"""
print "<p>Your name is %s %s</p>" %(fname,lname)
print """
</body>
</html
"""

