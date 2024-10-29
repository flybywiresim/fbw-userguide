---
title: Ventilation Panel
description: The A380 Flight Deck Ventilation Panel description.
---

# Ventilation Panel

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---

![Ventilation Panel](../../../assets/a380x-briefing/flight-deck/ovhd/vent-panel.png "Ventilation Panel"){loading=lazy}

## Usage

### AVNCS LIGHT

- OFF:
    - No smoke detected.
- SMOKE (red):
    - Smoke is detected in the ventilation duct of the main, upper, or aft avionics bay.
    - Associated with the following ECAM warning:
        - SMOKE L(R) MAIN AVNCS SMOKE (Refer to Procedure)
        - SMOKE L(R) UPPER AVNCS SMOKE (Refer to Procedure)
        - SMOKE AFT AVNCS SMOKE (Refer to Procedure)
    - The flight crew is pressing the CARGO SMOKE Panel Test pb (Refer to Test pb)

### AVNCS EXTRACT pb-sw

- AUTO: 
    - The overboard and extract valves operate automatically, to ensure ventilation
      of the avionic bays and the cockpit panels.
- OVRD: 
    - The overboard and extract valves are in override configuration, provided that
      the DITCHING pb-sw is not set to ON.
- FAULT: 
    - A low ventilation flow is detected in any avionics compartment.
    - Associated with the following ECAM alerts:
        - VENT AVNCS EXTRACT FAULT
        - SMOKE / FUMES.
    - The FAULT light goes off, when the flight crew sets the AVNCS
      EXTRACT pb-sw to OVRD.

### CAB FANS pb-sw

- ON: 
    - The cabin fans are on.
- OFF: 
    - The cabin fans are off.

### COOLG pb-sw

- AUTO: 
    - The supplemental cooling system operates automatically.
- OFF: 
    - The supplemental cooling system is off.
- FAULT: 
    - The supplemental cooling system is failed.
    - Associated with the following ECAM alerts:
        - VENT COOLG SYS 1(2) OVHT (with protection).
        - VENT COOLG SYS 1(2) OVHT (without protection).
        - VENT COOLG SYS PROT FAULT.

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---


