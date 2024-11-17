# Voice Recorder Panel

---

[Back to Flight Deck](../index.md){ .md-button }

---

![Voice Recorder Panel](../../../assets/a32nx-briefing/overhead-panel/Recorder.jpg "Voice Recorder Panel")

!!! note "API Documentation: [RCDR Panel API](../../../../../aircraft/a32nx/a32nx-api/a32nx-flightdeck-api.md#rcdr-panel)"

## Description

The voice recorder panel consist of cockpit voice recorder (CVR) and digital flight data recorder (DFDR) controls.

The CVR and DFDR are energized automatically during the following conditions:

- On the ground for five minutes following electrical power.
- On the ground continuously with at least one engine running.
- Continuously in flight regardless if engines are operating.
- The CVR and DFDR both automatically stop five minutes after the last engine is shut down.

The cockpit voice recorder is located in the aft section of the airplane, equipped with an underwater locating beacon. It records direct conversations between crew members through a cockpit area microphone and boom microphones, aural cockpit warnings, intercommunication and radio transmissions.

The passenger address system is also recorded if the PA reception knob is selected on.

Aircraft built after 2003 have a 120-min recording time requirement. Airbus installs CVRs capable of 25 h of recording since the end of 2020.

## Usage

- GND CTRL:
    - The ON function energizes the CVR and DFDR. This is used to test the CVR and DFDR.

- CVR ERASE:
    - When the ERASE button is pushed for two seconds, it erases the CVR tape, provided the airplane is on the ground, the parking brake is on and the GND CTRL button is on.

- CVR TEST:
    - When pushed and held, the CVR test is activated, provided the CVR is energized, and the parking brake is on. During the test, a low frequency tone is heard through the cockpit loudspeakers.

---

[Back to Flight Deck](../index.md){ .md-button }
