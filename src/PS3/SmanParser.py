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
    # then we use a second regular expression on the result to extract just the raw numbers
    TempStr = SmanContent.find("a", href="/cpursx.ps3?up").text
    PS3Data['CPUTemp']['C'] = re.search("[0-9]+" ,re.search("CPU(.+?)C", TempStr).group(0)).group(0)
    PS3Data['RSXTemp']['C'] = re.search("[0-9]+" ,re.search("RSX(.+?)C", TempStr).group(0)).group(0)

    TempStr = SmanContent.find("a", href="/cpursx.ps3?dn").text
    PS3Data['CPUTemp']['F'] = re.search("[0-9]+" ,re.search("CPU(.+?)F", TempStr).group(0)).group(0)
    PS3Data['RSXTemp']['F'] = re.search("[0-9]+" ,re.search("RSX(.+?)F", TempStr).group(0)).group(0)

    return PS3Data

with open("webMAN-page/webMAN.html", "r") as file:
    print(SmanHTMLParser(file.read()))

"""

class webMANParser(HTMLParser):
    checkTag = False
    valueIndex = 0
    ignoreChild = 0

    def handle_starttag(self, tag, attrs):
        if self.checkTag and tag != 'a': self.ignoreChild += 1;return
        if tag != 'a': return

        # Here we'll check for distinctive attributes of the tags we want
        # to retrieve data from i.e. CPU temps, current game, etc
        attributes = dict(attrs)

        match attributes:
            # Title ID
            case {'target': '_blank'}:
                self.checkTag = True
                self.valueIndex = 1

            # Title Name
            case {'href': url} if url.startswith('http://google.com/'):
                self.checkTag = True
                self.valueIndex = 2

            # Temps in Celsius
            case {'href': '/cpursx.ps3?up'}:
                self.checkTag = True
                self.valueIndex = 3

            # Temps in Fahrenheit
            case {'href': '/cpursx.ps3?dn'}:
                self.checkTag = True
                self.valueIndex = 5

            # On the XMB ?
            case {'href': '/browser.ps3$slaunch'}:
                self.checkTag = True
                self.valueIndex = 7

            # Fan Speed
            case {'href': '/cpursx.ps3?mode'}:
                self.checkTag = True
                self.valueIndex = 8

            # Firmware version
            case {'href': '/setup.ps3'}:
                self.checkTag = True
                self.valueIndex = 9

    def handle_endtag(self, tag):
            if not self.checkTag: return
            if tag != 'a': self.ignoreChild -= 1; return
            
            self.checkTag = False
            self.valueIndex = 0

    def handle_data(self, data):
        if not self.checkTag or self.ignoreChild != 0 or not data.strip(): return

        match self.valueIndex:
            case 1:
                PS3Data['TitleID'] = data.strip()
            case 2:
                PS3Data['TitleName'] = re.search("(.+)[0-9]{2}.[0-9]{2}", data.strip()).group(1).strip() if re.search("(.+)[0-9]{2}.[0-9]{2}", data.strip()) != None else data.strip()
            case 3:
                PS3Data['CPUTemp']['C'] = re.search("[0-9]+", data.strip()).group(0)
                self.valueIndex += 1
            case 4:
                PS3Data['RSXTemp']['C'] = re.search("[0-9]+", data.strip()).group(0)
            case 5:
                PS3Data['CPUTemp']['F'] = re.search("[0-9]+", data.strip()).group(0)
                self.valueIndex += 1
            case 6:
                PS3Data['RSXTemp']['F'] = re.search("[0-9]+", data.strip()).group(0)
            case 7:
                PS3Data['TitleName'] = 'XMB'
            case 8:
                PS3Data['FanSpeed'] = re.search("[0-9]+", data.strip()).group(0)
            case 9:
                PS3Data['Firmware'] = ' '.join(re.search("[0-9].[0-9]{2}(.*)", data.strip()).group(0).split(' ')[0:2])
"""