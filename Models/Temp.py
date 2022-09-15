import sqlite3
from config import APP_PATH










class Temp:
    def __init__(self):
        self.path=APP_PATH+"/DB/temps.db"
    
    
    def _getNext(self,value):
        con=sqlite3.connect(self.path)
        cur=con.cursor()
        cur.execute("SELECT {} FROM Next".format(value))
        last=cur.fetchone()[0]
        con.close()
        return last
    def _putNext(self,value,next):
        con=sqlite3.connect(self.path)
        cur=con.cursor()
        cur.execute("SELECT {} FROM Next;".format(value))
        last=cur.fetchone()[0]
        cur.execute("UPDATE Next SET {} = '{}' WHERE {} = '{}' ".format(value,next,value,last))
        con.commit()
        con.close()