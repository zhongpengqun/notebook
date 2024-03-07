
import socket
import binascii

HOST = ''
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)


while True:
    print('1111')
    conn, address = s.accept()
    # recv(bufsize[, flags])
    # Returns the received data as bytes object.
    print('222222')
    request = conn.recv(1024)
    print('connected by', repr(address),
          'received ', binascii.hexlify(request))
    if request:
        # This function sends data to a connected socket 
        # socket.send is a low-level method and basically just the C/syscall method send(3) / send(2). It can send less bytes than you requested, but returns the number of bytes sent.
        # socket.sendall is a high-level Python-only method that sends the entire buffer you pass or throws an exception
        # It does that by calling socket.send until everything has been sent or an error occurs.
        # sendall use under the hood send
        conn.sendall(request)
    print('-----x---')