---
title: FlyByWire A380X - Overview 
description: Documentation and resources for the FlyByWire A380X add-on for Microsoft Flight Simulator 2020.
---

<link rel="stylesheet" href="../../stylesheets/toc-tables.css">

# FlyByWire A380X Overview

This section of the FlyByWire Documentation is dedicated to the A380X add-on. It covers the software and more technical aspects of the FlyByWire add-on.

### Aircraft Configuration

The following aircraft configurations are currently simulated:

```title="Simulated Hardware"
Model       A380-842
Engines     Rolls-Royce Trent 972B-84
APU         APU - Pratt & Whitney PW980
WV          003
TAWS        Honeywell AESS
ACAS        Honeywell AESS
ATC         Honeywell AESS
WXR         Honeywell AESS
```
## Quick Links

<div class="grid cards" markdown>

- **Support Guide**
    
    ---

    Troubleshoot basic issues and learn how to use the FlyByWire Products.

    [:octicons-arrow-right-24: Getting started](../support/index.md)

- **Reported Issues**

    ---

    View a list of reported issues and their status.

    [:octicons-arrow-right-24: View Issues](../support/known-issues/known-issues)

- **Feature Guides**

    ---

    Please see our initial list of available features below. Guides pending.

    [:octicons-arrow-right-24: Feature List](feature-guides/index.md)
  philippe@dellaert.org
</div>

## A380X Quick FAQ

