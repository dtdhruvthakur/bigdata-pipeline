#! /usr/bin/python

# See README.txt for information and build instructions.

import datalog_pb2
import sys

# Iterates though all requests in the logfile and prints
def ListRequest(log):
  for request in log.request:
    if request.HasField('gzip_ratio'):
      print "%s - %s [%s] \"%s\" %s %s \"%s\" \"%s\" \"%s\"" % (request.remote_addr, request.remote_user, request.time_local, request.request, request.status, request.bytes_sent, request.http_referer, request.http_user_agent, request.gzip_ratio)
      print ""

    else:
      print "%s - %s [%s] \"%s\" %s %s \"%s\" \"%s\"" % (request.remote_addr, request.remote_user, request.time_local, request.request, request.status, request.bytes_sent, request.http_referer, request.http_user_agent)
      print ""

      #print "'{0}' - '{1}' ['{2}'] \"'{3}'\" '{4}' '{5}' \"'{6}'\" \"'{7}'\"".format(request.remote_addr, request.remote_user, request.time_local, request.status, request.bytes_sent, request.http_referer, request.http_user_agent)

# Main procedure:  Reads the entire address book from a file and prints all
#   the information inside.
if len(sys.argv) != 2:
  print "Usage:", sys.argv[0], "LOG_FILE"
  sys.exit(-1)

log = datalog_pb2.Log()

# Read the existing address book.
f = open(sys.argv[1], "rb")
log.ParseFromString(f.read())
f.close()

ListRequest(log)
