# Most of this code is from https://github.com/FlamingNineteen/RichPresenceWUPS/blob/main/discord-script.py
from requests import get
from json import loads

IconDBRepo = "BenchatonDev/RichPresenceWUPS-DB"
IconDB = {}

def PullRepo():
    global IconDB

    if IconDB: return

    try:
        DB = get(f"https://raw.githubusercontent.com/{IconDBRepo}/main/titles.json")
        IconDB = loads(DB.text)

    except:
        pass

    return

def getIcon(LongTitleName: str):
    PullRepo()

    if LongTitleName in IconDB:
        return f"https://raw.githubusercontent.com/{IconDBRepo}/main/icons/{IconDB.get(LongTitleName)}"

    else:
        return "unknown"