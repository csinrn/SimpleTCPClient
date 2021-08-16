# SimpleTCPClient

Simple TCP client running under python3.6
usage:

'''
python3 simpleTCPclient.py 192.168.88.123 3000 ACK
'''

Some TCP message may need a 0A 0D or \r\n ending, if \r\n did not work for sys argv, try to edit the sys.argv[3] in python code  
for example: TCPsend(sys.argv[1], sys.argv[2], 'ACK\r]n')
