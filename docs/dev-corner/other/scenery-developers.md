---
title: Scenery Developers
description: Resources for scenery developers.
---

# Tips for Scenery Developers

## Navigation Data

In general, it's best to stay away from navigation data in scenery packages, as the default navdata from NAVBLUE is kept up-to-date each cycle, and third-party solutions like Navigraph can provide good service when their data isn't overridden.

## ILS Auto-Tuning

The A32NX relies on the navigation data from MSFS to link ILS to runways. This depends on runway definitions in the scenery. To ensure full functionality in FlyByWire aircraft (and other MSFS avionics), make sure your `<Runway />` definitions have an [`<IlsReference />`](https://docs.flightsimulator.com/html/Content_Configuration/Environment/Airports_And_Facilities/Runway_Definition_Properties.htm#h8) linking them to the runway-aligned localizer specified in the official AIP.
