from PresencedIcons import getIcon
from requests import get
from json import loads

IconDBRepo = "BenchatonDev/PresencedPS3-DB"
NamesDB = {}
IconDB = {}

def PullRepo():
    global IconDB, NamesDB

    if NamesDB and IconDB: return

    try:
        DB = get(f"https://raw.githubusercontent.com/{IconDBRepo}/main/titleids.json")
        NamesDB = loads(DB.text)

        DB2 = get(f"https://raw.githubusercontent.com/{IconDBRepo}/main/icons.json")
        IconDB = loads(DB2.text)
        
    except:
        pass

    return

def getAppIcon(TitleID: str):
    PullRepo()

    # This is really just for one liner glory, absolutely useless change compared to the last version's code
    return f"https://raw.githubusercontent.com/{IconDBRepo}/main/icons/{IconDB.get(NamesDB.get(TitleID))}" \
           if TitleID in NamesDB and NamesDB.get(TitleID) in IconDB else getIcon("Unknown")