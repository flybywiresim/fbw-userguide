---
title: Cargo Air Conditioning Panel 
description: The A380 Flight Deck Cargo Air Conditioning Panel description.
---

# Cargo Air Conditioning Panel

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---

![Cargo Air Conditioning Panel](../../../assets/a380x-briefing/flight-deck/ovhd/cargo-air-cond-panel.png 
"Cargo Air Conditioning Panel"){loading=lazy width=70%}

[//]: # (TODO API Doc Link)

## Description

The Cargo Air Conditioning Panel is used to control the air conditioning in the cargo compartments.

## Usage

### BULK(AFT)(FWD) ISOL VALVES PB-SW

- AUTO
    - The bulk (forward) cargo isolation valves are open.
- OFF
    - The bulk (forward) cargo isolation valves are closed, and the bulk (forward) cargo extraction fan stops.
- FAULT
    - The bulk (forward) cargo isolation valves are failed.
    - Associated with the following ECAM alerts:
        - BULK CARGO ISOL FAULT 
        - BULK CARGO VENT FAULT
        - FWD CARGO ISOL FAULT 
        - FWD CARGO VENT FAULT 
        - AFT CARGO ISOL FAULT 
        - AFT CARGO VENT FAULT 

### TEMP REGUL SELECTOR

- Used to select the desired temperature in the bulk cargo compartment.
- The selected bulk cargo temperature is 15 °C.

### HEATER pb-sw

- AUTO
    - Normal position: The bulk cargo heater automatically operates.
- OFF
    - The bulk cargo heater is off.
- FAULT
    - The bulk cargo heater is failed.
    - Associated with the following ECAM cautions:
        - COND BULK CARGO DUCT OVHT
        - COND BULK CARGO HEAT FAULT

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---
