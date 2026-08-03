# Skeleton to be implemented for any console I want to support

Clients = []
ActiveClients = []

class ConsoleClient:

    def __init__(self, IpAddress: str):
        """ This Function just set the IP address to be used for console communications, likely from a
        config handler or smt like that which has yet to be implemented, just like 99% of this class """
        self.IpAddress = IpAddress
        self.ClientData = {}

        Clients.append(self)

    def __del__(self):
        """ This Function is very unlikely to be called with the design I have in mind but it's there in 
        the event that I ever need it in the future. I need to fill the remaining space so it's aligned :) """

        Clients.remove(self)

        if self in ActiveClients:
            ActiveClients.remove(self)

        return

    def pingConsole(self):
        """ This Function will be called for all clients in the Clients list routinely, if it succeeds
        then the client will be added to the ActiveClients list, and in reverse if it fails. In the case
        the client is found to be active it should also retrieve relevant data from the console """

        return

    def getRPCData(self):
        """ This Function will be called for the active client chosen to be displayed on your discord profile,
        it's point is to return the right stuff to the function that will handle the communication with discord """
        
        return