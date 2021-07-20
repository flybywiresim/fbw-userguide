---
hide:
    - navigation
---

# WX Radar Panel

---

[Back to Flight Deck](../flight-deck.md){ .md-button }

---

![WX Radar Panel](../../assets/a32nx-briefing/pedestal/WX-radar-Panel.png "WX Radar Panel")

## Description

The aircraft is fitted with a Multiscan weather radar systems with a Predictive WindShear (PWS) function and a weather hazard prediction function.

The flight crew can display weather data on the CAPT and/or F/O NDs in either ARC or ROSE mode.

The flight crew can adjust the brightness of the weather image on the ND thanks the outer knob of the ND Brightness Control knob.

The weather radar has a Predictive WindShear system (PWS) that operates when the PWS switch is in the AUTO position , and the aircraft radio height is below 2 300 ft, and

- Weather radar is ON (Radar sw on position 1 or 2), or
- Weather radar is OFF, and
 At least one engine is running, and
- Aircraft ground speed is greater than 30 kt, or
- Aircraft longitudinal acceleration is above a given threshold during at least 0.5 s.

The system scans the airspace for windshear within a range of 5 NM ahead of the aircraft. When the system detects windshear, a windshear symbol appears on the ND.

## Controls

### Radar sw

- This switch sets one radar to ON or turns both radars to OFF.

- Note: If only one radar is installed on the aircraft, no weather image is displayed on the Navigation Display (ND) when the "1/OFF/2" SYS sw is set to "2".

### GAIN knob

- This knob adjusts the sensitivity of the radar.

- CAL is the normal position of the knob:
    - When in Multiscan Automatic mode and gain set to CAL, the radar automatically adjusts the gain according to various parameters (aircraft altitude, geographical area, season, time of the day) to obtain the best weather display
    - When in Manual mode and gain set to CAL, the radar adjusts the gain to a calibrated setting.

### MODE - Display mode selector

- WX:
    - Weather mode:<br/>
        Colors indicate the intensity of precipitation (black for the lowest intensity, green, amber and red indicate progressively higher intensity).
- WX+T:
    - Weather and Turbulence mode :<br/>
    The ND indicates precipitation and turbulence areas. Turbulence areas are displayed in magenta (within 40 NM).
- TURB:
    - Turbulence mode:<br/>
    The ND only displays turbulence areas in magenta (within 40 NM).
- WX+T+HZD:
    - Weather, Turbulence and Hazard mode (recommended position):<br/>
    The ND indicates precipitation, turbulence areas in magenta (within 40 NM) and hazard prediction risk areas (Refer to DSC-34-SURV-30-30 Weather Hazard Prediction Function Indication on ND).
    Hazard prediction function is only available when the MULTISCAN sw is set to AUTO.
    - Note: When MULTISCAN sw is set to MAN, WX+T+HZD mode is equivalent to WX+T mode.
- MAP:
    - Map mode:<br/>
      The radar operates in ground mapping mode: black indicates water, green indicates the ground, and amber indicates cities and mountains.

###  TILT knob

This knob adjusts the antenna tilt when MULTISCAN sw is set to MAN. Zero indicates the horizon reference provided by the IRS.

### MULTISCAN sw

- AUTO:
    - Activates Multiscan mode. Multiscan controls the tilt automatically and combines two scans done at different tilt angles to optimize weather detection and minimize ground clutter.
- MAN:
    - When set to MAN, the crew can manually adjust the tilt by using the TILT knob.

### GCS sw

- The Ground Clutter Suppression (GCS) switch is spring-loaded to the AUTO position.

- AUTO:
    - If MULTISCAN sw is set to AUTO, the radar is in normal use. Ground clutter is not displayed on the screen
    - If MUTLISCAN sw is set to MAN, the GCS sw has no utility. Ground clutter is displayed on the screen.
- OFF: Ground clutter is displayed on the screen.

### PWS sw

- AUTO : Activates the Predictive WindShear function in accordance with activation  conditions (Refer to DSC-34-SURV-30-20 Windshear Alerts Above 50 feet).
- OFF : The Predictive WindShear function is off.

---

[Back to Flight Deck](../flight-deck.md){ .md-button }

