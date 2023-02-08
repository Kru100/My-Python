import Pyro4
import math

#Here using Pyro4.expose we are exposing all the servers so that client can invoke the method using it.
#interface which provide the calculations

@Pyro4.expose                       #Exposing the server
class Chain(object):
    def add(self,n1, n2):           #Defining Addition object
        return n1+n2
    def sub(self,n1,n2):            #Defining Substraction object
        return n1-n2
    def mult(self,n1,n2):           #Defining Multiplication object
        return n1*n2
    def divi(self,n1,n2):           #Defining Division Object
        return n1/n2
    def modulo(self,n1,n2):         #Defining Modulo object
        if n1>n2:
            return n1%n2
        else:
            return n2%n1
    def fact(self,n1):              #Defining factorial object
        return math.factorial(n1)
    def Power(self,n1,n2):          #Defining Power object
        return n1 ** n2