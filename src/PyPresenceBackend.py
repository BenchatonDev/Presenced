from RichPresenceBackend import RichPresenceBackend
from pypresence.types import StatusDisplayType
from pypresence.presence import Presence

class PyPresenceBackend(RichPresenceBackend):

    def __init__(self, Config: dict):
        super().__init__(Config)
        self.Connection = Presence(Config["AppID"])

        return

    def _Connect(self):
        if self.Connected: return
        # Simplest function in the whole world tbh, might go
        # And get integrated in the UpdatePresence function
        # If it's also that simple in other backends, idk yet...

        try:
            self.Connection.connect()
            self.Connected = True
        except:
            pass

        return

    def UpdatePresence(self, RPCData: dict):
        # 99.999% Copy pasted from the first test run / implementation
        # Of the "full stack", because why change it ? All it needed is
        # To live in it's own subclass so I could handle other Backends
        # With ease, the implementation it self wasn't bad (imo, idk abt u)

        if not self.Connected: self._Connect()

        if self.Connected:

            DisplayTypes = {
                1: StatusDisplayType.NAME,
                2: StatusDisplayType.DETAILS,
                3: StatusDisplayType.STATE
            }

            DisplayType = RPCData.get("DisplayType")
            DisplayType = DisplayTypes.get(DisplayType) if isinstance(DisplayType, int) \
                          else DisplayTypes.get(1)

            try:
                self.Connection.update(
                    start=RPCData.get("StartTime"),
                    status_display_type=DisplayType,
                    name=RPCData.get("Name"),
                    details=RPCData.get("Details"),
                    state=RPCData.get("State"),
                    large_image=RPCData.get("LargeImage"),
                    large_text=RPCData.get("LargeText"),
                    small_image=RPCData.get("SmallImage"),
                    small_text=RPCData.get("SmallText")
                )

            except:
                self.Disconnect()

        return

    def Disconnect(self):
        # Damn that one was actually way more trivial than
        # The connection one, but this one I for sure can't
        # Integrate in the UpdatePresence function since it
        # Needs to be accessible Outside the internal scope
        # Of the class unlike the _Connect function. This
        # Might also just be the most useless comment inside
        # This project, at the time of writing at least >;(

        if self.Connected:
            self.Connection.close()
            self.Connected = False
        
        return