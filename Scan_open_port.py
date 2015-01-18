#!/usr/bin/python
import sys
import socket
import argparse
f=open('SName.csv','r')
dict={}
for line in f:
	line=line.split(',')
	try:
		if line[2]=='tcp' :
			dict[line[1]]=line[0]	
	except:
		pass
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("-i", type = str, dest = "serveripaddress", default = None)
parser.add_argument("-h", type = str, dest = "servername", default = None)
parser.add_argument("-p1", type = str, dest = "startingportnumber",default=-1)
parser.add_argument("-p2", type = str, dest = "endingportnumber",default=-1)

args = parser.parse_args()

serverName = args.servername
serverIP=args.serveripaddress
startingPortnumber=args.startingportnumber
startingPortnumber=int(startingPortnumber)
endingPortnumber=args.endingportnumber
endingPortnumber=int(endingPortnumber)

if startingPortnumber==-1 or endingPortnumber==-1:
	print "Enter both startingportnumber and endingportnumber"
	sys.exit()
if serverName==None and serverIP==None:
	print "Should enter either host name or ip address"
	sys.exit()
elif endingPortnumber>65535:
	print "Portnumber must not be greater than 65535"
	sys.exit()
elif startingPortnumber<0:
	print "Port number must be in range 0-65535"
	sys.exit()
if serverName!=None and serverIP!=None:
	if serverIP==socket.gethostbyname(serverName):
		remoteServerIP  = socket.gethostbyname(serverName)
	else:
		print "Either enter host name or ip address"
		sys.exit()
elif serverName!=None and serverIP==None:
	remoteServerIP  = socket.gethostbyname(serverName)
else:
	remoteServerIP=serverIP
try:
    for port in range(startingPortnumber,endingPortnumber):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
			print "Port {}: \t Open".format(port)
			port=str(port)
			print "Service provided",dict[port]
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C or Ctrl+Z"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()
