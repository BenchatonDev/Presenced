from .SmanParser import SmanHTMLParser
from ConsoleClient import ConsoleClient, ActiveClients
from icmplib import ping
from copy import deepcopy
from requests import get

RequestHeaders = { "User-Agent": "Mozilla/5.0" }

class PS3Client(ConsoleClient):

    def pingConsole(self):
        if ping(self.Config["PS3Address"], privileged=False, interval=0, timeout=1).is_alive:
            try:
                get(f"http://{self.Config["PS3Address"]}", headers=RequestHeaders, timeout=1)

            except:
                ActiveClients.remove(self); self.ClientData["ConsoleData"], self.ClientData["OldConsoleData"] = {}, {} \
                if self in ActiveClients else None

                return
            
            else:
                ActiveClients.insert(0, self); self.ClientData["AppStartTime"] = 10 \
                if self not in ActiveClients else None

                SmanHTML = get(f"http://{self.Config["PS3Address"]}/cpursx.ps3?/sman.ps3", headers=RequestHeaders).text

                self.ClientData["OldConsoleData"] = deepcopy(self.ClientData)
                self.ClientData["ConsoleData"] = SmanHTMLParser(SmanHTML)

        else:
            ActiveClients.remove(self); self.ClientData["ConsoleData"], self.ClientData["OldConsoleData"] = {}, {} \
            if self in ActiveClients else None

            return

        return

    def getRPCData(self):
            return