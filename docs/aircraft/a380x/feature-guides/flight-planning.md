---
title: Flight Planning
description: Discover how to load a flight plan into the FlyByWire A380X across various methods, and integrate it with your chosen ATC service.
---

# Flight Planning

## Overview

Flying an airliner is usually done using IFR (Instrument Flight Rules). This means that you will be flying with an IFR 
flight plan. The IFR flight plan is typically created before the flight, and is then loaded into the aircraft's flight 
management system (FMS).

Flying IFR (Instrument Flight Rules) even in a simulation like Microsoft Flight Simulator always requires some level of 
flight planning.

In addition to the obvious route planning, there are several other aspects which are critical to any good flight plan:

- Route Planning
  - Origin and Destination
  - Runways, SID, and STAR
  - Compliance with ATC Requirements
  - Routing and Constraints
- Fuel Calculation
- Weather Forecast
- Wind Profiles
- Cost and Time Optimization

See [Flight Planning](https://en.wikipedia.org/wiki/Flight_planning){target=new} on Wikipedia for more information.

Microsoft Flight Simulator tries to offer a simple way to do route planning (World Map before starting a flight) however,
this falls short, especially for users wanting a more realistic experience for airliner flying.

There are various ways to load a flight plan into the aircraft. In real life, pilots typically use an external data link 
to load flight plans made for the flight by their company. Or they use the FMS in the 
[MFD](../../../pilots-corner/a380x/a380x-briefing/flight-deck/main-panel/mfd.md) to enter a flight plan 
manually from their flight briefing documents.

As in real-world aircraft, it is common in flight simulation aircraft to integrate these systems directly with the 
aircraft's flight management system to be able to import all the relevant planning data. This includes the route, 
altitudes, constraints, fuel, payload (passengers, cargo), and other data points.

Also see the [Preparing the FMS](../../../pilots-corner/a380x/a380x-beginner-guide/03_preparing-fms.md) guide for more 
information. on flight planning especially for the A380X.

## Loading a flight plan in the A380X

In the A380X for Microsoft Flight Simulator, we have these options to load a flight plan:

!!! tip ""
    - [Entering a Flight Plan Manually](../../../pilots-corner/a32nx/a32nx-beginner-guide/preparing-mcdu.md#flight-plan)
    - [Loading a Flight Plan from SimBrief](simbrief.md) (recommended)
    - Creating and Loading a Flight Plan from the MSFS World Map

    <!--
    - [Creating and Loading a Flight Plan from the MSFS World Map](#msfs-world-map-flight-planning-atc-and-vfr-map)
    -->

    !!! warning ""
        MSFS World Map, MSFS ATC, MSFS VFR MAP are not yet supported in the A380X

As Microsoft Flight Simulator uses a very simplified flight planning system, we have created our own custom FMS (Flight 
Management System) which is used in the A380X. It is much closer to the FMS in the real aircraft, and it understands and 
represents real-world flight plans much more accurately.

A custom FMS on the other hand results in issues syncing the flight plan from the aircraft back into the simulator. 
Therefore, simulator-features as the MSFS ATC or the VFR Map will not always work as expected. Especially flight plans 
with complex routing may have significant issues if saved backwards or loaded externally through the simulator's 
simplified flight planning.

This is a general issue for all realistic and complex airliners in Microsoft Flight Simulator and unless the simulator's
built-in flight planner and ATC is significantly improved this will always cause problems with realistic airliners.

## MSFS World Map Flight Planning, ATC and VFR Map

Depending on how you want to use the A380X in combination with the MSFS' World Map Planning, ATC and VFR Map, you can 
choose between different methods to load a flight plan into the A380X:

!!! tip ""
    - [Not Using MSFS World Map, MSFS ATC or MSFS VFR Map](#not-using-msfs-world-map-msfs-atc-or-msfs-vfr-map) (recommended)

    <span style="color:orange;">
    The A380X does not yet support loading a flight plan from MSFS World Map or writing it back to the sim's flight plan
    for use with the MSFS ATC or the VFR Map. 
    </span>

    - Loading a Flight Plan from the MSFS World Map
    - Using MSFS World Map and MSFS ATC
    - Using a SimBrief Flight Plan and MSFS ATC

<!--
    - [Loading a Flight Plan from the MSFS World Map](#using-the-msfs-world-map-flight-planner-to-create-and-load-a-flight-plan)
    - [Using MSFS World Map and MSFS ATC](#using-the-msfs-world-map-flight-planner-and-msfs-atc)
    - [Using a SimBrief Flight Plan and MSFS ATC](#importing-a-simbrief-flight-plan-and-using-msfs-atc)

See [Setting `Sync MSFS Flight Plan`](../../common/flypados3/settings.md#sim-options) for more information.

-->

### Not Using MSFS World Map, MSFS ATC or MSFS VFR Map

!!! note ""
    This is the ideal setup for users who want to use the A380X in combination with Online ATC services (Vatsim, Ivao, 
    PilotEdge,...), 3rd party ATC add-ons or no ATC at all.

We recommend using our built-in integration with [SimBrief](https://www.simbrief.com){target=_blank} for flight 
planning. This allows you to directly import flight plans from SimBrief into the FMS.

See our [SimBrief Integration Guide](./simbrief.md) for more information.

As long as MSFS ATC and VFR Map are not required, the aircraft's flight plan does not have to be synchronized back to
the MSFS flight planner (set `flyPad's Setting > Sim Options > Sync MSFS Flight Plan` to `None`).

The MSFS ATC and VFR Map will <span style="color:orange;">**not**</span> be aware of the flight plan at all and cannot 
be used.

!!! tip ""
    ### Workaround to use MSFS ATC

    To still have some use of the built-in MSFS ATC and VFR Map in the A380X you can load an identical flight plan into 
    the MSFS World Map and into the aircraft. You can either manually enter the flight plan into the aircraft's FMS or
    load it from SimBrief. 

    **Make sure the plan you enter into the MSFS World Map is really identical to the one in the aircraft.** 

<!--
!!! warning "For SimBrief Import, Do Not Set a Destination in the MSFS World Map"
    If you plan to import a SimBrief flight plan, please do **not** set a destination airport in the MSFS World Map as 
    otherwise the aircraft will import the MSFS World Map flight plan, and it will not offer the "INIT REQUEST" option.  

### Using the MSFS World Map Flight Planner to Create and Load a Flight Plan

!!! note ""
    This is the ideal setup for users who do not use Online ATC nor the MSFS ATC service and want to use the simplified 
    flight planning of the MSFS World Map. Please do expect some issues, especially for procedures (SID, STAR, APPR).

If you want to use the MSFS World Map Flight Planner to build and load a flight plan, you need to set the `Sync MSFS 
Flight Plan` option in the `flyPad's Setting > Sim Options > Sync MSFS Flight Plan` to `Load Only`.

This ensures the MSFS flight plan is loaded into the aircraft's flight plan when starting the flight.

Any changes made to the flight plan in the FMS will <span style="color:orange;">**not**</span> be saved back to the 
MSFS flight plan. This means the MSFS ATC and VFR Map will <span style="color:orange;">**not**</span> be aware of these 
changes.

### Using the MSFS World Map Flight Planner and MSFS ATC

!!! note ""
    This is the ideal setup for users who want to use the simplified flight planning of the MSFS World Map and the MSFS 
    ATC service (despite the known issues with MSFS ATC).
    Please do expect issues, especially for procedures (SID, STAR, APPR) and MSFS ATC instructions.

If you are using the MSFS Flight Planner to build and load a flight plan, and you also want to use the MSFS ATC even 
after making changes to the aircraft's flight plan, you need to set the `flyPad's Setting > Sim Options > Sync MSFS 
Flight Plan` option to `Save`.

With this setting, the aircraft will attempt to save any changes to the flight plan made in the MCDU back to the 
simulator's flight plan. This will **not** always work as expected and may result in issues with the MSFS ATC. See the 
warning below for more information.

!!! warning "Synchronization Issues Expected"
    The aircraft's custom Flight Management System provides better accuracy and features over the default flight plan 
    manager in Microsoft Flight Simulator. This results in issues syncing the flight plan from the MCDU back into the 
    simulator. Do not expect it to work properly in all cases.

### Importing a SimBrief Flight Plan and Using MSFS ATC

!!! note ""
    This is the ideal setup for users who want to use the advanced flight planning of SimBrief
    but still use the MSFS ATC service (despite the known issues with MSFS ATC).
    Please do expect issues, especially for procedures (SID, STAR, APPR) and MSFS ATC instructions.

If you are using the aircraft's built-in SimBrief integration to import a flight plan, and you also want to use the MSFS 
ATC, you need to set the `flyPad's Setting > Sim Options > Sync MSFS Flight Plan` option to `Save`.

When importing a flight plan from SimBrief into the MCDU, do not select a destination airport and do not build a flight 
plan using the MSFS World Planner.

With this setting, the aircraft attempts to save the loaded SimBrief flight plan and any subsequent changes to the 
flight plan made in the MCDU back to the simulator's flight plan. This will **not** always work as expected and may result in issues with the MSFS ATC. See the warning below for more information.

!!! warning "Synchronization Issues Expected"
    The aircraft's custom Flight Management System provides better accuracy and features over the default flight plan
    manager in Microsoft Flight Simulator. This results in issues syncing the flight plan from the MCDU back into the 
    simulator. Do not expect it to work properly in all cases.

-->
