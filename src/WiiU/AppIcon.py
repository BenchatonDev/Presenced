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

    # This is really just for one liner glory, absolutely useless change compared to the last version's code
    return f"https://raw.githubusercontent.com/{IconDBRepo}/main/icons/{IconDB.get(LongTitleName)}" \
           if LongTitleName in IconDB else "unknown"