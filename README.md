## bigdata-pipeline

######Ingestor

To install and run nginx on Mac OS X
$ brew install nginx
$ sudo nginx
$ curl localhost

The logfiles are located in /usr/local/var/log/nginx/access.log in the nginx log format.
They contain requests to localhost.

To run the program for parsing the curl requests:
$ python test2.py /usr/local/var/log/nginx/access.log file.txt

where file.txt is the document you want to store the logs in.
The program will keep running in the background until you press C-c

To see the generated curl requests as they are added to access.log, on another window:
$ tail -f /usr/local/var/log/nginx/access.log

This will also keep running until you press C-c

Generate the curl requests on another terminal window using
$ curl localhost
or enter localhost as the URL on a web browser.
You should see the request added to the access.log file in the nginx log format.
test2.py running in the background will add the generated requests to file.txt using
protobuf.

To display the requests:
$ python listRequest.py file.txt
The format in which you want to display the messages can be varied.

To automatically generate curl requests to localhost every 5 seconds (delay can be
varied):
$ ./curlRequests.sh

######Druid

*Setting up Imply (Druid, Tranquility, Plywood, Pivot) on AWS Instance*

