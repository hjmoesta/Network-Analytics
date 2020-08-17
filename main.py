
import data_export
import wifi_statistics
from email_functions import SendMessage
import email_details

def main():
    value = 0
    db = 'wifi_stats.db'
    table = 'wifi_speed'

    while value < 3:
        download, upload = wifi_statistics.speed_test()
        print(download,upload,value)
        data_export.export_data(download, upload, table, db)
        value += 1
    result = SendMessage(email_details.sender, email_details.to, email_details.subject, email_details.msgHtml, email_details.msgPlain)

main()
