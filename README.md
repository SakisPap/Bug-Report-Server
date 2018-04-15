# Bug-Report-Server

### Dependencies
Ubuntu Server

sendmail (sudo apt-get install sendmail)

### Edit
edit the /etc/hosts file:
127.0.0.1 localhost.localdomain localhost hostname (<-here goes the hostname type "hostname" to view)

### Format
the php request has the following format:

http://serverddns.com/bugreport.php?bodyofmessage=<here goes a url encoded string>
