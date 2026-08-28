from RichPresenceBackend import RichPresenceBackend
from discord import Client, Activity, ActivityType, \
                    ActivityAssets, StatusDisplayType, \
                    ActivityTimestamps, ApplicationAsset
from asyncio import run_coroutine_threadsafe
from datetime import datetime, timezone
from threading import Thread
from copy import deepcopy

class DiscordPyBackend(RichPresenceBackend):

    def __init__(self, Config: dict):
        super().__init__(Config)
        self.Connection = Client()

        self._ProxiedAssetCache : list[str] = []
        self._Connecting = False
        self._ActivityCache = {}
        self._AppAssets = {}

        return

    def _Connect(self):
        if self.Connected or self._Connecting: return

        if self.Connection is None or self.Connection.is_closed():
            self.Connection = Client()

        @self.Connection.event
        async def on_ready():
            self.Connected = True
            self._Connecting = False

            if not self._AppAssets:
                TmpAppAssets = await self.Connection.http.get_app_assets(int(self.Config["AppID"]))
                for Asset in TmpAppAssets:
                    if Asset.get("type") == 1:
                        self._AppAssets.setdefault(Asset.get("name"), Asset.get("id"))

            if self._RPCDataCache:
                # Kind of a stupid fix for a stupid mistake but ot works so eh
                Thread(target=self.UpdatePresence, args=(self._RPCDataCache,), daemon=True).start()

        @self.Connection.event
        async def on_disconnect():
            self.Connected = False
            self._Connecting = False

        try:
            self._Connecting = True
            Thread(target=self.Connection.run, args=(self.Config["DiscordPyToken"],), \
                   kwargs={"log_handler": None}, daemon=True).start()

        except:
            self.Connected = False
            self._Connecting = False
            
        return

    def UpdatePresence(self, RPCData: dict):
        if not self.Connected: self._Connect(); self._RPCDataCache = deepcopy(RPCData)

        if self.Connected:
            def AssetResolver(Asset: str):
                ResolvedAsset = None
    
                SupportedFileTypes = (".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif")
                UrlPrefixes = ("http://", "https://")
                
                if Asset in self._AppAssets:
                    ResolvedAsset = self._AppAssets.get(Asset)
    
                elif Asset.lower().startswith(UrlPrefixes) and Asset.lower().endswith(SupportedFileTypes):
                    AlreadyProxied = False
    
                    for Index in range(len(self._ProxiedAssetCache)):
                        if self._ProxiedAssetCache[Index].endswith(Asset.replace("://", "/", 1)): # Kinda holds on hopes and dreams lol
                            self._ProxiedAssetCache.insert(0, self._ProxiedAssetCache[Index])
                            self._ProxiedAssetCache.pop(Index + 1)
                            AlreadyProxied = True
    
                            break
                            
                    if not AlreadyProxied:
                        self._ProxiedAssetCache.insert(0, run_coroutine_threadsafe(self.Connection.proxy_external_application_assets(
                                                          int(self.Config["AppID"]), Asset), self.Connection.loop).result()[0])
    
                    if len(self._ProxiedAssetCache) > 30: # Very Arbitrary number
                        self._ProxiedAssetCache.pop()
    
                    ResolvedAsset = self._ProxiedAssetCache[0]
    
                return ResolvedAsset
            
            DisplayTypes = {
                1: StatusDisplayType.name,
                2: StatusDisplayType.details,
                3: StatusDisplayType.state
            }
    
            DisplayType = RPCData.get("DisplayType")
            DisplayType = DisplayTypes.get(DisplayType) if isinstance(DisplayType, int) \
                          else DisplayTypes.get(1)
            
            LargeImage = RPCData.get("LargeImage")
            LargeImage = AssetResolver(LargeImage) if isinstance(LargeImage, str) else None
    
            SmallImage = RPCData.get("SmallImage")
            SmallImage = AssetResolver(SmallImage) if isinstance(SmallImage, str) else None
    
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

        # I just needed to create a new client each time, took me
        # Way too long to figure out but it works now so Yipeee
        if self.Connected and not self.Connection.is_closed():
            run_coroutine_threadsafe(self.Connection.close(), self.Connection.loop)

        return
