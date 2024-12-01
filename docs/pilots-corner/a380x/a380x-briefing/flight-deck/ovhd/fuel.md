---
title: Fuel Panel
description: The A380 Flight Deck Fuel Panel description.
---

# Fuel Panel

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---

![Fuel Panel](../../../assets/a380x-briefing/flight-deck/ovhd/fuel-panel.png "Fuel Panel"){loading=lazy}

!!! note "API Documentation: [FUEL Panel API](../../../../../aircraft/a380x/a380x-api/a380x-flight-deck-api.md#fuel-panel)"

## Description

The fuel system stores fuel, monitors the quantity and temperature of fuel in each tank, and controls
fuel transfers to:

- Supply fuel to the engines and to the Auxiliary Power Unit (APU)
- Maintain the Center of Gravity (CG) within limits
- Reduce structural loads
- Control refueling and defueling
- Enable fuel jettison, if necessary.

## Usage

### FEED TK 1(2)(3)(4) MAIN pb-sw

- AUTO:
    - The main pump is running.
- OFF:
    - The main pump is off.
- FAULT:
    - The main pump is running at low pressure or is failed.
    - Associated with one of the following ECAM cautions:
        - FUEL FEED TK 1(2)(3)(4) MAIN PMP FAULT
        - FUEL FEED TK 1(2)(3)(4) MAIN + STBY PMP FAULT
        - FUEL L(R) WING FEED PMPs FAULT.
    - The FAULT light goes off, when the flight crew sets the FEED TK 1(2)(3)(4) MAIN pb-sw to OFF.

### FEED TK 1(2)(3)(4) STBY pb-sw

- AUTO:
    - The standby pump runs automatically, when the associated main pump is failed, or is off.
- OFF:
    - The standby pump is off.
- FAULT:
    - The standby pump is running at low pressure or is failed.
    - Associated with one of the following ECAM alerts:
        - FUEL FEED TK 1(2)(3)(4) STBY PMP FAULT
        - FUEL FEED TK 1(2)(3)(4) MAIN + STBY PMP FAULT
        - FUEL L(R) WING FEED PMPs FAULT.
    - The FAULT light goes off, when the flight crew sets the FEED TK 1(2)(3)(4) STBY pb-sw to OFF.

### L(R) INR(MID)(OUTR) TK FWD pb-sw

- AUTO:
    - The transfer pump runs, if necessary:
        - For an automatic fuel transfer from the inner, middle, or outer tanks, via the forward gallery, or
        - For a manual transfer from the outer tanks, via the forward gallery (except if any outer tank pump has been switched off), or
        - During jettison.
- OFF:
    - The transfer pump is off.
- FAULT:
    - Comes on:
        - When the transfer pump is failed, or is abnormally on
            - Associated with one of the following ECAM alerts:
                - FUEL L(R) INR FWD PMP FAULT
                - FUEL L(R) INR FWD+AFT PMPs FAULT
                - FUEL L(R) MID FWD PMP FAULT
                - FUEL L(R) MID FWD+AFT PMPs FAULT
                - FUEL L(R) OUTR PMP FAULT.
        - Or, when the transfer pump must be turned off to allow a manual gravity transfer:
            - Associated with the following ECAM alert:
                - FUEL OUTR TK XFR FAULT
    - The FAULT light goes off, when the flight crew sets the L(R) INR(MID)(OUTR) TK FWD pb-sw to OFF.

### L(R) MID(INR) TK AFT pb-sw

- ON:
    - The transfer pump runs, if necessary:
        - For an automatic or manual fuel transfer from the inner, or middle tanks, via the aft gallery, or
        - During jettison.
- OFF:
    - The transfer pump is off.
- FAULT:
    - The transfer pump is failed, or is abnormally on, or a low pressure is detected during a manual transfer.
    - Associated with one of the following ECAM alerts:
        - FUEL L(R) INR AFT PMP FAULT (Refer to procedure)
        - FUEL L(R) INR FWD+AFT PMPs FAULT (Refer to procedure)
        - FUEL L(R) MID AFT PMP FAULT (Refer to procedure)
        - FUEL L(R) MID FWD+AFT PMPs FAULT (Refer to procedure)
    - The FAULT light goes off, when the flight crew sets the L(R) MID(INR) TK AFT pb-sw to OFF.

### TRIM TK L(R) pb-sw

- ON:
    - The transfer pump runs, if necessary:
        - For an automatic or manual fuel transfer, or
        - During jettison.
- OFF:
    - The transfer pump is off.
- FAULT:
    - Comes on:
        - When the transfer pump is failed, or is abnormally on, or a low pressure is detected during a manual transfer
            - Associated with one of the following ECAM alerts:
                - FUEL TRIM TK L(R) PMP FAULT (Refer to procedure)
                - FUEL TRIM TK L+R PMPs FAULT (Refer to procedure)
                - FUEL TRIM TK XFR FAULT (Refer to procedure)
        - Or, when the trim line is damaged and all trim tank transfers must be inhibited.
            - Associated with the following ECAM alert:
                - FUEL TRIM & APU LINES FAULT (Refer to procedure)
    - The FAULT light goes off, when the flight crew sets the TRIM TK L(R) pb-sw to OFF.

