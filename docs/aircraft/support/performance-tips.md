---
title: Performance Tips
description: Learn how to maximize performance and minimize resource usage in Microsoft Flight Simulator 2020.
---

# Performance Tips
---

!!! warning "Disclaimer"

    This guide is for a simulator wide performance increase. Your results may vary depending on your hardware and other outside factors. This means you may experience no performance increase, so please make a note of existing settings in case you need to revert.
	
	**This guide is for Nvidia graphics cards only.**

Author: BenW#8484 on Discord

---

## Windows Settings

- Make sure your graphics drivers are up-to-date. You can do this by using NVIDIA GeForce Experience. Or downloading directly from their website.

- Make sure windows itself is up-to-date. This can be done under the `Update & Security` tab in Windows settings.

- Under the `Gaming` tab in Windows settings, navigate to `Captures`. We would recommend turning off `Background Recording`.

- Then, navigate to the `Game Mode` tab. Make sure it is set to `On`.

- Set graphics performance to `High Performance`, instructions below. (This may be less effective on a desktop than a laptop).

!!! info "Methods - Graphics Performance"

    === "Windows Store Version"
        - Open Windows settings and search for `Graphics Settings`.

        - Under 'Choose an app to set preference', select `Microsoft Store App`. 

        - In the dropdown below, find and select `Microsoft Flight Simulator`, then add.

        - Click options, then select `High Performance`, save your selection.

        - You can now close Windows Settings.
        
    === "Steam Version"
        - Open Windows settings and search for `Graphics Settings`.

        - Under 'Choose an app to set preference', select `Desktop App` and click Browse

        - You will need to locate the Microsoft Flight Simulator executable.

          - The default location for steam is:

            - `C:\Program Files (x86)\Steam\steamapps\common\MicrosoftFlightSimulator\FlightSimulator.exe`

                - (If you have it installed in another location, point it there instead)

        - Click options, then select `High Performance`, save your selection.

        - You can now close Windows Settings.

- Lastly, we would recommend closing any programs running in the background that you don't need. This can be done in your system tray (the upwards pointing arrow to the right side of the task bar). Right-click the icon of the program you would like to close and close it.
    - You may have many programs open here that you don't use often, but start with Windows. You can stop them automatically running by going to task manager, navigating to the `Start-up` tab and disabling programs you don't want to start with Windows.

!!! warning "Please note"

    If you are running the most recent Nvidia graphics driver after an update to Microsoft Flight Simulator, you may encounter some performance issues. 

    If this happens, and you notice a decrease in performance, you can try rolling back your graphics driver until a new one is available.

    **Do this at your own risk**
---

## NVIDIA GeForce Experience

Open GeForce Experience and navigate to the settings cog. Under `General` turn off the `In-Game Overlay`. This disables a feature called ShadowPlay, which is similar to the background recording we talked about in Windows settings.

Alternatively, if you do want to use the overlay, you can leave it on, but turn off ShadowPlay individually by pressing ++alt+z++ and making sure `Instant Replay` is set to off. We would recommend disabling the overlay entirely though if you don't intend to use it.

(The fewer overlays you have running, the better performance you will get. Examples of overlays are the Steam Overlay, Windows Game Bar etc.)

---

## NVIDIA Control Panel

Open NVIDIA Control Panel. This can be done by right-clicking on your desktop and clicking `NVIDIA Control Panel`.

Once it is open, navigate to the `Manage 3D Settings` tab on the left, then navigate to `Program Settings`.

In the dropdown, select `Microsoft Flight Simulator (Microsoft Flight Simulator)`

Change the settings listed below:

- Power management mode - `Prefer maximum performance`
- Texture Filtering Quality - `High Performance`
    - This setting may mean you lose a small amount of quality in textures with the benefit of more FPS, you can experiment with this to achieve an acceptable balance.
- Vertical Sync - `On`
    - If you have a G-SYNC compatible monitor, set Monitor Technology to `G-SYNC Compatible`

Make sure to press `Apply` to save these settings.

!!! info "Global Settings"

    These settings can be applied in the `Global Settings` tab instead of the `Program Settings` tab. This may give you an FPS increase in all of your games.

    If you decide to change settings in the `Global Settings` tab, make sure that Power management mode is set to `Adaptive`.

    You will then need to go into `Program Settings`, choose Microsoft Flight Simulator and change it to `Max Performance` as detailed above.

    This is important, as having it set to Max Performance globally will force your GPU to stay at its max clock speed, causing excess heat and power draw, even at idle. It is okay to have this setting in the `Program Settings` tab, as we want the GPU to run at its highest clock speed for maximum performance when actually running the game.

    We would also recommend having Vertical Sync set to `Use the 3D application setting` if choosing to apply these settings globally. This is because most games handle V-Sync well on their own, whereas MSFS doesn't currently.

---

## Microsoft Flight Simulator

These settings are ultimately up to you. It all depends on your hardware and whether you want higher FPS, or a better-looking game. You will need to find a balance between performance and graphical quality for your specific hardware.

You can use the built-in settings presets (low, medium, high, and ultra) to establish a baseline. Once you have found a preset you like, you can then start to change individual settings to further optimize your experience. We strongly encourage you to make a note of existing settings in case you wish to revert to your previous settings for any reason.

Below is a really useful guide which shows what each graphics setting in Microsoft Flight Simulator does, as well as outlining how they affect your performance. You can use it in with this guide to help you dial in your Microsoft Flight Simulator graphics settings.

[MSFS Settings Guide](https://forums.flightsimulator.com/t/how-to-graphics-settings-and-performance-guide-3-16-2021/132407){ .md-button target=new}

!!! info "Note"

    After applying all of these settings, it is essential that you restart your PC for some of them to take effect.

    We would also recommend restarting your PC each time you experiment and change graphics settings from within Microsoft Flight Simulator.
