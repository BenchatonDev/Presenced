# Config File Documentation

The configuration for Presenced is represeted as a dictionary which allows it to easely be read or saved to a json file, the configuration as two main parts, the "General" part which stores settings that affect the whole program and the "Presence" part which stores settings in relation to how the Rich Presence will look on your discord profile. Additionally if a field preset in the `{Presence}Format` can't poll it's data from the `ConsoleClient` it will use strings set in a dictionary of the corresponding `ConsoleClient`'s name.

## General

- **AppID** *[STR]* : A Discord app ID created from the [Discord Developer Portal](https://discord.com/developers/applications/)
- **DiscordPyToken** *[STR]* : A Discord user token, used to log into the account if the `Discord.py` backend is used (Not the default)
- **PollInterval** *[INT]* : The time in seconds between console pings, manages how fast Presenced checks consoles for activity and updates relating data (Current game etc)
- **ConsoleClients** *[STR]* | *[LIST]*: Which of the supported ConsoleClients to use (i.e. which consoles do you want to use with Presenced).
  <details>
    <summary>Click to see field options</summary>

    - *all* (***Default***) **➤** Use all supported ConsoleClients
    - *[]* **➤** List of client names, supported list members are `"PS3"`

  </details>
- **PyPresenceBackend** *[BOOL]* : Wether or not to use `pyPresence` as the Rich Presence backend, `True` by default

## Presence

- **UseCommonFormat** *[BOOL]* : Wether or not to use the same Presence config for every configured `ConsoleClient` (Layout / How fields are filled)
- **ResetTimeOnAppChange** *[BOOL]* : Wether to display time since the currently in use `ConsoleClient` started being active or since the last Application Change (i.e. switching from game A to game B)
- <a id="common-format"></a> **CommonFormat** *[DICT]* : Decides how fields are filled for every configured `ConsoleClient`
  <details>
    <summary>Click to see subfields</summary>

  - **AppName** *[STR]* : What gets displayed after the `"Playing"` text on Discord
    <details>
        <summary>Click to see field options</summary>

      - *console_name* (***Default***) **➤** Display's the currently active `ConsoleClient`'s name (i.e. `"PlayStation 3"`)
      - *app_name* **➤** Display's the currently running app's name (i.e. `"XMB"`)
      - *{customstring}* **➤** In the case you don't input any of the above the value of the field will be displayed, empty will fallback to the default value
    
    </details>

  - **Details1** *[STR]* : First line below the **AppName** when looking at the Presence details
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Display's the currently active `ConsoleClient`'s name (i.e. `"PlayStation 3"`)
      - *network_name* **➤** Display's the in use online network's name determined by the `ConsoleClient`'s name (i.e. `"Pretendo Network"`), this option might use a predefined string if there is no way to poll it from the console (i.e. on PS3)
      - *app_name* (***Default***) **➤** Display's the currently running app's name (i.e. `"XMB"`)
      - *info_firmware* **➤** Display's the console's Firmware version (i.e. `"4.90 CEX"`), this option might use a predefined string if there is no way to poll it from the console (i.e. on Wii U)
      - *info_network* **➤** Display's the user's online network ID (i.e. `"PNID : Benchatooo"`), this option might use a predefined string if there is no way to poll it from the console (i.e. on PS3)
      - *info_hardware* **➤** Display's hardware information about the console (i.e. `"Cell: 65°C | RSX: 73°C"`) this option might use a predefined string if there is no way to poll it from the console (i.e. on Wii U)
      - *{customstring}* **➤** In the case you don't input any of the above the value of the field will be displayed, empty means nothing to be displayed
    
    </details>

  - **Details2** *[STR]* : Second line below the **AppName** when looking at the Presence details
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Display's the currently active `ConsoleClient`'s name (i.e. `"PlayStation 3"`)
      - *network_name* **➤** Display's the in use online network's name determined by the `ConsoleClient`'s name (i.e. `"Pretendo Network"`), this option might use a predefined string if there is no way to poll it from the console (i.e. on PS3)
      - *app_name* **➤** Display's the currently running app's name (i.e. `"XMB"`)
      - *info_firmware* **➤** Display's the console's Firmware version (i.e. `"4.90 CEX"`), this option might use a predefined string if there is no way to poll it from the console (i.e. on Wii U)
      - *info_network* (***Default***) **➤** Display's the user's online network ID (i.e. `"PNID : Benchatooo"`), this option might use a predefined string if there is no way to poll it from the console (i.e. on PS3)
      - *info_hardware* **➤** Display's hardware information about the console (i.e. `"Cell: 65°C | RSX: 73°C"`) this option might use a predefined string if there is no way to poll it from the console (i.e. on Wii U)
      - *{customstring}* **➤** In the case you don't input any of the above the value of the field will be displayed, empty means nothing to be displayed

    </details>

  - **ImageBigText** *[STR]* : The text that appears when hovering over the big image
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Display's the currently active `ConsoleClient`'s name (i.e. `"PlayStation 3"`)
      - *network_name* **➤** Display's the in use online network's name determined by the `ConsoleClient`'s name (i.e. `"Pretendo Network"`), this option might use a predefined string if there is no way to poll it from the console (i.e. on PS3)
      - *app_name* (***Default***) **➤** Display's the currently running app's name (i.e. `"XMB"`)
      - *info_firmware* **➤** Display's the console's Firmware version (i.e. `"4.90 CEX"`), this option might use a predefined string if there is no way to poll it from the console (i.e. on Wii U)
      - *info_network* **➤** Display's the user's online network ID (i.e. `"PNID : Benchatooo"`), this option might use a predefined string if there is no way to poll it from the console (i.e. on PS3)
      - *info_hardware* **➤** Display's hardware information about the console (i.e. `"Cell: 65°C | RSX: 73°C"`) this option might use a predefined string if there is no way to poll it from the console (i.e. on Wii U)
      - *{customstring}* **➤** In the case you don't input any of the above the value of the field will be displayed, empty means nothing to be displayed
    
    </details>

  - **ImageBigType** *[STR]* : The big image to show on the presence
  
    <details>
        <summary>Click to see field options</summary>

      - *image_app* (***Default***) **➤** Uses the running app's icon determined by the `ConsoleClient`
      - *image_console* **➤** Uses the console's logo determined by the currently displayed `ConsoleClient`
      - *image_network* **➤** Uses the currently displayed `ConsoleClient` to display the appropriate Multiplayer Network icon (i.e. Pretendo Network on Wii U), this option might use a predefined icon if there is no way to poll it from the console (i.e. on PS3)
      - *{customurl}* **➤** In the case you don't input any of the above we'll try to use the string as an image url, if it's not one (i.e. empty string) then no image shall be displayed
    
    </details>

  - **ImageSmallText** *[STR]* : The text that appears when hovering over the small image
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Display's the currently active `ConsoleClient`'s name (i.e. `"PlayStation 3"`)
      - *network_name* **➤** Display's the in use online network's name determined by the `ConsoleClient`'s name (i.e. `"Pretendo Network"`), this option might use a predefined string if there is no way to poll it from the console (i.e. on PS3)
      - *app_name* **➤** Display's the currently running app's name (i.e. `"XMB"`)
      - *info_firmware* (***Default***) **➤** Display's the console's Firmware version (i.e. `"4.90 CEX"`), this option might use a predefined string if there is no way to poll it from the console (i.e. on Wii U)
      - *info_network* **➤** Display's the user's online network ID (i.e. `"PNID : Benchatooo"`), this option might use a predefined string if there is no way to poll it from the console (i.e. on PS3)
      - *info_hardware* **➤** Display's hardware information about the console (i.e. `"Cell: 65°C | RSX: 73°C"`) this option might use a predefined string if there is no way to poll it from the console (i.e. on Wii U)
      -  *{customstring}* **➤** In the case you don't input any of the above the value of the field will be displayed, empty means nothing to be displayed
    
    </details>

  - **ImageSmallType** *[STR]* : The small image to show on the presence
  
    <details>
        <summary>Click to see field options</summary>

      - *image_app* **➤** Uses the running app's icon determined by the `ConsoleClient`
      - *image_console* (***Default***) **➤** Uses the console's logo determined by the currently displayed `ConsoleClient`
      - *image_network* **➤** Uses the currently displayed `ConsoleClient` to display the appropriate Multiplayer Network icon (i.e. Pretendo Network on Wii U), this option might use a predefined icon if there is no way to poll it from the console (i.e. on PS3)
      - *{customurl}* **➤** In the case you don't input any of the above we'll try to use the string as an image url, if it's not one (i.e. empty string) then no image shall be displayed
    
    </details>

  </details>

- **PS3Format** *[DICT]* : Decides how fields are filled for the PS3 `ConsoleClient`, same fields as [CommonFormat](#common-format)
  <details>
    <summary>Click to see subfields</summary>

  - **AppName** *[STR]* : What gets displayed after the `"Playing"` text on Discord
    <details>
        <summary>Click to see field options</summary>

      - *console_name* (***Default***) **➤** Display's the currently active `ConsoleClient`'s name (i.e. `"PlayStation 3"`)
      - *app_name* **➤** Display's the currently running app's name (i.e. `"XMB"`)
      - *{customstring}* **➤** In the case you don't input any of the above the value of the field will be displayed, empty will fallback to the default value of *`console_name`*
    
    </details>

  - **Details1** *[STR]* : First line below the **AppName** when looking at the Presence details
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Display's the currently active `ConsoleClient`'s name (i.e. `"PlayStation 3"`)
      - *network_name* **➤** Display's the in use online network's name determined by the `ConsoleClient`'s name (i.e. `"Playstation Network"`), Network Full Name is configured manualy as it can't be easely be polled from WebMAN
      - *app_name* (***Default***) **➤** Display's the currently running app's name (i.e. `"XMB"`)
      - *info_firmware* **➤** Display's the console's Firmware version (i.e. `"4.90 CEX"`)
      - *info_network* **➤** Display's the user's online network ID (i.e. `"PSN : Benchatooo"`), Network Name and Network ID are configured manualy as they can't be easely be polled from WebMAN
      - *info_hardware* **➤** Display's hardware information about the console (i.e. `"Cell: 65°C | RSX: 73°C"`)
      - *{customstring}* **➤** In the case you don't input any of the above the value of the field will be displayed, empty means nothing to be displayed
    
    </details>

  - **Details2** *[STR]* : Second line below the **AppName** when looking at the Presence details
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Display's the currently active `ConsoleClient`'s name (i.e. `"PlayStation 3"`)
      - *network_name* **➤** Display's the in use online network's name determined by the `ConsoleClient`'s name (i.e. `"Playstation Network"`), Network Full Name is configured manualy as it can't be easely be polled from WebMAN
      - *app_name* **➤** Display's the currently running app's name (i.e. `"XMB"`)
      - *info_firmware* **➤** Display's the console's Firmware version (i.e. `"4.90 CEX"`)
      - *info_network* (***Default***) **➤** Display's the user's online network ID (i.e. `"PSN : Benchatooo"`), Network Name and Network ID are configured manualy as they can't be easely be polled from WebMAN
      - *info_hardware* **➤** Display's hardware information about the console (i.e. `"Cell: 65°C | RSX: 73°C"`)
      - *{customstring}* **➤** In the case you don't input any of the above the value of the field will be displayed, empty means nothing to be displayed

    </details>

  - **ImageBigText** *[STR]* : The text that appears when hovering over the big image
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Display's the currently active `ConsoleClient`'s name (i.e. `"PlayStation 3"`)
      - *network_name* **➤** Display's the in use online network's name determined by the `ConsoleClient`'s name (i.e. `"Playstation Network"`), Network Full Name is configured manualy as it can't be easely be polled from WebMAN
      - *app_name* (***Default***) **➤** Display's the currently running app's name (i.e. `"XMB"`)
      - *info_firmware* **➤** Display's the console's Firmware version (i.e. `"4.90 CEX"`)
      - *info_network* **➤** Display's the user's online network ID (i.e. `"PSN : Benchatooo"`), Network Name and Network ID are configured manualy as they can't be easely be polled from WebMAN
      - *info_hardware* **➤** Display's hardware information about the console (i.e. `"Cell: 65°C | RSX: 73°C"`)
      - *{customstring}* **➤** In the case you don't input any of the above the value of the field will be displayed, empty means nothing to be displayed
    
    </details>

  - **ImageBigType** *[STR]* : The big image to show on the presence
  
    <details>
        <summary>Click to see field options</summary>

      - *image_app* (***Default***) **➤** Uses the running app's icon determined by the `ConsoleClient`
      - *image_console* **➤** Uses the console's logo determined by the currently displayed `ConsoleClient`
      - *image_network* **➤** Uses the currently displayed `ConsoleClient` to display the appropriate Multiplayer Network icon (i.e. the PSN logo), Network icon has to be configured manualy as the in use multiplayer online network can't be easely be polled from WebMAN
      - *{customurl}* **➤** In the case you don't input any of the above we'll try to use the string as an image url, if it's not one (i.e. empty string) then no image shall be displayed
    
    </details>

  - **ImageSmallText** *[STR]* : The text that appears when hovering over the small image
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Display's the currently active `ConsoleClient`'s name (i.e. `"PlayStation 3"`)
      - *network_name* **➤** Display's the in use online network's name determined by the `ConsoleClient`'s name (i.e. `"Playstation Network"`), Network Full Name is configured manualy as it can't be easely be polled from WebMAN
      - *app_name* **➤** Display's the currently running app's name (i.e. `"XMB"`)
      - *info_firmware* (***Default***) **➤** Display's the console's Firmware version (i.e. `"4.90 CEX"`)
      - *info_network* **➤** Display's the user's online network ID (i.e. `"PSN : Benchatooo"`), Network Name and Network ID are configured manualy as they can't be easely be polled from WebMAN
      - *info_hardware* **➤** Display's hardware information about the console (i.e. `"Cell: 65°C | RSX: 73°C"`)
      - *{customstring}* **➤** In the case you don't input any of the above the value of the field will be displayed, empty means nothing to be displayed
    
    </details>

  - **ImageSmallType** *[STR]* : The small image to show on the presence
  
    <details>
        <summary>Click to see field options</summary>

      - *image_app* **➤** Uses the running app's icon determined by the `ConsoleClient`
      - *image_console* (***Default***) **➤** Uses the console's logo determined by the currently displayed `ConsoleClient`
      - *image_network* **➤** Uses the currently displayed `ConsoleClient` to display the appropriate Multiplayer Network icon (i.e. the PSN logo), Network icon has to be configured manualy as the in use multiplayer online network can't be easely be polled from WebMAN
      - *{customurl}* **➤** In the case you don't input any of the above we'll try to use the string as an image url, if it's not one (i.e. empty string) then no image shall be displayed
    
    </details>

  </details>

- **WiiUFormat** *[DICT]* : Decides how fields are filled for the Wii U `ConsoleClient`, same fields as [CommonFormat](#common-format)
  <details>
    <summary>Click to see subfields</summary>

  - **AppName** *[STR]* : What gets displayed after the `"Playing"` text on Discord
    <details>
        <summary>Click to see field options</summary>

      - *console_name* (***Default***) **➤** Display's the currently active `ConsoleClient`'s name (i.e. `"Wii U"`)
      - *app_name* **➤** Display's the currently running app's name (i.e. `"Wii U Menu"`)
      - *{customstring}* **➤** In the case you don't input any of the above the value of the field will be displayed, empty will fallback to the default value of *`console_name`*
    
    </details>

  - **Details1** *[STR]* : First line below the **AppName** when looking at the Presence details
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Display's the currently active `ConsoleClient`'s name (i.e. `"Wii U"`)
      - *network_name* **➤** Display's the in use online network's name determined by the `ConsoleClient`'s name (i.e. `"Pretendo Network"`)
      - *app_name* (***Default***) **➤** Display's the currently running app's name (i.e. `"Wii U Menu"`)
      - *info_firmware* **➤** Display's the console's Firmware version (i.e. `"5.5.5E"`), Firmware version can't be polled from the Discord RPC Aroma plugin meaning it's manually configured
      - *info_network* **➤** Display's the user's online network ID (i.e. `"PNID : Benchatooo"`)
      - *info_hardware* **➤** Display's hardware information about the console (i.e. `"IBM Espresso | AMD Latte"`), temperature data can't be polled from the Discord RPC Aroma plugin meaning it uses manually configured strings
      - *{customstring}* **➤** In the case you don't input any of the above the value of the field will be displayed, empty means nothing to be displayed
    
    </details>

  - **Details2** *[STR]* : Second line below the **AppName** when looking at the Presence details
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Display's the currently active `ConsoleClient`'s name (i.e. `"Wii U"`)
      - *network_name* **➤** Display's the in use online network's name determined by the `ConsoleClient`'s name (i.e. `"Pretendo Network"`)
      - *app_name* **➤** Display's the currently running app's name (i.e. `"Wii U Menu"`)
      - *info_firmware* **➤** Display's the console's Firmware version (i.e. `"5.5.5E"`), Firmware version can't be polled from the Discord RPC Aroma plugin meaning it's manually configured
      - *info_network* (***Default***) **➤** Display's the user's online network ID (i.e. `"PNID : Benchatooo"`)
      - *info_hardware* **➤** Display's hardware information about the console (i.e. `"IBM Espresso | AMD Latte"`), temperature data can't be polled from the Discord RPC Aroma plugin meaning it uses manually configured strings
      - *{customstring}* **➤** In the case you don't input any of the above the value of the field will be displayed, empty means nothing to be displayed

    </details>

  - **ImageBigText** *[STR]* : The text that appears when hovering over the big image
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Display's the currently active `ConsoleClient`'s name (i.e. `"Wii U"`)
      - *network_name* **➤** Display's the in use online network's name determined by the `ConsoleClient`'s name (i.e. `"Pretendo Network"`)
      - *app_name* (***Default***) **➤** Display's the currently running app's name (i.e. `"Wii U Menu"`)
      - *info_firmware* **➤** Display's the console's Firmware version (i.e. `"5.5.5E"`), Firmware version can't be polled from the Discord RPC Aroma plugin meaning it's manually configured
      - *info_network* **➤** Display's the user's online network ID (i.e. `"PNID : Benchatooo"`)
      - *info_hardware* **➤** Display's hardware information about the console (i.e. `"IBM Espresso | AMD Latte"`), temperature data can't be polled from the Discord RPC Aroma plugin meaning it uses manually configured strings
      - *{customstring}* **➤** In the case you don't input any of the above the value of the field will be displayed, empty means nothing to be displayed
    
    </details>

  - **ImageBigType** *[STR]* : The big image to show on the presence
  
    <details>
        <summary>Click to see field options</summary>

      - *image_app* (***Default***) **➤** Uses the running app's icon determined by the `ConsoleClient`
      - *image_console* **➤** Uses the console's logo determined by the currently displayed `ConsoleClient`
      - *image_network* **➤** Uses the currently displayed `ConsoleClient` to display the appropriate Multiplayer Network icon (i.e. Pretendo Network)
      - *{customurl}* **➤** In the case you don't input any of the above we'll try to use the string as an image url, if it's not one (i.e. empty string) then no image shall be displayed
    
    </details>

  - **ImageSmallText** *[STR]* : The text that appears when hovering over the small image
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Display's the currently active `ConsoleClient`'s name (i.e. `"Wii U"`)
      - *network_name* **➤** Display's the in use online network's name determined by the `ConsoleClient`'s name (i.e. `"Pretendo Network"`)
      - *app_name* **➤** Display's the currently running app's name (i.e. `"Wii U Menu"`)
      - *info_firmware* (***Default***) **➤** Display's the console's Firmware version (i.e. `"5.5.5E"`), Firmware version can't be polled from the Discord RPC Aroma plugin meaning it's manually configured
      - *info_network* **➤** Display's the user's online network ID (i.e. `"PNID : Benchatooo"`)
      - *info_hardware* **➤** Display's hardware information about the console (i.e. `"IBM Espresso | AMD Latte"`), temperature data can't be polled from the Discord RPC Aroma plugin meaning it uses manually configured strings
      - *{customstring}* **➤** In the case you don't input any of the above the value of the field will be displayed, empty means nothing to be displayed
    
    </details>

  - **ImageSmallType** *[STR]* : The small image to show on the presence
  
    <details>
        <summary>Click to see field options</summary>

      - *image_app* **➤** Uses the running app's icon determined by the `ConsoleClient`
      - *image_console* (***Default***) **➤** Uses the console's logo determined by the currently displayed `ConsoleClient`
      - *image_network* **➤** Uses the currently displayed `ConsoleClient` to display the appropriate Multiplayer Network icon (i.e. Pretendo Network)
      - *{customurl}* **➤** In the case you don't input any of the above we'll try to use the string as an image url, if it's not one (i.e. empty string) then no image shall be displayed
    
    </details>

  </details>

## PS3

- **NetworkName** *[STR]* : Acronym of the in use Multiplayer Network for the *`info_network`* preset (i.e. `"PSN"`), if not set will default to `"PSN"`
- **NetworkNameFull** *[STR]* : Full name of the in use Multiplayer Network for the *`network_name`* preset (i.e. `"PlayStation Network"`), if not set will default to `"PlayStation Network"`
- **NetworkID** *[STR]* : Your Multiplayer Network username for the *`info_network`* preset (i.e. `"Benchatooo"`), if not set will default to `"{anon-user}"`
- **UseCelsius** *[BOOL]* : Wether to use Celsius or Fahrenheits in the *`info_hardware`* preset, if not set will default to `True`

## Wii U

- **FirmwareVer** *[STR]* : CafeOS version number for the *`info_firmware`* preset, can be found by going into the settings (i.e. `"5.5.5E"`), if not set will default to `"{unkown-ver}"`
- **HWInfoText** *[STR]* : Information you're Wii U for the *`info_hardware`* preset (i.e. CPU/GPU name ➤ `"IBM Espresso | AMD Latte"`, or board revision ➤ `"WUP-50"`, modchip if you want `"de_fuse"`, anything hardware related you can come up with), if not set will default to `"IBM Espresso | AMD Latte"` for consistence with the PS3's `"Cell: {temp}°{C/F} | RSX: {temp}°{C/F}"`