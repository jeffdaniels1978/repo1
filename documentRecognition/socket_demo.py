import socket
import struct
import sys
import time
    
def testHttp(host = 'www.null.com'):
    port = 80
    request = bytes( 'GET / HTTP/1.1\nhost: %s\n\n' % host, 'utf8' )
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(request)
    return s.recv(1024)

def testFtp(host = 'ftp.ietf.org'):
    port = 21
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s.recv(1024)

def testSmtp(host = 'smtp.attwireless.net'):
    port = 25
    request = bytes( 'EHLO %s\n.\n' % host, 'utf8' )

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(request)
    s.close()
    return s.recv(1024)

def testNtp(addr='time.nist.gov'):
    TIME1970 = 2208988800
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = bytes( '\x1b' + 47 * '\0', 'utf8' )
    client.sendto( data, (addr, 123))
    data, address = client.recvfrom( 1024 )
    if data:
        t = struct.unpack( '!12I', data )[10]
        t -= TIME1970
        return time.ctime(t),t
    
        
print('http response', testHttp())
print('ftp response', testFtp())
#print('smpt response', testSmtp())
print('ntp response', testNtp())