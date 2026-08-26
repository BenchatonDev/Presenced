from RichPresenceBackend import RichPresenceBackend
from discord import Client, Activity, ActivityType, \
                    ActivityAssets, StatusDisplayType, \
                    ActivityTimestamps, ApplicationAsset
from asyncio import run_coroutine_threadsafe, create_task
from datetime import datetime, timezone
from threading import Thread

class DiscordPyBackend(RichPresenceBackend):

    def __init__(self, Config: dict):
        super().__init__(Config)
        self.Connection = Client()
        self.AppAssets = {}
        self._connecting = False

        @self.Connection.event
        async def on_ready():
            self.Connected = True
            self._connecting = False

        @self.Connection.event
        async def on_disconnect():
            self.Connected = False
            self._connecting = False

        return

    def _Connect(self):
        if self.Connected or self._connecting: return

        try:
            self._connecting = True
            Thread(target=self.Connection.run, args=(self.Config["DiscordPyToken"],), \
                   kwargs={"log_handler": None}, daemon=True).start()
        except:
            self.Connected = False
            self._connecting = False
            
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

            DisplayTypes = {
                1: StatusDisplayType.name,
                2: StatusDisplayType.details,
                3: StatusDisplayType.state
            }

            DisplayType = RPCData.get("DisplayType")
            DisplayType = DisplayTypes.get(DisplayType) if isinstance(DisplayType, int) \
                          else DisplayTypes.get(1)

            LargeImage = RPCData.get("LargeImage")
            LargeImage = self.AppAssets.get(LargeImage) \
                         if LargeImage in self.AppAssets \
                         else run_coroutine_threadsafe(self.Connection.proxy_external_application_assets(int(self.Config["AppID"]), \
                                                       LargeImage), self.Connection.loop).result()[0] if LargeImage else None

            SmallImage = RPCData.get("SmallImage")
            SmallImage = self.AppAssets.get(SmallImage) \
                         if SmallImage in self.AppAssets \
                         else run_coroutine_threadsafe(self.Connection.proxy_external_application_assets(int(self.Config["AppID"]), \
                                                       SmallImage), self.Connection.loop).result()[0] if SmallImage else None

            Name = RPCData.get("Name")
            Name = Name if isinstance(Name, str) else "{name-error}"

            StartTime = RPCData.get("StartTime")
            StartTime = StartTime if isinstance(StartTime, (int, float)) else 0
            
            PresencedRPC = Activity(
                # Setup Stuff
                type=ActivityType.playing,
                status_display_type=DisplayType,
                application_id=int(self.Config["AppID"]),

                # Actuall presence
                timestamps=ActivityTimestamps(start=datetime.fromtimestamp(StartTime, tz=timezone.utc)),
                name=Name,
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

        # Correction, not trivial at all, this thing is a nightmare
        # I can't fucking understand how to solve, god damn it
        if self.Connected and not self.Connection.is_closed():
            self.Connection.loop.call_soon_threadsafe(create_task, self.Connection.close())

        return
