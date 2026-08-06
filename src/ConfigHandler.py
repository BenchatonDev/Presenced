from PS3.PS3Client import PS3Client
import json

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

Config = {}
# TM for TradeMark, Have fun naming your most private of functions with silly names too~
def SanitizerTM(config: dict):
    SanitizedConf = {}

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

    def TelePrompter():
        return

    def FormatSanitizerTM():
        return

    return SanitizedConf

def ConfigLoader():

    return
