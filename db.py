import sqlite3

class Db():
    con = sqlite3.connect("file.db")
    cur = con.cursor()
    #cur.execute("CREATE TABLE user(name,data)")

           


x = Db()

"""    
        
con = sqlite3.connect("data.db")
cur = con.cursor()

#cur.execute("CREATE TABLE save(name,value)")
#con.commit()
cur.execute("DELETE FROM save")
cur.execute("INSERT INTO save(name,value) VALUES (?,?)",("sop","gmail"))
cur.execute("SELECT * FROM save")
#con.commit()
rows = cur.fetchall()
for row in rows:
    print(row)"""