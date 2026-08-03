from bs4 import BeautifulSoup
import re

# TODO: Rewrite to use beautifulsoup

def SmanHTMLParser(html : str):
    SmanPage = BeautifulSoup(html, 'html.parser')
    SmanContent = SmanPage.find("div", id="content")

    if not SmanContent: return {}

    PS3Data = {'TitleID': '', 'TitleName': '', 'CPUTemp': {'C': '', 'F': ''},
               'RSXTemp': {'C': '', 'F': ''}, 'FanSpeed': '', 'Firmware': ''}

    # The /browser.ps3$slaunch href is only present when you're 
    # On the XMB so this is equivalent to an if InGame: statement
    if not SmanContent.find("a", href="/browser.ps3$slaunch"):
        # PS2 Classics completely unload WebMan and PS1 Classics don't create
        # this specific <a> tag, so this equivalent to an if PS3/PSP: statement
        if SmanContent.find("a", target="_blank"):
            PS3Data['TitleID'] = SmanContent.find("a", target="_blank").text

            # The TitleName <a> tag is always the next one to the title ID but can also
            # Be identified from it's href which always starts by "http://google.com"
            TitleName = SmanContent.find("a", target="_blank").find_next_sibling().text

            # All PS3 / PSP games have a version number that goes XX.XX, the regular
            # Expression below ignores the whole string exept the end checking if the
            # String ends in XX.XX, if it does we only keep the first part of it
            HasVersionNumber = re.search("(.+)[0-9]{2}.[0-9]{2}", TitleName)
            if HasVersionNumber:
                TitleName = HasVersionNumber.group(1).strip()

            PS3Data['TitleName'] = TitleName

        else:
            PS3Data['TitleID'] = "PS1"
            PS3Data['TitleName'] = "PlayStation Classics"

    else:
        PS3Data['TitleID'] = "XMB"
        PS3Data['TitleName'] = "XMB"

    # For the CPU and RSX temps we first isolate the IC's part from the <a> tag containing both
    # Then we use a second regular expression on the result to extract just the raw numbers
    TempStr = SmanContent.find("a", href="/cpursx.ps3?up").text
    PS3Data['CPUTemp']['C'] = re.search("[0-9]+" ,re.search("CPU(.+?)C", TempStr).group(0)).group(0)
    PS3Data['RSXTemp']['C'] = re.search("[0-9]+" ,re.search("RSX(.+?)C", TempStr).group(0)).group(0)

    TempStr = SmanContent.find("a", href="/cpursx.ps3?dn").text
    PS3Data['CPUTemp']['F'] = re.search("[0-9]+" ,re.search("CPU(.+?)F", TempStr).group(0)).group(0)
    PS3Data['RSXTemp']['F'] = re.search("[0-9]+" ,re.search("RSX(.+?)F", TempStr).group(0)).group(0)

    # For fanspeed we just extract the number directly since it's the only one in the char sequence
    TempStr = SmanContent.find("a", href="/cpursx.ps3?mode").text
    PS3Data['FanSpeed'] = re.search("[0-9]+", TempStr).group(0)

    # Firmware version is annoying, the string we are looking for is the first
    # Segment of the sequence before the "PSID" string so we extract that, then we look
    # For the first occurence of the firmware version which is alway X.XX formated,
    # We only keep what comes after this sequence (including it self) and separate
    # The string at each space char, since the firmware type comes right after the
    # Version number we can then just join back the first 2 indexes of the split string
    # To get the exact firmware version and type formated like this: X.XX CEX / DEX
    TempStr = SmanContent.find("a", href="/setup.ps3").text
    PS3Data['Firmware'] = ' '.join(re.search("[0-9].[0-9]{2}(.*)", re.search("(.+?)PSID(.+?)", TempStr).group(1)).group(0).split(' ')[0:2])

    return PS3Data
