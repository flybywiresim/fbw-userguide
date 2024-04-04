---
title: flyPadOS 3 EFB - Settings
description: Learn how to configure various aspects of flyPadOS3 itself in the FlyByWire A32NX, from aircraft options to 3rd party settings.
---

<link rel="stylesheet" href="../../../../stylesheets/efb-interactive.css">

# flyPad Settings

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-settings-overview.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

## Overview

There are various aspects of the aircraft and its simulation which can and sometimes must be configured. 

Find a description of all available setting categories and their settings below. 

## Aircraft Options / Pin Programs

Settings for A32NX aircraft configuration.

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-settings-aircraft-configuration.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

### Usage

- Thrust Reduction Height (ft):
    - Default for the MCDU setting for thrust reduction height (above ground).
- Acceleration Height (ft):
    - Default for the MCDU setting for acceleration height (above ground).
- Engine-Out Acceleration Height (ft):
    - Default for the MCDU setting for engine-out acceleration height (above ground).
- ISIS Baro Unit
    - User can set which baro setting he wants to have in the ISIS backup instrument.
- ISIS Metric Altitude
    - User can set which units setting he wants to have in the ISIS backup instrument.
- PAX Signs:
    - Configures if the aircraft should use "No Smoking" or "No Portable Devices" in its ECAM message when the no smoking selector switch on the overhead panel is selected on.
