from PS3.PS3Client import PS3Client
from WiiU.WiiUClient import WiiUClient
import json; from copy import deepcopy

# Look a constant, in this economy ???
DEFAULT_CONFIG = {
    "General": {
        "AppID": "1534965343422906582",
        "DiscordPyToken": "DISCORD_USER_TOKEN_HERE",
        "PollInterval": 10,
        "ConsoleClients": "all",
        "PyPresenceBackend": True
    },
    "Presence": {
        "UseCommonFormat": True,
        "ResetTimeOnAppChange": True,
        "CommonFormat": {
            "DisplayType": 2,
            "AppName": "console_name",
            "Details1": "app_name",
            "Details2": "info_network",
            "ImageBigText": "app_name",
            "ImageBigType": "image_app",
            "ImageSmallText": "info_firmware",
            "ImageSmallType": "image_console"
        },
        "PS3Format": {
            "DisplayType": 2,
            "AppName": "console_name",
            "Details1": "app_name",
            "Details2": "info_network",
            "ImageBigText": "app_name",
            "ImageBigType": "image_app",
            "ImageSmallText": "info_firmware",
            "ImageSmallType": "image_console"
        },
        "WiiUFormat": {
            "DisplayType": 2,
            "AppName": "console_name",
            "Details1": "app_name",
            "Details2": "info_network",
            "ImageBigText": "app_name",
            "ImageBigType": "image_app",
            "ImageSmallText": "info_firmware",
            "ImageSmallType": "image_console"
        }
    },
    "ClientConfig": {
        "PS3": {
            "PS3Address": "X.X.X.X",
            "NetworkName": "PSN",
            "NetworkNameFull": "PlayStation Network",
            "NetworkID": "{anon-user}",
            "UseCelsius": True
        },
        "WiiU": {
            "UDPPort": 5005,
            "FirmwareVer": "{unknown-ver}",
            "HWInfoText": "IBM Espresso | AMD Latte"
        }
    }
}

# More Constants ??? Oh my, Oh my !
VALID_CLIENTS = ["PS3", "WiiU"]

Config = {}

