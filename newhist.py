import sqlite3


conn=sqlite3.connect('C:/Users/*username*/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/History')
c=conn.cursor()

web=str(input("Enter the website: "))
query="SELECT id,url FROM urls WHERE url like '%"+web+"%'"

id_select=[]
for rows in c.execute(query):
    print("Deleting....",rows[1])
    id_del=rows[0]
    id_select.append((id_del,))
c.executemany('DELETE from urls WHERE id=?',id_select)
conn.commit()

conn.close()
