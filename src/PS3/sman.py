from html.parser import HTMLParser

PS3Data = {}

class webMANParser(HTMLParser):
    checkTag = False
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
                print("Game ID part")

            # Title Name
            case {'href': url} if url.startswith('http://google.com/'):
                self.checkTag = True
                print("Game Name part")

            # Temps in Celsius
            case {'href': '/cpursx.ps3?up'}:
                self.checkTag = True
                print("Celcius Temp Part")

            # Temps in Fahrenheit
            case {'href': '/cpursx.ps3?dn'}:
                self.checkTag = True
                print("Fahrenheit Temp Part")

            # Fan Speed
            case {'href': '/cpursx.ps3?mode'}:
                self.checkTag = True
                print("Fan Speed Part")

            # Firmware version
            case {'href': '/setup.ps3'}:
                self.checkTag = True
                print("Firmware version Part")

    def handle_endtag(self, tag):
            if not self.checkTag: return
            if tag != 'a': self.ignoreChild -= 1; return
            
            self.checkTag = False

    def handle_data(self, data):
        if not self.checkTag or self.ignoreChild != 0: return

        print("Data     :", data)

parser = webMANParser()

with open("webMAN-page/webMAN.html", "r") as file:
    parser.feed(file.read())

print(PS3Data)