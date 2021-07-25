---
hide:
    - navigation
---

# ATC TCAS Panel

---

[Back to Flight Deck](../flight-deck.md){ .md-button }

---

![ATC-TCAS Panel](../../../assets/a32nx-briefing/pedestal/ATC-TCAS.png "ATC-TCAS Panel")

## Description

The aircraft has two ATC transponders (XPDR) which are controlled by a control panel (ATC/TCAS) on the center pedestal.

Only the selected XPDR operates.

The XPDR automatically responds to requests:

- From the ATC, to ensure effective air traffic surveillance
- From other aircraft that have a TCAS, to ensure that traffic alerts are triggered.

The XPDR is capable of elementary surveillance (ELS) and enhanced surveillance (EHS). It transmits the following data to the ATC center:

‐ The aircraft 24 bit address, the aircraft altitude, the flight number, the RA report
‐ The indicated airspeed, the Mach number, and the barometric vertical speed that are all supplied by the ADRs
‐ The magnetic heading, the roll angle, the ground speed, the track angle, the track angle rate, and the inertial vertical speed, that are all supplied by the IRs
‐ The selected altitude and barometric reference settings supplied by the FCUs.

## Usage

### XPDR Selector

This switch selects XPDR 1 or 2.

###  Mode Selector

- STBY:
    - Both XPDR are electrically supplied but do not operate.
- ON:
    - Selected XPDR operates.
- AUTO:
    - In flight : Selected XPDR operates.
    - On ground : Selected XPDR only operates in mode S (Selective aircraft interrogation mode).

### ALT RPTG Switch

- ON:
    - The XPDR sends barometric standard altitude data.
- OFF:
    - No altitude data transmission. If the TCAS is installed, the upper ECAM displays "TCAS STBY" in green.

### IDNT Switch

- The flight crew presses this button to send the aircraft identification signal.

### Code Display

- The window displays the selected code.

### Keypad

- The flight crew uses the keypad to set the code assigned by ATC.

### CLR Key

- The flight crew uses this key to clear the code display.
- Note: As long as the four figures of the new code are not entirely written, the previous code remains.

### ATC FAIL Light

- This light comes on if the selected XPDR fails.

---

[Back to Flight Deck](../flight-deck.md){ .md-button }
