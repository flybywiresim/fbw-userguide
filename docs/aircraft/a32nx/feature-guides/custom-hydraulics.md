---
title: Custom Hydraulics
description: Explore the detailed workings of the A32NX's custom hydraulics system, including features, known issues, and expert tips.
---

# Custom Hydraulics

## Gear system
Our new gear system aims at replicating its real counterpart even in the slightest details. While further enhancements will come, the current system already features:

- Rigid body physics of gears and doors, affected by aerodynamics
- Hydraulic actuators' simulation with "push to retract" main gears and "push to extend" nose gear
- All proximity sensors, one set per LGCIU computer
- LGCIU computers monitoring, sequence control state machine and their change-over mechanism
- Safety valve / Shut off valve / Vent valves controls
- Gear lever bulk lock mechanism powered by LGCIUs
- Emergency extension system
- Failures

!!! warning "Not Yet Implemented"
    Non-exhaustive list of features yet to come:

    - Doors vs. gear collisions
    - Complete fault monitoring and BITE tests of LGCIUs

### Functionality
Using the gear system should not be different from before. Selecting gear up will switch to the next available LGCIU computer available, and will start the retracting sequence. Gear down will start the extension sequence same as before.

However, because it's now closer to the real system under the hood, you have to be aware of some subtleties of the gear system.

Since all the hydraulics are simulated, the behavior of the system will highly depend on the hydraulic status of the plane. Even in nominal conditions, the gear system is such a high flow consumer that it can impact the green system pressure. In turn, this will also trigger the PTU to help provide hydraulic power from the yellow side. 

Be aware that any degraded condition will impact the behavior of the retraction/extension sequence. PTU being off will cause green system pressure to reach lower pressure level during the sequence, while using only yellow electric pump for the gear sequence might cause LGCIU faults as the sequence can get quite a long time to perform.

Be aware that there's a safety valve that will cut off any hydraulic supply to the gear system above approximately 260kts. This safety system is independent of LGCIU computers, and if you use the gear while crossing that speed limit, strange behavior and ECAM faults are to be expected.

If such a situation happens:

- Get your speed below 260 kt (which is already too high!!)
- Getting the gear lever back to the down position, then to up, will hopefully switch on the second LGCIU computer and save the day.

!!! tip "Always check your speed when using the gear system, and everything will be ok!"  

### Failures
Some first failures are provided, and while ECAM information impact is a temporary placeholder, consequences on the gear system are fully modeled.

- LGCIU power input failure will cause complete electrical loss of the computer and its outputs. Other LGCIU will take control to ensure gear control. 

!!! tip "Power failure on LGCIU1 will cause the gear light indicator to be lost."
!!! tip "A failed LGCIU can be reset by toggling this fault on and off, as would a circuit breaker cycle do."

- LGCIU internal error failure will cause the LGCIU to fail its internal continuous tests. It will declare a fault and other LGCIU will take control to ensure gear control. Power input in that case is still present, so an internal error on LGCIU1 will still maintain the gear light indicator.

- Proximity sensor failure are physical issues on the considered LGCIU sensors. Those cannot be electrically detected by the computer, so it may cause gear retraction or extension sequence to fail and get stuck. A LGCIU fault will finally be declared because of too long sequence time. A gear lever recycling down to up will switch gear control to the other computer to complete the current sequence.

!!! tip "Only issues on LGCIU1 proximity sensors will show erroneous information on the gear light indicator."

### Gravity Extension
Gravity extension is fully supported by our gear system. 

To use this mechanical-only device, you need to deploy the handle by clicking on the emergency crank handle back on the center pedestal.
Then every click of the handle, or using the mouse scroll wheel, will make the handle turn once.
It can be stowed back by clicking on the black plastic lock at any time.

Each turn of the handle will cause various things to happen:

- After 1 turn, hydraulic supply to gear system is closed
- After 2 turns, doors uplocks will be released and doors will stay opened
- During the last third turn, all gear uplocks will be mechanically released and gears go down

To revert the process and stow the crank handle back into its place, just click again until the handle is stowed back

!!! tip "The lower the speed, the harder it will be to have a full down lock of the gear, especially for the main gear. Doing steep turns to increase the load of the plane can be quite effective to help the gears to lock into place."

!!! warning "Don't rush the handle turning"
    The lower the speed, the slower doors will open due to smaller aerodynamic forces. Turning the handle too fast might cause the gears to hit the doors that have not yet fully opened. Always wait 3 to 5 seconds between handle turns.

!!! warning "Before Using Gravity Extension"
    Have the plane correctly stabilized before using this procedure. Remember that gears are physically simulated, and are really heavy. Bank angle and/or load factor WILL have impacts on:

    - The extension time  
    - Asymmetry  
    - Ability to reach downlock position

!!! warning "Gear lever when using gravity extension"
    When gravity extension is used, you have to set gear lever to down position to avoid possible LGCIU faults. 
    
### Known Issues

{--

**Please Note:** Gear system can only be used through in game binding events or in-cockpit lever. Writing to simvars to control gear is not supported.

--}

- If a hardware input is set to GEAR UP or GEAR DOWN, the in-cockpit lever cannot be clicked or mouse dragged.
