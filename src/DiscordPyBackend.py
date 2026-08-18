from RichPresenceBackend import RichPresenceBackend
from discord import Client, Activity, ActivityType, \
                    ActivityAssets, StatusDisplayType, \
                    ActivityTimestamps, ApplicationAsset
from asyncio import run_coroutine_threadsafe; from threading import Thread
from datetime import datetime, timezone

class DiscordPyBackend(RichPresenceBackend):

    def __init__(self, Config: dict):
        super().__init__(Config)
        self.Connection = Client()
        self.AppAssets = {}

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
            if not self.AppAssets:
                TmpAppAssets = run_coroutine_threadsafe(self.Connection.http.get_app_assets(int(self.Config["AppID"])), \
                                                        self.Connection.loop).result()
                for Asset in TmpAppAssets:
                    if Asset.get("type") == 1:
                        self.AppAssets.setdefault(Asset.get("name"), Asset.get("id"))

            DisplayType : StatusDisplayType = StatusDisplayType.name # type: ignore

            match RPCData.get("DisplayType"):
                case 1:
                    DisplayType = StatusDisplayType.name # type: ignore
                case 2:
                    DisplayType = StatusDisplayType.details
                case 3:
                    DisplayType = StatusDisplayType.state

            LargeImage = self.AppAssets.get(RPCData.get("LargeImage")) \
                         if RPCData.get("LargeImage") in self.AppAssets else RPCData.get("LargeImage")

            SmallImage = self.AppAssets.get(RPCData.get("SmallImage")) \
                         if RPCData.get("SmallImage") in self.AppAssets else RPCData.get("SmallImage")
    
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
                assets=ActivityAssets(
                    large_image=LargeImage,
                    large_text=RPCData.get("LargeText"),
                    small_image=SmallImage,
                    small_text=RPCData.get("SmallText"),
                )
            )

            run_coroutine_threadsafe(self.Connection.change_presence(activity=PresencedRPC), self.Connection.loop)

        return

    def Disconnect(self):
        # Damn that one was actually way more trivial than
        # The connection one, but this one I for sure can't
        # Integrate in the UpdatePresence function since it
        # Needs to be accessible Outside the internal scope
        # Of the class unlike the _Connect function. This
        # Might also just be the most useless comment inside
        # This project, at the time of writing at least >;(

        if self.Connected and not self.Connection.is_closed():
            run_coroutine_threadsafe(self.Connection.close(), self.Connection.loop)
            self.Connected = False

        return