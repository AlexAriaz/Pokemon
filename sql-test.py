import MySQLdb

cnx=MySQLdb.connect(host="localhost",user='root',passwd="farside159",db='pokemon_stats')
cur=cnx.cursor()

query=("SELECT * from gen7_info")

cur.execute(query)
for row in cur.fetchall():
	print row[1],int(row[2]),int(row[3])

cur.close()
cnx.close()