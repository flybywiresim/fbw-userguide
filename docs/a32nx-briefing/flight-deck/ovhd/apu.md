---
hide:
    - navigation
---

# Auxiliary Power Unit

---

[Back to Flight Deck](../index.md){ .md-button }

---

![APU Panel](../../../assets/a32nx-briefing/overhead-panel/Apu-Panel.jpg "APU Panel")

## Usage

### MASTER SW

Controls the APU operation and its start- and shutdown sequence.

- ON:
    - Blue ON light comes.
    - APU system is powered and performs a power-up test is done.
    - APU Air intake flap opens.
    - Fuel valve opens.
    - APU fuel pump operates if fuel pumps are not in operation.
    - ECAM shows APU page
- OFF:
    - Manual shutdown sequence.
    - ON light and the AVAIL light on the START pushbutton, go off.
    - The APU keeps running for a cooling period of 60 seconds, if the aircraft was using APU bleed air.
    - Air inlet flap closes at 7 %
- FAULT Lt:
    - Amber light and ECAM warning message, if an automatic APU shutdown occurs. Possible causes:
        - Fire (on ground only)
        - Reverse flow
        - Air inlet flap not open
        - Low oil pressure
        - Overspeed
        - High oil temperature
        - No acceleration
        - No speed
        - DC power loss. (BAT OFF when aircraft on batteries only)
        - EGT over-temperature
        - ECB failure
        - No flame
        - Loss of overspeed protection
        - Under-speed
        - Oil system shutdown
        - Inlet overheat
        - Clogged oil filter
        - Loss of EGT thermocouples

### START

- ON:
    - Blue ON light.
    - Starter is energized when the flap is completely open.
    - Ignition activates 1.5 second after the starter is energized.
    - When N = 60 %. The APU starter is de-energized. The ignition is turned off.
    - 2 seconds after N reached 95%, or when N is above 99.5% the the ON light on START button goes out. The APU can now supply bleed air and electrical power to the aircraft.
    - APU page disappears from the ECAM display after >10sec.
- AVAIL Lt:
    - Green light comes on when N is above 99.5 % or 2 seconds after N reaches 95%.

---

[Back to Flight Deck](../index.md){ .md-button }
