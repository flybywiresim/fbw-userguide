# Reported Known Issues

!!! info "Always Try This First"

    Please try and remove all other mods/liveries from the community folder and test our add-on again. This will help rule out conflicts.

    <sub>Report back the result of this test on our Discord.

!!! warning "Read our Support Guide"

    1. [Learn how to fly an A32NX](index.md#1-learn-how-to-fly-an-a32nx)
    - [Troubleshoot](index.md#2-troubleshoot)
    - [Research Known Issues](index.md#3-research-known-issues)
    - [Report Issue on Discord](index.md#4-report-issue-on-discord)
    - [Report Issue on the A32NX Github](index.md#5-report-issue-on-the-a32nx-github)
    - [Collecting Support Information](index.md#collecting-support-information)

    ---
    
    Do this before reporting bugs.

!!! danger "No Support for Experimental - use at own risk"

    Refer to this page for [Known Issues in the Experimental Version](exp.md#known-issues).

FBW Installer - [Download Here](https://api.flybywiresim.com/installer){target=new} / *Sim Version: 1.19.8.0*

*Last Update: {{git_revision_date_localized}}*

---

!!! warning "Important Notice"
    If you have the following issues you are **most likely on stable**:

    - White EFB screen
    - PFD is missing bank angle protection indicators
    - `NOT IN DATABASE` MCDU error
    - External lights are not working

    Go to your content manager and find our aircraft. If you see the following image:

    ![content manager image](https://media.discordapp.net/attachments/828975068947939368/870365130335088660/unknown.png?width=1440&height=123)

    Uninstall it and restart the sim. Reinstall development version from our installer.

    <sub> You may install Stable v0.6.3 for compatibility. We recommend staying on development.

    This information is stated on [Installation Guide](../installation.md).

## Latest Issues

!!! info "Autopilot / Fly-By-Wire Issues"
    Please visit the dedicated Autopilot / Fly-By-Wire page for more information:

    - [**Main Page**](../feature-guides/autopilot-fbw.md)
    - [**Typical Issues + Solutions**](../feature-guides/autopilot-fbw.md#typical-issues-and-how-to-solve-them)
    - [**Known Issues**](../feature-guides/autopilot-fbw.md#known-issues)

#### Fuel Consumption

!!! tip ""
    *Affected versions: Stable, Development*

- May be larger than normal
- *Under Investigation*

#### Fuel Prediction

!!! tip ""
    *Affected versions: Stable, Development*

- Prediction numbers in the F-PLN and FUEL PRED pages are inaccurate.
- *A fix is in the works.*

#### Toolbar Pushback Addon

!!! tip ""
    *Affected versions: Stable, Development*

May cause unwanted behavior and prevent use of nose wheel steering.

- Solution:
    - Remove the addon from your community folder or wait for developer to update.
    - Use our EFB which has built in pushback controls or another addon.

#### Custom Autopilot Unwanted Disconnection

!!! tip ""
    *Affected versions: Development*

- Excessive speed decay during level off from open descent can lead to unwanted autothrust disconnection or even alpha floor in certain high drag/low speed situations. *Currently under investigation.*

#### Unwanted behavior - UTF8

!!! tip ""
    *Affected versions: Stable, Development*

Affects our custom autopilot, FADEC, and electrical system

- In rare cases the above mentioned systems may not start or behave erratically. This is in part due to `UTF-8` language support beta not enabled on your machine.
- Solution:
    1. - Open Windows Control Panel -> Region.
         - Go to the Administrative tab and click ++"Change system locale"++
         - Make sure the check mark next to `Beta: Use UTF-8 for worldwide language support` is selected.
         - Click ++"OK"++ and restart your computer.
    1. - Ensure `simconnect.cfg` does not appear in your Documents folder on your computer.

#### ADIRS - Runway

!!! tip ""
    *Affected versions: Development*

ADIRS may not be aligned when spawning anywhere except cold & dark at a gate (*intermittent issue*)

- Workaround: Restart the flight

#### Outer Tank Fuel Transfer

!!! tip ""
    *Affected versions: Stable, Development*

Sometimes the sim will "*miss*" the trigger point being reached for outer tank fuel transfer to initialize. This may happen if the sim is "busy" when working with something else OR initial FOB at the start of flight is below the trigger point.

*Intermittent Issue / Under Investigation*

- Workaround: Add enough fuel to get past the trigger point of 239 gallons before departing.

#### EFB Issues in External View

!!! tip ""
    *Affected versions: Stable, Development*

Can't interact with EFB when popped-out (++ralt+"Left Click"++) and switching to the external camera.

- Workaround: Make sure to click on the actual EFB screen (not the popped out window) before switching to external camera.

#### Printing METAR Reports May Cause a CTD

!!! tip ""
    *Affected versions: Stable, Development*

- Intermittent / Single time event only
- *Under investigation*

#### Freelook with Mouse

!!! tip ""
    *Affected versions: Stable, Development*

Using freelook may cause controls to freeze.

- Workaround: Try setting `TOGGLE COCKPIT FREELOOK` to your mouse ++middle-button++. Reference: [MSFS Forum Post](https://forums.flightsimulator.com/t/freelook-with-mouse-causes-controls-to-freeze-after-su5/426349/15){target=new}

#### Cockpit Decals Flicker

!!! tip ""
    *Affected versions: Stable, Development*

- Solution: Update to the latest Stable or Development version.

#### Strobe Light Function Reversed

!!! tip ""
    *Affected versions: Stable, Development*

When strobe lights are set to `OFF` but the lights are on when starting on the runway. *Under investigation*

- Workaround: Start cold and dark at the gate.

#### TCA (Thrustmaster) hardware

!!! tip ""
    *Affected versions: Stable, Development*

Can't start engines:

- Open the controls menu
    - REMOVE the below:
        - “Toggle Engine 2 Fuel Valve” - Set to Joystick Button 4
        - “Toggle Engine 1 Fuel Valve” - Set to Joystick Button 3
    - KEEP the below:
        - “Set Engine 2 Fuel Valve” - Set to Joystick Button 4
        - “Set Engine 1 Fuel Valve” - Set to Joystick Button 3

![throttle config image](https://cdn.discordapp.com/attachments/754130199804772372/869697814458945546/unknown.png)

Also see our [Throttle Calibration Guide](../feature-guides/throttle-calibration.md)

---

## Altitude Issues

!!! tip ""
    *Affected versions: Stable, Development*

### MSFS

The effects of non-standard day pressure and temperature on altitude in MSFS were inaccurate during *Sim Update 5* affecting the following:

- In game ATC may still see you at a different altitude than what you see in the flight deck.
    - **Workaround:** Climb or descend a couple hundred feet at a time until the in game ATC stops requesting you to climb or descend.

!!! info ""
    This is reported to be fixed by Asobo in current patch - **World Update 6**.

### VATSIM

- VATSIM controllers may also see you at a different altitude when you are below the transition altitude. We recommend including a note on your flight plan that you are using MSFS.

!!! info ""
    VATSIM software is being modified to remedy this.

---

## Cockpit Interaction System

!!! tip ""
    *Affected versions: Stable, Development*

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
- Move the mouse left to turn the knob left, move it right to turn the knob right (with the ++"Left Click"++ held down)
- You can also use the scroll wheel while holding ++"Left Click"++ down to turn the knob left or right.
- To push a control / knob in, lock to the control using ++"Left Click"++ and then ++"Right Click"++.
- To pull a control / knob out, hold ++"Left Click"++ and then click your scroll wheel ++"Middle Mouse"++.
    - Note: If you already use the ++"Middle Mouse"++ button to activate freelook this may not work. Check your keybinds so this feature does not conflict.

!!! tip ""
    This list is based on our testing and feedback. For more information see the [MSFS Release Notes](https://forums.flightsimulator.com/t/microsoft-flight-simulator-available-today-on-xbox-series-x-s-and-xbox-game-pass/425795) - Cockpit Interactions.

    Direct your support questions and feedback of this feature to Asobo.

---

## Package Separation Issues

!!! tip ""
    *Affected versions: All versions*

!!! warning "Liveries incompatible due to package separation"

    **Affects all versions of the A32NX (Stable, Development)**

    Liveries made for the default A320neo will no longer function in the new FlyByWire package. Liveries will need to be converted by their respective authors.

    While this might represent an inconvenience for a short amount of time, we are sure that 3rd party content authors will be quick to provide you with updated liveries and programs.

    **Convert Your Liveries:**

    - See our guide to [liveries](../liveries.md)
    - Visit Flightsim.to with updated liveries [here](https://flightsim.to/c/liveries/flybywire-a32nx/){target=new}

!!! block "Package separation or "fork" issues:"
    ![New Aircraft](../assets/new-aircraft.png){width=50% align=left loading=lazy}

    - Default aircraft showing
        - Solution: Select the **^^FlyByWire Simulations A320neo (LEAP)^^** in the aircraft selector instead of the Asobo one.

    - Invisible plane / Sounds not working / Installation issues
        - Workaround: Reinstall A32NX, delete any old version from your Community Folder. Ensure you are on Installer v2.0.0 or above.

---

## Common Issues

#### NOT IN DATABASE when Loading Flight Plan

!!! tip ""
    *Affected versions: Stable, Development*

- Upgrade to the latest A32NX package (stable or development).
- Install/uninstall Navigraph data with the Navigraph Navdata Center application.
- __Do not__ delete `navigraph-navdata` from the community packages directory, as this will leave default navdata disabled.

#### AP not Following the Flight Plan

!!! tip ""
    *Affected versions: Stable, Development*

- Caused by leaking input from controller, but doesn't disconnect the AP
- Workaround: Set dead-zones for your input device higher
    - Go to your settings
    - Controls and select your yoke/joystick/controller.
    - After that click the sensitivity button on the top left which should take you to the menu where you can adjust your deadzones. Start with 20% deadzone, if the problem persists keep increasing it. If it's fine with 20% you can then slowly decrease it too.

#### Autopilot goes Direct to RWY on APP (same with the Default A320)

!!! tip ""
    *Affected versions: Stable, Development*

- This is a bug in the default Asobo flight plan manager - the FlyByWire team is working on a customFPM which fixes all these bugs and adds much better navigation
- For now the workaround is to use DIRECT to the next waypoint again or selected heading.
- If you can, always enter your expected approach in the MCDU before departing. If this doesn't need to be changed, this will skip the turnaround bug on approach. This issue and others like it will be resolved in cFPM.

#### CTD when pressing **FLY** on world menu

!!! tip ""
    *Affected versions: Stable, Development*

- Check your content manager for missing packages

#### Plane is Invisible

!!! tip ""
    *Affected versions: Stable, Development*

- Check your content manager for missing packages
- Livery/Mod Conflict

#### Rudder Keybindings not Working

!!! tip ""
    *Affected versions: Stable, Development*

- You have to set your keybinding to rudder axis right and left

#### Wing Dips on Landing

!!! tip ""
    *Affected versions: Stable*

- Caused by bad transition to direct law in flare, same with the default A320
- Workaround: use minimal aileron input on landing

#### Black Screens / Unable to Start

!!! tip ""
    *Affected versions: Stable, Development*

- Conflict with another mod/livery or incorrect installation of the A32NX add-on
- Use our [installer](https://api.flybywiresim.com/installer){target=new}

#### Upper ECAM Displays Wrong THR Levers Position / N1 Rating

!!! tip ""
    *Affected versions: Stable*

- Solved in Development version after calibrating the throttle.

#### Incompatibilities

!!! tip ""
    *Affected versions: Stable, Development*

- ASOBO *Aviator/Beta Club* A320 liveries are incompatible with the A32NX add-on
- Wipers don't function correctly with converted FSX Liveries

---

## MSFS Live Weather

!!! tip ""
    *Affected versions: Stable, Development*

If the live weather feature is experiencing issues you may experience the following:

- Degraded aircraft performance.
- Airspeed and climb rate issues.

You will typically see higher or excessive fuel flow alongside exceedingly high SAT, which leads to high TAT and ISA deviation.

!!! info ""
    ISA deviation is the difference between SAT and the ISA temperature for that altitude and is indicated by the value next to ISA in the ECAM.

**Workaround**: Use a static weather preset for your flight.

---

## CTD Resolution

!!! tip ""
    *Affected versions: Stable, Development*

Crash to desktop (CTD) can either be a sim issue or a conflict with the A32NX. There also is currently no known guaranteed solution, however users have found success with by trying the following:

1. [Perform a clean install](../installation.md#clean-install-steps)
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

!!! tip ""
    Unless stated otherwise, all fixed issues are first released on our development version.

- Using the *"Pounds (lbs)"* on the EFB. *[Fixed PR #5344](https://github.com/flybywiresim/a32nx/pull/5344){target=new}*
    - Closed Issues: [#5316](https://github.com/flybywiresim/a32nx/issues/5316), [#5321](https://github.com/flybywiresim/a32nx/issues/5321)

- Installer v1.2.0 issues resolved in v2.0.0.

- Selected Heading may not work after using DIR feature or inputting a STAR. *[Fixed PR #5593](https://github.com/flybywiresim/a32nx/pull/5593)*
    - Closed Issue: [#5479](https://github.com/flybywiresim/a32nx/issues/5479)

* ND Terrain does not appear. *[Fixed #5470](https://github.com/flybywiresim/a32nx/pull/5470)*

* Turning off right PFD also disables left one. *Fixed*

* Vertical speed indicator not working. *[Fixed PR #5398](https://github.com/flybywiresim/a32nx/pull/5398)*

* In development/experimental versions, the engine startup sound is bugged due to a fuel flow issue. This will be fixed when engine startup procedures will be implemented. *(fixed)*

* Due to changes in the way flap lift is modelled, the plane may bounce when transitioning between certain flaps settings (flaps 1 to flaps 2 and flaps 3 to flaps FULL). *(fixed)*
    - The stable version is less affected than the development version.

* Installer v1.1.1 potential issues: *(fixed)*
    - Getting default version or black screens after using installer on v1.1.0
        - Workaround: Delete the `flybywire-aircraft-a320-neo folder`, then install it again.
    - Installer not showing your existing installation:
        - This is due to the new modular system which requires a new full installation.
        - Workaround: Install the add-on again via the installer.

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
