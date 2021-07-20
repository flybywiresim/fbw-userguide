# Flight Control Unit

---

Back to [Flight Deck](../flight-deck.md)

---

![Flight Control Unit (FCU)](../../assets/a32nx-briefing/glareshield/FCU.png "Flight Control Unit (FCU)")

## Description

The Flight Control Unit (FCU) provides short-term interface between the Flight Management and Guidance Computer (FMGC) and crew for:

-	Engagement of A/P, FD, A/THR
-	Selection of required guidance modes
-	Manual selection of flight parameters SPD, MACH, ALT, VSPD, HDG or track.

## FCU Philosophy

The pilot can use two types of guidance to control the aircraft in auto flight. One type is managed by the Flight Management Guidance System (FMGS). The other uses target quantities which are manually entered by the pilot.

When the aircraft uses target quantities from the FMGS (managed guidance), the FCU windows display dashes and the white dots next to those windows light up.

When the aircraft uses target quantities, entered by the pilot (selected guidance), the windows display the selected numbers and the white dots do not light up.

Note : The altitude window always displays an altitude selected by the pilot (never dashes).

The FCU has four selector knobs :

- SPD-MACH
- HDG-TRK
- ALT
- V/S-FPA

The selector knobs can be rotated, pushed in, and pulled out.

- In order to arm or engage managed guidance for a given mode, the pilot pushes in the associated selector knob. If, for example, he pushes in the HOG selector knob, he engages or arms the NAV mode.
- In order to engage a selected guidance mode, the pilot turns the selector knob to set the desired value, then pulls the knob out to engage the mode with a target value equal to the selected value.

Note : In managed guidance (lateral, vertical guidance or managed speed), the corresponding window is dashed. Turning a selector knob without pulling it, displays a value that is the sum of the current target and the turn action value. The display remains 45 seconds on the HDG/TRK and VIS windows and 10 seconds on the Speed/Mach window before the dashes reappear. This rule does not apply to the ALT selector knob/window.

## Controls and Indications

###  SPD/MACH selector knob

Display range : between 100 and 399 knots for speed, between 0.10 and 0.99 for Mach number. One rotation of the knob corresponds to approximately 32 knots or 0.32 Mach.

### SPD/MACH pushbutton

Pushing this pushbutton changes the SPD target to the corresponding MACH target and vice versa.

###  HDG/TRK selector knob

Display range : between 0° and 359°. One rotation of the knob corresponds to 32° ( 1 ° per click).

### LOC pushbutton

Pushing this pushbutton arms, engages, or disengages the LDC mode.

### HDG V/S - TRK FPA pushbutton

The pilot uses this pushbutton to select HDG (associated with V/S) or TRK (associated with FPA). Pushing it:

- Displays the Flight Path Vector (FPV) on the Primary Flight Display (PFD) or deletes it.
- On the PFD, changes the FD crossbar display (with the aircraft attitude as its reference) to the aircraft Flight Path Director (with the flight path vector as its reference) and vice versa.
- Changes heading reference into track reference in the HDG/TRK window and vice versa.
- Changes vertical speed reference target into flight path angle reference target in the V/S-FPA window and vice versa.

### AP1 AP2 pushbuttons

The pilot uses these pushbuttons to engage or disengage the autopilots. The buttons illuminate green when the autopilot is engaged.

### A/THR pushbutton

The pilot uses this pushbutton to arm, activate, or disconnect the autothrust (A/THR). This button illuminates green if the A/THR is armed or active.

### Altitude selector knob (inner and outer)

Display range : 100 to 49000 feet
- The outer knob has two positions : 100 and 1000.
- The inner knob sets the altitude in the FCU windows in increments of 100 or 1000 feet, depending upon the position of the outer knob.

### EXPED pushbutton

This pushbutton is used to engage the expedite mode.

### METRIC ALT pushbutton

This pushbutton is used to display the FCU altitude target in meters on the ECAM, or the current altitude and FCU/FM altitude target in meters on the PFD

### V/S or FPA selector knob

Range (V/S):

- -6000 to +6000 feet/min
- 2 clicks = 100 feet/min
- If the pilot turns the knob slowly, each click equals 100 feet/min.

Range (FPA):

- -9.9° to +9.9°
- 1 click= 0.1°

The pilot turns this knob to set the value of the vertical speed (V/S) or flight path angle (FPA) to be displayed in the V/S or FPA window. (pilot chooses which, V/S or FPA, is to be displayed by pushing the HDG V/S/TRK FPA pushbutton, as discussed previously).

One rotation of the knob corresponds to 32 clicks. One complete rotation sets:

- FPA = 3.2°
- V/S = 1600 ft/min

When the pilot pushes in the V/S or FPA knob the system commands an immediate level-off by engaging the V/S or FPA mode with a target of zero. The flight mode annunciator (FMA) then displays "V/S = O" in green when V/S or FPA is nulled. If the pilot now turns the knob to put in a new setting for V/S or FPA, the aircraft changes flight path accordingly.

### APPR pushbutton

This pushbutton arms, disarms, engages, or disengages the approach modes:

- LOC and G/S modes, if an ILS approach is selected in the active F-PLN.
- APP NAV-FINAL modes, if a non precision approach is selected in the active F-PLN.


---

Back to [Flight Deck](../flight-deck.md)


