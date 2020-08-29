import sqlite3
import datetime
import matplotlib.pyplot as plt
import julian

def export_data(download, upload,table,db):
   conn = sqlite3.connect(db)
   cur = conn.cursor()
   data = (download,upload)
   string = "INSERT INTO {} VALUES(?,?,julianday('now'));".format(table)
   cur.execute(string,data)
   conn.commit()
   conn.close()

def todays_data(table,db):
   download = []
   upload=[]
   julian_date=[]
   conn = sqlite3.connect(db)
   cur = conn.cursor()
   string = "SELECT * FROM {} WHERE date > julianday('now')-1;".format(table)
   cur.execute(string)
   rows = cur.fetchall()
   for row in rows:
      download.append(row[0])
      upload.append(row[1])
      julian_date.append(row[2])
   date = julian_to_seconds(julian_date)
   return(graph_data(download,upload,date))

def graph_data(upload,download,time):
   plt.plot(time,download,linewidth=2.0)
   plt.plot(time,upload,linewidth=2.0)
   plt.show()
   #plt.savefig("todays_newtworkk_graph.pdf")

def julian_to_seconds(jul):
   date=[]
   for i in range(len(jul)):
      time=julian.from_jd(jul[i],fmt='mjd')
      total_sec = time.hour*3600 + time.minute*60 + time.second 
      date.append(total_sec)
   for i in range(len(date)):
      date[i]=date[i]-date[0]
   return date