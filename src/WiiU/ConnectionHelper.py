from socket import (socket, AF_INET, SOCK_DGRAM)
from time import sleep; from json import (loads, JSONDecodeError)

def WiiUConnector(WiiUPort: int, Retries: int = 5, Delay: int = 0) -> dict:
    Connection = socket(AF_INET, SOCK_DGRAM)
    Connection.settimeout(1)
    Bound = False

    while Retries > 0:
        if not Bound:
            try:
                Connection.bind(("", WiiUPort))
                Bound = True

            except:
                sleep(Delay)
                Retries -= 1
                continue

        try:
            # They used 1024 buffer sized in the StackOverflow page I read so I kept it that way
            UDPData, Address = Connection.recvfrom(1024)
            if UDPData and len(UDPData) > 0:
                UDPData = UDPData.decode('utf-8', errors='ignore')
                try:
                    WiiUData = loads(UDPData)
                                
                    if WiiUData.get("sender") == "Wii U":                 
                        WiiUData.pop("sender")
                        WiiUData.pop("ctrls")
                        WiiUData.pop("dst")

                        # Useless step but I like my capitalized names
                        # And my naming scheme better :))
                        FormatedData = {
                            "LongTitleName": WiiUData.get("long"),
                            "ShortTitleName": WiiUData.get("name"),
                            "NetworkID": WiiUData.get("nnid") if WiiUData.get("img") else "{anon-user}",
                            "Network": WiiUData.get("img") if WiiUData.get("img") else "uk",
                            "Time": WiiUData.get("time"),
                        }

                        return FormatedData
                    
                    else:
                        raise Exception
                                    
                except JSONDecodeError:
                    sleep(Delay)
                    Retries -= 1
                    continue

            else:
                raise Exception

        except:
            sleep(Delay)
            Retries -= 1
            continue
    
    return {}
