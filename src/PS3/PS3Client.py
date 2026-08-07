from .SmanParser import SmanHTMLParser
from ConsoleClient import ConsoleClient, ActiveClients
from icmplib import ping
import requests

RequestHeaders = { "User-Agent": "Mozilla/5.0" }

class PS3Client(ConsoleClient):

    def pingConsole(self):
        if ping(self.IpAddress, privileged=False).is_alive:
            try:
                requests.get(f"http://{self.IpAddress}", headers=RequestHeaders)

            except:
                ActiveClients.remove(self) if self in ActiveClients else None
                return
            
            else:
                ActiveClients.insert(0, self) if self not in ActiveClients else None
                SmanHTML = requests.get(f"http://{self.IpAddress}/cpursx.ps3?/sman.ps3", headers=RequestHeaders).text

                self.ClientData = SmanHTMLParser(SmanHTML)

        else:
            ActiveClients.remove(self) if self in ActiveClients else None
            return