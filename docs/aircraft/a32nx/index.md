---
title: FlyByWire A32NX - Overview 
description: Documentation and resources for the FlyByWire A32NX add-on for Microsoft Flight Simulator 2020.
---

<link rel="stylesheet" href="../../stylesheets/toc-tables.css">

# FlyByWire A32NX Overview

This section of the FlyByWire Documentation is dedicated to the A32NX add-on itself. It covers the software and more technical aspects of the FlyByWire add-on.

The A32NX Project is a community-driven open-source project to create a free Airbus A320neo in Microsoft Flight Simulator that is as close to reality as possible. It started out as an enhancement project to the default A320neo and is now proceeding as an independent add-on project aiming to bring the FlyByWire A32NX up to payware-level systems depth and functionality, all for free.

### **Aircraft Configuration(s)**

The following aircraft configurations are currently simulated:

```title="Simulated Hardware"
Model       A320-251N
Engine      CFM LEAP 1A-26
APU         APS3200
FMS         Honeywell Release H3
FWC Std.    H2F13
RA          Honeywell ALA-52B
TAWS        Honeywell EGPWS
ACAS        Honeywell TPA-100B
ATC         Honeywell TRA-100B
MMR         Honeywell iMMR
WXR         Honeywell RDR-4000
ACSC        S1803A0001
```

## Quick Links

<div class="grid cards" markdown>

- **Support Guide**
    
    ---
    
    Troubleshoot basic issues and learn how to use the FlyByWire A32NX.
    
    [:octicons-arrow-right-24: Getting started](../support/index.md)
    
- **Reported Issues**

    ---
    
    View a list of reported issues and their status.
        
    [:octicons-arrow-right-24: View Issues](../support/known-issues/known-issues)

- **Feature Guides**

    ---
    
    Learn how to use the various FlyByWire A32NX's features.
    
    [:octicons-arrow-right-24: View Guides](feature-guides/index.md)

- **Throttle Calibration Guide**
    
    ---
        
    Calibrate your throttle to work with the FlyByWire A32NX.
        
    [:octicons-arrow-right-24: View Guide](../common/flypados3/throttle-calibration.md)

</div>

##  Topics

| Featured List                                           |
|:--------------------------------------------------------|
| [Installation Guide](../install/installation.md)        |
| [Version and Feature Guide](../install/fbw-versions.md) |
| [Livery Guide](../install/liveries.md)                  |
| [Support](../support/index.md)                          |
| [API and Hardware](a32nx-api/index.md)                  |

## A32NX Quick FAQ

???+ info "Q: I cannot hear the Flaps or PTU in the cockpit anymore?"
    This change was made due to feedback from IRL A320 pilots who identified the sounds could not be heard from the cockpit IRL as they currently are in the simulator.

    The PTU has a toggleable switch on the EFB (flyPad) settings that allows you to hear it in the cockpit when it is running.

??? info "Q: Why is the overall interior lighting different? (Blue light effect on pedestal and displays)"
    Based on IRL A320 pilot feedback, the blue light effect can only be seen from images. Also, the pedestal should be dark at night to improve pilots' vision at night.

??? info "Q: Why does light bleed into the cockpit? Can this be fixed?"
    Unfortunately, no - This is a more profound issue which will require work from the Asobo team.

??? info "Q: The new sounds are different from the default ones, why?"
    The default sounds were shared sounds from other default aircraft. The new sounds are accurate and very well-developed based on the A320 and A320neo pilot feedback.
