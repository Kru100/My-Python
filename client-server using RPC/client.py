import socket
s = socket.socket()     #socket creation at client side
port = 5000
s.connect(('10.200.7.90',port))     #connect() : connect with server via port number and send the IP address
while True:
    print('Choose the following option\n 1.Add Two Numbers? \n 2.Factorial of a number \n 3.Find the binerary of an Decimal \n')
    k = input()
    s.send(str(k).encode('utf8'))
    print(s.recv(1024))
    
    k = int(k)
    if k == 0:
        print(s.recv(1024))
        break
    
    if k == 1:
        print("\n")
        m = input()
        n = input()
        s.send(str(m).encode('utf8'))
        s.send(str(n).encode('utf8'))
        ans = s.recv(1024)
        str1 = ans.decode('utf8')
        ansn = str(str1)
        print(ansn)
        
    if k == 2:
        print("\n")
        m = input()
        s.send(str(m).encode('utf8'))
        ans = s.recv(1024)
        str1 = ans.decode('utf8')
        print(str1)
        
    if k == 3:
        print("\n")
        m = input()
        s.send(str(m).encode('utf8'))
        ans = s.recv(1024)
        str1 = ans.decode('utf8')
        print(str1)
        
s.close()