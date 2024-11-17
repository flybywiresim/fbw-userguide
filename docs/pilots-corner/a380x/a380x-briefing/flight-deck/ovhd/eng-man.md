---
title: Engine Manual Start Panel
description: The A380 Flight Deck Engine Manual Start Panel description.
---

# Engine Manual Start Panel

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---

![Engine Manual Start Panel](../../../assets/a380x-briefing/flight-deck/ovhd/eng-man-panel.png "Engine Manual Start Panel"){loading=lazy}

## Description

The Engine Manual Start Panel is used to manually start the engines.

## Usage

### ENG MAN START pb-sw

- ON:
    - During a manual engine start, the start valve opens, provided ENG START selector is set to IGN/START or CRANK.
    - *Note*: The start valve automatically closes when N2 reaches 58.4%.

- OFF:
    - The start valve closes, provided the ENG MASTER lever is set to OFF.
    - This stops the engine start sequence.

### ALTN MODE

In ALTN mode, the N1 parameter is the primary engine parameter. However, the THR parameter remains displayed on the EWD.

In ALTN mode, the TPR control loop is lost. The FADEC reverts to N1 control and uses the current N1 to control the 
engine thrust.

The FADEC computes the N1 command as a function of the thrust levers position, speed/mach, altitude, and temperature.

An automatic reversion to ALTN mode occurs when some engine parameters are not available. Automatic reversion to ALTN 
mode occurs when the P30 or the EGT engine parameter is failed.

When the FADEC operates in ALTN mode:

- The A/THR remains available
- The thrust rating modes and the corresponding thrust rating limit are available, except flexible and derated takeoff 
  modes
- The maximum available thrust at takeoff and go-around is reduced. The maximum available thrust is reduced by 4\%.
- The soft go-around function is available.

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---





