#! /usr/bin/python

import sys
import fileinput
import datalog_pb2
import time

def main(input):
  #input = raw_input("Enter input: ")
  arr = input.split("\n")
  arr = filter(None, arr)

  for line in arr:
    logParser(line, log.request.add())

def logParser(entry, request):
  delimiter = " "
  ctr = 0
  i = 0
  arrword = []

  while (i < len(entry)):
    word = ""
    while (i < len(entry)):
      if (entry[i] == "\""):
        i+=1
        while (entry[i] != "\""):
          word += entry[i]
          i+=1
        break
      elif (entry[i] == "["):
        i+=1
        while (entry[i] != "]"):
          word += entry[i]
          i+=1
        break
      elif (entry[i] == " "):
        break
      
      word += entry[i]
      i+=1

    if (i == len(entry)):
      break

    i+=1
    arrword.append(word)

  arrword = filter(None, arrword)
  p = arrword.pop(1)

  request.remote_addr = arrword[0]
  request.remote_user = arrword[1]
  request.time_local = arrword[2]
  request.request = arrword[3]
  request.status = arrword[4]
  request.bytes_sent = arrword[5]
  request.http_referer = arrword[6]
  request.http_user_agent = arrword[7]
  if (len(arrword) == 9):
    request.gzip_ratio = arrword[8]

  # Write new log back to disk
  f = open(sys.argv[2], "wb")
  f.write(log.SerializeToString())
  f.close()

log = datalog_pb2.Log()

fo = open(sys.argv[1], "r")
lines = fo.read()

# Read existing log                          
try:
  f = open(sys.argv[2], "rb")
  log.ParseFromString(f.read())
  f.close()
except IOError:
  print sys.argv[2] + ": File not found. Creating a new file."

main(lines)

fn = '/usr/local/var/log/nginx/access.log' #path for nginx log
fp = open(fn, "r")
while True:
  new = fp.readline()
  if new:
    main(new)
  else:
    time.sleep(0.5)
