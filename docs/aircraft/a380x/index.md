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
APU         Honeywell 331-350C (Confirm)
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

    [:octicons-arrow-right-24: View Issues](../support/reported-issues.md)

- **Feature Guides**

    ---

    Please see our initial list of available features below. Guides pending.

    [:octicons-arrow-right-24: Feature List](feature-guides/index.md)

[//]: # (    Learn how to use the various FlyByWire A380X's features.)

[//]: # ()
[//]: # (    [:octicons-arrow-right-24: View Guides]&#40;feature-guides/index.md&#41;)

[//]: # (- **Throttle Calibration Guide**)

[//]: # (    )
[//]: # (    ---)

[//]: # ()
[//]: # (    Calibrate your throttle to work with the FlyByWire A380X.)

[//]: # ()
[//]: # (    [:octicons-arrow-right-24: View Guide]&#40;../common/flypados3/throttle-calibration.md&#41;)

</div>

## A380X Quick FAQ

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

??? info "Q: Will there be a performance calculator?"

    We aim for the outmost accuracy with our projects, and as such we want to hold on making a performance calculator that could potentially provide bad data. 

    We suggest using the (free) simBrief calculator for the time being, as it has been found to provide acceptable outputs for the current configuration of the A380X.

??? info "Q: Is the Vertical Situation Display (VSD) functional?"

    Partially. The VSD will only display the terrain ahead, but currently won't display the flight plan.

??? info "Q: Is there a terrain display?"

    Yes the ND can project a map of the terrain when using SimBridge. You can enable terrain on ND by pressing the `TERR` button on the EFIS panel.

??? info "Q: Is there a taxi cam?"
    Due to sim limitations there isn't a taxi cam mode on the instruments available. We will provide preset camera *views* however which you can use as a solution.
  
??? info "Q: Does the EFB on the First Officer (FO) side work?"
    The EFB currently receives touch input but does not have a display. It will be fully operational in the future.

??? info "Q: why is the 2nd ISIS blank?"
    The 2nd ISIS has been disabled due to some technical difficulties. It will be re-enabled in the future.

??? info "Q: What does the screen between the EFB and the PFD do that's blank?"
    This is called the OIT (Onboard Information Terminal). It will be INOP for the initial release of the A380X.

    **Can the OIT be used for the EFB?**

    Currently this is not possible due to size differences. Most likely this won't be used for the EFB but reserved for aircraft related functionality.