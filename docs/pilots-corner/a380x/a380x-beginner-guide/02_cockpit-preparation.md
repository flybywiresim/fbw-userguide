<link rel="stylesheet" href="/stylesheets/bg.css">

# Cockpit Preparation

This guide will help you with preparing and powering up the Airbus A380.  
It includes images to help you understand the locations of all buttons and switches.

!!! warning "Disclaimer"
    The level of detail in this guide is meant to teach an Airbus A380 beginner to start the aircraft correctly.

    A *beginner* is defined as someone familiar with flying a GA aircraft or different types of airliners. Aviation 
    terminology and know-how is a requirement to fly any airliner, even in Microsoft Flight Simulator.

    This guide simplifies the process of starting the aircraft to accomodate beginners and the fact that this is a 
    simulation. More advanced sim pilots can use the [A380X SOP](../a380x-sop.md) directly. 

    When this guide refers to ATC it is referring to any Online ATC network but **NOT** the built-in ATC in the 
    simulator as this is very unrealistic and unreliable.

    
---

## Prerequisites

This guide assumes that your aircraft is in a cold and dark state at a gate.

[Download FlyByWire Checklist](../assets/sop/FBW_A380X_Checklist.pdf){ .md-button target=new }

## Pre-checks

??? tip "What and Why"
    Before starting the aircraft, we need to ensure that all switches are in the correct position.
    This is to prevent any damage to the aircraft systems and to ensure that the aircraft is ready for flight.

    (Of course, this is not an issue in the sim, but in real life it is crucial to check this!)

`ENGINE MASTER SWITCHES (1, 2, 3, 4) .................................. OFF`<br/>
`PARKING BRAKE (OR CHOCKS).............................................. ON`<br/>
`SPEED BRAKE LEVER .............................................. RETRACTED`<br/>
`FLAPS LEVER .................................................... RETRACTED`<br/>
`WEATHER RADAR ........................................................ OFF`<br/>
`ENGINE MODE SELECTOR ................................................ NORM`<br/>
`THRUST LEVERS ....................................................... IDLE`<br/>
`GEAR LEVER .......................................................... DOWN`<br/>
`WIPERS (BOTH) ........................................................ OFF`<br/>

??? tip "How and Where"
    Use the Flight Deck Overview to locate the items mentioned above. The Flight Deck Overview is a
    clickable cockpit that will show you where each item is located.

