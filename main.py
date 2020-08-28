
import data_export
import wifi_statistics
from email_functions import SendMessage
import email_details

def main():
    value = 0
    db = 'wifi_stats.db'
    table = 'wifi_speed'

    while value < 1:
        upload, download = wifi_statistics.speedtest_cli()
        print(download,upload,value)
        if download <= 10.0:
            SendMessage(email_details.sender, email_details.to, email_details.subject, email_details.msgHtml_error + str(download), email_details.msgPlain)
        data_export.export_data(download, upload, table, db)
        value += 1

    

main()
