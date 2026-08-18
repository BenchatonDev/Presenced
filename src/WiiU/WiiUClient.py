from ConsoleClient import ActiveClients, ConsoleClientLock, ConsoleClient, RPCFormat
from .ConnectionHelper import WiiUConnector, ToEpoch
from datetime import datetime, timezone
from PresencedIcons import getIcon
from .AppIcon import getAppIcon
from copy import deepcopy

class WiiUClient(ConsoleClient):

    def pingConsole(self):
        WiiUData = WiiUConnector(self.Config["UDPPort"])
        
        if WiiUData:
            with ConsoleClientLock:
                if self not in ActiveClients: ActiveClients.insert(0, self); \
                   self.ClientData["AppStartTime"] = int(datetime.now(timezone.utc).timestamp())

            if self.Config["Presence"]["ResetTimeOnAppChange"]:
                self.ClientData["AppStartTime"] = ToEpoch(WiiUData["Time"])
            WiiUData.pop("Time")
            
            self.ClientData["OldConsoleData"] = deepcopy(self.ClientData["ConsoleData"])
            self.ClientData["ConsoleData"] = deepcopy(WiiUData)

        else:
            with ConsoleClientLock:
                if self in ActiveClients: ActiveClients.remove(self); \
                   self.ClientData["ConsoleData"], self.ClientData["OldConsoleData"] = {}, {}

        return

    def getRPCData(self):
        with ConsoleClientLock:
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
            "image_app": lambda : getAppIcon(self.ClientData["ConsoleData"].get("LongTitleName")),
            "image_console": lambda : getIcon("WiiU"), # Change that to a URL or asset name if you ever change the AppID
            "image_network": lambda : getIcon("NintendoN") if self.ClientData["ConsoleData"].get("Network") == "nn" else \
                                      getIcon("PretendoN") if self.ClientData["ConsoleData"].get("Network") == "pn" else getIcon("Unknown")
        }

        return RPCFormat(TextRules, ImageRules, self.Config["Presence"].get("Format"), self.ClientData["AppStartTime"])