- RMP VHF Spacing
    - Changes the spacing for selectable frequencies in the RMPs from 8.33 kHz to 25 kHz and vice versa.

    ??? note "Channel Spacing (click to expand)"
         Aircraft radio systems transmit on a Very High Frequency (VHF) band between 117.975 and 137 MHz. The number of available VHF assignments has increased over the years by splitting the radio spectrum into narrower bandwidths, from 50 kHz to 25 kHz channels. The bandwidth can support 760 channels, if channels are spaced by 25 kHz. In 1994, it was decided to introduce a further channel split from 25 to 8.33 kHz. 8.33 kHz spacing was introduced above Flight Level (FL) 240 in International Civil Aviation Organization (ICAO) European (EUR) regions in October 1999 and above FL 195 from March 15, 2007. Currently, 8.33-kHz channels have been implemented in the airspace of all 20 ICAO EUR region states. So far, Europe is the only region that’s moved to 8.33 kHz channel spacing.

         Source: [universalweather.com](https://www.universalweather.com/blog/8-33-khz-radio-channel-spacing-changes-are-coming-to-europe/){target=new)}

         See also: [8.33 kHz Voice Channel Spacing communications](https://833radio.com/news/show/7){target=new}

- FMGC Lat/Lon Waypoint Format
    - Configures the name format for the [Stored Waypoints](../../../../pilots-corner/a32nx/a32nx-advanced-guides/data-management.md#stored-waypoints) to be used when NAT routes are imported via SimBrief.  
- Weight Unit:
    - The weight unit of the aircraft used for aircraft weight, fuel and simBrief imports.
- Satcom:
    - Enables showing the Honeywell JetWave Satcom antenna on the fuselage.   
- Automatic Call Outs:
    - Enables selection of various radio altitude auto call outs.
  
    !!! info "Please Note Some Airbus Rules"
        - one of "five hundred" or "four hundred" is mandatory,
        - only one of "two thousand five hundred" and "twenty five hundred" can be selected.
  
    ![flypad-settings-callouts.png](../../assets/flypados3/flypad-settings-callouts.png){loading=lazy}
  
## Sim Options

Settings for simulation aspects of the A32NX aircraft.

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-settings-sim-options.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

### Usage

- Default Baro:
    - User can set which baro setting is wanted as a default: inHg, hPA or Auto (depends on the airport where the aircraft spawned).
     
- Sync MSFS Flight Plan:
    - User can set if and how the flight plan synchronization between the simulator and the aircraft should work.
    - The options are:
        - None: 
            - The simulator's flight plan will not be loaded and changes to the aircraft's flight plan will not be saved back to the sim's flight plan. 
        - Load Only: 
            - The simulator's flight plan set in the World Map will be loaded once when starting the flight. Any subsequent changes to the flight plan in the aircraft will not be synchronized back to the simulator.
        - Save: 
            - The simulator's flight plan set in the World Map will be loaded once when starting the flight. Any subsequent changes to the flight plan in the aircraft will be synchronized back to the simulator if possible. See the warning below for more information.
   
        !!! note "There is No synchronization from the sim's flight plan to the aircraft after initial load."

        !!! warning "Synchronization Issues Expected"
            The aircraft's custom Flight Management System provides better accuracy and features over the default flight plan manager in Microsoft Flight Simulator, which results in issues syncing the flight plan from the MCDU back into the simulator. Do not expect it to work properly in all cases.

- Enable SimBridge Connection
    - Auto:
        - The aircraft attempts to connect to the SimBridge for 5min after pressing "Ready to Fly" (`Active` is 
          shown).
        - If this setting is selected the aircraft will try to connect to the SimBridge for 5min after every start of 
           a new flight.
        - After 5min of unsuccessful connection attempts the aircraft will stop any further attempts and `Inactive` 
          will be shown.
        - If `Inactive` is shown, but you want to connect to the SimBridge just click on `Off`, wait a few 
          seconds, and then click on `Auto` again.
    - Off:
        - The aircraft will not make any attempts to connect to the SimBridge.
    - Also see our [SimBridge Guide](../../../../tools/simbridge/index.md) on which features require the SimBridge and how to set up and configure it. 
 
- External SimBridge Port
    - User can change the port for the SimBridge in case the default port is already occupied on the user's system.
    - Default is: 8380

- Dynamic Registration Decal:
    - The dynamic registration number decal shown on the external livery can be disabled to improve appearance when using liveries with a static registration number.
- Use calculated ILS signals
    - Enable this setting to use a calculated ILS signal instead of the signal provided by Microsoft Flight Simulator.
    - This avoids unwanted and unrealistic loss of the ILS signal in Microsoft Flight Simulator which often happens when the aircraft gets below the antenna position.
    - In some rare cases this can cause a faulty G/S signal. In this case this setting can be disabled with immediate effect.
- Wheel Chocks
    - Enable wheel chocks visible in the external view
    - Only visible if ground crew has not removed them - see [Wheel Chocks and GSE Safety Cones](../wheel-chocks-cones.md) for more information. 
- Safety Cones
    - Enable safety cones visible in the external view
    - Only visible if ground crew has not removed them - see [Wheel Chocks and GSE Safety Cones](../wheel-chocks-cones.md) for more information.
- Throttle Detents
    - Please see the [Throttle Configuration Guide](throttle-calibration.md).

## Realism
Settings for realism aspects of the A32NX aircraft.

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-settings-realism.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

### Usage

- ADIRS Align Time:
    - User can set this to either a realistic time (~ 8 min), a faster time (~ 2 min) or instant.
- DMC Self Test Time:
    - User can set the time for the Display Management Computer's self test (Real ~ 15 s, Fast ~ 5 s, Instant).
- Boarding Time:
    - User can set the simulated boarding time to either a realistic time (~ 15 min), a faster time (~ 3-4 min), or instant.
        - Based on full load - 174 passengers and full cargo.
- Autofill Checklists
    - Supports the user with checking items from the checklists by watching the corresponding switches, knobs, and buttons and setting the checklist item to complete when the setup is correct.  
- Home Cockpit Mode
    - Removes backlight bleed from PFD, ND, and ECAMs
    - Removes reflection from the ISIS
- Separate Tiller from Rudder Inputs
    - User can choose to use how the nose wheel shall be controlled:
        - Legacy mode (Disabled): Rudder controls also move the nose wheel. No separation.
        - Realistic mode (Enabled): Nose Wheel steering with tiller handwheel is separate from the rudder.
            - See our guide: [Nose Wheel and Tiller Operation](../nw-tiller.md)
- MCDU Keyboard Input (unrealistic)
    - Enables the MCDU Keyboard input feature (see [MCDU Keyboard](../mcdu-keyboard.md)).
- MCDU Focus Timeout (s)
    - The timeout feature will automatically deactivate the focus of the MCDU screen after the given amount of seconds.
    - Valid range is 5 - 120 seconds.
    - Setting is only available if MCDU Keyboard Input is enabled.
- Sync EFIS controls between Captain and FO (unrealistic)
    - When enabled, the EFIS controls will be synchronized between the Captain and FO.
    - This includes the Flight Director (FD), Landing System (LS) and Baro (STD, QNH and inHg/hPa) controls.
    - Note: Baro is currently not separated between the Captain and FO and is always synchronized independent of this setting. 
- Show Pilot Avatar
    - When enabled, the pilot avatar will be visible in the cockpit. 
    - The avatar style can be chosen in the MSFS settings `General Options -> Misc`.
- Show First Officer Avatar
    - When enabled, the first officer avatar will be visible in the cockpit.
    - The avatar style can be chosen in the MSFS settings `General Options -> Misc`.
- Pause At TOD (Top of Descent)
    - Pause at TOD can be configured by distance between 0 - 50 NM before TOD
    - When enabled, your aircraft will pause at the specified distance before TOD
    - If the TOD point shifts before your present position, or AP mode reverts to CRZ, it will pause the simulation.

    !!! block ""
        ![img_3.png](../../assets/flypados3/flypad-settings-realism-avatars.png){loading=lazy align=center width=49%}
        ![img_2.png](../../assets/flypados3/flypad-settings-realism-avatars2.png){loading=lazy align=center width=49%}
  

## 3rd Party Options
Settings for integrations with various 3rd party applications

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-settings-third-party-options.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

#### Navigraph Integration 

- Navigraph Account Link
    - Setup wizard to connect your Navigraph Account with the flypad.
- Override SimBrief User ID
    - Allows users to input a custom SimBrief User ID. For more information see [A32NX simBrief Integration](../simbrief.md/#setup-a32nx-simbrief-integration).
- Automatically Import SimBrief Data
    - Imports latest SimBrief flight automatically when starting the flyPad.

#### GSX Integration
These options are separate to provide you with the flexibility to choose what to sync with GSX and what not to sync. 

!!! warning ""
    Enabling any of these options will retroactively disable the [chocks and cones](../wheel-chocks-cones.md). You cannot re-enable as long as any of these options are enabled. This is due to how GSX detects the parking brake.

!!! warning "Profile provided"
    The aircraft comes with a GSX profile, please read [here](../gsxintegration/profile.md) for more information.

- GSX Payload Sync:
    - Enables the option to synchronize GSX and the aircraft's own payload management system.
- GSX Fuel Sync:
    - Enables the option to synchronize GSX and the aircraft's own fuel management system.

## ATSU/AOC

Settings for integration with various data and information sources.

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-settings-atsu-aoc.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

### Usage

- ATIS/ATC Source:
    - Choose which Online ATC service should be used for ATIS and ATC.
- METAR Source:
    - Choose which weather data provider should be used (Aircraft only - does not change sim weather).
    - MeteoBlue is the weather service the sim uses as well.
- TAF Source:
    - Choose, which Terminal Area Forecast (TAF) service should be used.   
- Error Reporting
    - Enables error reports to be sent to Sentry.io to allow the FlyByWire team to easier find and resolve issues with the aircraft.
- TELEX:
    - Enables free text and live map ([FlyByWire Live Map](https://flybywiresim.com/map/){target=new}).

        !!! warning
            If enabled, aircraft position data is published for the duration of the flight. Messages are public and not moderated.

            ~~USE AT YOUR OWN RISK~~

            [Free Text - Feature Guide](../freetext.md){.md-button}

    - If enabled, a message will be displayed to confirm sharing of the free text and position data to the public.

        ![flypad-settings-atsu-aoc-telex-warning](../../assets/flypados3/flypad-settings-atsu-aoc-telex-warning.png)

- Hoppie User ID:
    - Unique logon code that is used to identify the user for the Hoppie ACARS communication.
    - See [Create a logon code](../hoppie.md#create-a-logon-code) in our documentation for Hoppie ACARS.

## Audio

Settings for various audio sources and sounds.

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-settings-audio.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

- Volume Sliders:
    - Dynamically adjust various audio elements while in the virtual cockpit.  
- PTU Audible in Cockpit (unrealistic):
    - The aircraft's PTU sound (barking sound) is not audible in the cockpit in the real aircraft.
    - To make it audible in the cockpit, set this option to on.
- Passenger Ambience:
    - Select if passenger audio sounds should be played.  
- Announcements:
    - Select if crew announcements should be played.
- Boarding Music:
    - Select if music should be played while boarding. 

For detailed information on these settings, please visit:

[Audio Configuration Page](../audio.md){.md-button}

## flyPad Settings

Settings for the flyPad itself.

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-settings-flypad.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

### Usage

- Language
    - Selects the flyPad language
- Onscreen Keyboard Layout
    - Selects the keyboard layout of the flyPad's on screen keyboard
- Automatically Show Onscreen Keyboard:
    - A virtual keyboard will appear whenever the user enteres an input field. 
- Auto Brightness:
    - Sets the brightness of the flyPad automatically based on the time of day.
- Brightness:
    - Manually set the brightness of the flyPad.
    - This setting is only available if Auto Brightness is off.
- Battery Life Simulated
    - If enabled, the flyPad battery will discharge if the aircraft is not powered.
    - The battery will last about 9 h. 
    - If the sim's time is changed forward 9+ h after loading the flight, the battery will be empty.
    - Battery will be charged if the aircraft is powered (Ext. Power, APU, one engine)
- Show Status Bar Flight Progress:
    - Select if the progress of the flight shall be shown in the top status of the flyPad screen.
- Show Colored Metar:
    - Enable or disable the colored raw METAR on the flyPad Dashboard.
- Time Displayed:
    - Select which time should be displayed in the top bar of the flyPad screens.  
- Local Time Format:
    - Select if local time should be shown in 12 or 24 hours format.
    - This setting is only available if Time Displayed is showing local time.
- Theme:
    - Select which coloring theme the flyPad should have.

### About

The About page provides the build information which is sometimes requested when seeking support on the FlyByWire Discord.

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-settings-about.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>