# Skeleton to be implemented for any console I want to support
from threading import Lock

Clients = []
ActiveClients = []
# Should provent race conditions on the two shared variables above 
# If I understood the documentation page right, It needs to be 
# Imported alongside the vars tho, but that shouldn't be a problem
ConsoleClientLock = Lock()

class ConsoleClient:

    def __init__(self, Config: dict):
        """ This Function just set the config used by the console client, likely from a config handler or smt
        like that which has yet to be implemented, just like 99% of this class (Actually it's all here now) """
        self.Config = Config
        self.ClientData = {
            "ConsoleData": {},
            "OldConsoleData": {},
            "AppStartTime": 0
        }

        with ConsoleClientLock: Clients.append(self)

        return

    def __del__(self):
        """ This Function is very unlikely to be called with the design I have in mind but it's there in 
        the event that I ever need it in the future. I need to fill the remaining space so it's aligned :) """

        with ConsoleClientLock: Clients.remove(self)

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
        
        return {}

def RPCFormat(TextRules: dict, ImageRules: dict, Format: dict, Time: int):
    try: # The Rules' items must be callable
        for Value in TextRules.values(): Value()
        for Value in ImageRules.values(): Value()
    except:
        return {}
    
    # For the Name a smaller subset of presets are available
    ValidNameRules = ["console_name", "app_name"]

    # Shorthands (is that the right word ?) for config
    # Value Retrieval
    AppName = Format.get("AppName")
    Details1 = Format.get("Details1") if Format.get("Details1") else None
    Details2 = Format.get("Details2") if Format.get("Details2") else None
    ImageBigText = Format.get("ImageBigText") if Format.get("ImageBigText") else None
    ImageBigType = Format.get("ImageBigType")
    ImageSmallText = Format.get("ImageSmallText") if Format.get("ImageSmallText") else None
    ImageSmallType = Format.get("ImageSmallType") if Format.get("ImageSmallType") else None

    RPCData = {
        "StartTime": Time,
        "DisplayType": Format.get("DisplayType"),
        "Name": AppName if AppName not in ValidNameRules else TextRules[AppName](),
        "Details": Details1 if Details1 not in TextRules else TextRules[Details1](),
        "State": Details2 if Details2 not in TextRules else TextRules[Details2](),
        "LargeText": ImageBigText if ImageBigText not in TextRules else TextRules[ImageBigText](),
        "LargeImage": ImageBigType if ImageBigType not in ImageRules else ImageRules[ImageBigType](),
        "SmallText": ImageSmallText if ImageSmallText not in TextRules else TextRules[ImageSmallText](),
        "SmallImage": ImageSmallType if ImageSmallType not in ImageRules else ImageRules[ImageSmallType](),
    }

    return RPCData