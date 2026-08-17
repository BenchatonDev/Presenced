from RichPresenceBackend import RichPresenceBackend
from discord import Client, Activity, ActivityType, \
                    ActivityAssets, StatusDisplayType, \
                    ActivityTimestamps, ApplicationAsset
from asyncio import run; from threading import Thread
from datetime import datetime, timezone

class DiscordPyBackend(RichPresenceBackend):

    def __init__(self, Config: dict):
        super().__init__(Config)
        self.Connection = Client()

        @self.Connection.event
        async def on_ready():
            self.Connected = True
            self._connecting = False

        return

    def _Connect(self):
        if self.Connected and not self._connecting: return

        try:
            self._connecting = True
            Thread(target=self.Connection.run, args=(self.Config["DiscordPyToken"],), \
                   kwargs={"log_handler": None, "reconnect": True}, daemon=True).start() # type: ignore
        except:
            pass

        return

    def UpdatePresence(self, RPCData: dict):
        if not self.Connected: self._Connect()

        if self.Connected:

            DisplayType : StatusDisplayType = StatusDisplayType.name # type: ignore

            match RPCData.get("DisplayType"):
                case 1:
                    DisplayType = StatusDisplayType.name # type: ignore
                case 2:
                    DisplayType = StatusDisplayType.details
                case 3:
                    DisplayType = StatusDisplayType.state

            PresencedRPC = Activity(
                # Setup Stuff
                type=ActivityType.playing,
                status_display_type=DisplayType,
                application_id=int(self.Config["AppID"]),

                # Actuall presence
                timestamps=ActivityTimestamps(start=datetime.fromtimestamp(RPCData.get("StartTime"), tz=timezone.utc)), # type: ignore
                name=RPCData.get("Name"), # type: ignore
                details=RPCData.get("Details"),
                state=RPCData.get("State"),
                assets=ActivityAssets( # Documentation wants to proxy external assets but I don't
                    large_image=RPCData.get("LargeImage"), # Know how to cleanly handle that with internal assets
                    large_text=RPCData.get("State"), # I need to read further.
                    small_image=RPCData.get("SmallImage"),
                    small_text=RPCData.get("SmallText"),
                )
            )

            run(self.Connection.change_presence(activity=PresencedRPC))

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
            run(self.Connection.close())
            self.Connected = False
        
        return