---
title: Recording and Evacuation Panel
description: The A380 Flight Deck Recording and Evacuation Panel description.
---

# Recording and Evacuation Panel

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---

![Recording and Evacuation Panel](../../../assets/a380x-briefing/flight-deck/ovhd/evac-panel.png "Recording and Evacuation Panel"){loading=lazy}

!!! note "API Documentation: [RCDR Panel API](../../../../../aircraft/a380x/a380x-api/a380x-flight-deck-api.md#rcdr-panel)"

## Usage RCDR

### RCDR GND CTL PB

-AUTO: 
    - All recorders operate automatically.
- ON:
    - The flight crew has manually started the recorders.
    - The system automatically switches from ON to AUTO when the first engine is started.

## Usage EVAC

### COMMAND PB-SW

- OFF and guarded:
    - Normal Operation. 
    - Neither the Captain nor the Chief Purser order an evacuation.
- EVAC (red) : 
    - The Chief Purser requests or orders an evacuation.
    - If the CAPT and PURS sw is set to CAPT position, when the Chief Purser requests an evacuation:
        - The EVAC light comes on
        - A horn sounds in the cockpit during 3 s.
    - If the CAPT and PURS sw is set to CAPT & PURS position, when the Chief Purser orders an evacuation:
        - The EVAC light flashes
          - A horn sounds in the cockpit
          - The EVACUATION ALERT message appears on all Attendant Indication Panels (AIP) in the cabin
          - EVAC CMD pb on FAPs, MINI FAPs and AAPs will be lit in the cabin
          - The evacuation horn sounds in the cabin.
- EVAC and ON:
    - The Flight Crew orders an evacuation, regardless of the CAPT and PURS sw position (CAPT or CAPT & PURS).
    - When pressed:
        - The ON light and the EVAC light flashes
        - The EVACUATION ALERT message appears on all Attendant Indication
          Panels (AIP) in the cabin
        - EVAC CMD pb on FAPs, MINI FAPs and AAPs will be lit in the cabin
        - The evacuation horn sounds in the cabin.

### HORN OFF pb
When pressed, silences the evacuation horn in the cockpit.

### CAPT AND PURS sw

- CAPT:
    - The Captain is the only person who can order an evacuation.
- CAPT & PURS:
    - The Captain and the Chief Purser can order an evacuation.

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---

