from .ConnectionHelper import WiiUConnector
from ConsoleClient import ConsoleClient, ActiveClients
from datetime import datetime, timezone
from copy import deepcopy


class WiiUClient(ConsoleClient):

    def pingConsole(self):
        WiiUData = WiiUConnector(self.Config["UDPPort"])

        if WiiUData:
            if self not in ActiveClients: ActiveClients.insert(0, self); \
                self.ClientData["AppStartTime"] = int(datetime.now(timezone.utc).timestamp())

            if self.Config["Presence"]["ResetTimeOnAppChange"]:
                self.ClientData["AppStartTime"] = WiiUData["Time"]
            WiiUData.pop("Time")
            
            self.ClientData["OldConsoleData"] = deepcopy(self.ClientData["ConsoleData"])
            self.ClientData["ConsoleData"] = deepcopy(WiiUData)

        else:
            if self in ActiveClients: ActiveClients.remove(self); \
                self.ClientData["ConsoleData"], self.ClientData["OldConsoleData"] = {}, {}

        return

    def getRPCData(self):
        return {}