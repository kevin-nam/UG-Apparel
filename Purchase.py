#!/usr/bin/python
import cgi,cgitb,csv

form = cgi.FieldStorage()

#Setting up Inventory 
f = open("Inventory.csv","r")
cr = csv.reader(f)
item = []
i=0
for row in cr:
	item.append(row)
	i += 1
f.close()
#Variable to calculate total cost	
sum = 0

#START HTML PRINTING
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
	if(int(item[0][1])):
		item[0][1] = int(item[0][1]) - 1
		print "<p>Charcoal Black UG Beanie - $10</p>"
		sum += 10
	else:
		print "<p>Charcoal Black UG Beanie - Sold out!</p>"
		
if form.getvalue('crewneck'):
	if(int(item[1][1])):
		item[1][1] = int(item[1][1]) - 1
		print "<p>Heather Black UG Crewneck - $20</p>"
		sum += 20
	else:
		print"<p>Heather Black UG Crewneck - Sold out!</p>"
if form.getvalue('shirt'):
	if(int(item[2][1])):
		item[2][1] = int(item[2][1]) - 1
		print "<p>Black UG T-Shirt - $15</p>"
		sum += 15
	else:
		print"<p>Black UG T-Shirt - Sold out!</p>"
if form.getvalue('snapback'):
	if(int(item[3][1])):
		item[3][1] = int(item[3][1]) - 1 
		print "<p>Black UG Snapback - $12</p>"
		sum += 12
	else:
		print "<p>Black UG Snapback - Sold out!</p>"
if form.getvalue('baseball'):
	if(int(item[4][1])):
		item[4][1] = int(item[4][1]) - 1
		print "<p>Black UG Baseball Tee - $15</p>"
		sum += 15
	else:
		print"<p>Black UG Baseball Tee - Sold out!</p>"
if form.getvalue('pants'):
	if(int(item[5][1])):
		item[5][1] = int(item[5][1]) - 1
		print "<p>Black UG Sports Pants - $30</p>"
		sum += 30
	else:
		print"<p>Black UG Sports Pants - Sold Out!</p>"
print "<br><h1> Total cost: <b>$ %.2f</b></h1>" %(sum)
print '<a href="index.html">Return to homepage</a>'

print "</center></body>"

print """
<!-- START FOOTER -->
<div id="footer">
		<br><br><br>		
		<a href="index.html">HOME</a>
		<a href="catalogue.html">CATALOGUE</a>
		<a href="www.google.ca">LOGIN</a>
		<br>
		<p>Created by: Kevin Nam & Thomas Wong (2014)<p>
</div>
<!-- END FOOTER -->
"""
#Writing to new Inventory
g = open("Inventory.csv","w")
cw = csv.writer(g)
cw.writerows(item)
g.close()

