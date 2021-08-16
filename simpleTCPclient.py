import socket 
import sys

def TCPsend(ip, port, msg):
    clientsock=socket.socket()
    addr = (ip, port)
    clientsock.connect(addr)
    clientsock.send(bytes(msg, encoding='gbk'))
    rec = clientsock.recv(1024)
    res = str(rec, encoding='gbk')
    clientsock.close()
    return res


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('please enter ip, port, and message to send. For example:  python3 simpleTCPclient.py 192.168.1.10 3000 ACK\r\n')
        sys.exit()
    print('ip: ', sys.argv[1])
    print('port: ', sys.argv[2])
    print('msg: ', sys.argv[3])

r = TCPsend(sys.argv[1], sys.argv[2], sys.argv[3])
print(r)