[//]: # (TODO)

    <p style="color:yellow; font-size:18px;">TODO: images or link to flight-deck</p> 

After these pre-checks, we can start the aircraft starting with the initial power up.

---

## Initial Power Up

??? tip "What and Why?"
    The initial power up is the first step in starting the aircraft. This is where we turn on the batteries and external
    power to provide power to the aircraft systems.

    The batteries are the first source of power for the aircraft. The external power is used to provide power to the
    aircraft systems when the engines are not running. The aircraft needs at least two external power units to power the 
    whole electrical network.

`ENGINES MASTER SWITCHES (1, 2, 3, 4) ................................. OFF`<br/>
`BATTERIES (BAT 1, BAT 2) .............................................. ON`<br/>
`EXTERNAL POWER (2, 3, 1, 4) ........................................... ON`<br/>
`COCKPIT LIGHTING ............................................. AS REQUIRED`<br/>

??? tip "How and Where?"

[//]: # (TODO)
    <p style="color:yellow; font-size:18px;">TODO: images or link to flight-deck</p>     

## Fire Tests and APU Startup

??? tip "What and Why?"
    The fire tests are done to ensure that the fire detection system is working correctly.

    The APU startup is done to provide power and bleed air to the aircraft systems when the engines are not running.

    Turning on and setting up the radios at this point is also important in case of any emergencies.

`RMP 1 and 2 ........................................................... ON`<br/>
`STANDBY RADIO NAVIGATION ............................................. OFF`<br/>
`COMMUNICATION FREQUENCIES ........................................... TUNE`<br/>
`INTERPHONE RECEPTION ...................................... RELEASE/ADJUST`<br/>
`APU FIRE ............................................ CHECK IN and GUARDED`<br/>
`APU AGENT ............................................................ OFF`<br/>
`ENGINE 1/2/3/4 FIRE.................................. CHECK IN and GUARDED`<br/>
`ENGINE 1/2/3/4 AGENT 1 and 2 ......................................... OFF`<br/>
`FIRE TEST .......................................................... PRESS`<br/>
??? note "Fire Test Result"
    Verify that the fire detection systems and extinguishing systems are functional by checking the following items:

    A constant repetitive chime sound, the master warning light flashes on the glareshield, the ECAM displays the engine 
    fire alert messages (ENG 1(2)(3)(4) FIRE, APU FIRE, MLG BAY FIRE), All engine fire pushbutton and the auxiliary power 
    unit fire pushbutton displays in red, the squib light of the engine and apu agent pushbuttons are illuminated, the disch 
    light of the engine and auxiliary power unit agent pushbuttom illuminates and all fire lights on the engine master panel 
    illuminates.

`APU MASTER SWITCH ..................................................... ON`<br/>
`APU START ............................................................. ON`<br/>
`EXTERNAL POWER .................................................... AS REQ`<br/>
??? note "External Power"
    It is recommended to keep the external power units to ON to reduce the APU load in hot weather conditions.

??? tip "How and Where?"

[//]: # (TODO)
    <p style="color:yellow; font-size:18px;">TODO: images or link to flight-deck</p>

## Cockpit Preparation Flow

<p style="color:yellow; font-size:18px;">TODO: Improve description and check with pilots</p>

The cockpit preparation flow is an easy way to remember the steps to startup and setup the aircraft correctly.
It follows a flow starting on the overhead panel on the left buttom moving up and then to the right.
Then it continues the flow on the main panel starting and moving to the pedestal, setting up the FMS to then continue
to the glareshield. At last the lateral consoles are checked and set up.

<p style="color:yellow; font-size:18px;">TODO: insert image showing the setup flow.</p>

## Overhead Panel

??? tip "What and Why?"
    We scan the overhead panel from left to right and bottom to top to ensure that all switches are in the correct position.

### Overhead Panel Left (bottom to top)

`ALL WHITE LIGHTS ..................................................... OFF`<br/>
`RECORDER GROUND CTL ................................................... ON`<br/>
`EVAC CAPT/CAPT & PURS ............................................... CAPT`<br/>
`PROBE & WINDOW HEAT ................................................. AUTO`<br/>
`ADIRS ALL IR MODE .................................................... NAV`<br/>
??? note "ADIRS Alignment"
    It is recommended to align the inertial references as soon as possible. The initialization may take some time.
    It is also recommended to complete a full alignment if this is the first flight of the day, the flight crew has
    changed, the GPS is not available to all segment in the flights, or that the pilot expects long segments with low
    NAVAID coverage. It is recommended to perform a fast alignment for all other flight conditions.
`EMERGENCY LOCATOR TRANSMITTER (ELT) ................................ ARMED`<br/>

??? tip "How and Where?"
    Use the Flight Deck Overview to locate the items mentioned above. The Flight Deck Overview is a
    clickable cockpit that will show you where each item is located.

    All White Lights
    <p style="color:yellow; font-size:18px;">TODO: insert image of all white lights or link to interactive flight deck</p>
    
    Recorder Ground Control
    <p style="color:yellow; font-size:18px;">TODO: insert image of recorder ground control or link to interactive flight deck</p>
    
    Evac Capt/Capt & Purs
    <p style="color:yellow; font-size:18px;">TODO: insert image of evac capt/capt & purs or link to interactive flight deck</p>
    
    Probe & Window Heat
    <p style="color:yellow; font-size:18px;">TODO: insert image of probe & window heat or link to interactive flight deck</p>
    
    ADIRS All IR Mode
    <p style="color:yellow; font-size:18px;">TODO: insert image of ADIRS all IR mode or link to interactive flight deck</p>
    
    Emergency Locator Transmitter
    <p style="color:yellow; font-size:18px;">TODO: insert image of emergency locator transmitter or link to interactive flight deck</p>

### Overhead Panel Center (bottom to top)

`STROBE .............................................................. AUTO`<br/>
`BEACON ............................................................... OFF`<br/>
`NAV ....... ........................................................... ON`<br/>
`REMAINING EXTERIOR LIGHTS .....................................AS REQUIRED`<br/>
`SEAT BELTS ............................................................ ON`<br/>
`NO SMOKING .......................................................... AUTO`<br/>
`EMERGENCY EXIT LIGHTS ................................................ ARM`<br/>
`ENGINE STARTER ...................................................... NORM`<br/>
`APU BLEED ............................................................. ON`<br/>
??? note "APU BLEED"
    It is not recommended to use the auxiliary power unit bleed system if a high-pressure ground air unit is connected to
    the aircraft. This can be checked on the bleed page of the system display. If there is pressure in the bleed air
    system, the high-pressure ground air unit is connected.
`XBLEED .............................................................. AUTO`<br/>
`AIR FLOW ............................................................ NORM`<br/>
??? note "AIR FLOW"
    The bleed system works with the flight management system. If there is no number of passengers entered into the
    flight-management-system, the airflow will be automatically set the air flow like when the value entered is the maximum
    number of passengers. If the number of passengers is entered, the airflow will automatically adjust to that number.
`CKPT ......................................................... AS REQUIRED`<br/>
`CABIN ........................................................... PURS SEL`<br/>
`TRIM TK FEED ........................................................ AUTO`<br/>
`MAINTENANCE PANEL ALL LIGHTS.......................................... OFF`<br/>

??? tip "How and Where?"
    Use the Flight Deck Overview to locate the items mentioned above. The Flight Deck Overview is a
    clickable cockpit that will show you where each item is located.

    Strobe
    <p style="color:yellow; font-size:18px;">TODO: insert image of strobe or link to interactive flight deck</p>
    
    Beacon
    <p style="color:yellow; font-size:18px;">TODO: insert image of beacon or link to interactive flight deck</p>
    
    Nav
    <p style="color:yellow; font-size:18px;">TODO: insert image of nav or link to interactive flight deck</p>
    
    Remaining Exterior Lights
    <p style="color:yellow; font-size:18px;">TODO: insert image of remaining exterior lights or link to interactive flight deck</p>
    
    Seat Belts
    <p style="color:yellow; font-size:18px;">TODO: insert image of seat belts or link to interactive flight deck</p>
    
    No Smoking
    <p style="color:yellow; font-size:18px;">TODO: insert image of no smoking or link to interactive flight deck</p>
    
    Emergency Exit Lights
    <p style="color:yellow; font-size:18px;">TODO: insert image of emergency exit lights or link to interactive flight deck</p>
    
    Engine Starter
    <p style="color:yellow; font-size:18px;">TODO: insert image of engine starter or link to interactive flight deck</p>
    
    APU Bleed
    <p style="color:yellow; font-size:18px;">TODO: insert image of APU Bleed or link to interactive flight deck</p>
    
    Xbleed
    <p style="color:yellow; font-size:18px;">TODO: insert image of xbleed or link to interactive flight deck</p>
    
    Air Flow
    <p style="color:yellow; font-size:18px;">TODO: insert image of air flow or link to interactive flight deck</p>
    
    CKPT
    <p style="color:yellow; font-size:18px;">TODO: insert image of ckpt or link to interactive flight deck</p>
    
    Cabin
    <p style="color:yellow; font-size:18px;">TODO: insert image of cabin or link

    Trim TK Feed
    <p style="color:yellow; font-size:18px;">TODO: insert image of trim tk feed or link to interactive flight deck</p>

    Maintenance Panel All Lights
    <p style="color:yellow; font-size:18px;">TODO: insert image of maintenance panel all lights or link to interactive flight deck</p>

### Overhead Panel Right (bottom to top)

`CARGO AIR COND ............................................... AS REQUIRED`<br/>
`RADIO MANAGEMENT PANEL 3 .............................................. ON`<br/>
`STBY RAD NAV ......................................................... OFF`<br/>
`CVR TEST ........................................................... PRESS`<br/>

??? tip "How and Where?"
    Use the Flight Deck Overview to locate the items mentioned above. The Flight Deck Overview is a
    clickable cockpit that will show you where each item is located.

    Cargo Air Cond
    <p style="color:yellow; font-size:18px;">TODO: insert image of cargo air cond or link to interactive flight deck</p>
    
    Radio Management Panel 3
    <p style="color:yellow; font-size:18px;">TODO: insert image of radio management panel 3 or link to interactive flight deck</p>
    
    Standby Radio Navigation
    <p style="color:yellow; font-size:18px;">TODO: insert image of standby radio navigation or link to interactive flight deck</p>
    
    CVR Test
    <p style="color:yellow; font-size:18px;">TODO: insert image of CVR Test or link to interactive flight deck</p>

### Main Instrument Panel

`SWITCHING PANEL ..................................................... NORM`<br/>
`INTEGRATED STANDBY INSTRUMENT SYSTEM ............................... CHECK`<br/>
`LANDING GEAR GRAVITY SYSTEM .......................................... OFF`<br/>
`CLOCK ...........................................CHECK and SET AS REQUIRED`<br/>
`ANTI AKID (A-SKID) ................................................... ON`<br/>

??? tip "How and Where?"
    Use the Flight Deck Overview to locate the items mentioned above. The Flight Deck Overview is a
    clickable cockpit that will show you where each item is located.

    Switching Panel
    <p style="color:yellow; font-size:18px;">TODO: insert image of switching panel or link to interactive flight deck</p>
    
    Integrated Standby Instrument System
    <p style="color:yellow; font-size:18px;">TODO: insert image of integrated standby instrument system or link to interactive flight deck</p>
    
    Landing Gear Gravity System
    <p style="color:yellow; font-size:18px;">TODO: insert image of landing gear gravity system or link to interactive flight deck</p>
    
    Clock
    <p style="color:yellow; font-size:18px;">TODO: insert image of clock or link to interactive flight deck</p>
    
    Anti Akid (A-Skid)
    <p style="color:yellow; font-size:18px;">TODO: insert image of anti akid (a-skid) or link to interactive flight deck</p>

### Pedestal

`PARKING BRAKE ........................................................ ON`<br/>
`BODY ACCUMULATOR PRESSURE ............................... CHECK/REINFLATE`<br/>
`THRUST LEVERS ...................................................... IDLE`<br/>
`THRUST REVERSE LEVERS ............................................ STOWED`<br/>
`ENGINE MASTER SWITCHES (1, 2, 3, 4) ................................. OFF`<br/>
`COCKPIT DOOR SWITCH ................................................ NORM`<br/>
`ATC CLEARANCE .....................................................OBTAIN`<br/>
??? note "ATC Clearance"
    <p style="color:yellow; font-size:24px;">TODO: Improve.</p>
    It is recommended to obtain the ATC clearance before starting the engines.
`NAVIGATION CHARTS ............................................... PREPARE`<br/>
`MFD SURVEILLANCE DEFAULT SETTINGS................................. SELECT`<br/>
??? note "MFD Default Settings"
    Verify on the multi function display surveillance control page that the transponder is set to AUTO, the squawk code
    is the same, the TCAS is set to TA/RA and Norm, all TAWS modes are ON, and the weather radar is set to AUTO, the
    elevation/tilt to AUTO, Mode set to WX, TURB set to AUTO, GAIN set to AUTO, WX ON VD set to ON and PRED W/S to AUTO)

??? tip "How and Where?"
    Use the Flight Deck Overview to locate the items mentioned above. The Flight Deck Overview is a
    clickable cockpit that will show you where each item is located.

    Parking Brake
    <p style="color:yellow; font-size:18px;">TODO: insert image of parking brake or link to interactive flight deck</p>
    
    Body Accumulator Pressure
    <p style="color:yellow; font-size:18px;">TODO: insert image of body accumulator pressure or link to interactive flight deck</p>
    
    Thrust Levers
    <p style="color:yellow; font-size:18px;">TODO: insert image of thrust levers or link to interactive flight deck</p>
    
    Thrust Reverse Levers
    <p style="color:yellow; font-size:18px;">TODO: insert image of thrust reverse levers or link to interactive flight deck</p>
    
    Engine Master Switches
    <p style="color:yellow; font-size:18px;">TODO: insert image of engine master switches or link to interactive flight deck</p>
    
    Cockpit Door Switch
    <p style="color:yellow; font-size:18px;">TODO: insert image of cockpit door switch or link to interactive flight deck</p>
    
    ATC Clearance
    <p style="color:yellow; font-size:18px;">TODO: insert image of ATC clearance or link to interactive flight deck</p>
    
    Navigation Charts
    <p style="color:yellow; font-size:18px;">TODO: insert image of navigation charts or link to interactive flight deck</p>
    
    MFD Surveillance Default Settings
    <p style="color:yellow; font-size:18px;">TODO: insert image of MFD surveillance default settings or link to interactive flight deck</p>

At this point, the Flight Management System (FMS) should be initialized.
See [Preparing the MFD](03_preparing-fms) for more information.

### Glareshield

`INTEGRAL LIGHTS ............................................. AS REQUIRED`<br/>
`BAROMETRIC REFERENCE ................................................ SET`<br/>
`NAVIGATION DISPLAY (ND) MODE AND RANGE ........................... AS REQ`<br/>
`WEATHER RADAR ............................................... AS REQUIRED`<br/>
`OTHER EFIS OPTIONS .......................................... AS REQUIRED`<br/>
`FLIGHT DIRECTOR ...................................................... ON`<br/>
`NORTH REF ........................................................... MAG`<br/>
??? note "North Reference"
    It is recommended to ensure that the “TRUE” message does not appear on the primary flight display or on the HDG/TRK
    display.
`SPD/MACH, HDG / TRK, V/S / FPA display ........................... DASHED`<br/>
`ALTITUDE display .................... INITIAL EXPECTED CLEARANCE ALTITUDE`<br/>
`AUTO FLIGHT SYSTEM CONTROL PANEL ............................. CROSSCHECK`<br/>

??? tip "How and Where?"
    Use the Flight Deck Overview to locate the items mentioned above. The Flight Deck Overview is a
    clickable cockpit that will show you where each item is located.

    Integral Lights
    <p style="color:yellow; font-size:18px;">TODO: insert image of integral lights or link to interactive flight deck</p>
    
    Barometric Reference
    <p style="color:yellow; font-size:18px;">TODO: insert image of barometric reference or link to interactive flight deck</p>
    
    Navigation Display (ND) Mode and Range
    <p style="color:yellow; font-size:18px;">TODO: insert image of navigation display (ND) mode and range or link to interactive flight deck</p>
    
    Weather Radar
    <p style="color:yellow; font-size:18px;">TODO: insert image of weather radar or link to interactive flight deck</p>
    
    Other EFIS Options
    <p style="color:yellow; font-size:18px;">TODO: insert image of other EFIS options or link to interactive flight deck</p>
    
    Flight Director
    <p style="color:yellow; font-size:18px;">TODO: insert image of flight director or link to interactive flight deck</p>
    
    North Reference
    <p style="color:yellow; font-size:18px;">TODO: insert image of north reference or link to interactive flight deck</p>
    
    SPD/MACH, HDG / TRK, V/S / FPA display
    <p style="color:yellow; font-size:18px;">TODO: insert image of SPD/MACH, HDG / TRK, V/S / FPA display or link to interactive flight deck</p>
    
    Altitude Display
    <p style="color:yellow; font-size:18px;">TODO: insert image of altitude display or link to interactive flight deck</p>
    
    Auto Flight System Control Panel
    <p style="color:yellow; font-size:18px;">TODO: insert image of auto flight system control panel or link to interactive flight deck</p>

### Lateral Consoles

`OXYGEN MASKS TEST ............................................... PERFORM`<br/>
`DOOR SD PAGE REGUL PR LO indication ................. CHECK NOT DISPLAYED`<br/>
`SLIDING WINDOWS LOCKED .................................... CLOSED/LOCKED`<br/>

??? tip "How and Where?"
    Use the Flight Deck Overview to locate the items mentioned above. The Flight Deck Overview is a
    clickable cockpit that will show you where each item is located.

    Oxygen Masks Test
    <p style="color:yellow; font-size:18px;">TODO: insert image of oxygen masks test or link to interactive flight deck</p>
    
    Door SD Page Regul PR LO Indication
    <p style="color:yellow; font-size:18px;">TODO: insert image of door SD page regul PR LO indication or link to interactive flight deck</p>
    
    Sliding Windows Locked
    <p style="color:yellow; font-size:18px;">TODO: insert image of sliding windows locked or link to interactive flight deck</p>

### Pilot Briefing

As the last step the pilots would conduct the takeoff briefing:

`TAKE OFF BRIEFING ............................................... PERFORM`<br/>

??? tip "How and Where?"
    Take Off Briefing
    <p style="color:yellow; font-size:18px;">TODO: describe briefing</p>

---

This concludes the *Starting the Aircraft* guide.

Continue with [Preparing the FMS](03_preparing-fms).













