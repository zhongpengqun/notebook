### 笔记

AF_UNIX: address format is UNIX pathname
AF_INET: address format is host and port number

SOCK_STREAM means that it is a TCP socket.
SOCK_DGRAM means that it is a UDP socket.


- binascii.hexlify
    - Return the hexadecimal representation of the binary data. Every byte of data is converted into the corresponding 2-digit hex representation. The returned bytes object is therefore twice as long as the length of data.
    >>> binascii.hexlify(b'\xb9\x01\xef', '-')
    b'b9-01-ef'
    - why need such function ?


- getsockname
    - socket 与 port 与 进程 的关系？
        - socket 中存储了特定的四元组： 源ip+port，目的ip+port；
        - 在进程看来，socket 其实跟文件也没有什么不同，只不过通过描述符获得的对象不同而已，接口对应的系统调用也不同
            - 那么进程跟socket是一一对应的吗？
                - 其实不然，socket是一种资源，就像文件一样，一个进程打开了，另一个进程也可以用，只不过socket比较特殊而已。
                    - 当然，父子进程间，还有线程间，进行 socket 的共享，是比较常见的。
        - 进程与端口，其实并没有什么直接或必然的关系
        
```
ConnectionRefusedError: [Errno 61] Connection refused

- mac 打开防火墙端口
```