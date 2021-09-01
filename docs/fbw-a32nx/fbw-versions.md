# Versions and Features

## Version Overview

=== "Development Version (recommended)"

    Development will have the latest features that will eventually end up in the next stable release. 
    
    In general this version has the latest fixes and newest features but also a slightly higher risk of containing bugs as features had less time to be used and tested by users.

    This version updates often and sometimes several times a days. We recommend to update this version via our installer before every start of the simulator.

    Every addition to the development version is code-reviewed and tested by several people, our QA Team and also interested users. In general it tends to be very stable and robust.

    Latest additions to this version can be seen either in the official [CHANGELOG](https://github.com/flybywiresim/a32nx/blob/master/.github/CHANGELOG.md) or the commits to the master branch of the project: [Github Commits to Master](https://github.com/flybywiresim/a32nx/commits/master){target=new}

=== "Stable Version"

    !!! info ""
        **Current Stable Version - v0.6.3**

    Stable is our version which has features that are the most mature and most tested. This should be a reliable version for those users preferring stability over newest features.

    This version will not always be up to date but we work hard at ensuring its compatibility with the current version from Microsoft Flight Simulator.

=== "Experimental Version"

    This version is similar to the development version, but contains custom systems in earlier development phases.
    
    Currently the new FlyByWire Custom Flight Management System (cFMS) is available in the Experimental version.
    
    The experimental version will be updated with the latest changes to the cFMS regularly and also with the latest changes to the Development version. Expect updates about once a week (not guaranteed).     
    
    !!! warning 

    Please read [Experimental Version Support Page](support/exp.md) before using this version.

    !!! danger "No Support for Experimental - use at own risk"
        Please do not seek support for the Experimental Version on Discord and only report issues if you have read this page and the reported and known issues. You can report issues in the Discord channel "#ata-22-fms" in the thread "[CFMS LNAV ONLY Bugs + Issues](https://discord.com/channels/738864299392630914/876140343735771147/882442909918584862){ target=new }".

=== "Marketplace Version"

    This version is similar to Stable but is available via the Microsoft Flight Simulator in-sim marketplace.

    !!! warning ""
        **Due to Sim Update 5 platform stability issues that are out of our control, we have withdrawn the A32NX from the MSFS marketplace until further notice.**

## Version Comparison

This is a curated list with the most important features for users and
will be updated at least once a month.

For all changes refer to the official [CHANGELOG](https://github.com/flybywiresim/a32nx/blob/master/.github/CHANGELOG.md){target=new} or commits on the [:fontawesome-brands-github:{: .github } - **GitHub A32NX Repository Master Branch**](https://github.com/flybywiresim/a32nx/commits/master){target=new}.

| Feature                                                                                                                        |   Stable 0.6.3   | Development<br/>(Aug 21th 2021) |
|:-------------------------------------------------------------------------------------------------------------------------------|:----------------:|:-------------------------------:|
| Standalone Aircraft                                                                                                            | :material-check: |        :material-check:         |
| EFB                                                                                                                            | :material-check: |        :material-check:         |
| EFB Simbrief Integration                                                                                                       | :material-check: |        :material-check:         |
| EFB Ground Handling                                                                                                            | :material-check: |        :material-check:         |
| Printer                                                                                                                        | :material-check: |        :material-check:         |
| Custom Electrical System                                                                                                       | :material-check: |        :material-check:         |
| Custom APU Simulation                                                                                                          | :material-check: |        :material-check:         |
| Improved Flight Model Accuracy                                                                                                 | :material-check: |        :material-check:         |
| Split RMP1 and RMP2 Radios                                                                                                     | :material-check: |        :material-check:         |
| Custom Camera Views                                                                                                            | :material-check: |        :material-check:         |
| Support for CONF 3 (flaps 3) Landings                                                                                          | :material-check: |        :material-check:         |
| TRK/SPA Mode                                                                                                                   | :material-check: |        :material-check:         |
| GPWS Improvements                                                                                                              | :material-check: |        :material-check:         |
| Brake Fan                                                                                                                      | :material-check: |        :material-check:         |
| MCDU/FMC Improvements                                                                                                          | :material-check: |        :material-check:         |
| Forced Usage of Modern Flight Model                                                                                            | :material-check: |        :material-check:         |
| Sim Update 5 (SU5) Fixes (Aug 9th)                                                                                             | :material-check: |        :material-check:         |
| Custom Hydraulic System (initial implementation)                                                                               |                  |        :material-check:         |
| Connection between Electrical Power and Hydraulics                                                                             |                  |        :material-check:         |
| VOR/ADF Needles on ND                                                                                                          |                  |        :material-check:         |
| New PFD (in react)                                                                                                             |                  |        :material-check:         |
| BRG/DIST Feature on ECAM PROG Page                                                                                             |                  |        :material-check:         |
| Custom Fly-by-wire System                                                                                                      |                  |        :material-check:         |
| Custom Autopilot (with Autoland feature)                                                                                       |                  |        :material-check:         |
| Custom Autothrust                                                                                                              |                  |        :material-check:         |
| EFB Throttle Calibration                                                                                                       |                  |        :material-check:         |
| Improved AP, ROLL OUT and Ground Spoiler Logic                                                                                 |                  |        :material-check:         |
| Descent Initiation via FCU V/S Knob                                                                                            |                  |        :material-check:         |
| Improvement to Custom Fly-by-wire System (Protections)                                                                         |                  |        :material-check:         |
| Push FCU V/S Knob during APPR to Level off                                                                                     |                  |        :material-check:         |
| More EVENTS and LVARS for External Control                                                                                     |                  |        :material-check:         |
| Seatbelt Sign Sync to FCUIPC                                                                                                   |                  |        :material-check:         |
| Hydraulics ECAM Page                                                                                                           |                  |        :material-check:         |
| OVHD ANN Lt DIM functionality                                                                                                  |                  |        :material-check:         |
| Brakes use Hydraulic System                                                                                                    |                  |        :material-check:         |
| Custom Autobrake                                                                                                               |                  |        :material-check:         |
| APU Heat Blur                                                                                                                  |                  |        :material-check:         |
| ISIS and CHRONO Auto Brightness                                                                                                |                  |        :material-check:         |
| ISIS Brightness Button Push & Hold                                                                                             |                  |        :material-check:         |
| Support FD OFF Take-off Procedure                                                                                              |                  |        :material-check:         |
| Improved FCU init values (SPD=100kts, HDG=0°, ALT=100ft)                                                                       |                  |        :material-check:         |
| ILS Auto-tuning for Departure and Approach                                                                                     |                  |        :material-check:         |
| Scratchpad clear on CLR held                                                                                                   |                  |        :material-check:         |
| Improved Cold Engine Start-up Model                                                                                            |                  |        :material-check:         |
| Adapted t.o. A/THR Engagement                                                                                                  |                  |        :material-check:         |
| ISA Deviation on ECAM SD                                                                                                       |                  |        :material-check:         |
| MCDU Keyboard Input                                                                                                            |                  |        :material-check:         |
| New Potentiometer for Lights and Screens                                                                                       |                  |        :material-check:         |
| Improved CHRONO Logic                                                                                                          |                  |        :material-check:         |
| Pixelated Screens                                                                                                              |                  |        :material-check:         |
| Advanced ADIRs Implementation                                                                                                  |                  |        :material-check:         |
| Automatic and Improved Cabin Pressurization                                                                                    |                  |        :material-check:         |
| Preselected Speeds in ECAM PERF Pages                                                                                          |                  |        :material-check:         |
| Correct QNH Flashing at TL/TA                                                                                                  |                  |        :material-check:         |
| Several Sound Enhancements                                                                                                     |                  |        :material-check:         |
| Several Texture and Graphics Enhancements                                                                                      |                  |        :material-check:         |
| Auto Print on Printer when PRINTER is Selected                                                                                 |                  |        :material-check:         |
| EFB flyPadOS v2 New Layout, add. Settings and Features                                                                         |                  |        :material-check:         |
| EFB Navigraph Integration                                                                                                      |                  |        :material-check:         |
| EFB VATSIM/IVAO Frequencies, Landing Performance                                                                               |                  |        :material-check:         |
| EFB Landing Performance Calculator                                                                                             |                  |        :material-check:         |
| Workaround for Altitude Issues of MSFS                                                                                         |                  |        :material-check:         |
| Initial implementation of failures ( [#5359](https://github.com/flybywiresim/a32nx/pull/5359){target=new} )                    |                  |        :material-check:         |
| EFB: Make OFP font size persistent ( [#5538](https://github.com/flybywiresim/a32nx/pull/5538){target=new} )                    |                  |        :material-check:         |
| Un-mirror sharklet textures ( [#5490](https://github.com/flybywiresim/a32nx/pull/5490){target=new} )                           |                  |        :material-check:         |
| Improved handling of rudder axis plus/minus ( [#5636](https://github.com/flybywiresim/a32nx/pull/5636){target=new} )           |                  |        :material-check:         |
| EFB: Power Button  ( [#5624](https://github.com/flybywiresim/a32nx/pull/5624){target=new})                                     |                  |        :material-check:         |
| EFB: Tabbed Settings Page and Auto-brightness Option ([#5524](https://github.com/flybywiresim/a32nx/pull/5524){target=new})    |                  |        :material-check:         |
| Completed custom sounds for all sounds                                                                                         |                  |        :material-check:         |
| Cockpit door lock sounds                                                                                                       |                  |        :material-check:         |
| Realistic reduction of loudness of chimes in cockpit when door locked                                                          |                  |        :material-check:         |
| Notification Popup when changes to settings need reload ([#5261](https://github.com/flybywiresim/a32nx/pull/5261){target=new}) |                  |        :material-check:         |