# TM for TradeMark, Have fun naming your most private of functions with silly names too~
def SanitizerTM(Config: dict):
    from typing import Any

    SanitizedConf = {}
    ConfiguredClients = []
    DefaultInatorDefaults = {}
    CareOnlyCommonFormat = DEFAULT_CONFIG["Presence"].get("UseCommonFormat")

    def DefaultInator(DirtySegment: dict, InatorDefaultSegment: dict, GlobalDefaultSegment: dict):
        DefaultInated = {}
        ChangedKeys = []

        # DEFAULTINATE !!!
        for Key, GlobalDefault in GlobalDefaultSegment.items():
            InInatorDefaultToo = Key in InatorDefaultSegment
            InatorDefault = InatorDefaultSegment.get(Key)
            
            if Key in DirtySegment:
                Value = DirtySegment[Key]
                
                if InInatorDefaultToo and InatorDefault is not None and type(Value) is not type(InatorDefault):
                    Value = InatorDefault
                    ChangedKeys.append(Key)

            else:
                if InInatorDefaultToo:
                    Value = InatorDefault
                    ChangedKeys.append(Key)
                else:
                    continue

            if isinstance(Value, dict) and isinstance(GlobalDefault, dict):
                NextInator = InatorDefault if isinstance(InatorDefault, dict) else {}
                SubDefaultInated, SubChangedKeys = DefaultInator(Value, NextInator, GlobalDefault)
                DefaultInated[Key] = SubDefaultInated
                ChangedKeys += SubChangedKeys
            else:
                DefaultInated[Key] = Value

        return DefaultInated, ChangedKeys

    def AppIDChecker(AppID: str):
        AppID = "NotAnID" if AppID.strip() == "" else AppID
        from requests import get
        ValidID = ""

        if get(f"https://discord.com/api/v10/applications/{AppID}/rpc").status_code != 200:
            print("The provided AppID isn't valid, a valid AppID is required by Presenced in order to function")
            ValidID = AppIDChecker(input("Please enter a valid AppID: ").strip())
        else:
            ValidID = AppID

        return ValidID

    def UserTokenChecker(UserToken: str):
        UserToken = "NotAToken" if UserToken.strip() == "" else UserToken
        from discord import Client
        Connection = Client()
        ValidToken = ""

        @Connection.event
        async def on_ready():
            await Connection.close()

        try:
            Connection.run(UserToken, log_handler=None)
            ValidToken = UserToken
        except:
            print("The provided UserToken isn't valid, a valid UserToken is required by Presenced in order to function standalone with discord.py-self")
            ValidToken = UserTokenChecker(input("Please enter a valid UserToken: "))  

        return ValidToken

    def SuperChecker(DefaultInatorDefaults: dict, Config: dict):
        # Members of the checklist go like this (ConfigSegment [it's a dict], Key, Operator, DefaultValue)
        TheCheckListTM = [
            Presence
            for Format, Value in DefaultInatorDefaults["Presence"].items()
                if Format.endswith("Format") and isinstance(Value, dict)
            for Presence in 
                ((Config["Presence"][Format], "DisplayType", "in", range(1, 3), DEFAULT_CONFIG["Presence"][Format]["DisplayType"]),
                (Config["Presence"][Format], "AppName", "!=", "", DEFAULT_CONFIG["Presence"][Format]["AppName"]),
                (Config["Presence"][Format], "ImageBigType", "!=", "", DEFAULT_CONFIG["Presence"][Format]["ImageBigType"]))
        ]
        TheCheckListTM += [
            (Config["ClientConfig"]["WiiU"], "UDPPort", "in", range(0, 65535), DEFAULT_CONFIG["ClientConfig"]["WiiU"]["UDPPort"])
        ]

        # Just a vert dumb switch statement to apply the rules, you have to think in reverse
        # To understand the statements tho, for exemple let's say we want out value X to be in
        # A range of 10 to a 1000, else go to the default value then you call TheRuler with the
        # Parameter (X, range(10, 1000), "in", DefaultVal) so the function will actually check
        # If it's not in this range, see where this is going ? It applies the default it the value
        # Doesn't respect the rule that's why the logic is all reversed in the if statements
        def TheRuler(Value: Any, Operator: str, ComparedValue: Any, DefaultValue: Any):
            from collections.abc import Iterable
            
            Operator = "".join(Operator.strip().lower().split(" ")[::])
            IterOperators = ["in", "notin"]
            NormalOperators = [ "==", "!=", ">=", ">", "<=", "<"]

            # Safety first boys
            if Operator not in IterOperators + NormalOperators:
                return Value
            elif Operator in IterOperators and not isinstance(ComparedValue, Iterable):
                return Value
            elif Operator in NormalOperators[2::]:
                if isinstance(Value, (str, bytes, Iterable)) or isinstance(ComparedValue, (str, bytes, Iterable)):
                    return Value

            # For strings Remove trailing whitespaces because why not ?
            # It's really just there for the AppName field
            if isinstance(Value, str): Value = Value.strip()
            if isinstance(ComparedValue, str): ComparedValue = ComparedValue.strip()

            match Operator:
                # Iterable Checks
                case "in":
                    if Value not in ComparedValue:
                        return DefaultValue
                    
                case "notin":
                    if Value in ComparedValue:
                        return DefaultValue
                
                # Normal Checks
                case "==":
                    if Value != ComparedValue:
                        return DefaultValue
                case "!=":
                    if Value == ComparedValue:
                        return DefaultValue

                case ">=":
                    if Value < ComparedValue: # type: ignore (Hides the Error squigle since that case is already handled above)
                        return DefaultValue
                case ">":
                    if Value <= ComparedValue: # type: ignore (Hides the Error squigle since that case is already handled above)
                        return DefaultValue

                case "<=":
                    if Value > ComparedValue: # type: ignore (Hides the Error squigle since that case is already handled above)
                        return DefaultValue
                case "<":
                    if Value >= ComparedValue: # type: ignore (Hides the Error squigle since that case is already handled above)
                       return DefaultValue

            return Value

        for Setting in TheCheckListTM:
            Setting[0][Setting[1]] = TheRuler(Setting[0][Setting[1]], Setting[2], Setting[3], Setting[4])

    def TelePrompter(ChangedVars: list, Config: dict):
        # While pretty flexible TelePrompter is onl meant to handle single values, to support anything other than Bool, Int, and Str
        # You'll need to update the Recursive Prompt function, happy coding to you I guess, unless you're me then fuck you future me

        # I'm trying to be tree like with tuples, so the first item is the parent and the second item is a child list, because we love
        # Maintainable code and because I'd like you to add more Clients if you are so inclined the child list is automaticly generated
        # Thanks to python's list "Inline" for loops or whatever they're called, still some manual labour required which is bad but I
        # Can't think of anything better right now + it should be simple to implement and much better than my switch statement spam :)
        AttentionSeekingVars = {"ClientConfig": (None, [Child for Child in DEFAULT_CONFIG["ClientConfig"].keys()]),
                                "PS3": ("ClientConfig", [Child for Child in DEFAULT_CONFIG["ClientConfig"]["PS3"].keys()]),
                                "PS3Address": ("PS3", None), "NetworkName": ("PS3", None), "NetworkNameFull": ("PS3", None),
                                "NetworkID": ("PS3", None), "UseCelsius": ("PS3", None), # This is filler text so no gap here
                                "WiiU": ("ClientConfig", [Child for Child in DEFAULT_CONFIG["ClientConfig"]["WiiU"].keys()]),
                                "WiiUAddress": ("WiiU", None), "FirmwareVer": ("WiiU", None), "HWInfoText": ("WiiU", None),
                                "UDPPort": ("WiiU", None)} # More useless text to fill the gap because it looks better imo ;)

        def TreeClimber(Branch: str, Tree: dict[str, tuple], _Propagator: tuple[bool, list, dict, dict] | None = None):
            ShouldPropagate, GenealogicalTree, ConfigFold, DefaultConfigFold = _Propagator if _Propagator else (False, [], {}, {})

            if not ShouldPropagate:
                GenealogicalTree.append(Branch)

                if Tree[Branch][0]:
                    TreeClimber(Tree[Branch][0], Tree, (False, GenealogicalTree, {}, {}))                    

                # Edge case where the targeted key has the root for parent and no kids (sad ik), unlikely because of how
                # I decided to structure the config file but who knows, "flexible" code is better code I guess, maybe ??
                elif len(GenealogicalTree) == 1 and type(DEFAULT_CONFIG[Branch]) != dict:
                    Config[Branch] = RecursivePrompt(Branch, type(DEFAULT_CONFIG[Branch]), DEFAULT_CONFIG[Branch])

                else:
                    TreeClimber(Branch, Tree, (True, GenealogicalTree, Config[Branch], DEFAULT_CONFIG[Branch]))

            else:
                
                if len(GenealogicalTree) > 2:
                    GenealogicalTree.pop(-1)
                    TreeClimber(GenealogicalTree[-1], Tree, \
                                (True, GenealogicalTree, ConfigFold[GenealogicalTree[-1]], DefaultConfigFold[GenealogicalTree[-1]]))
                    
                else:
                    Key = GenealogicalTree[0]
                    
                    if Tree[Key][1]:
                        for Child in Tree[Key][1]:
                            TreeClimber(Child, Tree)

                    else:
                        ConfigFold[Key] = RecursivePrompt(Key, type(DefaultConfigFold[Key]), DefaultConfigFold[Key])

            return

        def RecursivePrompt(VariableName: str, VariableType: type, VariableDefault: Any):
            HasDefault = ": " if not VariableDefault else f"(ENTER to use default of \"{VariableDefault}\"): " 
            VariableValue = None

            UserInput = input(f"Configuration for variable \"{VariableName}\" of type \"{VariableType}\" needs to be set " + HasDefault).strip()
            if not UserInput and HasDefault != ": ":
                VariableValue = VariableDefault
            else:
                try:
                    # Bools may be tricky for non devs since anything other than "" counts as true, we hate if
                    # Satements but useability requires it, just don't look at the switch statement bomb below
                    # I pinky promise I'll maybe make something actually maintainable (Don't take my word)
                    # While not perfect I held my promise ! And just one commit later, like it's never been an issue
                    if VariableType == bool:
                        if UserInput.lower() in ["true", "t", "1", "y"]:
                            VariableValue = True
                        elif UserInput.lower() in ["false", "f", "0", "n", ""]:
                            VariableValue = False
                        else:
                            raise ValueError
                    else:
                        VariableValue = VariableType(UserInput)
                except (TypeError, ValueError):
                    print(f"Couldn't convert input for \"{VariableName}\" to \"{VariableType}\", please try again with another value")
                    VariableValue = RecursivePrompt(VariableName, VariableType, VariableDefault)
            
            return VariableValue

        if ChangedVars:
            TelePrompterMsg = "Configuration Variables were added / or changed because they were either missing or wrong in the config file,"
            TelePrompterMsg += "\nif any should be set by you, we'll make sure to ask for a value, in any other case the process is automatic"
            print(TelePrompterMsg)

            for Var in ChangedVars:
                if Var in AttentionSeekingVars:
                    TreeClimber(Var, AttentionSeekingVars)

        return

    def Striper(Config: dict):
        # Super Simple Recursive Function
        # That strips all strings in the config

        for Key, Value in Config.items():
            if isinstance(Value, dict):
                Striper(Config[Key])
            elif isinstance(Value, str):
                Config[Key] = Value.strip()

        return
            

    # Bootstraping the DEFAULTINATOR !
    if isinstance(Config.get("General"), dict) and isinstance(Config["General"].get("ConsoleClients"), list):
        ConfiguredClients = [Client for Client in Config["General"].get("ConsoleClients") if Client in VALID_CLIENTS] \
                            if Config["General"].get("ConsoleClients") else VALID_CLIENTS

    else:
        ConfiguredClients = VALID_CLIENTS

    if isinstance(Config.get("Presence"), dict) and isinstance(Config["Presence"].get("UseCommonFormat"), bool):
        CareOnlyCommonFormat = Config["Presence"].get("UseCommonFormat")

    DefaultInatorDefaults = deepcopy(DEFAULT_CONFIG)

    # Only DefaultInate Clients that will be used
    for Client in VALID_CLIENTS: 
        if Client not in ConfiguredClients: DefaultInatorDefaults["ClientConfig"].pop(Client)

    # Only Defaultinate Presence Formats that will be used
    for Format in [f"{FMT}Format" for FMT in VALID_CLIENTS] if CareOnlyCommonFormat else ["CommonFormat"] \
    + [f"{FMT}Format" for FMT in VALID_CLIENTS if FMT not in ConfiguredClients]: # Fancy expression I know :)
        DefaultInatorDefaults["Presence"].pop(Format)

    SanitizedConf, ChangedVars = DefaultInator(Config, DefaultInatorDefaults, DEFAULT_CONFIG)

    TelePrompter(ChangedVars, SanitizedConf)

    Striper(SanitizedConf)
    
    # Checking validity of important settings
    SanitizedConf["General"]["AppID"] = AppIDChecker(SanitizedConf["General"]["AppID"])

    if not SanitizedConf["General"]["PyPresenceBackend"]:
        SanitizedConf["General"]["DiscordPyToken"] = UserTokenChecker(SanitizedConf["General"]["DiscordPyToken"])

    # All other settings that need checking are handled by the SuperChecker
    # If I or You ig, need to add a value to the super checker list then
    # Go to the function's definition and add it to TheCheckListTM which
    # should be the first thing defined in the function for easy access
    SuperChecker(DefaultInatorDefaults, SanitizedConf)

    return SanitizedConf

