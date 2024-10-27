---
title: Cargo Smoke Panel 
description: The A380 Flight Deck Cargo Smoke Panel description. 
---

# Cargo Smoke Panel

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---

![Cargo Smoke Panel](../../../assets/a380x-briefing/flight-deck/ovhd/cargo-smoke-panel.png "Cargo Smoke Panel"){loading=lazy}

[//]: # (TODO API Doc Link)

## Description

The Cargo Smoke Panel is used to detect smoke in the cargo compartments.

## Usage

### AGENT TO FWD/AFT pb

- Guarded and dark:
    - No smke is detected.
- Smoke:
    - Smoke is detected in the associated cargo compartment.
    - Associated with the following ECAM warning:
        - SMOKE FWD (AFT/BULK) CARGO SMOKE 
    - The SMOKE light remains on as long as smoke is detected.
- Open and illuminated (red SMOKE):    
    - When pressed, the bottles discharge extinguisher agent in the associated cargo compartment.
- Open and illuminated (amber DISCH):
    - The fire extinguisher bottles discharge:
- Open and illuminated (red SMOKE and amber DISCH):
    - Smoke is detected in the associated cargo compartment, and the fire extinguisher bottles discharge, or
    - The flight crew is pressing the CARGO SMOKE Panel Test pb.

### BTL LIGHTS

- OFF
    - No bottle has discharged.
- BTL1 or BTL2 lights on
    - The fire extinguisher bottle has discharged.
- BTL1 and BTL2 lights on
  - The two fire extinguisher bottles have discharged, or
  - The flight crew is pressing the CARGO SMOKE panel Test pb.

### Test pb

When pressed for at least three seconds, and until released, tests the operation of the cargo compartments fire 
detection and extinguishing system:

- The continuous repetitive chime sounds
- The MASTER WARN lights flash
- The ECAM displays the cargo compartments SMOKE and AVNCS SMOKE warnings
- The isolation valve of the ventilation system closes
- All BTL lights come on
- All DISCH lights AGENT pb come on
- All SMOKE lights AGENT pb come on
- The AVNCS SMOKE light on the VENT panel comes on.

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---
