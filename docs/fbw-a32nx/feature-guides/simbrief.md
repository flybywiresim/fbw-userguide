# SimBrief Integration

## Why Flight Planning

Flying IFR (Instrument FLight Rules) even in a simulation like Microsoft Flight Simulator always requires some level of flight planning.

In addition to the obvious route planning there are several other aspects which are critical to any good flight plan:

- Route planning
    - Origin and destination
    - Runways, SID and STAR
    - Compliance with ATC requirements
    - Routing and constraints
- Fuel Calculation
- Weather Forecast
- Cost and time optimization

See [Flight Planning](https://en.wikipedia.org/wiki/Flight_planning){target=new} on Wikipedia for more information.

Although Microsoft Flight Simulator tries to offer a simple way to do route planning (World Map before starting a flight) this is falling short especially for users wanting a more realistic experience for airliner flying.

In real life airlines and pilots use dedicated software and various sources and services for creating their flight plans.

In the world of flight simulation simBrief does all that for the users based on real word data bases and sources. SimBrief provides on average ~40.000 flight plans to users each day and is the most commonly used tool for flight planning for non professional flight simulation.

It is absolutely possible to use the simBrief OFP (Operational Flight Plan) and configure and program the aircraft based on it without any special integration into the flight sim software or aircraft.

But as in real world aircraft it is common in flight simulation aircraft to integrate these systems directly with the aircraft's flight management system to be able to import all the relevant planning data.
This includes the route, altitudes, constraints, fuel, payload (passengers, cargo), and other data points.

This is why FlyByWire has implemented this integration into simBrief and will continue to improve this experience even further in the future.

## Flight Planning with SimBrief

This is best explained by simBrief itself: [simBrief User Guide](https://www.simbrief.com/system/guide.php){target=new}

## Setup A32NX simBrief Integration

See [Setup simBrief Integration](flyPad/settings.md#simbrief-integration)

## Importing the simBrief OFP to the FMS (MCDU)

See [A32NX simBrief Integration](../../pilots-corner/beginner-guide/preparing-mcdu.md#a32nx-simbrief-integration)

## Importing the simBrief OFP to the flyPad

See [flyPad Guide - Load from simBrief](flyPad/dashboard.md#load-from-simbrief)

See [flyPad Guide - OFP](flyPad/dispatch.md#ofp-page) on how to view the simBrief Operational Flight Plan.


