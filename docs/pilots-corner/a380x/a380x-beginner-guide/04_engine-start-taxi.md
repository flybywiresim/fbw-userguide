<link rel="stylesheet" href="/stylesheets/bg.css">

# Engine Start and Taxi

This guide will explain the correct procedures to accomplish a pushback with engine start and perform a safe taxi to the departure runway.

!!! warning "Disclaimer"
    The level of detail in this guide is meant to get an Airbus A380 beginner safely from the terminal to the runway hold short point.

    A *beginner* is defined as someone familiar with flying a GA aircraft or different types of airliners. Aviation terminology and know-how is a requirement to fly any airliner, even in Microsoft Flight Simulator.

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
    Any engine can be started first, at the pilots discretion.
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

`TAXI (ETACS) ..................................................AS REQUIRED`<br/>
??? note "TAXI (ETACS)"
    The External and Taxiing Aid Camera System (ETACS) helps the flight crew to navigate the aircraft on the ground by 
    showing outside video feeds on the lower ECAM display. 

    <span style="color:orange">*This is currently not available or possible to implement in the simulator.*</span>
`NAVIGATION DISPLAY RANGE selector .................... ZOOM AS APPROPRIATE`<br/>
??? note "NAVIGATION DISPLAY RANGE - OANS"
    At the pilot’s discretion, zoom as necessary to activate the onbard airport navigation system (OANS). Then, at the 
    pilot’s discretion, select either ARC, ROSE, or PLAN mode.

