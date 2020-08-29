
import data_export
import wifi_statistics
from email_functions import SendMessage
import email_details
import time
import datetime

wait_time = 600 #10 minutes

def main():
    db = 'wifi_stats.db'
    table = 'wifi_speed'
    upload, download = wifi_statistics.speedtest_cli()
    print(download,upload)
    if download <= 10.0:
        SendMessage(email_details.sender, email_details.to, email_details.subject, email_details.msgHtml_error + str(download), email_details.msgPlain)
    data_export.export_data(download, upload, table, db)
    current = datetime.datetime.now()
    if current.hour == 12 and current.minute == 0:
        graph = data_export.todays_data(table,db)

    time.sleep(wait_time)

    

main()