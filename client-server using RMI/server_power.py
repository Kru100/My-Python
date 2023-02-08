import Pyro4
import chainTopology

#Here is the code of server_calculator. daemon thread is here because server never mean to be stopped so its always running in background
#register() register the server in interface so that its objects can be used

servername = "Power"
daemon = Pyro4.core.Daemon()
obj = chainTopology.Chain()
url = daemon.register(obj)
ns = Pyro4.locateNS()
ns.register(servername, url)

print("server_Power started")
daemon.requestLoop() 