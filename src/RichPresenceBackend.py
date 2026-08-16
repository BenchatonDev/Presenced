# Skeleton to be implemented for any backend I want to support (Discord.py-self & PyPresence)

class RichPresenceBackend:

    def __init__(self, Config: dict):
        """ This Function just passes down the config to the class, the rest of the init willh ave to be
        handled differently per child class (RichPresenceBackend) since they're quite a bit different """
        self.Config = Config
        self.Connected = False

        return

    def _Connect(self):
        """ This Function will be called for the selected backend when it needs to connect to Discord which
        in our case is when an active client is detected and depending on the actual backend other reasons which
        would require the connection to be reset, supposed to be a private function used by the UpdatePresence()
        function, so don't call it outside the scope of that function (Probably can't harm if you do but don't) """

        return

    def UpdatePresence(self, RPCData: dict):
        """ This Function will be called for the selected backend when 1 or more ConsoleClient is active, it
        connects the backend to Discord if it has yet to do it and then sends the RPC data straight to Discord """

        return

    def Disconnect(self):
        """ This Function will be called for the selected backend when no ConsoleClient is active, it will
        disconnect the selected backend from Discord so the presence dissapears from your account profile """
        
        return