<h1 align="center">
    <br>
    <img src="repoIcon.png" alt="App Logo" height="100"/>
    <br>
    <img src="https://img.shields.io/github/license/BenchatonDev/Presenced"/>
    <br>
    A configurable Rich Presence for homebrewed consoles
</h1>

Presenced is an hopefully flexible and customizable Discord Rich Presence app for homebrewed consoles writen in python. Originally created to run on an headless computer as self-bot, it's not a self-bot by default since such things are against the Discord TOS and use at your own risk even if the risk of your account being banned is low it's not 0, which means you needd, by default, to have a Discord client opened alongside Presenced to use it.

# TODO:
- Make the `"{Client}Format"` fields in the Default config auto generare at runtime
- Make the `SanitizerTM()` run faster (Not necessary per say since it runs once at the start end never again + I have no idea how to do that)
- Game icons on PS3, no really
- Better quality appAssets
- Decouple static icons from the default AppID (I already have a system to do that but I'd like better assets first)

# Requirements:

Presenced relies on `discord.py-self`, `pypresence`, `bs4`, and `requests`. Install them by running
```bash
pip install -r requirements.txt
```

# Usage :

- Standard usage
```bash
python Presenced.py
```

- Get all available CLI arguments
```bash
python Presenced.py --help
```
```bash
python Presenced.py -h
```

- Custom config file path
```bash
python Presenced.py --config-file [FilePath]
```
```bash
python Presenced.py -c [FilePath]
```

- Run a config file check and add missing fields
```bash
python Presenced.py --update-config
```
```bash
python Presenced.py -u
```

# Configuration

The way the config file is structured and what values you can put in each field is documented in the [CONFIG.MD](CONFIG.MD) file. Bellow is the most minimal config you can use to customize your onboarding experience, Presenced will automagicly add all the required fields according to these settings, you can of course customize Presence much more by reading the Config documentation.
```json
{
  "General": {
    "PollInterval": 10,
    "ConsoleClients": "all",
    "PyPresenceBackend": true
  },
  "Presence": {
    "UseCommonFormat": true,
    "ResetTimeOnAppChange": true,
  }
}
```

# Game Icon databases

- [`WiiU`](https://github.com/FlamingNineteen/RichPresenceWUPS-DB): Feel free to comtribute to the Game icon database over at [Flaming's repo](https://github.com/FlamingNineteen/RichPresenceWUPS-DB)

# Acknowledgements
- [Zorua98741](https://github.com/zorua98741) Inspiration for this project, and WebManMOD's `CPURSX.PS3` scraping idea
- [FlamingNineteen](https://github.com/FlamingNineteen) His plugin is used to connect to the Wii U as well as his icon database
