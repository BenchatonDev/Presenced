from PS3.PS3Client import PS3Client
from os import path
import json

# Look a constant, in this economy ???
DEFAULT_CONFIG = {
    "General": {
        "AppID": "DISCORD_APP_ID_HERE",
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

    def AppIDChecker():
        return

    def UserTokenChecker():
        return

    def TelePrompter():
        return

    def FormatSanitizerTM():
        return

    return SanitizedConf

def ConfigLoader():

    return