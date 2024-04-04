---
title: Wheel Chocks and GSE Safety Cones
description: Ensure safe ground operations with wheel chocks and GSE Safety Cones around the FlyByWire A32NX.
---

# Wheel Chocks and GSE Safety Cones

## Overview

This page details the safety equipment available when parked with the A32NX. Other than just looking gorgeous, the wheel chocks even apply some braking force to hold the aircraft in place.

The flight crew activates the Wheel Chocks and Safety Cones through the 
[flyPad EFB Sim Option Settings](flypados3/settings.md#sim-options).
This simulates the ground crew automatically placing or removing the chocks or cones. The ground crew will determine if chocks and cones should be placed or removed based on specific criteria, which are described in the [next section](#usage).

!!! block ""
    ![Wheel Chocks](../assets/feature-guides/chocks-cones/chocks.png "Wheel Chocks"){loading=lazy align=left width=45%}
    ![Wheel Chocks](../assets/feature-guides/chocks-cones/chocks_2.png "Wheel Chocks"){loading=lazy align=left width=45%}
     <br>
    ![GSE Safety Cone](../assets/feature-guides/chocks-cones/cones.png "GSE Safety Cone"){loading=lazy align=left width=45%}
    ![EFB Ground Buttons for Chocks and Cones](../assets/feature-guides/chocks-cones/efb-ground-chocks-cones.png "EFB Ground Buttons for Chocks and Cones"){loading=lazy align=left width=45%}

## Usage

The Wheel Chocks and Safety Cones appear when the following conditions are given:

- Chocks and/or Safety Cones are enabled in the [flyPad EFB Sim Options Settings Page](flypados3/settings.md#sim-options)
- Engines are off (`ENG1+2 N1` < 3.5 %)
- Beacon lights are off
- Airplane is on ground
- Airplane is not moving / rolling
- Pushback is disconnected

The flyPad Ground page will show `Wheel Chocks` and/or `Safety Cones` in 

- <span style=color:green>green</span> if this ground equipment is enabled and visible.
- <span style=color:gray>gray</span> if this ground equipment is enabled but not visible due to the above criteria not 
  being 
  met. 

If chocks are in place, there will be brake force applied to the aircraft, so it should not move even when the parking brake is disengaged.

If any of the above conditions are not given, the chocks and cones will disappear (ground crew will virtually have them removed).
