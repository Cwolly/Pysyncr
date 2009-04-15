#!/usr/bin/env python
""" Initial creation of a username and password. This eventually will need to be hashed somehow, and the password will need to be saved on the server somehow """

import sys
import paramiko #paramiko implements the python ssh library


hostname = raw_input ("Please enter the IP or hostname of the pysyncr server: ") #needs to be stored for ssh and rsync connection later
port = raw_input ("Please enter the port that the server uses to connect (default is 22):")
username = raw_input ("Please create a username: ") #needs to be stored as permanent user authentication on server
password = raw_input ("Please create a password: ") #needs to be stored as permanent user password on server