def ConfigLoader(ConfigPath: str):
    ConfigFile = None
    DirtyConfig = {}
    
    try:
        ConfigFile = open(f"{ConfigPath}/config.json", "r", encoding="utf-8")
    except FileNotFoundError:
        print("Config File not found, File will be created")

    if ConfigFile:
        try:
            DirtyConfig = json.load(ConfigFile)
            ConfigFile.close()
        except json.JSONDecodeError:
            ConfigFile.close()
            print("Invalid Config File, failed to parse json, new File will be created")
    else:
        DirtyConfig = {}

    return SanitizerTM(DirtyConfig)

def ConfigSaver(ConfigPath: str, Config: dict):
    ConfigFile = open(f"{ConfigPath}/config.json", "w", encoding="utf-8")

    json.dump(Config, ConfigFile, indent=4)
    ConfigFile.close()

    return

def ConfigHandler(LocalPath: str):
    global Config

    ClientConstructors = {
        "PS3": PS3Client,
        "WiiU": WiiUClient
    }

    # Create / load a valid config
    Config = ConfigLoader(LocalPath)

    ConfiguredClients = VALID_CLIENTS if not isinstance(Config["General"]["ConsoleClients"], list) \
                                      else Config["General"]["ConsoleClients"]
    for Client in ConfiguredClients:
        ClientConf = {
            "Presence": {
                "ResetTimeOnAppChange": Config["Presence"]["ResetTimeOnAppChange"],
                "Format": deepcopy(Config["Presence"]["CommonFormat"]) if Config["Presence"]["UseCommonFormat"] \
                          else deepcopy(Config["Presence"][f"{Client}Format"])
            }
        }; ClientConf.update(Config["ClientConfig"][Client].items())

        ClientConstructors[Client](ClientConf)

    ConfigSaver(LocalPath, Config)

    return

