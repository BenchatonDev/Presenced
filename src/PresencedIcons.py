# Hello there, this is where the static icons used by Presenced are stored, think Multiplayer Network icons
# Console icons or fallback icons, it's all there in this centralised file. This is to make changing them
# For all the other scripts which use them much much less painful to do. HAPPY CUSTOMIZING ! :DD

# Use either asset names from the Discord developer portal or image urls
def getIcon(IconName: str):
    Icon = "unknown" # The default will always correspond to the placeholder icon

    Icons = {
        # Console Icons
        "WiiU": "wiiu",
        "PS3": "ps3",

        # Network Icons
        "PlayStationN": "playstation",
        "NintendoN": "nintendo",
        "PretendoN": "pretendo",
    }

    if IconName in Icons: Icon = Icons.get(IconName)

    return Icon