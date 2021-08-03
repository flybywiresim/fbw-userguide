# Reported Known Issues

!!! info "Always Try This First"

    Please try and remove all other mods/liveries from the community folder and test our mod again. This will help rule out mod conflicts.

    <sub>Report back the result of this test on our Discord.

!!! warning "Important Troubleshooting Information"
    ^^Updates^^

    If you are cannot resolve any issues with solutions listed below perform a clean reinstall of the A32NX. Delete either of the folders below from your community folder:

    * A32NX (old folder name)
    * flybywire-aircraft-a320-neo (new folder name)

    **[Read - Additional Clean Install Steps](installation.md#clean-install-steps)**

    ---

    ^^Flight Model^^

    **The modern flight model is required to fly the A32NX**.

    Please ensure that your flight model is set correctly via the MSFS settings.

    ---
    
    Do this before reporting bugs.

FBW Installer - [Download Here](https://api.flybywiresim.com/installer) / *Sim Version: 1.18.14.0*

*Last Update: {{git_revision_date_localized}}*

---

## Latest Issues

!!! info "Autopilot / Fly-By-Wire Issues"
    Please visit the dedicated Autopilot / Fly-By-Wire page for more information:

    - [**Main Page**](autopilot-fbw.md)
    - [**Typical Issues + Solutions**](autopilot-fbw.md#typical-issues-and-how-to-solve-them)
    - [**Known Issues**](autopilot-fbw.md#known-issues)

**EFB *"pounds (lbs)"* setting**

Using the "lbs" weight setting on the EFB may cause the following issues.

* Simbrief integration - fuel and payload showing 0 after OFP request in AOC.
    
* EFB unit conversions cause weights on ECAM and MCDU to show 0 when **lbs** is selected by the efb.

* FOB displays 0 on ECAM.

**Workaround:** Set lbs through the MCDU only and reload the aircraft.

!!! info ""
    **Fix in Progress [PR #5344](https://github.com/flybywiresim/a32nx/pull/5344)**
    
---

* Toolbar pushback addon may cause unwanted behavior and prevent use of nose wheel steering. 
    - Solution:
        - Remove the addon from your community folder or wait for developer to update. 
        - Use our EFB which has built in pushback controls or another addon. 
    
* Custom autopilot unexplained disconnection. 
    - There seems to be a speed decay issue in certain situations during turns and CONF2. It can also happen when approaching the level off altitude after open descent. Does not occur in level flight. 
    - *Currently under investigation.*
    
* Unwanted behavior - Autopilot, FADEC, electrical system 
    - In rare cases the above mentioned systems may not start or behave erratically. This is in part due to `UTF-8` language support beta not enabled on your machine.
        - Solution:
            1. - Open Windows Control Panel -> Region.
                - Go to the Administrative tab and click ++"Change system locale"++
                - Make sure the check mark next to `Beta: Use UTF-8 for worldwide language support is selected`.
                - Click ++"OK"++ and restart your computer.
            1. - Ensure `simconnect.cfg` does not appear in your Documents folder on your computer.
    
* ADIRS not aligned when spawning anywhere except cold & dark at a gate (*intermittent issue*)
    - Workaround: Restart the flight
    
* Wipers don't function correctly on FSX Liveries

***

### SU5 Issues

#### General SU5 Issues

!!! warning "Important Notice"
    If you have the following issues you are **most likely on stable**:

    - White EFB screen
    - PFD is missing bank angle protection indicators
    - `NOT IN DATABASE` MCDU error
    - External lights are not working

    Go to your content manager and find our aircraft. If you see the following image:

    ![content manager image](https://media.discordapp.net/attachments/828975068947939368/870365130335088660/unknown.png?width=1440&height=123)

    Uninstall it and restart the sim. Reinstall development verison from our installer. 

    This information is stated on [Installation Guide](installation.md).

- Navigraph FMS Beta Users - If you are missing SID/STARs please delete and reinstall your navdata via the Navigraph Center and **restart** your simulator.

- **Intermittent / Single time event only** - Printing METAR reports may cause a CTD. Please report this to us on our Discord.  

- Freelook with mouse causes controls to freeze.
    - Workaround: Try setting `TOGGLE COCKPIT FREELOOK` to your mouse ++middle-button++. Reference: [MSFS Forum Post](https://forums.flightsimulator.com/t/freelook-with-mouse-causes-controls-to-freeze-after-su5/426349/15)

- Cockpit decals flicker. *Under investigation*

- Strobe light function may be reversed (Set to `OFF` but lights on) when starting on the runway. *Under investigation*
    - Workaround: Start cold and dark at the gate.

- TCA (Thrustmaster) hardware - can't start engine
    - Open the controls menu
        - REMOVE the below:
            - “Toggle Engine 2 Fuel Valve” - Set to Joystick Button 4
            - “Toggle Engine 1 Fuel Valve” - Set to Joystick Button 3
        - KEEP the below:
            - “Set Engine 2 Fuel Valve” - Set to Joystick Button 4
            - “Set Engine 1 Fuel Valve” - Set to Joystick Button 3

  ![throttle config image](https://cdn.discordapp.com/attachments/754130199804772372/869697814458945546/unknown.png)

#### Altitude Issues

The effects of non-standard day pressure and temperature on altitude in MSFS is inaccurate for SU5 affecting the following:

- Airplane altitude provided to ATC from the airplane transponder will not correlate correctly with the airplane indicated on the airplane's altimeter. VATSIM / IVAO will see MSFS airplanes at a different altitude than what the pilots see.

- If temperature is different than ISA, the airplane altimeter will not indicate the correct altitude, most observable when airplane is on the ground at the airport with the proper QNH set. The altimeter should align with the airport's elevation, but it won't with SU5.

- If pressure or temperature is changing with live weather, the airplane's autopilot may wander from the set altitude or "chase" altitude.

- The built-in MSFS ATC will experience the same altitude issues - you may see FL390 on your altimeter, but the ATC will see you at a different altitude.


#### FCU Heading Knob

On the first load of the A32NX the heading knob push/pull may not work.

- Solution:
    - Restart once as for unknown reasons this event doesn't work the first time.

!!! info "**Legacy** Cockpit Interaction System"
    If you want to use the old method of interacting with the cockpit before Sim Update 5:

    - Go to Menu
    - General Options
    - Accessibility
    - Find the `Cockpit Interaction System` setting
    - Change to `legacy`
    
Using **New** Cockpit Interaction System

- Highlight a control (like a knob).
- Hold ++"Left Click"++ to lock to that control. Now your mouse will not affect any other controls or other mouse bindings.
- Move the mouse left to turn the knob left, more it right to turn the knob right (with the ++"Left Click"++ held down)
- You can also use the scroll wheel while holding ++"Left Click"++ down to turn the knob left or right.
- To push a control / knob in, lock to the control using ++"Left Click"++ and then ++"Right Click"++.
- To pull a control / knob out, hold ++"Left Click"++ and then click your scroll wheel ++"Middle Mouse"++.
    - Note: If you already use the ++"Middle Mouse"++ button to activate freelook this may not work. Check your keybinds so this feature does not conflict.
    
!!! warning ""
    This list is based on our testing and feedback. For more information see the [MSFS Release Notes](https://forums.flightsimulator.com/t/microsoft-flight-simulator-available-today-on-xbox-series-x-s-and-xbox-game-pass/425795) - Cockpit Interactions. 

    Direct your support questions and feedback of this feature to Asobo. 
    
---

### Package Separation Issues

!!! warning "Liveries incompatible due to package separation"

    **Affects all versions of the A32NX (Stable, Development, and Experimental)**

    Liveries made for the default A320neo will no longer function in the new FlyByWire package. Liveries will need to be converted by their respective authors.

    While this might represent an inconvenience for a short amount of time, we are sure that 3rd party content authors will be quick to provide you with updated liveries and programs.

    **Convert Your Liveries:**
    
    - See our guide to [convert liveries](convert-liveries.md)
    - Visit Flightsim.to with updated liveries [here](https://flightsim.to/c/liveries/flybywire-a32nx/)

* Package separation or "fork" issues (*All Versions*):
    -  Default aircraft showing
        - Solution: Select the **^^FlyByWire Simulations A320neo (LEAP)^^** in the aircraft selector instead of the Asobo one.
    - Invisible plane / Sounds not working / Installation issues
        - Workaround: Reinstall A32NX, delete any old version from your Community Folder. Ensure you are on Installer v1.2.0 or above.

***
    
### Installer Issues

![installer issue](https://media.discordapp.net/attachments/831654046405230652/832741603940237362/unknown.png)

* If there is an issue with your community directory our installer will display the error above. This means the installer detects a certain directory as your community directory even though it does not exist anymore.
    - Solution:
        1. - Inside `%userprofile%\AppData\Roaming\FlyByWire Installer` delete `config.json`
            - Restart the installer
            - Change the community directory in the installer settings if necessary
        1. - Create the specified directory stated in the error message
            - Restart the installer
            - Change the community directory in the installer settings
    
* Installer Memory Leak
    - Commonly happens when our installer updates. Currently being investigated.
        - Workaround: Exit out of the FlyByWire Installer. Open `Task Manager` and find FlyByWire Installer. End Task.
    
* Instructions to send us installer logs can be found [here](installation.md#flybywire-installer)

***

## MSFS Live Weather

If the live weather feature is experiencing issues you may experience the following:

- Degraded aircraft performance.
- Airspeed and climb rate issues.

You will typically see higher or excessive fuel flow alongside exceedingly high SAT, which leads to high TAT and ISA deviation. 

!!! info ""
    ISA deviation is the difference between SAT and the ISA temperature for that altitude and is indicated by the value next to ISA in the ECAM.

**Workaround**: Use a static weather preset for your flight. 

---

## Common Issues

* AP not following the flight plan (leaking input values affect, but doesn't disconnect the AP)
    - Workaround: Set dead-zones for your input device higher
        - Go to your settings
        - Controls and select your yoke/joystick/controller.
            - After that click the sensitivity button on the top left which should take you to the menu where you can adjust your deadzones. Start with 20% deadzone, if the problem persists keep increasing it. If it's fine with 20% you can then slowly decrease it too.

* Autopilot goes direct to RWY on APP (same with the default A320)
    - Workaround: Use DIR to a waypoint or selected heading

* CTD when pressing **FLY** on world menu
    - Check your content manager for missing packages

* Plane is invisible
    - Check your content manager for missing packages
    - Livery/Mod Conflict

* Rudder keybindings not working
    * You have to set your keybinding to rudder axis right and left

* Wing dips on landing (due to bad transition to direct law in flare, same with the default A320)
    * Workaround: use minimal aileron input on landing

* Black screens / unable to start
    * Conflict with another mod/livery or incorrect installation of the A32NX mod
    * Use our [installer](https://api.flybywiresim.com/installer)

* Upper ECAM displays wrong THR levers position / N1 rating

* ASOBO *Aviator/Beta Club* A320 liveries are incompatible with the A32NX mod

***

## CTD Resolution

Crash to desktop (CTD) can either be a sim issue or a conflict with the A32NX. There also is currently no known guaranteed solution, however users have found success with by trying the following:

1. [Perform a clean install](installation.md#clean-install-steps) 
2. Try without anything else installed in community.
3. Try without FSUIPC OR update FSUIPC.
4. Try downloading the bat file that is pinned in the #support channel on our [Discord](https://discord.gg/flybywire). Run it to clean up any FBW background files.
5. Run without live weather and/or live traffic.
6. Delete your rolling cache in the sim and create a new one.
7. Delete any manual cache in the sim and create new ones.
8. Run the game as Administrator.
9. Visit and read the [MSFS Known Issues Page](https://flightsimulator.zendesk.com/hc/en-us/articles/360016027399-KNOWN-ISSUES-Last-update-July-28-2021-) OR [MSFS Troubleshooting & Support](https://flightsimulator.zendesk.com/hc/en-us/sections/360004475200-Troubleshooting-Support-Windows-10-PC)

!!! warning "Peripherals"
    This is an important snippet from MSFS known issues.

    If you are getting CTDs, it could be one of your peripherals disconnecting sometime during the flight, which then causes the sim to CTD. 

    It could be anything from a usb drive to a controller. Please try to minimise how many peripherals you have connected.

---

## Fixed Issues

* ND Terrain does not appear. *[Fixed #5470](https://github.com/flybywiresim/a32nx/pull/5470)*
  
* Turning off right PFD also disables left one. *Fixed*

* Vertical speed indicator not working. *Fixed [PR #5398](https://github.com/flybywiresim/a32nx/pull/5398)*

* In development/experimental versions, the engine startup sound is bugged due to a fuel flow issue. This will be fixed when engine startup procedures will be implemented. *(fixed)*

* Due to changes in the way flap lift is modelled, the plane may bounce when transitioning between certain flaps settings (flaps 1 to flaps 2 and flaps 3 to flaps FULL). *(fixed)*
    - The stable version is less affected than the development version.
    
* Installer v1.1.1 potential issues: *(fixed)*
    - Getting default version or black screens after using installer on v1.1.0
        - Workaround: Delete the `flybywire-aircraft-a320-neo folder`, then install it again.
    - Installer not showing your existing installation:
        - This is due to the new modular system which requires a new full installation.
        - Workaround: Install the mod again via the installer.

* VOR/ADF indicators not showing on the ND *(fixed)*
  
* Unable to climb / flaps 1 issue *(fixed)*
  
* EFB not clickable *(fixed in development version)*
  
* V/S mode stuck at 1500 fpm or inoperable *(fixed)*
    
* ILS not showing on approach / does not auto populate in RADNAV *(fixed)*
    - Workarounds (may apply to 3rd party sceneries):
        - Manually input your ILS frequency into RADNAV. Type in the frequency found on your chart and press the key next to LS/Freq. Sample: 111.30

* Left PFD lagging / freezing *(fixed)*
    - The team is aware of the issue and is working hard to resolve it, potential fixes are being tested

* PFD artificial horizon freezes *(fixed)*
    - Workaround:
        - Turn off PFD, wait >10 seconds and turn PFD back on.
    
---

If you are here from our social media please visit our discord for support.

[:fontawesome-brands-discord:{: .discord } - **Discord Link**](https://discord.gg/flybywire)