## Over complicated path thingy for testing
import os
path = os.path.abspath(__file__).split("/")
path.pop(len(path) - 1); path.pop(len(path) - 1)
path = "/".join(path)

ConfigHandler(path)

from ConsoleClient import (Clients, ActiveClients)
from pypresence import types, presence
import time

RichPresence = presence.Presence(Config["General"]["AppID"])
Connected = False

while True:
    for Client in Clients:
        Client.pingConsole()

    if ActiveClients:
        if not Connected:
            try:
                RichPresence.connect()
                Connected = True
            except:
                print("Connexion Error")

        if Connected:
            RPCData = ActiveClients[0].getRPCData()

            DisplayType = None

            match RPCData.get("DisplayType"):
                case 1:
                    DisplayType = types.StatusDisplayType.NAME
                case 2:
                    DisplayType = types.StatusDisplayType.DETAILS
                case 3:
                    DisplayType = types.StatusDisplayType.STATE

            RichPresence.update(
                start=RPCData.get("StatTime"),
                status_display_type=DisplayType,
                name=RPCData.get("Name"),
                details=RPCData.get("Details"),
                state=RPCData.get("State"),
                large_image=RPCData.get("LargeImage"),
                large_text=RPCData.get("LargeText"),
                small_image=RPCData.get("SmallImage"),
                small_text=RPCData.get("SmallText")
            )

    elif Connected:
        RichPresence.close()
        Connected = False

    time.sleep(Config["General"]["PollInterval"])