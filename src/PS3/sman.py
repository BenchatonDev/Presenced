from html.parser import HTMLParser

PS3Data = {}

class webMANParser(HTMLParser):
    checkTag = False

    def handle_starttag(self, tag, attrs):
        if tag != 'a': return
        attributes = dict(attrs)

        match attributes:
            case {'href': '/setup.ps3'}:
                self.checkTag = True
                print("WOOOOOO")

        print(attributes)

    def handle_endtag(self, tag):
            if self.checkTag:
                return
            
            self.inAtag = False

    def handle_data(self, data):
        if not self.inAtag:
            return
        print("Data     :", data)

parser = webMANParser()

with open("webMAN-page/webMAN.html", "r") as file:
    parser.feed(file.read())

print(PS3Data)