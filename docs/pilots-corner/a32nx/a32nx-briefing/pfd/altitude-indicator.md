<link rel="stylesheet" href="../../../../stylesheets/pfd-interactive.css">

# Altitude Indicator

<div style="position: relative; width: 413px; height: auto; margin-left: auto;  margin-right: auto;">
    <img src="/pilots-corner/assets/a32nx-briefing/pfd/pfd-small.png" style="width: 413px; height: auto;">
    <a href="/pilots-corner/a32nx-briefing/pfd/fma/">               <div class="imagemap"             style="position: absolute; left:     0%; top:     0%; width:   100%; height: 15.00%;"><span class="imagemapname">Flight Mode Annunciators</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/altitude-indicator/"><div class="imagemap highlighted" style="position: absolute; left: 72.60%; top: 20.00%; width: 16.00%; height: 58.00%;"><span class="imagemapname">Altitude Indicator</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/vertical-speed/">    <div class="imagemap"             style="position: absolute; left: 89.00%; top: 18.15%; width: 11.00%; height: 64.20%;"><span class="imagemapname">Vertical Speed Indicator</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/baro-ref/">          <div class="imagemap"             style="position: absolute; left: 74.04%; top: 81.00%; width: 19.44%; height:   5.8%;"><span class="imagemapname">Barometric Reference</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/artificial-horizon/"><div class="imagemap "            style="position: absolute; left: 18.74%; top: 20.62%; width: 48.81%; height: 56.68%;"><span class="imagemapname">Attitude and Guidance</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/speedtape/">         <div class="imagemap"             style="position: absolute; left:     0%; top: 20.17%; width: 15.35%; height: 57.86%;"><span class="imagemapname">Actual Airspeed Reference Line and Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/heading-ref/">       <div class="imagemap"             style="position: absolute; left: 19.58%; top: 86.09%; width: 47.48%; height: 12.17%;"><span class="imagemapname">Heading Reference Line and Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/ils-indicator/">     <div class="imagemap"             style="position: absolute; left: 22.70%; top: 78.40%; width: 42.88%; height:  5.34%;"><span class="imagemapname">Loc and G/S Deviation Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/ils-indicator/">     <div class="imagemap"             style="position: absolute; left: 68.10%; top: 29.41%; width:  4.01%; height: 41.10%;"><span class="imagemapname">Loc and G/S Deviation Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/ils-indicator/">     <div class="imagemap"             style="position: absolute; left:     0%; top: 85.00%; width: 16.00%; height: 13.00%;"><span class="imagemapname">ILS Information</span></div></a>
</div>

## Description

The altitude is displayed as a white moving scale and as a green digital readout on a gray background. NEG will appear on the background if the altitude is negative. The altitude window will change from yellow to amber if the aircraft has deviated from the FCU selected altitude.

If an MDA has been entered into the MCDU PERF page, the altitude numbers will change from green to amber once the aircraft goes below the chosen altitude.

### Vertical Deviation

This green filled circle symbol appears next to the altitude corresponding to the theoretical vertical profile computed by the FMGC. It is displayed from the top of descent down to the MAP altitude. The flight crew can read the linear deviation directly from the altitude scale. The range is ± 500 ft. When the linear deviation value exceeds ±500 ft, the symbol stays at the range limit but changes to a half filled circle and the PROG page displays the exact value.

### Target Altitude or Selected Flight Level Symbol

This is displayed in blue and shows the FCU selected altitude (if the QNH baro reference is selected) or the selected flight level (if STD baro reference is selected). If the FMGC is in vertical managed mode, the symbol will be magenta if it represents a constraint it will follow.

If the altitude is on the scale, the numbers will be displayed inside the symbol. If it is off the scale, the numbers will be displayed above or below the scale.

### Target Altitude or Selected Flight Level (meters)

If metric alt is activated, this is shown in numbers above the altitude indicator. It is either magenta or blue depending on whether it's the FMGC calculated altitude or a pilot selected altitude.

### Altitude Indicator (meters)

If metric alt is activated, this is shown under the barometric reference and is displayed in green numbers. It shows the altitude in meters.

### Radio Height

This appears at the bottom of the artificial horizon and the aircraft is 2500 feet or lower (radio altitude)

If a decision height has been entered in the PERF page of the MCDU, then:

- The radio height appears in green when the decision height + 100 feet is less than the radio altitude and the radio altitude is less than 2500 feet.
- The radio height appears in amber when the decision height + 100 feet is greater than the radio altitude.

When the aircraft reaches the decision height, DH letters will flash in amber for 3 seconds and then stay in amber above the radio altitude indication.

If no decision height has been entered in the PERF page of the MCDU, then:

- The radio height appears in green when the radio height is greater than 400 feet but less than 2500 feet.
- In amber when the radio altitude is equal to or less than 400 feet.

The radio altitude changes every 10 feet down to 50 feet, then every 5 feet down to 10 feet, then every foot.

### Landing Elevation

This is a horizontal bar on the scale that shows the landing elevation at the destination. It is displayed during flight phases 7 and 8 (800 feet radio altitude and touchdown) and if the QNH barometric reference mode is selected.

### Ground Reference

A red ribbon alongside the scale displays the field elevation. It uses the radio altitude as the data source and is displayed below 570 feet. It moves up with the altitude scale as the aircraft descends. When the aircraft has touched down, the ribbon will be in the middle of the altitude window.

---
[Back to Interactive PFD](index.md){ .md-button }
