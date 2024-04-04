<link rel="stylesheet" href="../../../../stylesheets/pfd-interactive.css">

# Vertical Mode Annunciations

<div style="position: relative; width: 413px; height: auto; margin-left: auto;  margin-right: auto;">
    <img src="/pilots-corner/assets/a32nx-briefing/pfd/pfd-small.png" style="width: 413px; height: auto;">
    <a href="/pilots-corner/a32nx-briefing/pfd/fma/">               <div class="imagemap highlighted" style="position: absolute; left:     0%; top:     0%; width:   100%; height: 15.00%;"><span class="imagemapname">Flight Mode Annunciators</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/altitude-indicator/"><div class="imagemap"             style="position: absolute; left: 72.60%; top: 20.00%; width: 16.00%; height: 58.00%;"><span class="imagemapname">Altitude Indicator</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/vertical-speed/">    <div class="imagemap"             style="position: absolute; left: 89.00%; top: 18.15%; width: 11.00%; height: 64.20%;"><span class="imagemapname">Vertical Speed Indicator</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/baro-ref/">          <div class="imagemap"             style="position: absolute; left: 74.04%; top: 81.00%; width: 19.44%; height:   5.8%;"><span class="imagemapname">Barometric Reference</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/artificial-horizon/"><div class="imagemap"             style="position: absolute; left: 18.74%; top: 20.62%; width: 48.81%; height: 56.68%;"><span class="imagemapname">Attitude and Guidance</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/speedtape/">         <div class="imagemap"             style="position: absolute; left:     0%; top: 20.17%; width: 15.35%; height: 57.86%;"><span class="imagemapname">Actual Airspeed Reference Line and Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/heading-ref/">       <div class="imagemap"             style="position: absolute; left: 19.58%; top: 86.09%; width: 47.48%; height: 12.17%;"><span class="imagemapname">Heading Reference Line and Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/ils-indicator/">     <div class="imagemap"             style="position: absolute; left: 22.70%; top: 78.40%; width: 42.88%; height:  5.34%;"><span class="imagemapname">Loc and G/S Deviation Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/ils-indicator/">     <div class="imagemap"             style="position: absolute; left: 68.10%; top: 29.41%; width:  4.01%; height: 41.10%;"><span class="imagemapname">Loc and G/S Deviation Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/ils-indicator/">     <div class="imagemap"             style="position: absolute; left:     0%; top: 85.00%; width: 16.00%; height: 13.00%;"><span class="imagemapname">ILS Information</span></div></a>
</div>

## Flight Mode Annunciator Columns (Interactive)

<div style="position: relative;">
    <img src="/pilots-corner/assets/a32nx-briefing/pfd/fma.png" style="width: 100%; height: 100%;">
    <a href="/pilots-corner/a32nx-briefing/pfd/first-column">                <div class="imagemap" style="position: absolute; left:     0%; top:    0%; width: 20.77%; height:  95%;"><span class="imagemapname">First Column: Autothrust</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/second-column">               <div class="imagemap highlighted" style="position: absolute; left: 21.22%; top:    0%; width: 20.35%; height:  66%;"><span class="imagemapname">Second Column: Vertical Guidance</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/third-column">                <div class="imagemap" style="position: absolute; left: 41.40%; top:    0%; width: 22.90%; height:  66%;"><span class="imagemapname">Third Column: Lateral Guidance</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/fourth-column">               <div class="imagemap" style="position: absolute; left: 64.50%; top:    0%; width: 19.70%; height:  95%;"><span class="imagemapname">Fourth Column: Approach</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/fifth-column">                <div class="imagemap" style="position: absolute; left: 84.25%; top:    0%; width: 15.80%; height:  95%;"><span class="imagemapname">Fifth Column: Autoflight Engagement Status</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/special-message-annunciators"><div class="imagemap" style="position: absolute; left: 21.22%; top:   67%; width: 43.08%; height:  31%;"><span class="imagemapname">Special Message and Common Mode Annunciators</span></div></a>
</div>

## Description

These annunciations tell the pilots which vertical mode the autopilot and flight director are engaged in and which mode is armed.

### SRS

Displayed in green when takeoff or go around mode is engaged.

SRS is the speed reference system, and it controls pitch to steer the aircraft along a path in the vertical plan at a speed defined by the SRS guidance law.

