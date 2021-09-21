# Fuel and Weight

## Overview

This short appendix describes appropriate loading of fuel and weights for the A32NX to ensure that you have the best center of gravity (CG) configured for the aircraft.

!!! danger "Please do not touch values in MSFS Fuel & Weights window in the toolbar."

### A32NX Configuration

**Development + Experimental Version Only** - See our [simBrief Profile](../installation.md#simbrief-airframe)

- OEW (Empty Weight): 46262 (in kilograms)
- MZFW (Max Zero Fuel Weight): 64300 (in kilograms)
- MTOW (Max Takeoff Weight): 79000 (in kilograms)
- MLW (Max Landing Weight): 67400 (in kilograms)
- Max Fuel Capacity: 19045 (in kilograms)
- Passenger Weight: 140 (in kilograms)

## Zero Fuel Weight

In simple terms the zero fuel weight (ZFW) is the empty weight of the aircraft + payload. The payload would be pilot, passengers, baggage, and no fuel on board. In a situation where your payload would be something like 14000kg *based on our new airframe:* 

!!! tip ""
    Your ZFW would total - 60262kg

You can reference this against any OFP you may have generated through simBrief. For usage of our simBrief integration - [read here](simbrief.md).

## Zero Fuel Weight Center of Gravity

The A32NX simBrief integration's auto-loading feature allows for automated ZFWCG configuration. The auto population of ZFW and ZFWCG on the INIT B page (once the aircraft and associated payload is loaded into the simulator) will accurately reflect what simBrief has configured when you have generated an OFP. 

- See our [Loading Fuel & Weights](simbrief.md#loading-fuel-and-weight) section in the simBrief integration feature guide.
- You can read about INIT B configuration [here](../../pilots-corner/beginner-guide/preparing-mcdu.md#init-b).

## Center of Gravity

An acceptable range for takeoff CG in the A32NX is between 16-40%. An easy way to check your takeoff CG is to open the MSFS fuel and weights window from the toolbar. It will show you the current CG of the aircraft.

!!! info ""
    It would be best to check MSFS fuel and weights window shortly before takeoff to account for taxi fuel burned.

[sample image here]

Trimming the aircraft for takeoff can be optional, we recommend pilots continue to trim their aircraft based on the reported CG value on INIT B or on your simBrief OFP prior to takeoff. "Auto-rotation" indicates an issue with your CG being well aft of the limits (and/or THS too far nose up).

Ideally, anything less than 25% CG is considered FWD load, and anything more than 25% is considered an AFT load.

!!! info "Notes on Differing CG Configurations"
    There are a few arguments worth considering when it comes to favoring an aft CG or fwd CG. Generally an aft CG would provide for better aircraft performance (lower stall speed, drag, and angle of attack for a given lift coefficient) but generally worse for pitch stability. 

    This does not equate to have better takeoff or landing performance with an aft CG configuration. For a smaller aircraft as the A320neo, most operators would favor an aft CG loading for fuel consumption benefits when considering the lifetime of the a fleet and how easy the benefits can be obtained.

    While opting to choose between either CG configuration (aft/fwd) please consider the above information.
    