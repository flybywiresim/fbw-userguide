<link rel="stylesheet" href="/stylesheets/bg.css">

# Engine Start and Taxi

This guide will explain the correct procedures to accomplish a pushback with engine start and perform a safe taxi to the departure runway.

!!! warning "Disclaimer"
    The level of detail in this guide is meant to get a FlyByWire A320neo beginner safely from the terminal to the runway hold short point.

    A *beginner* is defined as someone familiar with flying a GA aircraft or different types of airliners. Aviation terminology and know-how is a requirement to fly any airliner, even in Microsoft Flight Simulator.

    You will find many great videos on YouTube on how to fly the FlyByWire A32NX.<br/>
    Check out the FlyByWire YouTube Channel as well: [FlyByWire on YouTube](https://www.youtube.com/c/FlyByWireSimulations/playlists)

---

## Prerequisites

- BEFORE START checklist completed
- IFR clearance obtained
- The aircraft is secure
- APU MASTER SW - `Set to ON` and the APU is available
- Beacon light - `Set to ON`

At this time, we may request for clearance to push and start from ATC.

[Download FlyByWire Checklist](../assets/sop/A32NX%20Documentation/FBW%20A32NX%20Checklist.pdf){ .md-button }

---

## Chapters / Phases

This guide will cover these chapters:

1. [Pushback](#pushback)
2. [Engine Start](#engine-start)
3. [After Engine Start](#after-engine-start)
4. [Flight Controls Check](#flight-controls-check)
5. [Taxi](#taxi)
6. [General Resources](#general-resources)

---

## Before Pushback and Start

Once all passengers have boarded and secured, we are ready to begin pushback.

??? tip "What and Why"
    Before pushback the flight crew need to ensure the external power is not used any more so the ground crew can
    safely disconnect the aircraft from the ground power. The same goes for the low-pressure ground carts as keeping 
    them connected during engine start could cause faulty triggers. 

`EXTERNAL POWER (1, 2, 3, 4).....................DISCONNECT and CHECK AVAIL`<br/>
`EXTERNAL POWER DISCONNECTION (GROUND CREW) ....................... REQUEST`<br/>
`LOW PRESSURE GROUND CARTS ............................. CHECK DISCONNECTED`<br/>

??? tip "How and Where"
    These actions are performed on the overhead panel. The external power is disconnected by pressing the respective 
    button on the overhead panel. The external power connections and low-pressure ground carts are disconnected by the 
    ground crew.

    <p style="color:yellow; font-size:18px;">TODO: add images or links to the flight deck</p>

`BEFORE START CHECKLIST - DOWN TO THE LINE ....................... COMPLETE`<br/>

### Pushback Clearance and Preparation

??? tip "What and Why"

    Contact ground ATC and inform them you are ready to push and start. If you are on a network such as VATSIM, a typical
    response from ground would give you clearance for your request and a direction to face (or any direction). 

`PUSHBACK/START UP CLEARANCE ....................................... OBTAIN`<br/>
`WINDOWS AND DOORS ............................................CHECK CLOSED`<br/>
`SLIDES ............................................................. ARMED`<br/>
`BEACON ................................................................ ON`<br/>
`THRUST LEVERS ....................................................... IDLE`<br/>
`PARKING BRAKE ........................................................ OFF`<br/>
`N/W STEERING DISC MEMO ................................... CHECK DISPLAYED`<br/>

??? tip "How and Where"
    <p style="color:yellow; font-size:18px;">TODO: add images or links to the flight deck</p>
    
    At EDDM on gate 208 ans runway 08L you could expect the following push and start clearance from ground:

    "** Your Aircraft Callsign**, ground. You are clear to push and start onto Whiskey 3 facing north."

    At this point, we may begin pushback away from the terminal onto the taxiway Alpha 3.

    <p style="color:yellow; font-size:18px;">TODO: optimze image</p>
    ![parking stands](../assets/beginner-guide/taxi/parking-stands-guidelines.png){loading=lazy}
    <sub>Copyright © 2021 Navigraph / Jeppesen<br>
    "Navigraph Charts are intended for flight simulation use only, not for navigational use."

`BEFORE START CHECKLIST - BELOW TO THE LINE ...................... COMPLETE`<br/>

### Pushback

There are several options available to you in MSFS to achieve a successful pushback.

- The flyPad (EFB) ground control screen
- MSFS built in ATC pushback controls
- Third-party pushback add-ons

This guide assumes that the flyPad's pushback functionality is used. 

Click below to learn more about the flyPad and how to use it for pushback.

??? tip "How to Pushback" 
    ### How-to Pushback

    The FlyByWire A32NX has a ground operations page on its built-in flyPad EFB (Electronic Flight Bag). This page allows 
    controlling the pushback of the aircraft and other useful ground operations such as calling the Jetway, baggage or 
    catering, etc.
    
    Although Microsoft Flight Simulator also has some pushback functionality built into the default ATC service, this guide 
    will only cover the A32NX pushback functionality.
    
    ![flyPad Pushback](../../../aircraft/a32nx/assets/flypados3/flypad-ground-pushback.png "flyPad Pushback"){loading=lazy}
    
    !!! block ""
        ![Call Tug](../../../aircraft/a32nx/assets/flypados3/flypad-pushback-tugcall.png "Call Tug"){loading=lazy align=left width=30%}
        
        After we received clearance to pushback, we will call the pushback tug by pressing the `Call Tug` button on the flyPad.
    
        If a pushback tug is available at this gate or stand, it will then start attaching itself to the nose wheel.
    
        !!! warning ""
            Some airports / gates / stands do not show a tug. This functionality still works, and you can push back as if a 
            tug is attached. It looks like an invisible tug is pushing the aircraft.
    
    After the tug is attached to the nose wheel, we can start pushing back by using the control buttons or the rudder and elevator controls.
    
    See the flyPad documentation for more details: [flyPad Pushback](../../../aircraft/a32nx/feature-guides/flypados3/ground.md#pushback)

---

## Engine Start

Once we are clear of the terminal and/or the ground crew has notified the flight crew it is clear to start engines, we 
can proceed with the following steps.

??? tip "What and Why"
    The engines 

`ENGINE START selector .......................................... IGN START`<br/>
??? Note "ENGINE START Selector"
    The engine page on the system display should appear. It's recommended to wait 10 seconds before setting the engine 
    masters lever to the ON position. This waiting time ensures a series of tests conducted to the engines in order to 
    detect a fault.
`START ENGINES 1 and 2 ........................................... ANNOUNCE`<br/>
`ENGINE MASTER 1 then 2................................................. ON`<br/>
??? Note "ENGINE START"
    Any engines can be started first, at the pilots discretion.
`WHEN AVAIL: ENGINE IDLE PARAMETERS .......................... CHECK NORMAL`<br/>
??? note "ENGNIE IDLE PARAMETERS"
    The engine idle parameters are displayed on the engine page on the system display. The engine idle parameters should 
    be checked to ensure the engines are starting normally.
    
    <p style="color:yellow; font-size:18px;">TODO: use correct A380 values</p>

    - N1 is at roughly 19 %
    - N1 reported `AVAIL`  
    - N2 is at roughly 68 %
    - EGT settles at about 520 °C
    - FF is at roughly 290 kg/h

`START ENGINES 3 and 4 ........................................... ANNOUNCE`<br/>
`ENGINE MASTER 3 then 4................................................. ON`<br/>
`WHEN AVAIL: ENGINE IDLE PARAMETERS .......................... CHECK NORMAL`<br/>

??? tip "How and Where"
    <p style="color:yellow; font-size:18px;">TODO: add additional info, images or links to the flight deck</p>


??? note "Note: Bleed Air"
    The A380 needs pressurized air to start the engines. This pressurized air is usually generated by the APU for the 
    start of the engines. This is called bleed air, as it is a byproduct of a running jet engine where pressurized air 
    is taken from the engine to be used on other systems.

    **To start the engines, you need to have the APU available and the APU Bleed ON - see [Cockpit Preparation](./02_cockpit-preparation.md#overhead-panel-center-bottom-to-top).**

    You can also use a so called Ground Air Starter Unit (ASU) to start the engines which you can connect to the aircraft
    using the Ground Services page of the flyPad. <p style="color:yellow; font-size:18px;">TODO: link or image</p>

    You can start the second engine with bleed air (X-Bleed) from the first engine. It would usually not be used at the 
    gate as the APU would be running anyway, but it is used during single engine taxi when the second engine is started 
    while rolling to the runway. <p style="color:yellow; font-size:18px;">TODO: link to separate x-start guide</p>

---

## After Engine Start

??? tip "What and Why"
    After the engines have been started, the flight crew need to ensure that all systems are functioning correctly and 
    that the aircraft is ready for taxi.

`ENGINE START selector ............................................... NORM`<br/>
`APU BLEED ............................................................ OFF`<br/>
`ENGINE ANTI_ICE .............................................. AS REQUIRED`<br/>
??? note "ENGINE ANTI_ICE"
    It is recommended to set the engine anti-ice to ON when icing conditions are expected, standing water/slush/ice/snow 
    is on the taxiway or on the runway when the outside air temperature is less than 10°C.
`APU MASTER SW ........................................................ OFF`<br/>
`GROUND SPOILERS ...................................................... ARM`<br/>
`RUDDER TRIM ......................................................... ZERO`<br/>
`FLAPS T.O POSITION.................................................... SET`<br/>
`PITCH TRIM ......................................................... CHECK`<br/>
`ECAM STATUS ........................................................ CHECK`<br/>
`CLEAR TO DISCONNECT AND HAND SIGNALS ............................ ANNOUNCE`<br/>
`N/W STEERING DISC MEMO ............................... CHECK NOT DISPLAYED`<br/>
`FLIGHT CONTROLS .................................................... CHECK`<br/>
??? note "FLIGHT CONTROLS"
    It is recommended to perform the flight control verification when the flaps are set to the takeoff configuration. 
    To perform the test, the captain remain silent, while the first officer announces call-outs. It is recommended to 
    start with the pitch, then roll, then yaw. The captain must ensure to maintain the sidestick to the position to give
    enough time to the control to reach the full position. The first officer monitors the flight control page of the 
    system display and announces “FULL UP”, “FULL DOWN”, “NEUTRAL”, “FULL LEFT”, “FULL RIGHT”, “NEUTRAL”. For the 
    rudder, the captain must press the PEDAL DISC pushbutton to disconnect the nosewheel steering, then apply the left 
    and right position of the rudder.

??? tip "How and Where"
    <p style="color:yellow; font-size:18px;">TODO: add additional info, images or links to the flight deck</p>

`AFTER START CHECKLIST ........................................... COMPLETE`<br/>

[//]: # (TODO)
<p style="color:yellow; font-size:18px;">TODO: update checklist image</p>
![after start checklist](../assets/beginner-guide/taxi/afterstart.png){loading=lazy}

Perform the AFTER START checklist.

---

## Taxi

Make sure to have charts or diagrams of the airport you are currently in will as it help you navigate efficiently and 
safely. There are many resources and applications available online that are either free or paid which you can use.

For additional information on signs and markings on the ground, please see [General Resources](#general-resources).

`TAXI CLEARANCE .................................................... OBTAIN`<br/>

??? note "TAXI CLEARANCE"
    After having successfully started the engines, we can contact ATC to request taxi clearance. As per our routing in the
    [Preparing FMS Guide](03_preparing-fms.md), we should be expecting a takeoff from runway 08L. As such, a sample taxi 
    clearance may be as follows:
    
    "**Your Aircraft Callsign**, ground. Runway 08L, taxi via Whiskey 2, hold short of November 3, continue via November 
    to Alpha 3, hold short Alpha 3."
    
    Referencing the airport chart below, the aircraft should be sitting near the A3 holding point.
    
    [//]: # (TODO)
    <p style="color:yellow; font-size:18px;">TODO: optimize image</p>
    ![Taxi Chart](../assets/beginner-guide/taxi/airport-chart-guidelines.png){loading=lazy}
    <sub>Copyright © 2021 Navigraph / Jeppesen<br>
    "Navigraph Charts are intended for flight simulation use only, not for navigational use."
    
    Make sure to pay attention to any warnings or notices on the respective taxi chart beforehand, so you are aware of any 
    important information while performing your taxi.
    
    Once we have the routing from ATC and have read back the taxi clearance, we are now free to taxi to the runway.

`NAVIGATION DISPLAY RANGE selector .................... ZOOM AS APPROPRIATE`<br/>
??? note "NAVIGATION DISPLAY RANGE - OANS"
    At the pilot’s discretion, zoom as necessary to activate the onbard airport navigation system (OANS). Then, at the 
    pilot’s discretion, select either ARC, ROSE, or PLAN mode. 
`NOSE LIGHTS ......................................................... TAXI`<br/>


### Moving the Aircraft

Exterior Lights:

- RWY TURN OFF - `Set to ON`
- NOSE - `Set to Taxi`

![exterior lights](../assets/beginner-guide/taxi/taxi-lights.png){loading=lazy}

Before Moving Safety Check:

- Verify the ground crew is safely away.
- Look to the left and right to ensure clearance from other aircraft or vehicles.
- Release the parking brake.
- Brakes pressure - `Check at Zero`

![brakes pressure](../assets/beginner-guide/taxi/brakes.png)

At this point, the aircraft may start rolling. Depending on the weight of the aircraft, we may need to add a little power to the engines to get going. Increase power to roughly ~25-30% N1. Be mindful that we are not blasting N1 towards or around the terminal.

- Leave a bit of thrust on and perform a quick brake check to ensure the hydraulics and brakes are fully functioning.
    - We don't need to come to a complete stop, but merely check the brake pressure status when performing the brake check.
- If an arc is shown above the brake temperature on the WHEEL SD page on the lower ECAM, turn the brake fans on.

If it is required to perform a sharp turn immediately, we may need more than ~ 25 - 30 % N1 and should set the thrust accordingly. Try not to perform the brake check while in a turn, as we don't want to come to a complete stop while turning.

### During Taxi

While underway to the runway, perform the following as part of the taxi flow:

- Use the tiller or rudder pedals to steer the aircraft.
    - See [Nose Wheel and Tiller Operation](../../../aircraft/a32nx/feature-guides/nw-tiller.md)
- Perform a [flight controls check](#flight-controls-check) (if you haven't already).
- Verify the ATC clearance for departure.

It is important to verify and confirm the information in the MCDU as we taxi. This is increasingly important if the ATC clearance changes en route to the runway.

#### **Takeoff Data/Conditions**

*In case of a runway or takeoff data change, perform the following:*

- FINAL TAKEOFF DATA - `Confirm or Recompute`
- FMS TAKEOFF DATA - `Check/Revise as RQRD`
- REVISED FMS TAKEOFF DATA - `Crosscheck`
- F-PLN (RUNWAY) - `Revise`
- FLAPS lever - `As Appropriate` *Select takeoff position*
- V1, VR, V2 - `Reinsert`
- FLX TO temperature - `Reinsert`

#### **AFS/Flight Instruments**

Perform the following:

- F-PLN (SID, TRANS) - `Revise or Check`
    - Check to ensure that the ATC clearance agrees with the flight plan if we are departing using NAV mode.
- INITIAL CLIMB SPEED AND SPEED LIMIT - `Modify or Check`
- CLEARED ALTITUDE ON FCU - `Set`
- HDG ON FCU - `If Required, Preset`
    - If ATC requires a specific heading after takeoff, preset the heading on the FCU. NAV mode will be disarmed and RWY TRK mode will keep the aircraft on the runway track.

This is the FCU (more details are provided in the [Take off, Climb, and Cruise Guide](05_takeoff-climb-cruise)):
![FCU](../assets/beginner-guide/taxi/FCU.png "FCU"){loading=lazy}

- BOTH FD (*flight directors*) - `Check on`
- PFD/ND - `Check`
- TAKEOFF BRIEFING - `Confirm`
- RADAR (if required) - `On`

    The current implementation of the weather radar in MSFS will show precipitation along the route. Additional functions are unavailable at this time. However, we should set the Radar to Sys 1 if required for departure.

- PREDICTIVE WINDSHEAR SYSTEM - `Auto`

    Currently, this only clears the warning on the ECAM and does not provide a function in the sim. We should perform this action regardless.

The weather panel is located on the bottom left of the lower pedestal and looks like the following:

![WX Radar Panel](../assets/beginner-guide/taxi/wx-radar-panel.png "WX Radar Panel"){loading=lazy}

- ATC code/mode - `Confirm/Set for Takeoff`
- TERR ON ND - `As RQRD`
- AUTO BRK MAX pb-sw - `On`

![Auto Brake](../assets/beginner-guide/taxi/auto-brk.png "Auto Brake"){loading=lazy}

!!! info "Getting Ready for Take off"
    At this point in the guide, you should have performed many of the essential flow items before you line up at the runway. The next guide [Take off, Climb, and Cruise](05_takeoff-climb-cruise) will instruct you on performing your final checks and before take off checklist.

**For additional information:** See the sections below for extended taxi information, and visit the [General Resources Section](#general-resources) on this page to help you understand the different signs and elements found on the ground at an airport.

---

#### Speed While Taxiing

Pay attention to the ground speed (visible on the ND) while taxiing.

- **Straight Line**

    Anything up to 30 kt is reasonable, but some airports may carry their own local restrictions that should be noted. This is not an absolute rule and is usually typical SOP for airlines in a straight line.

- **90° (Sharp) Turns**

    A good speed would be around 10kts. This provides safety for the flight crew as they perform their safety demonstration/checks.

- **Regular Turns**

    Around 15kts is an acceptable speed, with a similar concept to providing safety as described above.

#### Handy Tips While Taxiing

- **Maintaining Center Line**

    We can use the gray vertical bar in between the PFD and ND as a reference point and keep the taxi line in between the two screens.

- **Turning**

    Using the same bar mentioned above, try to "over steer" (keep the nose wheel slightly ahead of the line while we turn). This helps keep the aircraft centered while performing a turn.

    Slow down while turning!

#### Crossing a Runway

When approved to cross a runway (active or not) perform the following actions:

- Look out the windows and visually ensure that there are no visible aircraft to the left and right.
- Turn on extra lights to ensure the aircraft is visible when crossing:
    - Strobe lights - `Set to ON`
- Inform ATC we have vacated the runway if required.

!!! warning
    Never cross a runway without express permission from ATC and providing a read back of said instructions. Always ensure maximum safety when crossing.

---


## General Resources
<p style="color:yellow; font-size:18px;">TODO: maybe move this to a separate page (also for the A32NX bg to avoid duplication </p>

This section provides you with information on understanding the different signs and markings you may see while taxiing at the airport.

### Airport Signage and Markings

!!! info "Scenery / Accuracy Issues"
    Please be aware that the default scenery or 3rd party sceneries may not be entirely accurate with the posted signage on the ground. However, this guide will explain how to read and understand them.

#### FAA Quick Reference Guide

The FAA has a handy guide available for download that contains images of all the pertinent signs you may encounter, their purpose, and location at the airport.

[Download FAA Guide](https://www.faa.gov/sites/faa.gov/files/airports/runway_safety/publications/QuickReferenceGuideProof8.pdf){ .md-button }

---

There are two types of signage at airports - operational guidance signs and mandatory instruction signs.

#### Operational Guidance Signs

^^Location Signs^^

- These signs are yellow text on a black background. Typically, indicates a specific taxiway or runway your aircraft is on or entering.

^^Direction/Runway Exit Signs^^

- Black text on a yellow background. These will have an arrow indicating the direction to turn, which helps pilots identify what taxiways they are approaching or runway exits towards a specified runway.

    ![signs1](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Ben_Gurion_International_Airport_taxiway_signs.JPG/640px-Ben_Gurion_International_Airport_taxiway_signs.JPG){loading=lazy}

^^Stop Bar Signs^^

- White text on a blue background. These are non-standard signs that may appear at some airports, usually indicating which taxiway a stop bar is positioned. Airports usually use more conventional traffic signs you may see on the road, such a regular stop sign. See the [FAA Guide](#faa-quick-reference-guide) for samples.

    ![signs2](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Ben_Gurion_International_Airport_4_taxiway_signs.JPG/639px-Ben_Gurion_International_Airport_4_taxiway_signs.JPG){loading=lazy}

#### Mandatory Instruction Signs

^^Runway Signs^^

- White text on a red background. These signs inform pilots that a runway intersection is ahead.

^^Holding Position Signs / Markings^^

There are typically three very important holding position signs / markings that appear on the ground at airports. At various airports that operate with low visibility, these positions are also paired with a line of red lights across a taxiway to help visually indicate the holding positions.

1. Runway Holding Position
    - Two sets of solid yellow lines and two sets of dashed yellow lines indicate a holding position for a runway ahead. These **must never be crossed** without express permission from ATC.

        ![holding position](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Holding_position_runway.svg/320px-Holding_position_runway.svg.png){loading=lazy}

        <sub>"Holding position markings pattern A ahead of a crossing runway" by Claudius Henrichs [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0)</sub>
    
2. Taxiway Holding Position
    - Single dashed yellow line. If this is present along your taxi route, it will indicate a position that ground control may request you stop and hold short before another taxiway.

        ![taxiway hold](../assets/beginner-guide/taxi/taxiway-hold.png){ loading=lazy style="width:320px;height:79px" }

3. ILS Critical Area
    - Solid yellow lines that look like a railroad or ladder. These are another form of hold short point but indicate a critical area Where your aircraft would violate the ILS approach airspace while on the ground.

        ![ils critical](../assets/beginner-guide/taxi/ils-critical.png){loading=lazy}

---

### Taxiway Lighting

Taxiway lighting helps the flight crew and ground crew navigate the airport at night or in low visibility and stop at the appropriate locations as given by ATC.

There are usually two types of lighting on taxiways - centerline and edge. Depending on the airport operator, the lightning may differ if the airport operates in low visibility conditions.

- Centerline lighting is green on the principal taxiways located along the taxiway centerline. These lights can alternate between green and yellow when a taxiway crosses a runway, or highlight a "lead-off" taxiway from a runway to join a taxiway.
- Edge lighting is typically blue and characteristically appears at the edges of a taxiway. Spacing can range from 50 - 200 ft apart, usually condensing in distance when approaching an intersection.

![taxiway lights](https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/ATL_TWY_B_-_RWY_Crossing_%2813534655025%29.jpg/640px-ATL_TWY_B_-_RWY_Crossing_%2813534655025%29.jpg){loading=lazy}

<sub>John Murphy, [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0)</sub>

This concludes the *Taxi*.

Continue with [Takeoff, climb and cruise](05_takeoff-climb-cruise)

