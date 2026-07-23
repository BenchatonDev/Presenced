from html.parser import HTMLParser

PS3Data = {'TitleID': '',
           'TitleName': 'XMB',
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

            # Fan Speed
            case {'href': '/cpursx.ps3?mode'}:
                self.checkTag = True
                self.valueIndex = 7

            # Firmware version
            case {'href': '/setup.ps3'}:
                self.checkTag = True
                self.valueIndex = 8

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
                PS3Data['TitleName'] = data.strip()
            case 3:
                PS3Data['CPUTemp']['C'] = data.strip().removeprefix('CPU: ').removesuffix('°C')
                self.valueIndex += 1
            case 4:
                PS3Data['RSXTemp']['C'] = data.strip().removeprefix('RSX: ').removesuffix('°C')
            case 5:
                PS3Data['CPUTemp']['F'] = data.strip().removeprefix('CPU: ').removesuffix('°F')
                self.valueIndex += 1
            case 6:
                PS3Data['RSXTemp']['F'] = data.strip().removeprefix('RSX: ').removesuffix('°F')
            case 7:
                PS3Data['FanSpeed'] = data.strip()
            case 8:
                PS3Data['Firmware'] = data.strip()

parser = webMANParser()

with open("webMAN-page/webMAN.html", "r") as file:
    parser.feed(file.read())

print(PS3Data)