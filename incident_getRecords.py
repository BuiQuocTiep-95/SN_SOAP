#!/bin/env python

from SOAPpy  import SOAPProxy

 # read instance info
file = open("login.txt", "r");
lines = file.read().splitlines();

instance = lines[0]
username = lines[1]
password = lines[2]

proxy = 'https://%s:%s@%s.service-now.com/incident.do?SOAP' % (username, password, instance)
namespace = 'http://www.service-now.com/'

server  = SOAPProxy (proxy ,namespace )
response  = server.getRecords (category  = 'Network' )

for record  in response:
	 print record.number + ' ' + record.sys_id + ' ' + record.caller_id + ' ' + record.sys_updated_on

# response  = server.getKeys (category  = 'Network' )
# print response. sys_id. split ( ',' )
