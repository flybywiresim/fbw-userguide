---
hide:
    - navigation
---
# Vertical Mode Annunciators

## Description

These annunciators tell the pilots what vertical mode the Autopilot and Flight Director are relying on and which modes are armed.  

### SRS 

Displayed with green text. Displayed when takeoff or go around mode is engaged. 

### CLB

Displayed with green text. Displayed when climb mode is engaged and the FMGS Target altitude is higher than the actual altitude. Altitude Constraints are accounted for. 

### OP CLB

Displayed with green text. Displayed when open climb mode is engaged and the FCU selected altitude is higher that the actual altitude. Altitude constraints are disregarded. 

### ALT\* or ALT CST\*

Altitude Capture is engaged

- ALT\* displayed with green text in case of FCU selected altitude capture.
- ALT CST\* displayed with green text in case of ALT CSTR capture.

### ALT or ALT CST

Altitude hold mode is engaged. 

- ALT is green when the FCU selected altitude is held. 
- ALT CST is green when an ALT CSTR (altitude constraint) is held.

### ALT CRZ 

Displayed with green text. Displayed when ALT mode is engaged and the Cruise Flight Level is held. 

### DES

Displayed with green text. Displayed when Descent mode is engaged and the FMGS target altitude is lower than the current altitude. Altitude Constraints are taken into account.

### OP DES

Displayed with green text. Displayed when open descent mode is engaged and the FCU selected altitude is lower than the current altitude. Altitude Constraints are not taken into account. 

### G/S\*

Displayed with green text. Displayed when Glideslope capture mode is engaged. 

### G/S

Displayed with green text. Displayed when Glideslope mode is engaged. 

### V/S ± XXXX

Displayed in green text with blue numbers. Displayed when vertical speed mode is engaged to hold the vertical speed selected on the FCU. Altitude constraints are not taken into account. 

### FPA ± XX 

Displayed in green text with blue numbers. Displayed when flight path angle mode is engaged to hold the flight path angle selected on the FCU. Altitude constraints are not taken into account. 

### CLB (Blue text)

Displayed in blue text. Displayed when climb mode is armed. 

### ALT (Blue or Magenta Text)

Altitude mode is armed:

- Blue when the target altitude is the FCU selected altitude. 
- Magenta when the target altitude is an altitude constraint. 

### DES (Blue)

Displayed in blue text. Displayed when descent mode is armed before the descent phase. 

### G/S (Blue)

Displayed in blue text. Displayed when Glideslope mode is armed. 

### FINAL 

Displayed in blue text. Displayed when final descent mode is armed. 

### ALT G/S 

Displayed in blue text. Displayed when both altitude and Glideslope modes are armed. 

### ALT G/S (Magenta/Blue Text)

ALT is displayed in magenta text and G/S is displayed in blue text. Displayed when altitude constraint and Glideslope modes are armed. 

### ALT FINAL 

Displayed in blue text. Displayed when descent and Glideslope modes are armed. 

### ALT FINAL (Magenta/Blue Text)

ALT is displayed in magenta text and FINAL is displayed in blue text. Displayed when altitude constraint and final modes are armed. 

### DES G/S

Displayed in blue text. Displayed when descent and Glideslope modes are armed.

### DES FINAL 

Displayed in blue text. Displayed when descent and final modes are armed. 

### SPEED SEL : XXX

Displayed in blue text. Indicates a preset speed associated with the climb or cruise phase. 

### MACH SEL : .XX

Displayed in blue text. Indicates a preset mach associated with the climb or cruise phase. 

---

[Back to Flight Mode Annunciators](FMA.md){ .md-button }