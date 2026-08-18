# Hello, this is the Main file in case someone is looking for it, I know it's not standar naming
# But like, I felt the name Main.py didn't fit in with the rest of my file names so that's that :)
from argparse import ArgumentParser
from pathlib import Path; import sys
from time import sleep, monotonic
from concurrent.futures import ThreadPoolExecutor

from ConfigHandler import ConfigHandler
from ConsoleClient import Clients, ActiveClients
from RichPresenceBackend import RichPresenceBackend
from PyPresenceBackend import PyPresenceBackend
from DiscordPyBackend import DiscordPyBackend

# Man, naming a function "Main" with a capital "M" feels wrong but not doing it isn't
# Fitting for my a capitalisation aesthetic :sob: <- Imagine the emoji here please
def MainFunction():
    # CLI arguments their shall be, I'm feeling fancy on this project :DD
    ArgumentInator = ArgumentParser()

    # Lambda is such a cool keyword tbh, I love this thing
    ArgumentInator.add_argument("-c", "--config-file", help="Loads the config file from the provided path", type=lambda ConfigPath : Path(ConfigPath) \
                                if Path(ConfigPath).suffix.lower() == ".json" else ArgumentInator.error("The config file must be a json file"))
    ArgumentInator.add_argument("-u", "--update-config", help="Adds any missing entries in the config file and then exits", action="store_true")

    Arguments = ArgumentInator.parse_args()

    # You've got to give credit where it's not due, this name makes absolutely no sense
    # And I fucking LOVE that, god am I great at making unmaintainable code, truly gifted
    def WhereAmIQuestionMark():
        if getattr(sys, 'frozen', False):
            return Path(sys.executable).resolve().parent
        else:
            return Path(__file__).resolve().parent

    ConfigFilePath = WhereAmIQuestionMark() if not Arguments.config_file else Arguments.config_file.resolve()

    Config = ConfigHandler(str(ConfigFilePath))
    Backend : RichPresenceBackend

    if Arguments.update_config: print("Finished, exiting..."); return

    if Config["General"].get("PyPresenceBackend"):
        Backend = PyPresenceBackend(Config["General"])
    else:
        print("The Discordpy backend needs work, you can enable it by uncomenting" \
              + "line 46 in Presenced.py, very much not finalized, don't use")
        return
        # Backend = DiscordPyBackend(Config["General"])

    while True:
        PollTime = monotonic()
        with ThreadPoolExecutor() as Executor:
            for Client in Clients:
                Executor.submit(Client.pingConsole)
        PollDeltaTime = monotonic() - PollTime

        if ActiveClients:
            Backend.UpdatePresence(ActiveClients[0].getRPCData())

        else:
            Backend.Disconnect()

        sleep(Config["General"].get("PollInterval") - PollDeltaTime if PollDeltaTime < Config["General"].get("PollInterval") else 0)

# This try is litterally just here for aesthetic reasons lol
# No really, I just HATE the error spam when you press CTRL+C
# To exit the script + doesn't feel "Production Ready" when it
# Just spews useless error messages (Also I really don't like saying
# "Production Ready", feels too profesional / corpo speak Eeeeeeew)
try:
    MainFunction()

except KeyboardInterrupt:

    print("\nPresenced will exit, Have a nice day !")
