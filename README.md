# SimpleTCPClient
Simple TCP client running under python3.6. 
  
usage:  python3 simpleTCPclient.py 'ip' 'port' 'message'.   
For example:  
```
python3 simpleTCPclient.py 192.168.88.123 3000 ACK
```
  
  
Some TCP message may need a 0A 0D or \r\n ending, if \r\n did not work in command line input, try to edit the sys.argv[3] in python code directly.  
For example:
```
r = TCPsend(sys.argv[1], int(sys.argv[2]), 'ACK\r\n')
```
