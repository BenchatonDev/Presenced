from ConsoleClient import ConsoleClient, ActiveClients, RPCFormat
from .SmanParser import SmanHTMLParser
from PresencedIcons import getIcon
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
                   self.ClientData["OldConsoleData"].get("TitleID") != self.ClientData["ConsoleData"].get("TitleID"):
                    self.ClientData["AppStartTime"] = int(datetime.now(timezone.utc).timestamp())

        else:
            if self in ActiveClients: ActiveClients.remove(self); \
                self.ClientData["ConsoleData"], self.ClientData["OldConsoleData"] = {}, {}

            return

        return

    def getRPCData(self):
        if self not in ActiveClients: return {}

        TemperatureUnit = "C" if self.Config.get("UseCelsius") else "F"

        TextRules = {
            "console_name":  lambda : "PlayStation 3",
            "app_name":      lambda : self.ClientData["ConsoleData"].get("TitleName"),
            "network_name":  lambda : self.Config.get("NetworkNameFull"),
            "info_firmware": lambda : f"GameOS: {self.ClientData["ConsoleData"].get("Firmware")}",
            "info_network":  lambda : f"{self.Config.get("NetworkName")}: {self.Config.get("NetworkID")}",
            "info_hardware": lambda : f"Cell: {self.ClientData["ConsoleData"]["CPUTemp"].get(TemperatureUnit)}°{TemperatureUnit} | RSX: {\
                                        self.ClientData["ConsoleData"]["RSXTemp"].get(TemperatureUnit)}°{TemperatureUnit}"
        }

        ImageRules = {
            "image_app": lambda : getIcon("Unknown"), # URL resolved by an helper function I have yet to implement
            "image_console": lambda : getIcon("PS3"), # Change that to a URL or asset name if you ever change the AppID
            "image_network": lambda : getIcon("PlayStationN") if self.Config.get("NetworkName") == "PSN" else getIcon("Unknown")
        }

        return RPCFormat(TextRules, ImageRules, self.Config["Presence"].get("Format"), self.ClientData["AppStartTime"])