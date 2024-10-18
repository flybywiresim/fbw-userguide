---
title: A380X Feature Guides - Overview
description: A collection of guides for selected features of the A380X.
---

# Overview

This section is dedicated to guides for specific features and functionalities of the FlyByWire A380X. 

!!! tip "Feature Guides Status"
    The list below is not a complete collection of all features, but an initial list of features on release. 

    We will move this list eventual and extend this section of our documentation with dedicated feature guides when available to explain a feature in more detail.

## Release Feature List

### Flight Management
- [x] Working flight management system (FMS) -> based on the novel A32NX’s **fms-v2**

### ECAM
- [x] Accurate MEMOs for a multitude of systems
- [x] Electronic checklists for normal procedures (checklists) and abnormal sensed procedures (faults)

### Navigation
- [x] Onboard Airport Navigation (OANS) display, including RWY AHEAD advisory
- [x] Radio altimeters (RAs) simulated as three independent units
- [x] Ground proximity warning system (GPWS) with messages shown on PFD
- [x] Terrain display with A380-specific animations

### Instruments
- [x] Accurate representation of PFD, ND, EWD, SD and MFD
- [x] Modern, resource-efficient implementation
- [x] QNH pre-selection in the FCU

### Flight Controls
- [x] Flap load relief systems (FLRS) and auto extension/retraction (AES/ARS)
- [x] Accurate hydraulic and electronic actuation of flight control surfaces (except for flaps and slats still to do)
- [x] Triple aileron simulation on each wing, resulting in the “Valse Des Ailerons” (VDA/Aileron Dance)

### Landing Gear / Braking Systems:
- [x] Brake-to-Vacate (BTV) functionality
- [x] Runway overrun warning/protection (ROW/ROP)
- [x] Body wheel steering (visual only no hydraulics simulation yet)

### flyPad
- [x] Throttle Calibration
- [x] Binding for 4 throttles/2 throttle/1 throttle hardware configuration
- [x] Payload Page for A380
- [x] Main/Upper Deck
- [x] 4 Class Configuration
- [x] Economy, Premium Economy, Business and First Class Suites
- [x] Multiple Gate Boarding (use with GSX OR open M1L, U1L doors etc.)
- [x] Triple/Quad Stair GSX config possible* (should work, needs testing)
- [x] Real-Time/Fast/Instant with live seat layout map
- [x] GSX config/ground services in general has not been tested…
!!! info "GSX Note"
    Only single jetway in MSFS, open multiple doors to “pretend” to have dual/triple jetway.
- [x] Refueling Page for A380
!!! info "Fueling Note"
    Accurate Trim tank refueling values is a WIP

### Miscellaneous
- [x] Accurate Air Condition/Ventilation system
- [x] Engine and APU fire implemented, with respective abnormal procedures via ECAM
- [x] Accurate implementation of the electrical system
- [x] Accurate implementation of hydraulic core system architecture
- [x] RAT simulation including visible variable pitch animation
- [x] Custom physical based flex system for wings/rudder/elevator. Wings simulated as soft bodies and reacting to fuel load.