[//]: # (TODO)
    <p style="color:yellow; font-size:18px;">TODO: link to separate OANS documentation if available</p> 
`NOSE LIGHTS ......................................................... TAXI`<br/>
`RWY TURN OFF & CAMERA ........................................ AS REQUIRED`<br/>
??? note "RWY TURN OFF & CAMERA"
    The RWY TURN OFF lights are used to illuminate the taxiway and runway during taxi. The camera is used to help the 
    flight crew navigate the aircraft on the ground by showing outside video feeds on the lower ECAM display.

    <span style="color:orange">*The camera is currently not available or possible to implement in the simulator.*</span>
`PARKING BRAKE ........................................................ OFF`<br/>
`THRUST LEVERS ............................................. .. AS REQUIRED`<br/>
??? note "THRUST LEVERS"
    The aircraft doesn't need too much power to move. Not more than 10% of the engine thrust is needed at heavy weight 
    in an uphill taxi slope. Excessive thrust can damage airport signalisation. If need of higher thrust, it is 
    recommended to add the thrust on the outer engines to prevent ingestion of foreign object debris. Please note that 
    when the engine anti-ice is on, the ground idle thrust is higher. 
`BRAKES ............................................................. CHECK`<br/>
`NOSEWHEEL STEERING ........................................... AS REQUIRED`<br/>
`ATC CLEARANCE .................................................... CONFIRM`<br/>

??? tip "How and Where"
    <p style="color:yellow; font-size:18px;">TODO: add additional info, images or links to the flight deck</p>

At this point, the aircraft may start rolling. Depending on the weight of the aircraft, we may need to add a little
power to the engines to get going.

It is recommended to verify the brakes by pressing smoothly the brake pedals and release. It is recommended to have a 
taxi speed between 10 and 20 knots in a straight line. If the speed is exceeded, brake until it reaches 10 knots, then 
let the aircraft accelerate again. It is recommended to be between 8 and 10 knots in a sharp turn.

If it is required to perform a sharp turn immediately, we may need a bit more thrust. Try not to perform the brake 
check while in a turn, as we don't want to come to a complete stop while turning.

### Taxi Limitations

It is generally recommended that pilots only taxi on taxiways large enough to support the aircraft. Because of how wide the wingspan of the A380 is, we need large taxiways available to use. Appropriate taxiways are commonly found at large, international airports, such as EGLL, EDDM, KJFK, CYYV, etc.

<p style="color:yellow; font-size:18px;">WIP</p>

??? tip "2 engine taxi"
    There are several scenarios where taxiing can be limited. If, for example, the pilot opts for a 2-engine taxi, the engines must be symmetrical. Symmetrical engines are engines on either wing symmetrical to another engine on the opposite wing. For example, if we were to 2-engine taxi to the runway, we would use either `ENG 2+3` OR `ENG 1+4.` In situations where tight turns are involved, it's recommended to use `ENG 1+4.` <p style="color:yellow; font-size:18px;">TODO: insert image showing engine symmetry</p>

For taxi on outer engines only:

`ENGINE 1 AND 4 ..................................................... START`<br/>
`AFTER START SOP .................................................. PERFORM`<br/>

For taxi on inner engines only:

`ENGINE 2 AND 3 ..................................................... START`<br/>
`AFTER START SOP .................................................. PERFORM`<br/>

In such a case that 2 engine taxi is performed, delay the `AFTER START CL` until all 4 engines are running.

### During Taxi

While underway to the runway, perform the following as part of the taxi flow:

- Use the tiller or rudder pedals to steer the aircraft.
    - See [Nose Wheel and Tiller Operation](../../../aircraft/a32nx/feature-guides/nw-tiller.md)

#### **FMS Data Check**

??? tip "What and Why"
    It is important to verify and confirm the information in the FMS as we taxi. This is increasingly important if the ATC
    clearance changes en route to the runway.

`SELECTED RUNWAY AND INPUT DATA ..................................... CHECK`<br/>
`F-PLN (SID, TRANS) ....................................... REVISE OR CHECK`<br/>
`INITIAL CLIMB SPEED AND SPEED LIMIT ...................... MODIFY OR CHECK`<br/>
`CLEARED ALTITUDE ON FCU .............................................. SET`<br/>
`HDG ON FCU ........................................... IF REQUIRED, PRESET`<br/>
`FLIGHT DIRECTOR ........................................ CHECK SELECTED ON`<br/>
`PFD/ND ............................................................. CHECK`<br/>
`MULTIFUNCTION DISPLAY (MFD) ........................................ CHECK`<br/>

`TAKEOFF BRIEFING ................................................. CONFIRM`<br/>

`AUTOBRAKE RTO ........................................................ ARM`<br/>
`ATC CODE ..................................................... CONFIRM/SET`<br/>
`T.O CONFIG .......................................................... TEST`<br/>
`T.O MEMO .................................................... NO BLUE LINE`<br/>
`CABIN .............................................................. READY`<br/>
??? note "CABIN READY"
    The cabin crew should have completed their checks and are ready for takeoff. The cabin should be secure and all 
    passengers seated with their seatbelts fastened.In real life, the cabin crew would have informed the flight crew
    by sending the CABIN READY signal which would show up on the ECAM. 

    In the A380X we simulate this by pressing the CALL button on the overhead panel. 

??? tip "How and Where"

[//]: # (TODO)
    <p style="color:yellow; font-size:18px;">TODO: add additional info, images or links to the flight deck</p>

`BEFORE TAKEOFF CHECKLIST (down to the line)...................... COMPLETE`<br/>

#### Handy Tips While Taxiing

- **Maintaining Center Line**

    We can use the gray vertical bar in between the PFD and ND as a reference point and keep the taxi line in between the two screens.

- **Turning**

    Using the same bar mentioned above, try to "over steer" (keep the nose wheel slightly ahead of the line while we 
    turn). This helps keep the aircraft centered while performing a turn.

    Slow down while turning!

#### Crossing a Runway

When approved to cross a runway (active or not) perform the following actions:

`LANDING LIGHTS ........................................................ ON`<br/>
`STROBE LIGHTS ......................................................... ON`<br/>    

- Look out the windows and visually ensure that there are no visible aircraft to the left and right.
- Inform ATC we have vacated the runway if required.

!!! warning
    Never cross a runway without express permission from ATC and providing a read back of said instructions. 
    Always ensure maximum safety when crossing.

---

This concludes the *Taxi*.

Continue with [Takeoff, climb and cruise](05_takeoff-climb-cruise)

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

