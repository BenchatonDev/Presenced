# Config File Documentation

The configuration for Presenced is represented as a dictionary which allows it to easily be read or saved to a JSON file. The configuration has two main parts: the "General" part, which stores settings that affect the whole program, and the "Presence" part, which stores settings in relation to how the Rich Presence will look on your Discord profile. Additionally, if a field present in `{Presence}Format` cannot poll its data from the `ConsoleClient`, it will use strings set in a dictionary inside `ClientConfig` under the corresponding `ConsoleClient`'s name. Everything is case sensitive in the config so be careful.

## General

- **AppID** *[STR]* : A Discord app ID created from the [Discord Developer Portal](https://discord.com/developers/applications/), changing it isn't recommended since Presenced internally relies on some assets published on the default AppID, the option is there and accessible if you know what you are getting into
- **DiscordPyToken** *[STR]* : A Discord user token, used to log into the account if the `Discord.py` backend is used (Not the default)
- **PollInterval** *[INT]* : The time in seconds between console pings; manages how fast Presenced checks consoles for activity and updates related data (Current game, etc.)
- **ConsoleClients** *[STR]* | *[LIST]*: Which of the supported ConsoleClients to use (i.e., which consoles you want to use with Presenced).
  <details>
    <summary>Click to see field options</summary>

    - *all* (***Default***) **➤** Use all supported ConsoleClients
    - *[]* **➤** List of client names; supported list members are `"PS3"` and `"WiiU"`

  </details>
- **PyPresenceBackend** *[BOOL]* : Whether or not to use `pyPresence` as the Rich Presence backend (`True` by default)

## Presence

- **UseCommonFormat** *[BOOL]* : Whether or not to use the same Presence config for every configured `ConsoleClient` (Layout / How fields are filled)
- **ResetTimeOnAppChange** *[BOOL]* : Whether to display time since the currently used `ConsoleClient` started being active or since the last Application Change (i.e., switching from game A to game B)
- <a id="common-format"></a> **CommonFormat** *[DICT]* : Decides how fields are filled for every configured `ConsoleClient`
  <details>
    <summary>Click to see subfields</summary>

  - **DisplayType** *[INT]* : What gets displayed after the `"Playing"` text on Discord
    <details>
        <summary>Click to see field options</summary>

      - *1* **➤** Displays the content of **AppName** after the `"Playing"` text on Discord
      - *2* (***Default***) **➤** Displays the content of **Details1** after the `"Playing"` text on Discord
      - *3* **➤** Displays the content of **Details2** after the `"Playing"` text on Discord
      - *{customvalue}* **➤** In case none of the above are provided the default value will be applied
    
    </details>

  - **AppName** *[STR]* : The header / bold line of the Presence details
    <details>
        <summary>Click to see field options</summary>

      - *console_name* (***Default***) **➤** Displays the currently active `ConsoleClient`'s name (i.e., `"PlayStation 3"`)
      - *app_name* **➤** Displays the currently running app's name (i.e., `"XMB"`)
      - *{customstring}* **➤** In case you don't input any of the above, the value of the field will be displayed; an empty value will fall back to the default value
    
    </details>

  - **Details1** *[STR]* : First line below the **AppName** when looking at the Presence details
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Displays the currently active `ConsoleClient`'s name (i.e., `"PlayStation 3"`)
      - *network_name* **➤** Displays the online network name in use, determined by the `ConsoleClient`'s name (i.e., `"Pretendo Network"`); this option might use a predefined string if there is no way to poll it from the console (i.e., on PS3)
      - *app_name* (***Default***) **➤** Displays the currently running app's name (i.e., `"XMB"`)
      - *info_firmware* **➤** Displays the console's firmware version (i.e., `"4.90 CEX"`); this option might use a predefined string if there is no way to poll it from the console (i.e., on Wii U)
      - *info_network* **➤** Displays the user's online network ID (i.e., `"PNID : Benchatooo"`); this option might use a predefined string if there is no way to poll it from the console (i.e., on PS3)
      - *info_hardware* **➤** Displays hardware information about the console (i.e., `"Cell: 65°C | RSX: 73°C"`); this option might use a predefined string if there is no way to poll it from the console (i.e., on Wii U)
      - *{customstring}* **➤** In case you don't input any of the above, the value of the field will be displayed; an empty value means nothing will be displayed
    
    </details>

  - **Details2** *[STR]* : Second line below the **AppName** when looking at the Presence details
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Displays the currently active `ConsoleClient`'s name (i.e., `"PlayStation 3"`)
      - *network_name* **➤** Displays the online network name in use, determined by the `ConsoleClient`'s name (i.e., `"Pretendo Network"`); this option might use a predefined string if there is no way to poll it from the console (i.e., on PS3)
      - *app_name* **➤** Displays the currently running app's name (i.e., `"XMB"`)
      - *info_firmware* **➤** Displays the console's firmware version (i.e., `"4.90 CEX"`); this option might use a predefined string if there is no way to poll it from the console (i.e., on Wii U)
      - *info_network* (***Default***) **➤** Displays the user's online network ID (i.e., `"PNID : Benchatooo"`); this option might use a predefined string if there is no way to poll it from the console (i.e., on PS3)
      - *info_hardware* **➤** Displays hardware information about the console (i.e., `"Cell: 65°C | RSX: 73°C"`); this option might use a predefined string if there is no way to poll it from the console (i.e., on Wii U)
      - *{customstring}* **➤** In case you don't input any of the above, the value of the field will be displayed; an empty value means nothing will be displayed

    </details>

  - **ImageBigText** *[STR]* : The text that appears when hovering over the big image
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Displays the currently active `ConsoleClient`'s name (i.e., `"PlayStation 3"`)
      - *network_name* **➤** Displays the online network name in use, determined by the `ConsoleClient`'s name (i.e., `"Pretendo Network"`); this option might use a predefined string if there is no way to poll it from the console (i.e., on PS3)
      - *app_name* (***Default***) **➤** Displays the currently running app's name (i.e., `"XMB"`)
      - *info_firmware* **➤** Displays the console's firmware version (i.e., `"4.90 CEX"`); this option might use a predefined string if there is no way to poll it from the console (i.e., on Wii U)
      - *info_network* **➤** Displays the user's online network ID (i.e., `"PNID : Benchatooo"`); this option might use a predefined string if there is no way to poll it from the console (i.e., on PS3)
      - *info_hardware* **➤** Displays hardware information about the console (i.e., `"Cell: 65°C | RSX: 73°C"`); this option might use a predefined string if there is no way to poll it from the console (i.e., on Wii U)
      - *{customstring}* **➤** In case you don't input any of the above, the value of the field will be displayed; an empty value means nothing will be displayed
    
    </details>

  - **ImageBigType** *[STR]* : The big image to show on the presence
  
    <details>
        <summary>Click to see field options</summary>

      - *image_app* (***Default***) **➤** Uses the running app's icon determined by the `ConsoleClient`
      - *image_console* **➤** Uses the console's logo determined by the currently displayed `ConsoleClient`
      - *image_network* **➤** Uses the currently displayed `ConsoleClient` to display the appropriate Multiplayer Network icon (i.e., Pretendo Network on Wii U); this option might use a predefined icon if there is no way to poll it from the console (i.e., on PS3)
      - *{customurl}* **➤** In case you don't input any of the above, we'll try to use the string as an image URL; if it is not one (i.e., an empty string), then no image shall be displayed
    
    </details>

  - **ImageSmallText** *[STR]* : The text that appears when hovering over the small image
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Displays the currently active `ConsoleClient`'s name (i.e., `"PlayStation 3"`)
      - *network_name* **➤** Displays the online network name in use, determined by the `ConsoleClient`'s name (i.e., `"Pretendo Network"`); this option might use a predefined string if there is no way to poll it from the console (i.e., on PS3)
      - *app_name* **➤** Displays the currently running app's name (i.e., `"XMB"`)
      - *info_firmware* (***Default***) **➤** Displays the console's firmware version (i.e., `"4.90 CEX"`); this option might use a predefined string if there is no way to poll it from the console (i.e., on Wii U)
      - *info_network* **➤** Displays the user's online network ID (i.e., `"PNID : Benchatooo"`); this option might use a predefined string if there is no way to poll it from the console (i.e., on PS3)
      - *info_hardware* **➤** Displays hardware information about the console (i.e., `"Cell: 65°C | RSX: 73°C"`); this option might use a predefined string if there is no way to poll it from the console (i.e., on Wii U)
      - *{customstring}* **➤** In case you don't input any of the above, the value of the field will be displayed; an empty value means nothing will be displayed
    
    </details>

  - **ImageSmallType** *[STR]* : The small image to show on the presence
  
    <details>
        <summary>Click to see field options</summary>

      - *image_app* **➤** Uses the running app's icon determined by the `ConsoleClient`
      - *image_console* (***Default***) **➤** Uses the console's logo determined by the currently displayed `ConsoleClient`
      - *image_network* **➤** Uses the currently displayed `ConsoleClient` to display the appropriate Multiplayer Network icon (i.e., Pretendo Network on Wii U); this option might use a predefined icon if there is no way to poll it from the console (i.e., on PS3)
      - *{customurl}* **➤** In case you don't input any of the above, we'll try to use the string as an image URL; if it is not one (i.e., an empty string), then no image shall be displayed
    
    </details>

  </details>

- **PS3Format** *[DICT]* : Decides how fields are filled for the PS3 `ConsoleClient`, same fields as [CommonFormat](#common-format)
  <details>
    <summary>Click to see subfields</summary>

  - **DisplayType** *[INT]* : What gets displayed after the `"Playing"` text on Discord
    <details>
        <summary>Click to see field options</summary>

      - *1* **➤** Displays the content of **AppName** after the `"Playing"` text on Discord
      - *2* (***Default***) **➤** Displays the content of **Details1** after the `"Playing"` text on Discord
      - *3* **➤** Displays the content of **Details2** after the `"Playing"` text on Discord
      - *{customvalue}* **➤** In case none of the above are provided the default value will be applied
    
    </details>

  - **AppName** *[STR]* : What gets displayed after the `"Playing"` text on Discord
    <details>
        <summary>Click to see field options</summary>

      - *console_name* (***Default***) **➤** Displays the currently active `ConsoleClient`'s name (i.e., `"PlayStation 3"`)
      - *app_name* **➤** Displays the currently running app's name (i.e., `"XMB"`)
      - *{customstring}* **➤** In case you don't input any of the above, the value of the field will be displayed; an empty value will fall back to the default value
    
    </details>

  - **Details1** *[STR]* : First line below the **AppName** when looking at the Presence details
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Displays the currently active `ConsoleClient`'s name (i.e., `"PlayStation 3"`)
      - *network_name* **➤** Displays the online network name in use, determined by the `ConsoleClient`'s name (i.e., `"PlayStation Network"`); Network Full Name is configured manually as it cannot easily be polled from WebMAN
      - *app_name* (***Default***) **➤** Displays the currently running app's name (i.e., `"XMB"`)
      - *info_firmware* **➤** Displays the console's firmware version (i.e., `"4.90 CEX"`)
      - *info_network* **➤** Displays the user's online network ID (i.e., `"PSN : Benchatooo"`); Network Name and Network ID are configured manually as they cannot easily be polled from WebMAN
      - *info_hardware* **➤** Displays hardware information about the console (i.e., `"Cell: 65°C | RSX: 73°C"`)
      - *{customstring}* **➤** In case you don't input any of the above, the value of the field will be displayed; an empty value means nothing will be displayed
    
    </details>

  - **Details2** *[STR]* : Second line below the **AppName** when looking at the Presence details
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Displays the currently active `ConsoleClient`'s name (i.e., `"PlayStation 3"`)
      - *network_name* **➤** Displays the online network name in use, determined by the `ConsoleClient`'s name (i.e., `"PlayStation Network"`); Network Full Name is configured manually as it cannot easily be polled from WebMAN
      - *app_name* **➤** Displays the currently running app's name (i.e., `"XMB"`)
      - *info_firmware* **➤** Displays the console's firmware version (i.e., `"4.90 CEX"`)
      - *info_network* (***Default***) **➤** Displays the user's online network ID (i.e., `"PSN : Benchatooo"`); Network Name and Network ID are configured manually as they cannot easily be polled from WebMAN
      - *info_hardware* **➤** Displays hardware information about the console (i.e., `"Cell: 65°C | RSX: 73°C"`)
      - *{customstring}* **➤** In case you don't input any of the above, the value of the field will be displayed; an empty value means nothing will be displayed

    </details>

  - **ImageBigText** *[STR]* : The text that appears when hovering over the big image
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Displays the currently active `ConsoleClient`'s name (i.e., `"PlayStation 3"`)
      - *network_name* **➤** Displays the online network name in use, determined by the `ConsoleClient`'s name (i.e., `"PlayStation Network"`); Network Full Name is configured manually as it cannot easily be polled from WebMAN
      - *app_name* (***Default***) **➤** Displays the currently running app's name (i.e., `"XMB"`)
      - *info_firmware* **➤** Displays the console's firmware version (i.e., `"4.90 CEX"`)
      - *info_network* **➤** Displays the user's online network ID (i.e., `"PSN : Benchatooo"`); Network Name and Network ID are configured manually as they cannot easily be polled from WebMAN
      - *info_hardware* **➤** Displays hardware information about the console (i.e., `"Cell: 65°C | RSX: 73°C"`)
      - *{customstring}* **➤** In case you don't input any of the above, the value of the field will be displayed; an empty value means nothing will be displayed
    
    </details>

  - **ImageBigType** *[STR]* : The big image to show on the presence
  
    <details>
        <summary>Click to see field options</summary>

      - *image_app* (***Default***) **➤** Uses the running app's icon determined by the `ConsoleClient`
      - *image_console* **➤** Uses the console's logo determined by the currently displayed `ConsoleClient`
      - *image_network* **➤** Uses the currently displayed `ConsoleClient` to display the appropriate Multiplayer Network icon (i.e., the PSN logo); Network icon has to be configured manually as the multiplayer online network in use cannot easily be polled from WebMAN
      - *{customurl}* **➤** In case you don't input any of the above, we'll try to use the string as an image URL; if it is not one (i.e., an empty string), then no image shall be displayed
    
    </details>

  - **ImageSmallText** *[STR]* : The text that appears when hovering over the small image
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Displays the currently active `ConsoleClient`'s name (i.e., `"PlayStation 3"`)
      - *network_name* **➤** Displays the online network name in use, determined by the `ConsoleClient`'s name (i.e., `"PlayStation Network"`); Network Full Name is configured manually as it cannot easily be polled from WebMAN
      - *app_name* **➤** Displays the currently running app's name (i.e., `"XMB"`)
      - *info_firmware* (***Default***) **➤** Displays the console's firmware version (i.e., `"4.90 CEX"`)
      - *info_network* **➤** Displays the user's online network ID (i.e., `"PSN : Benchatooo"`); Network Name and Network ID are configured manually as they cannot easily be polled from WebMAN
      - *info_hardware* **➤** Displays hardware information about the console (i.e., `"Cell: 65°C | RSX: 73°C"`)
      - *{customstring}* **➤** In case you don't input any of the above, the value of the field will be displayed; an empty value means nothing will be displayed
    
    </details>

  - **ImageSmallType** *[STR]* : The small image to show on the presence
  
    <details>
        <summary>Click to see field options</summary>

      - *image_app* **➤** Uses the running app's icon determined by the `ConsoleClient`
      - *image_console* (***Default***) **➤** Uses the console's logo determined by the currently displayed `ConsoleClient`
      - *image_network* **➤** Uses the currently displayed `ConsoleClient` to display the appropriate Multiplayer Network icon (i.e., the PSN logo); Network icon has to be configured manually as the multiplayer online network in use cannot easily be polled from WebMAN
      - *{customurl}* **➤** In case you don't input any of the above, we'll try to use the string as an image URL; if it is not one (i.e., an empty string), then no image shall be displayed
    
    </details>

  </details>

- **WiiUFormat** *[DICT]* : Decides how fields are filled for the Wii U `ConsoleClient`, same fields as [CommonFormat](#common-format)
  <details>
    <summary>Click to see subfields</summary>

  - **DisplayType** *[INT]* : What gets displayed after the `"Playing"` text on Discord
    <details>
        <summary>Click to see field options</summary>

      - *1* **➤** Displays the content of **AppName** after the `"Playing"` text on Discord
      - *2* (***Default***) **➤** Displays the content of **Details1** after the `"Playing"` text on Discord
      - *3* **➤** Displays the content of **Details2** after the `"Playing"` text on Discord
      - *{customvalue}* **➤** In case none of the above are provided the default value will be applied
    
    </details>

  - **AppName** *[STR]* : What gets displayed after the `"Playing"` text on Discord
    <details>
        <summary>Click to see field options</summary>

      - *console_name* (***Default***) **➤** Displays the currently active `ConsoleClient`'s name (i.e., `"Wii U"`)
      - *app_name* **➤** Displays the currently running app's name (i.e., `"Wii U Menu"`)
      - *{customstring}* **➤** In case you don't input any of the above, the value of the field will be displayed; an empty value will fall back to the default value
    
    </details>

  - **Details1** *[STR]* : First line below the **AppName** when looking at the Presence details
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Displays the currently active `ConsoleClient`'s name (i.e., `"Wii U"`)
      - *network_name* **➤** Displays the online network name in use, determined by the `ConsoleClient`'s name (i.e., `"Pretendo Network"`)
      - *app_name* (***Default***) **➤** Displays the currently running app's name (i.e., `"Wii U Menu"`)
      - *info_firmware* **➤** Displays the console's firmware version (i.e., `"5.5.5E"`); firmware version cannot be polled from the Discord RPC Aroma plugin, meaning it is manually configured
      - *info_network* **➤** Displays the user's online network ID (i.e., `"PNID : Benchatooo"`)
      - *info_hardware* **➤** Displays hardware information about the console (i.e., `"IBM Espresso | AMD Latte"`); temperature data cannot be polled from the Discord RPC Aroma plugin, meaning it uses manually configured strings
      - *{customstring}* **➤** In case you don't input any of the above, the value of the field will be displayed; an empty value means nothing will be displayed
    
    </details>

  - **Details2** *[STR]* : Second line below the **AppName** when looking at the Presence details
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Displays the currently active `ConsoleClient`'s name (i.e., `"Wii U"`)
      - *network_name* **➤** Displays the online network name in use, determined by the `ConsoleClient`'s name (i.e., `"Pretendo Network"`)
      - *app_name* **➤** Displays the currently running app's name (i.e., `"Wii U Menu"`)
      - *info_firmware* **➤** Displays the console's firmware version (i.e., `"5.5.5E"`); firmware version cannot be polled from the Discord RPC Aroma plugin, meaning it is manually configured
      - *info_network* (***Default***) **➤** Displays the user's online network ID (i.e., `"PNID : Benchatooo"`)
      - *info_hardware* **➤** Displays hardware information about the console (i.e., `"IBM Espresso | AMD Latte"`); temperature data cannot be polled from the Discord RPC Aroma plugin, meaning it uses manually configured strings
      - *{customstring}* **➤** In case you don't input any of the above, the value of the field will be displayed; an empty value means nothing will be displayed

    </details>

  - **ImageBigText** *[STR]* : The text that appears when hovering over the big image
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Displays the currently active `ConsoleClient`'s name (i.e., `"Wii U"`)
      - *network_name* **➤** Displays the online network name in use, determined by the `ConsoleClient`'s name (i.e., `"Pretendo Network"`)
      - *app_name* (***Default***) **➤** Displays the currently running app's name (i.e., `"Wii U Menu"`)
      - *info_firmware* **➤** Displays the console's firmware version (i.e., `"5.5.5E"`); firmware version cannot be polled from the Discord RPC Aroma plugin, meaning it is manually configured
      - *info_network* **➤** Displays the user's online network ID (i.e., `"PNID : Benchatooo"`)
      - *info_hardware* **➤** Displays hardware information about the console (i.e., `"IBM Espresso | AMD Latte"`); temperature data cannot be polled from the Discord RPC Aroma plugin, meaning it uses manually configured strings
      - *{customstring}* **➤** In case you don't input any of the above, the value of the field will be displayed; an empty value means nothing will be displayed
    
    </details>

  - **ImageBigType** *[STR]* : The big image to show on the presence
  
    <details>
        <summary>Click to see field options</summary>

      - *image_app* (***Default***) **➤** Uses the running app's icon determined by the `ConsoleClient`
      - *image_console* **➤** Uses the console's logo determined by the currently displayed `ConsoleClient`
      - *image_network* **➤** Uses the currently displayed `ConsoleClient` to display the appropriate Multiplayer Network icon (i.e., Pretendo Network)
      - *{customurl}* **➤** In case you don't input any of the above, we'll try to use the string as an image URL; if it is not one (i.e., an empty string), then no image shall be displayed
    
    </details>

  - **ImageSmallText** *[STR]* : The text that appears when hovering over the small image
  
    <details>
        <summary>Click to see field options</summary>

      - *console_name* **➤** Displays the currently active `ConsoleClient`'s name (i.e., `"Wii U"`)
      - *network_name* **➤** Displays the online network name in use, determined by the `ConsoleClient`'s name (i.e., `"Pretendo Network"`)
      - *app_name* **➤** Displays the currently running app's name (i.e., `"Wii U Menu"`)
      - *info_firmware* (***Default***) **➤** Displays the console's firmware version (i.e., `"5.5.5E"`); firmware version cannot be polled from the Discord RPC Aroma plugin, meaning it is manually configured
      - *info_network* **➤** Displays the user's online network ID (i.e., `"PNID : Benchatooo"`)
      - *info_hardware* **➤** Displays hardware information about the console (i.e., `"IBM Espresso | AMD Latte"`); temperature data cannot be polled from the Discord RPC Aroma plugin, meaning it uses manually configured strings
      - *{customstring}* **➤** In case you don't input any of the above, the value of the field will be displayed; an empty value means nothing will be displayed
    
    </details>

  - **ImageSmallType** *[STR]* : The small image to show on the presence
  
    <details>
        <summary>Click to see field options</summary>

      - *image_app* **➤** Uses the running app's icon determined by the `ConsoleClient`
      - *image_console* (***Default***) **➤** Uses the console's logo determined by the currently displayed `ConsoleClient`
      - *image_network* **➤** Uses the currently displayed `ConsoleClient` to display the appropriate Multiplayer Network icon (i.e., Pretendo Network)
      - *{customurl}* **➤** In case you don't input any of the above, we'll try to use the string as an image URL; if it is not one (i.e., an empty string), then no image shall be displayed
    
    </details>

  </details>

## ClientConfig

- **PS3** *[DICT]* : Special configuration for the *`PS3`* `ConsoleClient`
  <details open>
    <summary>Click to see client configuration options</summary>

  - **PS3Address** *[STR]* : Your PS3's IP address, required for the `ConsoleClient` to work, an invalid IP will just make the `ConsoleClient` probe the void but wont break anything
  - **NetworkName** *[STR]* : Acronym of the in-use Multiplayer Network for the *`info_network`* preset (i.e., `"PSN"`); if not set, will default to `"PSN"`
  - **NetworkNameFull** *[STR]* : Full name of the in-use Multiplayer Network for the *`network_name`* preset (i.e., `"PlayStation Network"`); if not set, will default to `"PlayStation Network"`
  - **NetworkID** *[STR]* : Your Multiplayer Network username for the *`info_network`* preset (i.e., `"Benchatooo"`); if not set, will default to `"{anon-user}"`
  - **UseCelsius** *[BOOL]* : Whether to use Celsius or Fahrenheit in the *`info_hardware`* preset; if not set, will default to `True`
  </details>

- **Wii U** *[DICT]* : Special configuration for the *`WiiU`* `ConsoleClient`
  <details open>
    <summary>Click to see client configuration options</summary>

  - **UDPPort** *[STR]* : UDP port used by the *Rich Presence U* Aroma plugin, required for the `ConsoleClient` to work, an invalid port will just make the `ConsoleClient` probe the void but wont break anything
  - **FirmwareVer** *[STR]* : CafeOS version number for the *`info_firmware`* preset; can be found by going into settings (i.e., `"5.5.5E"`). If not set, will default to `"{unknown-ver}"`
  - **HWInfoText** *[STR]* : Information about your Wii U for the *`info_hardware`* preset (i.e., CPU/GPU name ➤ `"IBM Espresso | AMD Latte"`, board revision ➤ `"WUP-50"`, modchip if you want ➤ `"de_fuse"`, or anything hardware-related you can come up with); if not set, will default to `"IBM Espresso | AMD Latte"` for consistency with the PS3's `"Cell: {temp}°{C/F} | RSX: {temp}°{C/F}"`
  </details>