The list below will be updated as best as possible. If you have any questions, please feel free to ask in our Discord server and see our [#a380x-faq](https://discord.com/channels/738864299392630914/1300949191740358757) channel for the latest updates.

### General

???+ info "Q: What about Performance and System Requirements"
    We have recently provided a system requirements list for the A380X in our recent NOTAM. You can find it in our [Installation Guide](../install/installation.md#estimated-system-requirements-for-a380x).

    As a baseline please expect to see a framerate reduction of up to -25% compared to the default A32NX. We are working on improving this in the future as the A380X is in an 
    alpha state and certain aspects of the model or textures may not be fully optimised for performance.

    There are other factors than can affect the performance of the A380X in the simulator. Below is a short list.    

    - Using the A380X in conjunction with other addons can potentially have an impact on performance numbers such as:
        - FSLTL
        - Scenaries
        - Etc.
    - Graphical features such as DX12 Beta and Frame Generation

??? info "Q: Can I use the foldout keyboard in front of the pilot?"

    This foldout keyboard (which extends from below the PFD/ND) can't be used currently. In real-life operations, this keyboard can also only be used for OIT input, and OIT is 
    not yet implemented in the A380X.

??? info "Q: Is there a taxi cam?"
    Due to sim limitations there isn't a taxi cam mode on the instruments available. We will provide preset camera *views* however which you can use as a solution.

??? info "Q: Will there be a performance calculator?"

    We suggest using the (free) simBrief calculator for the time being, as it has been found to provide acceptable 
    outputs for the current configuration of the A380X.

    We might implement a performance calculator in the future, but it is not a priority at the moment.

??? info "Q: Will hardware and gear from the A32NX work on the A380X (e.g. FCU Hardware)?"

    While there are some differences in some variables for the physical controls, most of them do follow the same naming scheme as the A32NX. That being said, some changes maybe required, so we recommend you create separate profiles for both aircraft.

??? info "Q: What approaches can be flow with the A380X?"

    All types of approaches can be flown, with a differing degree in enabled automation.

    - ILS: Can be flown without problems, also as CAT/LAND 3 DUAL with AUTOLAND
    - FLS, F-G/S, F-LOC: Not yet implemented
    - Other non-precision approaches: You will have lateral guidance through NAV mode, but vertical guidance only through the FPA mode.

    <sub>Note: FINAL APP is a mode which can only be found on the A320 family in real-world operations for RNP (AR) approaches. As such, the A380X also doesn't implement it. Use the above method to fly other non-precision approaches.</sub>

??? info "Q: Can I use hardware that only has 1 or 2 levers instead of 4?"

    Absolutely! We have adjusted our Throttle Configuration page to allow using 1, 2 or 4 throttles for using with your hardware! Mapping of the axis will need to be done by the MSFS binding menu (or external software).

??? info "Q: Can you open the passenger and cargo door in the model?"

    Not all of them, some haven't been fully modeled (especially the ones in the upper deck). But you will be able to open the passenger doors from the inside using the lever. And also move the arm/disarm lever, albeit without function right now.

    The forward and aft cargo doors can be opened via the EFB, on the "Services" page using the Cargo Door button. The bulk cargo door is not yet animated.

    The cockpit door is animated and can be opened/closed, the locking mechanism which isn't implemented yet though, so you can open/close it no matter what.

??? info "Q: Does the A380X have a cabin?"

    Our aircraft has a detailed cabin, with careful attention to detail and craftmanship. Please note that its still an on-going effort, and changes/corrections will be done in future releases.

??? info "Q: Will there be online documentation, checklists or SOPs (standard operating procedures) documents?"

    Of course! Please visit our [Pilot's Corner](../../pilots-corner/a380x/index.md) for more information.

??? info "Q: What liveries will be included?"

    The A380X will come with a house liveries, but we recommend downloading compatible liveries from [Flightsim.to](https://flightsim.to/c/liveries/flybywire-a380x/){target=new} when they become available.

??? info "Q: Where will I be able to download the A380X"

    You will be able to download and install via the FlyByWire Installer! See our [Installation Guide](../install/installation.md) for more information.

### Onboard Systems

??? info "Q: Is the Vertical Situation Display (VSD) functional?"

    Partially. The VSD will only display the terrain ahead, but currently won't display the flight plan.

??? info "Q: Is there a terrain display?"

    Yes the ND can project a map of the terrain when using SimBridge. You can enable terrain on ND by pressing the `TERR` button on the EFIS panel.

??? info "Q: Does the EFB on the First Officer (FO) side work?"
    The EFB currently receives touch input but does not have a display. It will be fully operational in the future.

??? info "Q: Why is the 2nd ISIS blank?"
    The 2nd ISIS has been disabled due to some technical difficulties. It will be re-enabled in the future.

??? info "Q: What does the screen between the EFB and the PFD do that's blank?"
    This is called the OIT (Onboard Information Terminal). It will be INOP for the initial release of the A380X.

    **Can the OIT be used for the EFB?**

    Currently this is not possible due to size differences. Most likely this won't be used for the EFB but reserved for aircraft related functionality.

??? info "Q: Can I use the MFD/FMS with two separate screens?"

    Yes, the left and right MFD can be operated independently. You can open different pages on each of them.

### 3rd Party Integrations

??? info "Q: Is there a SimBrief Airframe and SimBrief Support?"

    **Airframe**

    We have released a compatible airframe. You will be able to find it on SimBrief natively, without having to import or add one.

    **Simbrief Support**

    Yes! Our EFB and the FMS initialization allows for the use of SimBrief profiles. You can use a Navigraph account or a SimBrief ID to enable this functionality. 

    A subscription is not required for using SimBrief, but note that free SimBrief tiers use older AIRAC cycles and might show import errors or not include specific procedures. It is your responsibility to validate this data for your flight plan, especially when flying in online networks.

??? info "Q: Does the A380X support GSX"

    Yes! The aircraft will have a GSX config file included so you won't have to download or configure anything additional.

    <sub>Please note that scenery configurations will require an update for the out-most compatibility with the aircraft due to its ICAO. Contact the creator of each airport-specific configuration file.</sub>

??? info "Q: What about cabin passengers?"

    This is a feature GSX will need to configure and add to their software, please contact the GSX developer via their forums.

??? info "Q: Will I require a Navigraph subscription for OANS and BTV"

    No, you will not require a Navigraph subscription for OANS and BTV. The data is provided by the simulator itself.

    OANS: Currently, a Navigraph Unlimited subscription is required to show airport maps on the ND. We are planning to work on integrating another free data source, but don't commit on a timeline. 

    BTV: You can operate BTV without a Navigraph subscription. The desired braking distance can either be selected graphically through the OANS (see above, Navigraph required), or entered manually in the OANS control panel if you don't have a subscription. Both ways are described in the A380X advanced guide for OANS/BTV.

    [OANS/BTV Guide](../../pilots-corner/a380x/a380x-advanced-guides/oans-btv.md){.md-button}



