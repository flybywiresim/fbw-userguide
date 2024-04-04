<link rel="stylesheet" href="../../../../stylesheets/pfd-interactive.css">

# ILS Indications

<div style="position: relative; width: 413px; height: auto; margin-left: auto;  margin-right: auto;">
    <img src="/pilots-corner/assets/a32nx-briefing/pfd/pfd-small.png" style="width: 413px; height: auto;">
    <a href="/pilots-corner/a32nx-briefing/pfd/fma/">               <div class="imagemap"             style="position: absolute; left:     0%; top:     0%; width:   100%; height: 15.00%;"><span class="imagemapname">Flight Mode Annunciators</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/altitude-indicator/"><div class="imagemap"             style="position: absolute; left: 72.60%; top: 20.00%; width: 16.00%; height: 58.00%;"><span class="imagemapname">Altitude Indicator</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/vertical-speed/">    <div class="imagemap"             style="position: absolute; left: 89.00%; top: 18.15%; width: 11.00%; height: 64.20%;"><span class="imagemapname">Vertical Speed Indicator</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/baro-ref/">          <div class="imagemap"             style="position: absolute; left: 74.04%; top: 81.00%; width: 19.44%; height:   5.8%;"><span class="imagemapname">Barometric Reference</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/artificial-horizon/"><div class="imagemap"             style="position: absolute; left: 18.74%; top: 20.62%; width: 48.81%; height: 56.68%;"><span class="imagemapname">Attitude and Guidance</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/speedtape/">         <div class="imagemap"             style="position: absolute; left:     0%; top: 20.17%; width: 15.35%; height: 57.86%;"><span class="imagemapname">Actual Airspeed Reference Line and Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/heading-ref/">       <div class="imagemap"             style="position: absolute; left: 19.58%; top: 86.09%; width: 47.48%; height: 12.17%;"><span class="imagemapname">Heading Reference Line and Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/ils-indicator/">     <div class="imagemap highlighted" style="position: absolute; left: 22.70%; top: 77.40%; width: 42.88%; height:  5.34%;"><span class="imagemapname">Loc and G/S Deviation Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/ils-indicator/">     <div class="imagemap highlighted" style="position: absolute; left: 67.10%; top: 29.41%; width:  4.01%; height: 41.10%;"><span class="imagemapname">Loc and G/S Deviation Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/ils-indicator/">     <div class="imagemap highlighted" style="position: absolute; left:     0%; top: 85.00%; width: 16.00%; height: 13.00%;"><span class="imagemapname">ILS Information</span></div></a>
</div>

## Description

The PFD can show important additional information for various types of approaches.

The most common ones are ILS and RNP-RNAV but depending on aircraft configuration others are available: [GLS](https://www.skybrary.aero/index.php/GBAS_Landing_System_(GLS)){target=new}, [MLS](https://en.wikipedia.org/wiki/Microwave_landing_system){target=new}.

The main features of the approach information are deviation scales for horizontal and vertical path deviation.

!!! info ""
    Currently, the FlyByWire A32NX is only capable of ILS approaches. RNP-RNAV will be available once the custom Flight Management System has LNAV and VNAV capabilities.

## ILS Deviation Scale

This scale appears when the pilot presses the LS pushbutton on the EFIS panel. The index is the magenta diamond and is displayed when the glideslope and localizer signals are valid.

If the deviation index is out of the displayed range, only half a diamond is displayed at the end of the scale.

The localizer scale is a horizontal set of dots below the artificial horizon.

The glideslope scale is a vertical set of dots on the right side of the artificial horizon.

The yellow line in the center of the dots is where the aircraft is in relation to the glideslope or the localizer signal.

The localizer scale flashes and will continue to flash if the deviation exceeds 1/4 of a dot for two seconds (above 15 feet radio altitude). The glide scale flashes and continues to flash if the deviation exceeds one dot for two seconds (above 100 feet radio altitude).

"LOC" and the glide scale half index symbols flash and continue to flash if the deviation exceeds two dots for two seconds.

One dot represents ± 0.8 degrees of deviation on the localizer scale and ± 0.4 degrees on the glideslope scale.

### ILS Information

ILS information received from the ILS signal will be displayed in magenta to the left of the heading reference line and scale. It shows the ILS identification, ILS frequency and the DME distance, if the ILS has a DME.

### ILS Course Pointer

This is displayed in magenta on the heading reference line and scale when the crew has selected an ILS frequency and course, and the LS button on the EFIS in on.

It is a dagger shaped symbol and the course is displayed as a numerical value when outside the heading scale.

### Marker Indications

These are displayed right underneath the glideslope deviation scale.

- OM is displayed in blue when the aircraft flies over the outer marker.
- MM is displayed in amber when the aircraft flies over the middle marker.
- AWY is displayed in white when the aircraft flies over an airways marker beacon or the ILS inner marker.

Different audio sounds are played as the aircraft passes over each marker.

### ILS Message

This appears to the right of the localizer deviation scale, and flashes amber when the approach mode is armed and the LS display is not selected.

!!! info ""
    Currently not available for the FBW A32NX for Microsoft Flight Simulator

## Non Precision Approaches

There is no localizer deviation scale.

This appears when in the approach phase and when either FINAL is armed or engaged or a non ILS approach has been entered. They are displayed in the approach or go around flight phase, until the MDA has been reached, or the MAP or runway has been sequenced. They give the vertical deviation from the path set out by the FMGC.

Each scale graduation represents 100 feet, and the range is ± 200 feet. These are horizontal bars instead of dots.

Note that if the LS pushbutton is pressed, the glide deviation has priority over the vertical deviation information. As long as V/DEV display conditions are met, and the LS pushbutton is selected, an amber V/DEV message flashes above the glide scale.

!!! info ""
    Currently, the FlyByWire A32NX is only capable of ILS approaches. RNP-RNAV will be available once the custom Flight Management System has LNAV and VNAV capabilities.

---
[Back to Interactive PFD](index.md){ .md-button }
