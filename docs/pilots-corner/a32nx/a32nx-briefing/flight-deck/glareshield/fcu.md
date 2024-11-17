# Flight Control Unit

---

[Back to Flight Deck](../index.md){ .md-button }

---

![Flight Control Unit (FCU)](../../../assets/a32nx-briefing/glareshield/FCU.jpg "Flight Control Unit (FCU)")

!!! note "API Documentation: [FCU Panel](../../../../../aircraft/a32nx/a32nx-api/a32nx-flightdeck-api.md#fcu-panel)"

## Description

The Flight Control Unit (FCU) provides short-term interface between the Flight Management and Guidance Computer (FMGC) and the flight crew for:

-	Engagement of A/P, FD, A/THR
-	Selection of required guidance modes
-	Manual selection of flight parameters SPD, MACH, ALT, VSPD, HDG or track.

## FCU Philosophy

In the Airbus A320, the Autopilot has two types on how to guide and control the aircraft. One is called "managed" and is done by the Flight Management Guidance System (FMGS). The other is usually called "selected" as it uses the selected values of the flight crew to control the aircraft.

When the aircraft is in managed mode, it shows 3 dashes and a dot to the right in the corresponding display.

When the aircraft uses selected values from the flight crew, the display shows the selected value and no dot.

The altitude window always displays an altitude selected by the pilot
and never dashes. The dot signifies managed altitude.

The four knobs used in the FCU, SPD-MACH, HDG-TRK, ALT, V/S-FPA basically all have the same philosophy:

- Push:
    - Let the FMGS manage the corresponding mode.

- Pull:
    - Use the flight crew selected value for the corresponding mode.

- Turn:
    - Change the value for the selected mode.

Note: In managed mode (lateral, vertical guidance or managed speed), the corresponding display is dashed. By changing the value without pulling the knob, the flight crew can pre-select a value before activating the selected mode. The display remains 45 seconds on the HDG/TRK and V/S windows and 10 seconds on the Speed/Mach window before the dashes reappear. This does not apply to the ALT selector knob/window.

## Usage

###  SPD/MACH knob

The range of this value is from 100 to 399 knots, and between 0.1 and 0.99 for Mach.

### SPD/MACH button

Changes the SPD target to the corresponding MACH target and vice versa.

###  HDG/TRK knob

The range of this value is between 0° and 359°.

### LOC

Arms, engages, or disengages the LOC (localizer intercept) mode.

### HDG V/S - TRK FPA pushbutton

Selects HDG and V/S or TRK and FPA.

If pushed it:

- shows the Flight Path Vector (FPV) on the Primary Flight Display (PFD) or deletes it.
- changes the FD crossbar display (with the aircraft attitude as its reference) to the aircraft Flight Path Director (with the flight path vector as its reference) on the PFD and vice versa.
- switches heading reference to track reference in the HDG/TRK window and vice versa.
- switches vertical speed reference target into flight path angle reference target in the V/S-FPA window and vice versa.

### AP1 AP2 pushbuttons

The flight crew uses these buttons to engage or disengage the autopilots. Lights up in green when the autopilot is engaged.

!!! note ""
    Typically, in normal procedures, the autopilot is not disengaged by pressing the AP buttons on the FCU but by pressing the takeover pushbutton on the sidestick.

    Disengaging the AP triggers a warning illuminating the Master Warning light, displaying a message on the ECAM, and sounding an audio warning (called Cavalry Charge):

    - If disengaged with the takeover pushbutton on the sidestick, the warnings are temporary (&#8924; 3 s Master Warning, &#8924; 9 s ECAM message "AP OFF" (red), &#8924; 1.5 s Cavalry Charge audio).
    - If disengaged by a failure, or by pushing the pushbutton on the FCU, or from a force on the sidestick, the visual, and audio warnings are continual (ECAM message "AUTO FLT AP OFF" in red).

    !!! info ""
        Currently, no continual warnings are implemented and also no ECAM message is displayed in the FBW A32NX for Microsoft Flight Simulator when the AP is disengaged.

### A/THR pushbutton

The flight crew uses this button to arm, activate, or disconnect the Autothrust (A/THR). Lights up in green if the A/THR is armed or active.

!!! note ""
    Typically, in normal procedures the Autothrust is not disengaged by pressing the A/THR button on the FCU but by pressing the disconnect pushbutton on the throttle levers or by setting both thrust levers to idle.

### Altitude selector knob (inner and outer)

The range of this value is between 100 and 49 000 feet.

The outer knob switches the step-size of the inner knob from 100 to 1000 and vice versa.

The inner knob sets the altitude in the FCU windows in the chosen increment step-size.

### EXPED

Engages the expedite mode, which is used in climb or descent to reach the desired altitude with the maximum vertical gradient.

### METRIC ALT

Used to show the FCU altitude target in meters on the ECAM, or the current altitude and FCU/FM altitude target in meters on the PFD.

### V/S or FPA knob

For V/S mode, the range of this value is from - 6000 to + 6000 ft/min

For FPA mode, the range of this value is from - 9.9° to + 9.9° descent/climb angle.

When pushed, an immediate level off is commanded (V/S of 0). The flight mode annunciator (FMA) then displays "V/S = O" in green.

### APPR

Approach modes are activated or deactivated (armed, disarmed, engaged, disengaged):

- If an ILS approach is selected in the flight plan, it activates LOC and G/S modes
- If a non precision approach is selected in the flight plan, it activates APP NAV-FINAL modes.

!!! note ""
    APP NAV-FINAL modes are currently not available in the FBW A32NX for Microsoft Flight Simulator (by 25th Aug 2021).

---

[Back to Flight Deck](../index.md){ .md-button }


