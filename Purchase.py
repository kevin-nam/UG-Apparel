#!/usr/bin/python
import cgi,cgitb

form = cgi.FieldStorage()

sum = 0
print "Content-type:text/html\r\n\r\n"
print "<html>"

print"""
<!-- START HEADER -->
<head>
<link rel="stylesheet" type="text/css" href="style.css">

	<title> Urban Groove Store - Catalogue </title>

	<center>
	<h1>URBAN GROOVE STORE</h1>
	<img src="uglogo.jpg" alt="Urban Groove Store" height="250" width="250">
	<div class="space"></div>
	<div id="umenu">
		<a href="index.html">HOME</a>
		<a href="catalogue.html">CATALOGUE</a>
		<a href="www.google.ca">LOGIN</a>
	</div>
	<div class="space"></div>
	<div class="line"></div>


	</center>

</head>
<!--END HEADER-->
"""

print "<body><center><br>"
print "<h1>You ordered the following: </h1>"

if form.getvalue('beanie'):
	beanie = 1
	print "<p>Charcoal Black UG Beanie - $10</p>"
	sum += 10
if form.getvalue('crewneck'):
	crewneck = 1
	print "<p>Heather Black UG Crewneck - $20</p>"
	sum += 20
if form.getvalue('shirt'):
	shirt = 1
	print "<p>Black UG T-Shirt - $15</p>"
	sum += 15
if form.getvalue('snapback'):
	snapback = 1
	print "<p>Black UG Snapback - $12</p>"
	sum += 12
if form.getvalue('baseball'):
	baseball = 1
	print "<p>Black UG Baseball Tee - $15</p>"
	sum += 15
if form.getvalue('pants'):
	pants = 1
	print "<p>Black UG Sports Pants - $30</p>"
	sum += 30

print "<br><h2> Total cost: <b>$ %.2f</b></h2>" %(sum)

print "</center></body>"
