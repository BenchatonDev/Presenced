from html.parser import HTMLParser
import re

PS3Data = {'TitleID': '',
           'TitleName': 'PlayStation 1',
           'CPUTemp': {'C': '', 'F': ''},
           'RSXTemp': {'C': '', 'F': ''},
           'FanSpeed': '',
           'Firmware': ''}

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
            case {'href': '/games.ps3'}:
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
                if re.search("XMB", data.strip()) == 'XMB':
                    PS3Data['TitleName'] = 'XMB'
            case 8:
                PS3Data['FanSpeed'] = re.search("[0-9]+", data.strip()).group(0)
            case 9:
                PS3Data['Firmware'] = ' '.join(re.search("[0-9].[0-9]{2}(.*)", data.strip()).group(0).split(' ')[0:2])

parser = webMANParser()

with open("webMAN-page/webMAN.html", "r") as file:
    parser.feed(file.read())

print(PS3Data)