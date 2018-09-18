#!/bin/env python

from SOAPpy  import SOAPProxy

 # read instance info
file = open("login.txt", "r");
lines = file.read().splitlines();

instance = lines[0]
username = lines[1]
password = lines[2]

proxy = 'https://%s:%s@%s.service-now.com/sys_user.do?SOAP' % (username, password, instance)
namespace = 'http://www.service-now.com/'
server  = SOAPProxy (proxy ,namespace )

response = server.getRecords(user_name = 'aaron.aaronson');
user_id = response['sys_id']
print user_id


proxy = 'https://%s:%s@%s.service-now.com/incident.do?SOAP' % (username, password, instance)
namespace = 'http://www.service-now.com/'
server  = SOAPProxy (proxy ,namespace )

response  = server.deleteMultiple ( sys_created_on = "Today@javascript:gs.beginningOfToday()@javascript:gs.endOfToday()" )

print response

# response  = server.getKeys (category  = 'Network' )
# print response. sys_id. split ( ',' )
