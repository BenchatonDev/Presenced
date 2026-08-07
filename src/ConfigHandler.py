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
            "PS3Address": "X.X.X.X",
            "NetworkName": "PSN",
            "NetworkNameFull": "PlayStation Network",
            "NetworkID": "{anon-user}",
            "UseCelsius": True
        },
        "WiiU": {
            "WiiUAddress": "X.X.X.X",
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
    DefaultInatorDefaults = {}
    CareOnlyCommonFormat = DEFAULT_CONFIG["Presence"].get("UseCommonFormat")

    def DefaultInator(DirtySegment: dict, InatorDefaultSegment: dict, GlobalDefaultSegment: dict):
        DefaultInated = {}
        ChangedKeys = []

        # DEFAULTINATE !!!
        for Key, GlobalDefault in GlobalDefaultSegment.items():
            InatorDefault = InatorDefaultSegment.get(Key)
            
            if Key in DirtySegment:
                Value = DirtySegment[Key]
                
                if InatorDefault is not None and type(Value) is not type(InatorDefault):
                    Value = InatorDefault
                    ChangedKeys.append(Key)

            else:
                Value = InatorDefault
                ChangedKeys.append(Key)

            if isinstance(Value, dict) and isinstance(InatorDefault, dict) and isinstance(GlobalDefault, dict):
                SubDefaultInated, SubChangedKeys = DefaultInator(Value, InatorDefault, GlobalDefault)
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

    def TelePrompter(ChangedVars: list, Config: dict):
        def RecursivePrompt(VariableName: str, VariableType: type):
            VariableValue = None

            return VariableValue

        if ChangedVars:
            TelePrompterMsg = "Configuration Variables were added / or changed because they were either missing or wrong in the config file,"
            TelePrompterMsg += "\nif any should be set by you, we'll make sure to ask for a value, in any other case the process is automatic"
            print(TelePrompterMsg)

            for Var in ChangedVars:

                match Var:
                    # If the whole general tag got changed, I safely assume
                    # Your using the default general config, very very safely lmao
                    case "General":
                        print("shit")
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

    # Only Defaultinate Presence Formats that will be used
    for Format in [f"{FMT}Format" for FMT in VALID_CLIENTS] if CareOnlyCommonFormat else ["CommonFormat"] \
    + [f"{FMT}Format" for FMT in VALID_CLIENTS if FMT not in ConfiguredClients]: # Fancy expression I know :)
        DefaultInatorDefaults["Presence"].pop(Format)

    SanitizedConf, ChangedVars = DefaultInator(Config, DefaultInatorDefaults, DEFAULT_CONFIG)

    SanitizedConf = TelePrompter(ChangedVars, SanitizedConf)

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

print(Config)