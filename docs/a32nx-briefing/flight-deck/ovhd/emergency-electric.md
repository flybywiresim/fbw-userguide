---
hide:
- navigation
---

# Emergency Electric Power Panel

---

[Back to Flight Deck](../index.md){ .md-button }

---

![Emergency Electric Power Panel Panel](../../../assets/a32nx-briefing/overhead-panel/Emergency-electrical.jpg "Emergency Electric Power Panel")

## Function

- MAN ON (guarded)
    - AUTQ: When the following conditions are met:
        - AC BUS 1 is not electrically supplied.
        - AC BUS 2 is not electrically supplied.
        - Aircraft speed is greater than 100 knots.
        - The Ram Air Turbine (RAT) extends.
        - The blue hydraulic system drives the emergency generator.
        - As soon as the emergency generator electrical parameters are within tolerance the emergency generator is connected to the aircraft network.
    - Pressed:
        - This selects manual RAT extension.
        - Emergency generator coupling occurs 3 seconds after the RAT is supplying
        - the emergency generator.

- FAULT LIGHT: This light comes on red if the emergency generator is not supplying power when AC BUS 1 and AC BUS 2 are not powered.

- EMER GEN TEST (guarded)
    - Pressed and held:
        - if AC NORMAL BUSES are supplied:
            - The EMER GEN is driven hydraulically if the blue electric pump is running.
            - The AC ESS BUS and the DC ESS BUS are connected to the emergency generator. (The DC ESS SHED and AC ESS SHED buses are not powered.)
            - ECAM displays the ELEC page automatically (only on the ground).
        - If only the batteries supply the aircraft:
            - The static inverter powers the AC ESS BUS.

- GEN 1 LINE
    - OFF:
        - GEN 1 line contactor opens.
        - The AC BUS 1 channel is supplied from GEN 2 through bus tie contactors. This is used for smoked drill.
    - SMOKE Light


---

[Back to Flight Deck](../index.md){ .md-button }
