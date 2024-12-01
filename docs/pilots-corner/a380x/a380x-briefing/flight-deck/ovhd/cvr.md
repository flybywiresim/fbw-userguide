---
title: Cockpit Voice Recorder (CVR) Panel 
description: The A380 Flight Deck Cockpit Voice Recorder (CVR) Panel description. 
---

# Cockpit Voice Recorder (CVR) Panel

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---

![CVR Panel](../../../assets/a380x-briefing/flight-deck/ovhd/cvr-panel.png "CVR Panel"){loading=lazy}

!!! note "API Documentation: [RCDR Panel API](../../../../../aircraft/a380x/a380x-api/a380x-flight-deck-api.md#rcdr-panel)"

## Description

The Cockpit Voice Recorder (CVR) Panel is used to control the cockpit voice recorder system.

## Usage

### Test pb

- When pressed, tests the CVR.
- If a boomset is connected to the BOOMSET jack, the flight crew will hear a low frequency signal.
- If the test is not successful, the ECAM triggers a RECORDER CVR FAULT alert 5 s after the pushbutton is pressed.
- To perform this test, the recorder must be on.

### ERASE pb

- When pressed for 2 seconds, the audio recording is erased, if the aircraft is on ground, and the parking brake is on.
- Note: Data recording cannot be erased.
- If a boomset is connected into the BOOMSET jack, the flight crew will hear a low frequency signal.
- To erase audio recording, the recorder must be in use.

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---

