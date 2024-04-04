# Preflight

Before you start your flight in earnest, we have included various features in the A32NX that assist in configuring the aircraft and in-flight support. Some of these features require the aircraft to be powered on. Additionally, these guides will be linked in the appropriate locations throughout the beginner guide. 

---

## Nav Data

The AIRAC cycle (nav data version) of MSFS's nav data is updated during MSFS's regular sim updates. It's important to take stock of what AIRAC cycle you are currently using for your flight planning and if it matches the current AIRAC cycle in MSFS. When using simBrief or other planning tools with older AIRAC cycles, you may encounter `NOT IN DATABASE`, `AWY/WPT Mismatch` OR the [flight plan import](#flight-plan-import) may fail due to outdated/incorrect AIRAC cycle.

Owning a Navigraph subscription gives you access to their standalone nav data add-on for MSFS that pairs with their simBrief flight planning. It will provide you with an up-to-date AIRAC alongside any revisions, and ensure compatibility when importing from simBrief or planning your flight manually.

## Flight Planning

We highly recommend **not** using the built-in MSFS flight planner (World Map). We recommend using [SimBrief](https://www.simbrief.com/){target=new} as it is a great resource that provides routing and other information to successfully plan your flight. 

You can choose to use other software/websites to plan your route, but when using simBrief we have a handy import feature as seen in the next section. Additionally, other tools often don't have the most current nav data AIRAC cycle available.

!!! tip "Important Links for Flight Planning"
    - [SimBrief Website](https://www.simbrief.com/){target=new} (Flight Planning)
    - [Little Nav Map](https://albar965.github.io/littlenavmap.html){target=new} (Flight Planning and Charts)
    - [ChartFox](https://chartfox.org/){target=new} (Charts)
    - [Navigraph](https://navigraph.com/){target=new} (Flight Planning and Charts) <span style="color:red;">**Requires Subscription**</span>
    - See our [Custom Flight Management System](../../../aircraft/a32nx/feature-guides/cFMS.md) page and the [special notes section](../../../aircraft/a32nx/feature-guides/cFMS.md#special-notes) section.

## Flight Plan Import

If you wish to expedite the process of inputting your flight plan on the MCDU, we have incorporated a simBrief import function on the MCDU. Our EFB can also display your generated OFP within MSFS.

!!! warning "IMPORTANT"
    If you plan to import the flight plan from SimBrief, do not select an arrival airport on the MSFS world menu or flight planner. Doing this "initializes" the `FROM/TO` field when loading into your flight, removing the `INIT REQ.` option from the `INIT A` page.

[SimBrief A32NX Features](../../../aircraft/a32nx/feature-guides/simbrief.md){.md-button}

### Manual Flight Planning

The [Flight Plan Section](preparing-mcdu.md#flight-plan) in the "Preparing the MCDU" guide contains a sample routing to showcase how to input your waypoints, departure SID, and arrival STAR / procedure.

### Flight Plan Discontinuities

When inputting your flight plan into the MCDU, discontinuities appearing is an intended feature. The page below describes how to handle these when encountered during your preflight preparations.

[Flight Plan Discontinuities](preparing-mcdu.md#discontinuity){.md-button}

## Payload Management

To configure your aircraft, we have provided options onboard the aircraft to load fuel and passengers / baggage. See the following page and note any advisories.

[Fuel and Weights](../../../aircraft/a32nx/feature-guides/loading-fuel-weight.md){.md-button}

## EFB Navigraph Charts

To help with navigation during your flight, our flyPad EFB can connect to your Navigraph account to provide access to all the en route charts for your flight!

[EFB Navigraph](../../../aircraft/a32nx/feature-guides/flypados3/charts.md){.md-button}

This concludes the *Preflight* guide.

Continue with [Starting the Aircraft](starting-the-aircraft.md).
