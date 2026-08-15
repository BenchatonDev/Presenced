from .ConnectionHelper import WiiUConnector, ToEpoch
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
                self.ClientData["AppStartTime"] = ToEpoch(WiiUData["Time"])
            WiiUData.pop("Time")
            
            self.ClientData["OldConsoleData"] = deepcopy(self.ClientData["ConsoleData"])
            self.ClientData["ConsoleData"] = deepcopy(WiiUData)

        else:
            if self in ActiveClients: ActiveClients.remove(self); \
                self.ClientData["ConsoleData"], self.ClientData["OldConsoleData"] = {}, {}

        return

    def getRPCData(self):
        if self not in ActiveClients: return {}

        TextRules = {
            "console_name":  lambda : "Wii U",
            "app_name":      lambda : self.ClientData["ConsoleData"].get("ShortTitleName"),
            "network_name":  lambda : "Nintendo Network" if self.ClientData["ConsoleData"].get("Network") == "nn" else \
                                      "Pretendo Network" if self.ClientData["ConsoleData"].get("Network") == "pn" else "Unknown",
            "info_firmware": lambda : f"CafeOS: {self.Config.get("FirmwareVer")}",
            "info_network":  lambda : f"{"NNID" if self.ClientData["ConsoleData"].get("Network") == "nn" else \
                                         "PNID" if self.ClientData["ConsoleData"].get("Network") == "pn" else "NID"}: {self.ClientData["ConsoleData"].get("NetworkID")}",
            "info_hardware": lambda : self.Config.get("HWInfoText")
        }

        ImageRules = {
            "image_app": lambda : "unknown", # URL resolved by an helper function I have yet to implement
            "image_console": lambda : "wiiu", # Change that to a URL or asset name if you ever change the AppID
            "image_network": lambda : "nintendo" if self.ClientData["ConsoleData"].get("Network") == "nn" else \
                                      "pretendo" if self.ClientData["ConsoleData"].get("Network") == "pn" else "unknown"
        }

        return {}