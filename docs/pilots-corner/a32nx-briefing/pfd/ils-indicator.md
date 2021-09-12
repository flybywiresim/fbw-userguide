# Localiser and Glideslope Deviation Scale and Index

## Description

This is a scale that displays the aircraft's deviation from the localiser and glideslope or the deviation from the trajectory defined by the FMGC in a non precision approach. 

## ILS Approach

This scale appears when the pilot presses the LS pushbutton on the EFIS panel. The index is the magenta diamond and is displayed when the glideslope and localiser signals are valid. 

If the deviation index is out of the displayed range, only half a diamond is displayed at the end of the scale. 

The localiser scale is a horizontal set of dots below the artificial horizon. The glideslope scale is a vertical set of dots on the right side of the artificial horizon. The yellow line in the centre of the dots is where the aircraft is in relation to the glideslope or the localiser signal. 

The localiser scale flashes and will continue to flash if the deviation exceeds 1/4 of a dot for two seconds (above 15 feet radio altitude). The glide scale flashes and continues to flash if the deviation exceeds one dot for two seconds (above 100 feet radio altitude).

"LOC" and the glide scale half index symbols flash and continue to flash if the deviation exceeds two dots for two seconds. 

One dot represents ± 0.8 degrees of deviation on the localiser scale and ± 0.4 degrees on the glideslope scale. 

### ILS Information

ILS information will be displayed in magenta to the left of the heading reference line and scale. This displays the ILS identification, ILS frequency and the DME distance, if the ILS has a DME. 

### ILS Course Pointer

This is displayed in magenta on the heading reference line and scale when the crew has selected an ILS frequency and course, and has pushed the LS button on the EFIS. 

It is a dagger shaped symbol and the course is displayed as a numerical value when outside of the heading scale. 

### Marker Indications

These are displayed right underneath the glideslope deviation scale. 

- OM is displayed in blue when the aircraft flies over the outer marker. 
- MM is displayed in amber when the aircraft flies over the middle marker. 
- AWY is displayed in white when the aircraft flies over an airways marker beacon or the ILS inner marker. 

Different beeps are played as the aircraft passes over each marker. 

### ILS Message

!!! attention "Currently not available for the FBW A32NX for Microsoft Flight Simulator"

This appears to the right of the localiser deviation scale, and flashes amber when the approach mode is armed and the ILS display is not selected. 

## Non Precision Approaches

!!! attention "Currently not available for the FBW A32NX for Microsoft Flight Simulator"

There is no localiser deviation scale. 

This appears when in the approach phase and when either FINAL is armed or engaged or a non ILS approach has been entered. They are displayed in the approach or go around flight phase, until the MDA has been reached, or the MAP or runway has been sequenced. They give the vertical deviation from the path set out by the FMGC. 

Each scale graduation represents 100 feet and the range is ± 200 feet. These are horizontal bars instead of dots. 

Note that if the LS pushbutton is pressed, the glide deviation has priority over the vertical deviation information. As long as V/DEV display conditions are met, and the LS pushbutton is selected, an amber V/DEV message flashes above the glide scale. 

---
[Back to Interactive PFD](index.md){ .md-button }