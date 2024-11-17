---
title: Maintenance Panel
description: The A380 Flight Deck Maintenance Panel description.
---

# Maintenance Panel

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---

![Maintenance Panel](../../../assets/a380x-briefing/flight-deck/ovhd/maintenance-panel.png 
"Maintenance Panel"){loading=lazy}

[//]: # (TODO API Doc Link)

## Description
The Airbus A380 overhead maintenance panel provides a central interface for accessing various aircraft systems and 
performing maintenance checks. The panel is divided into sections, each dedicated to specific systems or functions. 

Here's a breakdown of the major systems covered on the overhead maintenance panel:

### OXYGEN

#### RESET pb
Maintenance personnel uses this pushbutton to reset the control circuit, after the oxygen system has
been used.

- When pressed:
  - Resets the oxygen system: The PAX SYS ON light (on the OXYGEN panel) goes off.
  - When the reset is completed, ON goes off.
  - The reset lasts approximately three seconds.
- FAULT:
    - The reset has failed.

### GND HYD

See [Hydraulic Panel](./hyd.md) for more information.

### FUEL

#### REFUEL pb-sw
Refueling is usually initiated from the external REFUEL panel, that is under the aircraft belly fairing.
However, refueling can also be initiated from the cockpit, via the REFUEL pb-sw. Cockpit refueling
takes a priority over a refueling initiated from the external REFUEL panel.

- OFF:
  - Refueling from the cockpit is not activated.
- ON:
    - When pressed, refueling from the cockpit is enabled.
- END/ON:
    - Refueling was initiated from the cockpit and has completed, or has aborted.
    - If the FQMS aborts refueling, the light flashes. 
    - This is associated with the following ECAM alert: FUEL REFUEL FAULT 

#### AUTO GND XFR pb-sw

- OFF:
    - Automatic ground transfer is not active.
    - Note: Only manual transfers can be initiated from the external REFUEL panel.
- ON:
    - When pressed, automatic ground transfer is activated to automatically obtain the ground CG target.
    - Note: All transfer pumps must be ON to perform an automatic ground transfer.
- END/ON:
    - Automatic ground transfer is completed, or is aborted by the FQMS.
    - If the FQMS aborts the automatic ground transfer, the light flashes. 
    - This is associated with the following ECAM alert: FUEL AUTO GND XFR FAULT 

### BAT

#### BAT 1/2/APU/ESS selector
Selects the battery in order to display the voltage. 

#### BAT Display 
Displays the voltage of the selected battery.

### ENG

#### FADEC GND PWR pb

- AUTO: 
  - The aircraft electrical network or the FADEC alternator automatically supplies the FADEC.
- ON:
  - On ground, the aircraft electrical network supplies the FADEC for 10 min, provided that:
      - The ENG FIRE pb-sw is not pressed
      - The FADEC is not self-powered.
      - The FADEC is self-powered when N2 is above 12.5 %.

### MAINT

#### GND CONNECTION pb (INOP)

- OFF: 
    - The maintenance personnel cannot connect a PMAT to the NSS AVNCS side via the plugs distributed throughout the 
      aircraft.
- ON: 
    - The maintenance personnel pressed the MAINT GRND CONNECTION pb-sw .
    - For maintenance purposes on ground, the maintenance personnel can connect a PMAT to the NSS AVNCS side via the 
      plugs distributed throughout the aircraft.

### ELEC

#### REMOTE C/B CTL pb

- OFF:
    - Normal operation.
- ON:
    - The remote C/B controller is ON, and can be displayed on the OIT. 
    - This controller is for maintenance purposes only.

### NSS
Network Server System (NSS) communication between the NSS CAB side and the FLT OPS side.

#### NSS GATELINK pb-sw

- ON:
    - The Terminal Area Wireless LAN Unit (TWLU) is on.
    - Communication between NSS and ground via gatelink is possible.
- OFF:
    - The Terminal Area Wireless LAN Unit (TWLU) is off.
    - Communication between NSS and ground via gatelink is not possible.

#### NSS CAB DATA TO NSS pb-sw

- ON:
    - Communication between NSS CAB side and FLT OPS is enabled.
- OFF:
    - Communication between NSS CAB side and FLT OPS is disabled.

### AIR

#### OVHT COND AIR FANS RESET pb

In the case of overheat of a ventilation system fan, the affected fan automatically stops. The
Maintenance personnel uses this pushbutton to restart the fan.

- Not illuminated:
    - No overheat is detected.
- FAULT illuminated:
    - One or several fans of the ventilation system failed due to overheat.
    - The FAULT light is not always associated with an ECAM alert, depending on the location and the number of the 
      affected fan(s). For example:
        - If one primary cabin fan fails, the ECAM alert COND ONE PRIMARY CABIN FAN FAULT triggers
        - If one cabin air extraction fan fails, no ECAM alert triggers. There is no operational impact.
    - When pressed, resets the affected fan(s). When the reset is completed and successful, the FAULT light goes off.

### VENT

#### AVNCS GND COOLG pb

- AUTO:
    - Normal operation of the supplemental cooling system.
- OFF:
    - The supplemental cooling system is off.
- FAULT:
    - The supplemental cooling system is failed.
    - Associated with the following ECAM alerts:
        - VENT COOLG SYS 1(2) OVHT
        - VENT COOLG SYS PROT FAULT

### Miscellaneous

#### SVCE INT OVRD pb

- AUTO:
    - The service interphone is automatically inhibited in flight.
  - ON:
    - If the service interphone remains abnormally inhibited on ground, the ground crew can manually activate it, by 
      pressing the SVCE INT OVRD pb.

#### GND HF DATA LINK

- AUTO:
    - HF data communication is automatically inhibited on ground.
- OVRD:
    - For maintenance purposes, the ground crew can press the GND HF DATALINK pb-sw to activate HF data communication on
      ground.

#### CKPT DOOR LCKG SYS

Maintenance personnel uses this pushbutton-switch to turn off the Cockpit Door Locking System
(CDLS), in order to ease ground operations (e.g. servicing, cleaning, maintenance, etc.).

- AUTO:
    - The CDLS is operative.
    - When pressed, turns off the CDLS.
- OFF:
    - The CDLS is off, and the door is free to open from the cockpit or from the cabin.
    - When pressed, turns on the CDLS.

---

[Back to Overhead](../overviews/ovhd.md){ .md-button }

---


