import sqlite3
import datetime
def export_data(download, upload,table,db):
   conn = sqlite3.connect(db)
   cur = conn.cursor()
   data = (download,upload)
   string = "INSERT INTO wifi_speed VALUES(?,?,julianday('now'));"
   cur.execute(string,data)
   conn.commit()
   conn.close()

export_data(30.03,30.02,'wifi_speed','wifi_stats.db')  