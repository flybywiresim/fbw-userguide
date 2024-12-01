---
title: Electrical Panel
description: The A380 Flight Deck Electrical Panel description.
---

# Electrical Panel

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---

![Electrical Panel](../../../assets/a380x-briefing/flight-deck/ovhd/elec-panel.png "Electrical Panel"){loading=lazy}

!!! note "API Documentation: [ELEC Panel API](../../../../../aircraft/a380x/a380x-api/a380x-flight-deck-api.md#elec-panel)"


## Description

The Electrical Panel is used to control the electrical systems of the aircraft.

## Usage

### BAT1(2)(APU)(ESS) pb-sw

- AUTO: 
    - Normal position. Each TR automatically controls the charging of its associated Battery.
- OFF: 
    - The battery is disconnected from the network.
- FAULT: 
    - The charging or discharging current of the battery is abnormal. 
    - The battery automatically disconnects from its associated DC busbar. 
    - Associated with one of the following ECAM cautions:
        - ELEC APU BAT FAULT 
        - ELEC BAT 1 (2)(ESS) FAULT .

### BUS TIE pb-sw

- AUTO: 
    - Normal position. The BUS TIE contactors automatically open or close, to reconfigure the electrical network, as necessary.
- OFF: 
    - Some BUS TIE contactors open to segregate:
    - The AC 1 and AC 2 busbars from the AC 3 and AC 4 busbars, and
    - The DC 1 busbar from the DC 2 busbar.

### PAX SYS pb-sw

- ON: 
    - Normal Operation
    - The IFE system, the passenger communication means and the passenger seats are electrically-supplied.
- OFF: 
    - The IFE system, the passenger communication means and the seat power supply are manually shed.

### ELMU pb-sw

- AUTO: 
    - The automatic shedding function for high and low commercial loads is available.
- OFF: 
    - The ELMU is off: The automatic shedding function for low commercial loads is not available. ENMU 1 and 2 can shed high loads, if necessary.
- FAULT: 
    - The ELMU is failed: The automatic shedding function for low commercial loads is not available. ENMU 1 and 2 can shed high loads, if necessary. 
    - Associated with the following ECAM caution: ELEC LOAD MANAGT FAULT 

### AC ESS Feed pb-sw

- AUTO and closed: 
    - Normal position:
    - The AC 1 busbar supplies the AC ESS busbar.
    - If the AC 1 busbar is lost, the AC 4 busbar will automatically supply the AC ESS busbar.
- ALTN and open: 
    - The AC ESS FEED pb-sw is manually set to ALTN. 
    - The AC 4 busbar supplies the AC ESS busbar.
- FAULT and closed: 
    - The AC ESS busbar is not supplied. 
    - Associated with the following ECAM caution: ELEC AC ESS BUS FAULT .

### GALLEY pb-sw

- AUTO: 
    - The galleys are supplied. Some galleys may be automatically shed, if necessary.
- OFF: 
    - All galleys are manually shed.

### COMMERCIAL 1(2) pb-sw

- AUTO: 
    - All commercial loads of the main and upper left (right) cabin supply centers, are supplied. 
    - Some commercial loads may be automatically shed, if necessary.
- OFF: 
    - All commercial loads of the main and upper left (right) cabin supply centers, are manually shed. 
    - The commercial loads are:
        - All galleys
        - The In-Flight Entertainment (IFE) system
        - Ground servicing
        - The cargo loading system
        - Water and waste ice protection
        - Lavatory and cabin lights
        - The water heater
        - The heated floor panels
        - The trolley lift system.

### EXT 1(2)(3)(4) pb

- OFF: 
    - The external power unit is not connected to the aircraft.
- AVAIL: 
    - The external power unit is connected to the aircraft, and is available to supply the electrical network.
- ON: 
    - The external power unit supplies the electrical network.

### APU GEN A(B) pb-sw

- AUTO: 
    - The APU generator is available to supply the electrical network.
- OFF: 
    - The APU GEN A(B) pb-sw is set to OFF with the APU running.
- FAULT: 
    - The APU generator is disconnected from the electrical network. 
    - The applicable GGPCU disconnects the APU generator from the electrical network. 
    - Associated with the following ECAM alert: ELEC APU GEN A(B) FAULT

### GEN 1(2)(3)(4) pb-sw

- AUTO: 
    - The engine generator is connected to the electrical network.
- OFF: 
    - The GEN 1(2)(3)(4) pb-sw is set to OFF with the engine running.
- FAULT: 
    - The engine generator is disconnected from the electrical network. 
    - The applicable GGPCU disconnects the engine generator from the electrical network. 
    - Associated with the following ECAM alerts:ELEC GEN 1(2)(3)(4) FAULT.
    - If the DRIVE pb-sw is set to DISC, the engine is disconnected from the engine generator, and the ENG pb-sw 
      automatically sets to FAULT.

### DRIVE 1(2)(3)(4) pb

- AUTO:
    - The engine generator is driven by the engine.
- DISC: 
    - The engine generator is disconnected from the engine. It can only be reconnected by maintenance action on ground. The reconnection requires the removal of the engine generator from the aircraft, and refurbishment of the engine generator in workshop.
- FAULT: 
    - The engine generator must be disconnected from the engine. 
    - Associated with the following ECAM alerts:
        - ELEC DRIVE 1(2)(3)(4) OIL OVHT
        - ELEC DRIVE 1(2)(3)(4) OIL PRESS LO

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---

