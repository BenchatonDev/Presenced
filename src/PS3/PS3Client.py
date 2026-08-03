from ConsoleClient import * 
from icmplib import ping
import requests
# Smanparser include in the future here

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

        else:
            ActiveClients.remove(self) if self in ActiveClients else None
            return