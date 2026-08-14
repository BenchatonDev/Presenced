from .SmanParser import SmanHTMLParser
from ConsoleClient import ConsoleClient, ActiveClients
from datetime import datetime, timezone
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
                if self in ActiveClients: ActiveClients.remove(self); \
                    self.ClientData["ConsoleData"], self.ClientData["OldConsoleData"] = {}, {}

                return
            
            else:
                if self not in ActiveClients: ActiveClients.insert(0, self); \
                    self.ClientData["AppStartTime"] = int(datetime.now(timezone.utc).timestamp())

                SmanHTML = get(f"http://{self.Config["PS3Address"]}/cpursx.ps3?/sman.ps3", headers=RequestHeaders).text

                self.ClientData["OldConsoleData"] = deepcopy(self.ClientData["ConsoleData"])
                self.ClientData["ConsoleData"] = SmanHTMLParser(SmanHTML)

                if self.Config["Presence"]["ResetTimeOnAppChange"] and \
                   self.ClientData["OldConsoleData"]["TitleID"] != self.ClientData["ConsoleData"]["TitleID"]:
                    self.ClientData["AppStartTime"] = int(datetime.now(timezone.utc).timestamp())

        else:
            if self in ActiveClients: ActiveClients.remove(self); \
                self.ClientData["ConsoleData"], self.ClientData["OldConsoleData"] = {}, {}

            return

        return

    def getRPCData(self):
        return {}