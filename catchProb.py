#Alex Ariaz
#Pokemon This Calculator finds the Probability and Avg number of Balls you need to Catch a specific Pokemon.
#Gen 3 and 4 only. 
#(R,S,E,D,P,Pt,HG,SS)
import MySQLdb


def hp_value(base,lvl):
	a=int(((base+7)*2*lvl)/100)
	b=int(a+lvl+10)
	return b
#This Function gives the A Value of a throw. Can be used to find the probability.
#Each math operation is separate because that is how it is done in Pokemon.
def a_value(hpm, hpc, pball, stat, rate):
	a=int(3*hpm)-int(2*hpc)
	b=int(a*rate*pball*stat)
	c=int(b/(3*hpm))#Should be an int anyway.
	if c>255:
		return 255
	else:
		return c

#This function will probably not be used, but it is nice to have as it is in the game. 
#Each math operation is done separate because that is how it is done in Pokemon.
def b_value(aval):
	a=int(16711680/aval)
	b=int(a**(.5))
	c=int(b**(.5))
	return int((1048560/c))

#I do not want to write a super long if else statement, maybe later for efficiency. 
def catch_Prob(b):
	x=65536-b
	s=(1-(x/65536.0))
	return (s**4)*100

def aVal_Table():
	for x in range(1,256):
		a=int(16711680/x)
		b=int(a**(.5))
		c=int(b**(.5))
		d=int(1048560/c)#bvalue
		e=int(65536-d)
		shake=(1-(e/65536.0))
		chance=(shake**4)*100
		print (format(str(x),'3')+" Shake chance is "+"{:>6}".format(str(format(shake*100,'.3f')))+"% || Chance to catch: "+"{:>6}".format(str(format(chance,'.3f')))+"% || AVG Balls needed: "+str(int(100/chance)))
	print ("Done")
#this can be done by taking two hpIV values and averaging, or by taking the median IV value. 
#Math still works out.
#15 is the median IV value.
"""def hp_eval(lev,mon):#this require db lookup of mon and it's base hp.
	a=2*mon.base
	b=a*lev
	c=b/100
	d=c+lev+10
	return d

"""
#aVal_Table()

#-----------------start-----------------
print ("Hello Trainer, Welcome to the wonderful world of POKEMON\n")
cnx=MySQLdb.connect(host="localhost",user='root',passwd="farside159",db='pokemon_stats')
cur=cnx.cursor()
loop=True
while loop:
	pkmnname=str(raw_input("What PKMN are you trying to catch? "))
	cur.execute("SELECT * from gen7_info where name=%s",(pkmnname,))
	exists=cur.fetchone()
	if (str(exists)=="None"):
		print (pkmnname+" Does not exist, please try again")
	else:	
		lvl=int(input("What is the Pokemon's level: "))
		hm=hp_value(int(exists[2]),lvl)
		hc=int(hm*int(raw_input("What approx hp '%' are they at? "))/100)
		ball=float(input("Which ball are you using: "))
		status=float(input("2 for slp/frz. 1.5 for par/brn/psn. 1 for none: "))
		pkmnRate=int(exists[3])
		
		loop=False#exits loop once all data has been input

#print ("done")
"""
realnums=True
while realnums:
	try:
		hm=int(input("Max HP: "))#hopefully a database lookup, and this turns into name or PKMNnumber or something.
		hc=int(input("Current HP: "))#probably change to green, yellow or red. Then multiply by the pokemons Max HP.
		ball=float(input("Which ball are you using: "))
		status=float(input("2 for slp/frz. 1.5 else. 1 for none: "))
		pkmnRate=int(input("What is the Pokemon catch rate? "))#replace with db lookup Has to be 1-255
		lvl=int(input("What is the Pokemon's level: "))
		realnums=False#exits loop once all data has been input
	except ValueError:
		print ("Print a valid number")
"""

av=a_value(hm,hc,ball,status,pkmnRate)
bv=b_value(av)
cp=catch_Prob(bv)
print("The probability of success: "+str(format(cp, '.3f'))+"%")
print("Avg Balls needed: "+str(int(100/cp)))
