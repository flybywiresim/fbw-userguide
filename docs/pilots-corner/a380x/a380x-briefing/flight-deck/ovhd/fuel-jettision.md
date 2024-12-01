---
title: Fuel Jettison Panel
description: The A380 Flight Deck Fuel Jettison Panel description.
---

# Fuel Jettison Panel

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---

![Fuel Jettison Panel](../../../assets/a380x-briefing/flight-deck/ovhd/fuel-emer-panel.png "Fuel Jettison Panel"){loading=lazy}

## Description

The A380's fuel jettison system is designed to quickly reduce the aircraft's weight in emergency situations, allowing it
to safely return to land. It enables the controlled discharge of fuel from specific tanks through nozzles located on the 
wings. This process helps achieve the aircraft's maximum landing weight when required, enhancing safety during emergency 
landings. The system is carefully monitored and controlled to ensure efficient and safe operation during use.

!!! warning ""
    This is not available in the A380X yet. 

## Usage

### JETTISON ARM pb-sw

- OFF (not illuminated):
    - Jettison is not armed.
- ON:
    - Jettison is armed, and can be activated using the JETTISON ACTIVE pb-sw.

### JETTISON ACTIVE pb-sw

- OFF (not illuminated):
    - Jettison is not active.
- ON:
    - Jettison is selected active. The jettison valves open, if the JETTISON ARM pb-sw is also ON.
- ON and OPEN:
    - The jettison valves are fully open.
    - The ON and OPEN lights go off, when the FQMS automatically stops the jettison, or when the flight crew presses 
      the JETTISON ACTIVE pb-sw or JETTISON ARM pb-sw again.

### EMER OUTR TK XFR pb-sw

- OFF (not illuminated):
    - The emergency outer tank transfer valves are closed.
- ON:
    - The emergency outer tank transfer valves are commanded open.
    - Fuel transfers from the outer tanks into the outer feed tanks (FEED TK 1 or 4).
    - The EMER OUTR TK XFR pb-sw is used in the case of:
        - ENG 1(2)(3)(4) FAIL with damage
        - FUEL NORM XFR FAULT
        - FUEL NORM + ALTN XFR FAULT
        - ELEC EMER CONFIG
        - ELEC AC BUS 2 FAULT
        - ELEC AC BUS 4 FAULT
        - ELEC AC ESS BUS FAULT
        - ELEC DC BUS 1 FAULT
        - ELEC DC BUS 2 FAULT
        - ELEC DC ESS BUS FAULT

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---
