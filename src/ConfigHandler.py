from PS3.PS3Client import PS3Client
import json; import copy

# Look a constant, in this economy ???
DEFAULT_CONFIG = {
    "General": {
        "AppID": "1534965343422906582",
        "DiscordPyToken": "DISCORD_USER_TOKEN_HERE",
        "PollInterval": 20,
        "ConsoleClients": "all",
        "PyPresenceBackend": True
    },
    "Presence": {
        "UseCommonFormat": True,
        "ResetTimeOnAppChange": True,
        "CommonFormat": {
            "AppName": "console_name",
            "Details1": "app_name",
            "Details2": "info_network",
            "ImageBigText": "app_name",
            "ImageBigType": "image_app",
            "ImageSmallText": "info_firmware",
            "ImageSmallType": "image_console"
        },
        "PS3Format": {
            "AppName": "console_name",
            "Details1": "app_name",
            "Details2": "info_network",
            "ImageBigText": "app_name",
            "ImageBigType": "image_app",
            "ImageSmallText": "info_firmware",
            "ImageSmallType": "image_console"
        },
        "WiiUFormat": {
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
            "NetworkName": "PSN",
            "NetworkNameFull": "PlayStation Network",
            "NetworkID": "{anon-user}",
            "UseCelsius": True
        },
        "WiiU": {
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
    SanitizedConf = {}
    ConfiguredClients = []
    CareOnlyCommonFormat = True

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

    def DefaultInator(DirtySegment: dict, DefaultSegment: dict):
        DefaultInated = {}
        ChangedKeys = []

        for key in DirtySegment.keys():
            if key in DefaultSegment:
                print()

        return DefaultInated

    def TelePrompter():
        return

    def FormatSanitizerTM():
        return

    # Bootstraping the DEFAULTINATOR !
    if isinstance(Config.get("General"), dict) and isinstance(Config["General"].get("ConsoleClients"), list):
        ConfiguredClients = [Client for Client in Config["General"].get("ConsoleClients") if Client in VALID_CLIENTS] \
                            if Config["General"].get("ConsoleClients") else VALID_CLIENTS

    else:
        ConfiguredClients = VALID_CLIENTS

    if isinstance(Config.get("Presence"), dict) and isinstance(Config["Presence"].get("UseCommonFormat"), bool):
        CareOnlyCommonFormat = Config["Presence"].get("UseCommonFormat")

    DefaultInatorDefaults = copy.deepcopy(DEFAULT_CONFIG)
    # Only DefaultInate Clients that will be used
    for Client in VALID_CLIENTS: 
        if Client not in ConfiguredClients: DefaultInatorDefaults["ClientConfig"].pop(Client)

    # Only Defaultinate Presence Format's that will be used
    for Format in [f"{FMT}Format" for FMT in VALID_CLIENTS] if CareOnlyCommonFormat else ["CommonFormat"] \
    + [f"{FMT}Format" for FMT in VALID_CLIENTS if FMT not in ConfiguredClients]: # Fancy expression I know :)
        DefaultInatorDefaults["Presence"].pop(Format)

    print(DefaultInatorDefaults)
    #DefaultInator(Config)

    SanitizedConf = Config

    return SanitizedConf

def ConfigLoader():
    ConfigFile = None
    DirtyConfig = {}
    
    try:
        ConfigFile = open("config.json", "r")
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

Config = ConfigLoader()

#print(Config)