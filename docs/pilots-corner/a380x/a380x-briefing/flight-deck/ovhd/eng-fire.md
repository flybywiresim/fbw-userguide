---
title: Engine Fire Panel
description: The A380 Flight Deck Engine Fire Panel description.
---

# Engine Fire Panel

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---

![Engine Fire Panel](../../../assets/a380x-briefing/flight-deck/ovhd/eng-fire-panel.png "Engine Fire Panel"){loading=lazy}

!!! note "API Documentation: [FIRE Panel API](../../../../../aircraft/a380x/a380x-api/a380x-flight-deck-api.md#fire-panel)"

## Description

The Engine Fire Panel is used to control the engine fire detection and extinguishing systems.

## Usage

### ENG 1(2)(3)(4) FIRE pb

- IN, dark and closed: 
    - Normal position. 
    - No fire is detected.
- IN, illuminated and closed: 
    - Fire is detected. The FIRE light of the ENG MASTER panel comes on, and also indicates the affected engine.
    - Associated with the following ECAM warning: ENG 1(2)(3)(4) FIRE 
    - The light remains on, until the fire is extinguished, regardless of the position of the ENG FIRE pb.
    - The flight crew is pressing the ENG FIRE Panel Test pb (Refer to Test pb).
- OUT, illuminated and open (pressed): 
    - All associated systems are isolated from the engine.
    - The aural fire warning stops.
    - The fire extinguishing system is armed, the bottles are ready to discharge.

### AGENT 1(2) pb

- AUTO: 
    - Normal position.
- SQUIB: 
    - The squibs of the fire extinguisher bottles are armed. 
    - The fire extinguisher bottles are ready to discharge extinguisher agent.
    - When pressed, the extinguisher bottles discharge and the SQUIB light goes off.
- DISCH: 
    - The fire extinguisher bottle discharges or is empty.
- SQUIB & DISCH: 
    - The flight crew is pressing the ENG FIRE panel TEST pb (Refer to [TEST pb](#test-pb)).

### TEST pb

- Tests the engines, the APU and the main landing gear bay fire warnings.
- When pressed for at least three seconds, and until released, tests the operation of the engine fire detection and 
  extinguishing system:
    - The continuous repetitive chime sounds.
    - The MASTER WARN lights flash.
    - The ECAM displays ENG FIRE, APU FIRE and MLG FIRE warnings titles.
    - All ENG FIRE pb come on red.
    - The APU FIRE pb comes on red.
    - All SQUIB lights of the AGENT pb come on.
    - All DISCH lights of the AGENT pb come on.
    - All FIRE lights on the ENG MASTER panel come on.


---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---

