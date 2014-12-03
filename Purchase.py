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
		<a href="login.html">LOGIN</a>
	</div>
	<div class="space"></div>
	<div class="line"></div>


	</center>

</head>
<!--END HEADER-->
"""
print "<body><center><br>"

#CHECKS IF USER IS LOGGED IN:
user = form.getvalue("user")
if user == "null":
	print "<h1>You must be logged in to order</h1>"
	print '<a href="login.html">Click here to login</a>'
	print "</center></body>"
else:	
	print '<img src="items/thankyou.jpg" alt="Thank you!" width="800px" height="300px">'
	#QUANTITY USED
	beaniex = form.getvalue('beaniex')
	crewneckx = form.getvalue('crewneckx')
	shirtx = form.getvalue('shirtx')
	snapbackx = form.getvalue('snapbackx')
	baseballx = form.getvalue('baseballx')
	pantsx = form.getvalue('pantsx')
	print "<h1>You ordered the following: </h1>"
	if form.getvalue('beanie'):
		if(int(item[0][1])>=int(beaniex)):
			item[0][1] = int(item[0][1]) - int(beaniex)
			print "<p>%d x Charcoal Black UG Beanie - $%d</p>" %(int(beaniex),10*int(beaniex))
			sum += 10*int(beaniex)
		else:
			print "<p>Charcoal Black UG Beanie - Insufficient Quantity</p>"
			
	if form.getvalue('crewneck'):
		if(int(item[1][1])>=int(crewneckx)):
			item[1][1] = int(item[1][1]) - int(crewneckx)
			print "<p>%d x Heather Black UG Crewneck - $%d</p>" %(int(crewneckx),20*int(crewneckx))
			sum += 20*int(crewneckx)
		else:
			print"<p>Heather Black UG Crewneck - Insufficient Quantity</p>"
	if form.getvalue('shirt'):
		if(int(item[2][1])>=int(shirtx)):
			item[2][1] = int(item[2][1]) - int(shirtx)
			print "<p>%d x Black UG Tanktop - $%d</p>" %(int(shirtx),15*int(shirtx))
			sum += 15*int(shirtx)
		else:
			print"<p>Black UG T-Shirt - Insufficient Quantity</p>"
	if form.getvalue('snapback'):
		if(int(item[3][1])>=int(snapbackx)):
			item[3][1] = int(item[3][1]) - int(snapbackx)
			print "<p>%d x Black UG Snapback - $%d</p>" %(int(snapbackx),12*int(snapbackx))
			sum += 12*int(snapbackx)
		else:
			print "<p>Black UG Snapback - Insufficient Quantity</p>"
	if form.getvalue('baseball'):
		if(int(item[4][1])>=int(baseballx)):
			item[4][1] = int(item[4][1]) -int(baseballx)
			print "<p>%d x Black UG Baseball Tee - $%d</p>" %(int(baseballx),15*int(baseballx))
			sum += 15*int(baseballx)
		else:
			print"<p>Black UG Baseball Tee - Insufficient Quantity!</p>"
	if form.getvalue('pants'):
		if(int(item[5][1])>=int(pantsx)):
			item[5][1] = int(item[5][1]) - int(pantsx)
			print "<p>%d x Black UG Sports Pants - $%d</p>" %(int(pantsx),30*int(pantsx))
			sum += 30*int(pantsx)
		else:
			print"<p>Black UG Sports Pants - Insufficient Quantity</p>"
	print "<br><h1> Total cost: <b>$ %.2f</b></h1>" %(sum)
	print '<a href="index.html">Return to homepage</a>'

	print "</center></body>"

print """
<!-- START FOOTER -->
<div id="footer">
		<br><br><br>		
		<a href="index.html">HOME</a>
		<a href="catalogue.html">CATALOGUE</a>
		<a href="login.html">LOGIN</a>
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