### INR(MID)(OUTR) TK XFR pb-sw

- AUTO:
    - Automatic fuel transfers from the inner (middle)(outer) tanks are available.
    - For more information: Refer to Fuel Transfer Sequence
- MAN:
    - Fuel manually transfers from the inner (middle)(outer) tanks to the feed tanks.
- FAULT:
    - Comes on:
        - When automatic fuel transfers from the affected tanks are no longer possible.
            - Associated with one of the following ECAM alerts:
                - FUEL MAN XFR PROCEDURE
                - FUEL OUTR TK XFR FAULT
        - Or, when a low level is detected in one or more of the feed tanks.
            - Associated with the following ECAM alerts:
                - FUEL FEED TK 1(2)(3)(4) LEVEL LO
                - FUEL FEED TKs 1+2(3+4) LEVEL LO
                - FUEL ALL FEED TKs LEVEL LO
        - Or, (for the OUTR TK XFR pb-sw only) when a low fuel temperature is detected in the outer tanks.
            - Associated with the following ECAM alert:
                - FUEL TEMP LO
    - The FAULT light goes off, when the flight crew sets the INR(MID)(OUTR) TK XFR pb-sw to MAN.

### TRIM TK XFR pb-sw

- AUTO:
    - Automatic fuel transfers from the trim tank are available.
    - For more information: Refer to Fuel Transfer Sequence
- MAN:
    - Fuel manually transfers from the trim tank to the inner tanks.
- FAULT:
    - Comes on:
        - When an excessive aft CG is detected
            - The Weight and Balance Backup Computer (WBBC) monitors the CG.
            - Associated with the following ECAM alert:
                - FUEL EXCESS AFT CG
        - Or, when the CG has been previously detected at the forward limit, and the trim tank transfer can resume
            - Associated with the following ECAM alert:
                - FUEL CG AT FWD LIMIT
        - Or, when a manual trim tank transfer is required
            - Associated with the following ECAM alert:
                - FUEL TRIM XFR FAULT
                - FUEL MAN XFR PROCEDURE
        - Or, when a low fuel temperature is detected in the trim tank
            - Associated with the following ECAM alert:
                - FUEL TEMP LO
        - Or, when there is a low level of fuel in any feed tank, and there is still some fuel in the trim tank
            - Associated with one of the following ECAM alerts:
                - FUEL FEED TK 1(2)(3)(4) LEVEL LO
                - FUEL FEED TKs 1+2 (3+4) LEVEL LO
                - FUEL ALL FEED TKs LEVEL LO
        - Or, when an overflow of the trim tank is detected.
            - Associated with the following ECAM alert:
                - FUEL TRIM TK OVERFLOW
    - The FAULT light goes off, when the flight crew sets the TRIM TK XFR pb-sw to MAN.

### TRIM TK FEED SELECTOR

- AUTO:
    - The trim tank transfers are automatic.
- ISOL:
    - The trim tank forward transfer stops and the trim tank transfer line is isolated.
    - The following valves close to isolate the transfer line:
        - The trim tank isolation valve
        - The trim tank inlet valves
        - The trim pipe isolation valves.
- OPEN:
    - The following valves open, to allow gravity transfer from the trim tank to the inner tanks:
        - Trim tank inlet valves
        - Trim pipe isolation valve connected to the aft gallery
        - Inner tank aft inlet valves.

### CROSSFEED 1(2)(3)(4) pb-sw

- AUTO:
    - All crossfeed valves automatically open:
        - In electrical emergency configuration, while the slats are retracted, or
        - If required for an automatic ground transfer.
- ON and OPEN:
    - The CROSSFEED 1(2)(3)(4) pb-sw is set to ON and the crossfeed valve is open.
- ON:
    - The CROSSFEED 1(2)(3)(4) pb-sw is set to ON and the crossfeed valve remains closed.
    - Associated with the following ECAM alert:
        - FUEL CROSSFEED VLV 1(2)(3)(4) FAULT (Refer to procedure).
    - The OPEN/ON lights go off, when the flight crew deselects the CROSSFEED 1(2)(3)(4) pb-sw.
- OPEN:
    - The CROSSFEED 1(2)(3)(4) pb-sw is deselected and the crossfeed valve is open.
    - If the crossfeed valve is abnormally open, this is associated with the following ECAM alert:
        - FUEL CROSSFEED VLV 1(2)(3)(4) FAULT (Refer to procedure).
    - If the crossfeed valve is automatically commanded open (automatic ground transfer or electrical emergency configuration), there is no associated alert.


---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---
