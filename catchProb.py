#print "Hello Trainer, Welcome to the wonderful world of POKEMON\n"

"""realnums=True
while read:
	try:
		hm=float(raw_input("Max HP?\n"))#hopefully a database lookup, and this turns into name or PKMNnumber or something.
		hc=float(raw_input("Current HP?\n"))#probably change to green, yellow or red. Then multiply by the pokemons Max HP.
		ball=float(raw_input("Which ball are you using."))
		status=float(raw_input("2 for slp/frz. 1.5 else. 1 for none."))
		pkmnRate=float(raw_input("What is the Pokemon catch rate?"))#replace with db lookup
		realnums=False#exits loop once all data has been input
	except ValueError:
		print "Print a valid number"
"""




for x in range(1,256):
	a=16711680/x
	b=int(a**(.5))
	c=int(b**(.5))
	d=1048560/c#bvalue
	e=65536-d
	shake=(1-(e/65536.0))
	chance=(shake**4)*100
	print format(str(x),'3')+" is "+"{:>6}".format(str(format(shake*100,'.3f')))+"% || Chance to catch: "+"{:>6}".format(str(format(chance,'.3f')))+"% || AVG Balls needed: "+str(int(shake**-4))
print "Done"