### CLB

Displayed in green when climb mode is engaged and the FMGS Target altitude is higher than the actual altitude. Altitude Constraints are accounted for.

### OP CLB

Displayed in green when open climb mode is engaged and the FCU selected altitude is higher than the actual altitude. Altitude constraints are disregarded.

### EXP CLB

Displayed when the aircraft is in EXP CLB mode.

The target speed is Green Dot, which is maintained with pitch control. Autothrust, if active, sets the thrust to CLB THRUST automatically.

When EXPEDITE is engaged, the system disregards SPD CSTR, ALT CSTR, and SPD LIM.

### ALT\* or ALT CST\*

Altitude Capture is engaged

- ALT\* displayed with green text in case of FCU selected altitude capture.
- ALT CST\* displayed with green text in case of ALT CSTR capture.

### ALT or ALT CST

Altitude hold mode is engaged.

- ALT is green when the FCU selected altitude is held.
- ALT CST is green when an ALT CSTR (altitude constraint) is held.

### ALT CRZ

Displayed in green when altitude mode is engaged and the Cruise Flight Level is held.

### DES

Displayed in green when descent mode (managed) is engaged and the FMGS target altitude is lower than the current altitude. Altitude Constraints are taken into account.

### OP DES

Displayed in green when open descent (selected) mode is engaged and the FCU selected altitude is lower than the current altitude. Altitude Constraints are not taken into account.

### EXP DES

Displayed when the aircraft is in EXP DES mode.

When the aircraft is in EXP DES, the target speed is 340 kt or M 0.8 which is maintained with pitch control. Autothrust, if active, sets the thrust to IDLE automatically.

When EXPEDITE is engaged, the system disregards SPD CSTR, ALT CSTR, and SPD LIM.

### G/S\*

Displayed in green when glideslope capture mode is engaged.

### G/S

Displayed in green when glideslope mode is engaged.

### V/S ± XXXX

Displayed in green text with blue numbers. Displayed when vertical speed mode is engaged to hold the vertical speed selected on the FCU. Altitude constraints are not taken into account.

!!! note ""
    This has priority over speed, and the aircraft might slow down or accelerate if Autothrust cannot compensate for the requested vertical speed. If the aircraft's speed reaches V~LS~ or V~MAX~ the requested vertical speed cannot be maintained any longer and this annunciator is boxed in amber and flashes. The vertical speed target pulses.

### FPA ± XX

Displayed in green text with blue numbers. Displayed when flight path angle mode is engaged to hold the flight path angle selected on the FCU. Altitude constraints are not taken into account.

!!! note ""
    This has priority over speed, and the aircraft might slow down or accelerate if Autothrust cannot compensate for the requested flight path angle. If the aircraft's speed reaches V~LS~ or V~MAX~ the requested flight path angle cannot be maintained any longer and this annunciator is boxed in amber and flashes. The flight path angle target pulses.

### CLB (Blue text)

Displayed in blue when climb mode is armed.

### ALT (Blue or Magenta Text)

Altitude mode is armed:

- Blue when the target altitude is the FCU selected altitude.
- Magenta when the target altitude is an altitude constraint.

### DES (Blue)

Displayed in blue when descent mode is armed before the descent phase.

### G/S (Blue)

Displayed in blue when glideslope mode is armed.

### FINAL

Displayed in blue when final descent mode is armed.

### ALT G/S

Displayed in blue when both altitude and glideslope modes are armed.

### ALT G/S (Magenta/Blue Text)

ALT is displayed in magenta text and G/S is displayed in blue text. Displayed when altitude constraint and glideslope modes are armed.

### ALT FINAL

Displayed in blue when descent and Glideslope modes are armed.

### ALT FINAL (Magenta/Blue Text)

ALT is displayed in magenta text and FINAL is displayed in blue text. Displayed when altitude constraint and final modes are armed.

### DES G/S

Displayed in blue when descent and Glideslope modes are armed.

### DES FINAL

Displayed in blue when descent and final modes are armed.

### SPEED SEL : XXX

Indicates in blue a preset speed associated with the climb or cruise phase.

### MACH SEL : .XX

Indicates in blue a preset mach associated with the climb or cruise phase.

---

[Back to Flight Mode Annunciators](fma.md){ .md-button }
