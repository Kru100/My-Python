import socket
s = socket.socket()         #Creaction of Socket from server side
print('Socket Succesfully Created')
port = 5000
s.bind(('',port))           #Bind : Given the port to server
print(f'Socket Binded To port{port}')
s.listen(5)                 #Listen : Shows that server is ready to connect with client and 5 shows that that much connection is maximum
print('Socket is listening')
while True:
    c, addr = s.accept()    #Accept : Accept the response from a client also it has the ip address of client
    print('Got Connection from \n', addr)
    p = c.recv(1024)        #.recv(buffer_size) : recv the data from client
    st = p.decode('utf8')   #.decode() : Decode the recieved data which is encoded in utf8
    num = int(st)
    # p=int("p")
    # print(p)
    if num == 1:
        m1 = 'Enter The Two Number with space between them: '
        print("\n")
        c.send(m1.encode()) #.send() : send data to client in encoded manner
        m = c.recv(1024)
        n = c.recv(1024)
        t1 = m.decode('utf8')
        t2 = n.decode('utf8')
        num1 = int(t1)
        num2 = int(t2)
        ans = num1 + num2
        c.send(str(ans).encode('utf8'))
        
    elif num == 2:
        m2 = 'Enter The Number To Find Its Factorial: '
        c.send(m2.encode())
        m = c.recv(1024)
        t1 = m.decode('utf8')
        num1 = int(t1)
        ans = 1
        while num1>0 :
            ans *= num1
            num1 -= 1
        
        c.send(str(ans).encode('utf8'))
        
    elif num == 3:
        m3 = 'Enter The Number To Covert it to Binary Number'
        c.send(m3.encode())
        m = c.recv(1024)
        t1 = m.decode('utf8')
        num1 = int(t1)
        ans = bin(num1)[2:]
        c.send(str(ans).encode('utf8'))
        
    elif num == 0:
        msg = ('Thank You For Connecting')
        c.send(msg.encode())
        c.close() 
        
    else:
        m4 = 'Enter a Valid Choice Please'
        c.send(m4.encode())
      #.close() : Close the connection
    