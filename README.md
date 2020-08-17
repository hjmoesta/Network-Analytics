# Network Analytics 

## Details
This repository is initially supposed to be implimented onto a raspberry pi and run analytics on your network. The raspberry pi is supposed to be plugged into the router and running this code in the meantime. What occurs is that using selenium, google chrome is opened and a [speedtest](https://www.speedtest.net/) is run. The data is then pulled using web scrapping and then the upload, download, and time are noted and put into a local sqlite table. After some time and data has been collected there will be analytics run. There is also the opportunity for email updates such as end of day rundowns of the wifi. All of the collection is there, there is just some analytical work that needs to be done still

## Tasks to do
* There needs to be some sort of analytics done for the end of day report some options are graphing the upload and download speed and saving the graph as a png and sending it in a email to see how the network did today. 
* Find an API that will get the data from the network. Silenium works fine API would be better
* Make some test to ensure that everything is working okay
