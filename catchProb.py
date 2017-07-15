#Alex Ariaz
#Pokemon This Calculator finds the Probability and Avg number of Balls you need to Catch a specific Pokemon.
#Gen 3 and 4 only. (Ruby, Sapphire, Emerald, Diamond, Pearl, Paltinum, Heart Gold, Soul Silver)
#(R,S,E,D,P,Pt,HG,SS)

#This Function gives the A Value of a throw. Can be used to find the probability.
#Each math operation is separate because that is how it is done in Pokemon.
def a_value(hpm, hpc, pball, stat, rate):
	a=(3*hpm)-(2*hpc)
	b=int(a*rate*pball*stat)
	return int(b/(3*hpm))#Should be an int anyway.

#This function will probably not be used, but it is nice to have as it is in the game. 
#Each math operation is done separate because that is how it is done in Pokemon.
def b_value(aval):
	a=16711680/aval
	b=int(a**(.5))
	c=int(b**(.5))
	return (1048560/c)

#I do not want to write a super long if else statement, maybe later for efficiency. 
def catch_Prob(b):
	x=65536-b
	s=(1-(x/65536.0))
	return (s**4)*100

def aVal_Table():
	for x in range(1,256):
		a=16711680/x
		b=int(a**(.5))
		c=int(b**(.5))
		d=1048560/c#bvalue
		e=65536-d
		shake=(1-(e/65536.0))
		chance=(shake**4)*100
		print format(str(x),'3')+" Shake chance is "+"{:>6}".format(str(format(shake*100,'.3f')))+"% || Chance to catch: "+"{:>6}".format(str(format(chance,'.3f')))+"% || AVG Balls needed: "+str(int(100/chance))
	print "Done"

#aVal_Table()

#-----------------start-----------------
print "Hello Trainer, Welcome to the wonderful world of POKEMON\n"

realnums=True
while realnums:
	try:
		hm=int(raw_input("Max HP: "))#hopefully a database lookup, and this turns into name or PKMNnumber or something.
		hc=int(raw_input("Current HP: "))#probably change to green, yellow or red. Then multiply by the pokemons Max HP.
		ball=float(raw_input("Which ball are you using: "))
		status=float(raw_input("2 for slp/frz. 1.5 else. 1 for none: "))
		pkmnRate=int(raw_input("What is the Pokemon catch rate? "))#replace with db lookup Has to be 1-255
		realnums=False#exits loop once all data has been input
	except ValueError:
		print "Print a valid number"

av=a_value(hm,hc,ball,status,pkmnRate)
bv=b_value(av)
cp=catch_Prob(bv)
print "The probability of success: "+str(format(cp, '.3f'))+"%"
print "Avg Balls needed: "+str(int(100/cp))
