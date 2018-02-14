# Python Offensive PenTesting: - All rights reserved Nathan W Jones nathan.jones@arcadeusops.com

# This script is a simple, fast port scanner. Change range(1,1025) any range 0-65000+.

#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen and ask for input
subprocess.call('clear', shell=True)
remoteServer    = raw_input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print banner with info on host we are about to scan
print "-" * 60
print "Arcadeus OPS Port Scanner. Please wait, scanning remote host", remoteServerIP
print "-" * 60

# Check what time the scan started
t1 = datetime.now()

# Use the range function to specify ports (here it will scans all ports between 1 and 1024). We also put in some error handling for catching errors.

try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Check the time again, calculate time difference, calculate how long it took to run script
t2 = datetime.now()
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total