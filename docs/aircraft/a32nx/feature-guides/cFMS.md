---
title: Custom Flight Management System
description: Dive into the A32NX's custom FMS and stay informed with the latest known issues and troubleshooting tips.
---

<link rel="stylesheet" href="/../../stylesheets/reported-issues.css">

# Custom Flight Management System

This page outlines features and issues provided by the initial integration of our custom FMS. Please also make ensure you have read the [known issues](#known-issues) section.

{==

For guides on utilizing features included with our custom FMS, see the [Guides and Information](#guides-and-information) section below.

==}

---

## Features

We will always list the latest updates in the following section. As we improve our custom flight management system, older versions will be listed in a collapsible format in the [Older Versions](#older-versions) section.

### Latest - Version 2

FMS v2 is a complete rewrite of the entire flight planning system of the A32NX (and by extension A380X). It will also allow us to fully integrate planned features that have 
been waiting for this rewrite to be completed.

It entirely replaces the old system, a derivative of the CJ4 mod flight plan system, with a completely custom one, purpose-built for simulating Honeywell Airbus FMS software found on the A320/A330/A340/A350/A380.

[See Known Issues](#fms-v2-issues){ .md-button }

!!! warning "RNP/RNAV"
    FMS v2 lays the groundwork for many of our upcoming features to be implemented properly. 

    However, it is important to note that the full functionality of flying RNP/RNAV procedures is not yet implemented. Pilots are still capable of flying the procedure 
    laterally in NAV mode, but the vertical profile will not be followed and requires intervention via Autopilot features or Pilot Flying.

    This will be added in a future update.

!!! warning "Cloud Break Approaches"
    Cloud break approaches that are not assigned to a runway are not a feature of the FMS in use onboard the A32NX (and it's real life counterpart).

    If you have been using these procedures in the simulator, they are no longer available for selection in the MCDU.

#### New / Updated Capabilities

- [x] Introduction of missed approach capability
    - Loading of legs, stringing
      - Sequencing logic
- [x] Introduction of alternate flight plan capability
    - Origin/Destination airport revisions (DEPARTURE, ARRIVAL)
    - Element insertion/deletion on FPLN page
    - Hold revisions
    - Airway insertion
- [x] Improved logic and handling of FMS routing
    - Stringing logic has been improved where discontinuities in your flight plan are more accurately represented and handled
- [x] Improved logic for constraints and speed/altitude restrictions
    - Accurately loads a constraint at the first waypoint of a star
    - Merging values when clearing discontinuities
- [x] STARs with multiple IAFs now string correctly

#### Major Technical Design Differences

- Flight plan data structure
  - The main type of a flight plan is a `FlightPlanElement`, which resolves to type `FlightPlanLeg | Discontinuity`. Only the leg type actually contains information. This API is typed in a way that mandates proper verification of the type by the consumer and allows for semantic narrowing by TypeScript.
  - Flight plans are divided into segments, which are finite in number and match the only possibilities in a Honeywell Airbus FMS. There is no support for out-of-order segments and operations on flight plans are limited to this layout, reducing the API surface.
  - `FlightPlanManager` is split into two classes:
    - `FlightPlanService` (for now a singleton - will likely change) - this exposes allowed and common operations on flight plans, accepting parameters to target a specific plan or sub-plan (alternate). It also encapsulates TMPY logic.
    - `FlightPlanManager` - this exposes operations on managing the storage of flight plans (create, delete, copy, swap, etc.)

#### Motivation

- The previous flight planning system **possesses a segmenting system prone to breaking, causing potential bugs in many places.**
- The previous flight planning system **does not correctly manage origin and destination legs.** Those are often added ad-hoc, without real proper representation at appropriate times in the flight plan. This also results in problem correctly handling approach missed approach points and therefore, makes missed approach segments impossible.
- The previous system **operates on a flight plan data structure that does not suit the reality of an airliner flight planning system.** Legs are represented as waypoints, with irrelevant data strewn around like predictions, and important data present in untyped free-for-all dictionaries. Discontinuities exist solely as a property of the leg they come after, not as an actual flight plan element.
- The previous system is **not made in a way that can accommodate accurate stringing algorithms.**
- The previous system **does not support efficient flight plan synchronization across clients.**

### Older Versions

??? info "Version 1.5"

    We have introduced new features to the custom flight management system as part of a minor update. Please see the list below:

- LNAV Updates
  - Holding Patterns
  - Turn direction constraints on non-TF legs
  - Overfly restriction support
  - ARINC424 Leg Types
    - AF, CA, CI, CR, CF, DF, HF, HM, HA legs ([See List of Leg Types](../../../pilots-corner/a32nx/a32nx-advanced-guides/flight-planning/leg-types.md))
  - Turn Prediction Types
    - Path capture
    - Course capture
    - Direct to fix turn
    - Holding pattern entry turn
- Navigation Display
  - Removed flight plan loading from local storage
  - Corrected active waypoint ETA display
  - Added `EfisVectors` systems with optimized transmit task queue + support for future display of OFFSET, SECONDARY, SECONDARY DASHED, MISSED APPROACH, ALTERNATE and EOSID flight paths.

??? info "Version 1"

    This constitutes the original feature set of our custom flight management system.
        
    - Custom flight plan management, replacing the default Asobo flight plan manager (FPM).
    - SID/STAR/APPR waypoints can now be edited.
    - No more USR waypoints from the Asobo FPM.
    - Correct procedure and direct-to sequencing.
    - Added Discontinuities as in the real life aircraft. See [Guides and Information](#guides-and-information) below.
    - Support for multiple leg types:
        - TF: Track to a Fix defines a great circle track over ground between two known databases fixes.
        - RF: Constant Radius Arc defines a constant radius turn between two database fixes, lines tangent to the arc and a center fix.
        - VM: Heading to a manual termination defines a specified heading until a Manual termination.
    - Cross-track error indicator on the ND.
    - Improved LNAV turn prediction.
    - Roll anticipation distance.
    - Improved flight plan rendering / drawing.
    - Improved ND display filters for ARPT, VOR, NDB, WPTs.
    - MCDU FIX INFO page for radials and distance circles on navigation fixes. See [Guides and Information](#guides-and-information) below.

## Guides and Information

- [MCDU Fix Info](../../../pilots-corner/a32nx/a32nx-advanced-guides/flight-planning/fixinfo.md)
- [Flight Plan Discontinuities](../../../pilots-corner/a32nx/a32nx-advanced-guides/flight-planning/disco.md)

## Known Issues

### FMS v2 Issues

!!! warning ""
    Please note the following issues are listed in order of severity.

- Alternate fuel on INIT FUEL PRED is not calculated in some cases.
    - It's best to insert the alternate fuel from the OFP manually.
- CRZ FL/TEMP on the INIT page goes blank when starting descent.
    - Can just be ignored, no negative effect.
- No transition out of SRS when going around above GA ACC ALT.
    - Pull the altitude knob to enter OP CLB. It's unclear whether this is IRL behavior.
- ALTN CRZ FL in DESCENT WIND page does not consider alternate flight plan distance.
    - Ignore this for now, alternate fuel is not calculated with our current implementation.


### Standard Issues

- CA leg terminations are sometimes in the wrong place, and do not adapt to V/S.
- Some path captures will be incorrectly drawn. This will not affect guidance.
- INTCPT calculation can be off on large distances.
- Course captures do not adapt to PPOS when nextLeg is active. This can cause the final path to be off to the side.
- WX on ND is not implemented yet. We are waiting for better API support by Microsoft Flight Simulator. See our [Forums Feature Request](https://forums.flightsimulator.com/t/implement-weather-and-terrain-api-s-for-aircraft-developers-to-implement-accurate-radar-predictive-windshear-egpws-and-metar-wind-uplink/442016){target=new}.
- Rendering of flight path on the ND of terminal procedure legs may be glitched or incorrect during cruise. - [See Special Notes](#flight-path-rendering).
- Rendering of flight path on the ND of legs will be glitched or incorrect if you are flying faster than the appropriate/correct speed. - [See Special Notes](#flight-path-rendering).
- Syncing the aircraft flight plan with the sim's flight plan for default ATC and VFR map is not 100% supported. - [See Special Notes](#special-notes).
- Defining both FROM/TO in the world map shows in the FROM/TO INIT A page but does not populate the airport list in our METAR (AOC) integration.
- ETA in F-PLN A on the MCDU may not be 100% accurate.
- Flight plan frozen on loading in (Please post the specific route on which this occurs and under what circumstances, i.e. spawning in c&d using the MSFS flight planner, or simBrief, or loading in .PLN generated by simBrief or other external program).
- Fuel calculations might be incorrect.
- Route on the VFR map will not match up with what is shown on the ND.

## MSFS Flight Planning

Please see our [Flight Planning in MSFS Guide](flight-planning.md) for more information.

## WX/TER

!!! info "Important Notice"
    - TCAS is now available in the all versions.
    - Terrain Radar is now available in the all versions via [SimBridge](../../../index.md).
    - Please see our [CFMS NOTAM](https://flybywiresim.com/notams/cfms/) for further WX/TER information.

It is important to note that the weather radar is not available yet with the latest version of our cFMS(v2). Our current focus is to deliver a more realistic flight planning 
and navigation experience while maintaining performance and reliability. However, we are not satisfied with how the default code performs together with our custom systems.

We believe the benefits that cFMS provides outweigh the temporary lack of WX functionality. Weather will still prove to be a challenge due to the lack of a native SDK API. We have posted about it on the MSFS forums, where it currently sits at the top of the wishlist, and Asobo are investigating how to best improve their API.

[Read more about the weather and terrain API.](https://forums.flightsimulator.com/t/implement-weather-and-terrain-api-s-for-aircraft-developers-to-implement-accurate-radar-predictive-windshear-egpws-and-metar-wind-uplink/442016){target=new}
**Please note again that terrain radar is available on our Stable and Development Versions.**

## Flight Path Rendering

In certain instances, some legs may not render correctly with our current implementation and may look strange in PLAN mode or while en-route. In most cases, the A32NX will attempt to fly the route, and you won't experience any major issues.

Additionally, some flight plans may have extraneous waypoints that can lead to wrongly drawn flight paths. While this can be an edge case, going through your flight plan in `PLAN` mode you can find offending waypoints that need to be removed, which will provide a much more reasonable drawn flight path.
