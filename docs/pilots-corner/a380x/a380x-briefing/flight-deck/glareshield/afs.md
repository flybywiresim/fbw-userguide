---
title: Auto Flight System (AFS) Control Panel
description: The A380 Flight Deck Auto Flight System (AFS) Control Panel description.
---

# Auto Flight System (AFS) Control Panel

---

[Back to Main Instrument Panel and Glareshield](../overviews/main-glare.md){ .md-button }

---

![img.png](../../../assets/a380x-briefing/flight-deck/glare/aps.png)

## Description

The AFS Control Panel is the main interface with the FG. The flight crew can:

- Use [managed](#managed-targets) or [selected](#selected-targets) guidance
- Pick targets for short-term guidance (speed/Mach, heading/track, altitude, vertical speed/flight path angle)
- Use the AP, FD and A/THR
- Show altitude in meters
- Choose between magnetic or true North reference.
- If the AFS CP fails, the MFD FCU BKUP / AFS CP page has all the AFS CP controls and indicators

### Auto Flight System (AFS)

The Auto Flight System (AFS) includes:

- The Flight Guidance (FG)<br/>
  The FG gives guidance based on flight targets picked by the flight crew, or managed by the Flight Management System.
- The Flight Management System (FMS)<br/>
  The FMS handles the flight plan, set by the flight crew, and gives flight parameters to the FG accordingly.

### Flight Guidance (FG)

The FG's job is to give lateral and vertical guidance, including speed or Mach control, based on set targets. 
These targets can be either selected or managed.

#### Selected Targets

The flight crew picks the targets via the short-term interface: The AFS Control Panel (CP). Then the FG uses these 
targets to give selected guidance.

#### Managed Targets

The flight crew uses the long-term interface, the Multi Function Display (MFD), to set up the flight plan. The FMS 
calculates managed targets accordingly. Then the FG uses these targets to give managed guidance.

### AFS CP Philosophy

On the AFS CP, the SPD/MACH, HDG/TRK, V/S / FPA knobs can be turned, pulled, and pushed. This lets the flight crew:

- Preselect a target: Turn
- Use a mode that will guide the aircraft to a **selected** target: Pull
- Arm or use a mode that will guide the aircraft to a **managed** target: Push.

Here is an example with the ALT (altitude) knob:<br/>
![aps-knob-push-pull.png](../../../assets/a380x-briefing/flight-deck/glare/aps-knob-push-pull.png)<br/>
Pull = Selected / Push = Managed

### FG FUNCTIONS: AP, FD AND A/THR

To do its job (lateral guidance, vertical guidance, including speed or Mach control), the FG uses:

- The Autopilot 1 and/or 2 (AP1 and/or AP2)<br/>
  The AP gives flight guidance by calculating pitch, roll, yaw and nosewheel steering orders.
- The Flight Directors 1 and 2 (FD1 and FD2)<br/>
  The FDs show guidance orders on the PFDs to help the flight crew fly the aircraft manually. When the AP is on, the 
  flight crew can use the FD orders to monitor the guidance.
- The Autothrust (A/THR)<br/>
  A/THR controls the thrust by sending commands to the engines.

### FLIGHT MANAGEMENT SYSTEM (FMS)

The Flight Management System (FMS) gives **long-term guidance** along the set flight plan.

To do these long-term tasks, the FMS calculates managed targets, that are then sent to the FG.

Besides long-term guidance, the FMS:

- Gives flight planning and navigation info
- Calculates and optimizes performance data
- Shows info on the MFD, ND and PFD.

### FLIGHT MANAGEMENT COMPUTER (FMC)

There are two FMSs (FMS1 and FMS2), that use three FMCs: FMC-A, FMC-B and FMC-C.

In normal operation:

- FMC-A runs FMS1
- FMC-B runs FMS2
- FMC-C is on standby, ready to run FMS1 or FMS2.
  Each FMC can run all the flight management functions.

### Flight Director (FD)

The Flight Director (FD) shows guidance orders on the Primary Flight Displays (PFDs):

- If no AP is on, the flight crew can manually fly the aircraft by following FD orders
- If at least one AP is on, the flight crew can use the FD to monitor the flight guidance.<br/>

When the FDs are on, the PFDs can show the roll, pitch and yaw bars.

When the FDs are on:

- The FD pb on the AFS CP lights up
- 1FD2 shows up on both FMAs
- When a mode is active, the PFDs show the FD orders.

### Autopilot (AP)

The Autopilot (AP):

- Stabilizes the aircraft around its center of gravity
- Controls the lateral path
- Controls the vertical path, or speed/Mach
- Works with the A/THR
- Does the automatic landing, or the go-around.

The AP generates:

- Pitch, roll, and yaw orders
- The nosewheel angle.

There are two APs: AP1 and AP2. Only one works at a time. AP1 uses ADIRS1, and AP2 uses ADIRS2.

AP1 and AP2 usually work separately. In some conditions (e.g. APPR mode), the flight crew can use both at the same time.

One AP works when the flight crew presses the AP1 pb or the AP2 pb on the AFS CP, and:

- The aircraft is in flight for more than 5 s
- The aircraft pitch, bank angle, and speed are not too much.
    - The pitch is between -11 ° and 22.5 °
    - The bank angle is less than 40 °
    - The speed is between VLS and VMAX.

When AP1(2) works:

- The AP1(2) pb lights up
- Both FMAs show:
    - AP1 (AP2)
    - AP1+2, if both APs are on.
  
The status of the AP shows in the AP, FD, A/THR status column of FMAs.

The standard way to manually turn off the AP is to press two times the sidestick pb on either sidestick.

The AP also turns off when the flight crew:

- Press the AP1(2) pb, while AP1(2) is already on, or
- Move a sidestick, or the sidestick deflection goes beyond 5° on pitch axis, or 6° on roll axis.
- Moves the rudder pedals. The rudder pedal deflection goes beyond 10°.

The AP automatically turns off, if one of the following happens:

- The aircraft pitch, bank angle, speed/Mach, or Angle Of Attack (AOA) becomes too much:
    - The pitch is below -13 °, or above 25 °
    - The bank angle is above 45 °
    - The speed is below VLS, or above VMO + 15 kt
    - The Mach is above MMO + 0.04
    - The AOA is above αprot + 1 ° (above 100 ft RA).
    - This does not apply in LAND below 200 ft RA.
- A failure happens in approach

Different warnings will trigger, depending on how it disconnects.

As the AP system is a complex system, a full description of the AP system goes beyond this briefing. It is planned to 
provide a dedicated advanced guide on the Auto Flight System (AFS) in the future.

### Autothrust (A/THR)

The A/THR is either armed, active, or off.

When active, the A/THR can work in two different types of mode:

- SPEED/MACH mode: The A/THR continuously adjusts the thrust to keep a speed/Mach target, e.g. during cruise, and approach
- THRUST modes: The A/THR controls a fixed thrust, based on the active THRUST mode.

The A/THR modes are automatically linked to the AP/FD vertical modes:

- When an AP/FD vertical mode controls the path (e.g. altitude acquire modes, altitude hold modes, V/S / FPA, G/S, 
  F-G/S), the A/THR is in SPEED/MACH mode
- When an AP/FD vertical mode adjusts the aircraft pitch to keep a speed/Mach target (e.g. climb, descent), the A/THR is
  in THRUST mode.

The flight crew uses the thrust levers to:

- Arm, activate, and turn off the A/THR
- Use the takeoff and go-around modes
- Manually control the thrust of each engine, when the A/THR is off
- Use reverse thrust on engine 2 and 3.
- The thrust levers have:
    - Four detents: 0 (idle), CL, FLX-MCT, TOGA.
    - Two instinctive disconnect pushbuttons.

When the A/THR is active:

- The FMA shows:
    - The A/THR message on the third line of the fifth column
    - The A/THR mode in green on the first line of the first column.
- The A/THR pb light is on the AFS CP.

As the A/THR system is a complex system, a full description of the A/THR system goes beyond this briefing. It is planned
to provide a dedicated advanced guide on the Auto Flight System (AFS) in the future.

## Usage

### SPD/MACH pb

If the speed (Mach) target is selected pressing the SPD/MACH pb changes the speed target to the corresponding Mach 
target, and vice versa.

### SPD/MACH Display

- Shows `SPD` and the selected speed in selected target mode. 
- Shows `MACH` and the selected mach speed in selected target mode.
- Shows `SPD` and `---` in managed target mode.
- Shows `MACH` and `---` in managed target mode.

Note: At the speed/Mach crossover altitude, the managed speed target automatically changes to a managed Mach target. The 
display on the SPD/MACH window changes from SPD to MACH (and vice versa in descent).

### SPD/MACH Knob

- When turned, preselects a speed or Mach target
- Note: 
    - When the SPD/MACH window is dashed, and if the flight crew begins to turn the knob without pulling it, the window 
      displays:
        - The current aircraft speed, if SRS TO, or SRS GA is on, or
        - The managed speed/Mach target, in all other cases.
    - Then, turning the knob would change the value. If there is no action on the knob for 45 s, the dashes reappear.
- When pulled, activates the selected speed or Mach target
- When pushed, the speed or Mach becomes managed.
  
One entire rotation of the knob equals 32 kt (1 kt per click), or 0.32 Mach (0.01 Mach per click).

The selection has a range of:

- 100 kt to 399 kt for the speed
- M 0.01 to M 0.99 for the Mach.

### TRUE/MAG pb

When pressed, changes the TRUE North reference to Magnetic (MAG) North reference, and vice versa.

The North reference is magnetic, unless the aircraft is in the polar zone.

When the aircraft reaches the polar zone:

- The North reference automatically changes from MAG to TRUE in the ADIRSs
- The following messages ask the flight crew to change from MAG to TRUE North reference:
    - The SELECT TRUE NORTH REF memo shows up on the ND
    - The NAV EXTREME LATITUDE triggers.

### HDG/TRK pb

When pressed, selects either:

- HDG-V/S: Heading (HDG) is linked with Vertical Speed (V/S)<br/>
  If the VV pb is pressed on the EFIS CP, the linked PFD shows the Velocity Vector (VV) in black.
- TRK-FPA: Track (TRK) is linked with Flight Path Angle (FPA)<br/>
  The PFDs show the Flight Path Vector (FPV) in green.

### HDG/TRK Display

- Shows `HDG` and the selected heading in selected target mode
- Shows `TRK` and the selected track in selected target mode
- Shows `HDG` and `---` in managed target mode
- Shows `TRK` and `---` in managed target mode

Note: The HDG/TRK window shows TRUE, at the top left corner of the HDG/TRK window, if TRUE is selected with the 
TRUE/MAG pb.

### HDG/TRK Knob

- When turned, preselects a heading or track target
- Note: When the HDG/TRK window is dashed, and if the flight crew begins to turn the knob without pulling it, the window 
  shows the current aircraft heading/track. Then, turning the knob would change the value. If there is no action on the 
  knob for 45 s, the dashes reappear. However, if a HDG/TRK preset is set, the value stays permanently.
- When pulled, activates the selected heading or track target
- When pushed, a managed lateral mode arms or works.

One entire rotation of the knob equals 32 ° (1 ° per click).

The selection has a range of 0° to 359°.

### LOC pb

When pressed, arms/works or disarms/stops the LOC, LOC B/C, or F-LOC mode.

### FD pb

When pressed, works/stops the FDs.

### AP1/2 pb

When pressed, works/stops the AP1 or AP2.

### A/THR pb

When pressed, arms/works or disarms/stops the A/THR.

### METER pb

When pressed, shows the current and target altitudes in meters (in addition to feet) on the PFDs. When pressed again, 
clears the meter display from the PFDs.

### ALT Display

Shows the altitude set by the flight crew with the ALT knob.

Note: The window never shows dashes.

### ALT Knob

When turned, sets the target altitude on the AFS CP.

The outer knob has two positions: 100 and 1000, to set the target altitude in increments of 100 ft or 1 000 ft.

- When pulled, activates the selected target altitude on the AFS CP. The FMS vertical profile is ignored.
- When pushed, the altitude target becomes managed. The FMS vertical profile is followed, or the AFS CP target altitude 
  is followed, if applicable.

### ALT pb

When pressed, the aircraft immediately starts to level-off.

Note: The ALT pb also lights up, when the aircraft keeps a selected or managed altitude.

### V/S / FPA Display

- Shows `V/S` and the selected vertical speed in selected target mode
- Shows `FPA` and the selected flight path angle in selected target mode
- Shows `V/S` and `---` in managed target mode
- Shows `FPA` and `---` in managed target mode

### V/S / FPA Knob

When turned, preselects a vertical speed or flight path angle target

Note: When the V/S / FPA window is dashed, and if the flight crew turns the knob without pulling it, the window shows 
the current V/S / FPA aircraft. Then, turning the knob would change the value. If there is no action for 45 s, the 
dashes reappear.

- When pulled, activates the selected vertical speed or flight path angle target.
- When pushed: There is no effect.

One entire rotation equals 1 600 ft/min in vertical speed (100 ft/min per 2 clicks), or 3.2 ° in flight path 
angle (0.1 ° per click).

The selection has a range of:

- –6 000 ft/min to +6 000 ft/min for the vertical speed
- –9.9 ° to + 9.9 ° for the flight path angle.

### APPR pb

When pressed, arms or disarms/stops the APPR modes.

---

[Back to Main Instrument Panel and Glareshield](../overviews/main-glare.md){ .md-button }

---