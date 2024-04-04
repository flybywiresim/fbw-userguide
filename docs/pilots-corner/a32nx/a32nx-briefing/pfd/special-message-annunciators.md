<link rel="stylesheet" href="../../../../stylesheets/pfd-interactive.css">

# Common Mode and Special Message Annunciators

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
    <a href="/pilots-corner/a32nx-briefing/pfd/second-column">               <div class="imagemap" style="position: absolute; left: 21.22%; top:    0%; width: 20.35%; height:  66%;"><span class="imagemapname">Second Column: Vertical Guidance</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/third-column">                <div class="imagemap" style="position: absolute; left: 41.40%; top:    0%; width: 22.90%; height:  66%;"><span class="imagemapname">Third Column: Lateral Guidance</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/fourth-column">               <div class="imagemap" style="position: absolute; left: 64.50%; top:    0%; width: 19.70%; height:  95%;"><span class="imagemapname">Fourth Column: Approach</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/fifth-column">                <div class="imagemap" style="position: absolute; left: 84.25%; top:    0%; width: 15.80%; height:  95%;"><span class="imagemapname">Fifth Column: Autoflight Engagement Status</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/special-message-annunciators"><div class="imagemap highlighted" style="position: absolute; left: 21.22%; top:   63%; width: 43.08%; height:  31%;"><span class="imagemapname">Special Message and Common Mode Annunciators</span></div></a>
</div>


These types of annunciators are displayed on both columns two and three.

Special Message annunciators display three types of messages (in the order of priority):

- Flight controls messages
- Vertical flight management messages
- EFIS reconfiguration messages

Common mode annunciators display the common flight modes.

---

## Special Message Annunciators

### MAN PITCH TRIM ONLY

Displayed in red when there is a loss of both left and right elevators.

### USE MAN PITCH TRIM

Displayed in amber when the flight controls are in direct law.

### CHECK APP SEL

Displayed in white when the aircraft is in cruise at less than 100 nautical miles from the top of descent or in descent or in approach and:

- A non ILS approach has been selected.
- An ILS frequency is tuned on the MCDU RAD NAV page.

### CHECK SPEED MODE

Displayed in white when the speed target is selected, but a preselected speed does not exist for the next flight phase.

### SET GREEN DOT SPD

Displayed in white when the aircraft is in engine out mode and the speed target is selected. This message will be displayed if the FCU selected speed is:

- Less than or equal to the green dot speed minus 10 kt or
- Greater than or equal to the green dot speed plus 10 kt (except when the aircraft is in ALT\* mode or ALT mode).

!!! info ""
    Currently not available for the FBW A32NX for Microsoft Flight Simulator

### SET HOLD SPD

Displayed in white when the aircraft is in selected speed control, a holding pattern has been inserted into the MCDU flight plan and the aircraft is 30 seconds out from the deceleration point to the computed hold speed.

### DECELERATE

Displayed in white if the thrust is not reduced when the aircraft is passing the top of descent point, and the aircraft is above the descent profile.

!!! info ""
    Currently not available for the FBW A32NX for Microsoft Flight Simulator

### MORE DRAG

Displayed in white when descent mode is engaged, idle is selected, and:

- Either the aircraft is above the vertical profile and the predicted intercept point of the profile is at less than 2 nautical miles away from the next altitude constraint or
- In auto-speed control and the aircraft enters a speedbrake decelerating segment.

!!! info ""
    Currently not available for the FBW A32NX for Microsoft Flight Simulator

### VERT DISCON AHEAD

Displayed in amber text. Displays when descent mode is engaged and:

- A vertical path too steep exists on the next leg.
- The aircraft is less than 30 seconds from a path that is too steep.

!!! info ""
    Currently not available for the FBW A32NX for Microsoft Flight Simulator

---

## Common Mode Annunciators

### LAND

Displayed in green when land mode is engaged below 400 feet (radio altitude).

### FLARE

Displayed in green when flare mode is engaged.

### ROLL OUT

Displayed in green when roll out mode is engaged.

### FINAL APP

Displayed in green when APP NAV and Final modes are engaged during a non ILS approach.

!!! info ""
    Currently not available for the FBW A32NX for Microsoft Flight Simulator

---

[Back to Flight Mode Annunciators](fma.md){ .md-button }





