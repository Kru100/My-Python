from __future__ import print_function
import Pyro4

obj = Pyro4.core.Proxy("PYRONAME:Calculator")               #Syncing with the server using Proxy
print("Addition: %d" % obj.add(2,3))                        #calling add object
print("Subtraction: %d" % obj.sub(71,62))                   #calling sub object
print("Multiplication: %d" % obj.mult(6,5))                 #calling mult object
print("Division: %f" % obj.divi(12,5))                      #calling divi object
print("Modulo: %d \n\n" % obj.modulo(12,35))                #calling modulo object

print("From server_factorial")
obj1 = Pyro4.core.Proxy("PYRONAME:Factorial")               #Syncing with Factorial server
print("Factorial: %d\n\n" % obj1.fact(5))                   #calling fact object

print("From server_power")
obj2 = Pyro4.core.Proxy("PYRONAME:Power")                   #syncing with power server
print("Power of 4: %d" % obj2.Power(4,3))                   #calling Power object