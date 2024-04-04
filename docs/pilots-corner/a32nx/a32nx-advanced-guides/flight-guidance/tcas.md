# Traffic Alert and Collision Avoidance System

{==

For a list of compatible networks and known issues - [see here](#compatibilities-and-known-issues).

==}

## Overview

The Traffic Collision Avoidance System (TCAS) is a system available on aircraft that helps to reduce the risk of airborne collisions. In general, commercial airliners operating an IFR flight require TCAS as mandated by various regulatory bodies such as FAA, ICAO, or EASA. 

Numerous improvements have been made to this system over the years that enhance the pilot interface and decrease non-optimal pilot handling of advisories from TCAS. The FlyByWire A32NX uses the AP/FD TCAS mode function developed by Airbus.

There are two types of advisories pilots will encounter when TCAS detects an intruder in the flight path of the aircraft.

- [Traffic Advisory (TA)](#traffic-advisory): Potential threats to monitor
- [Resolution Advisory (RA)](#resolution-advisory): Collision threats that require intervention

The TCAS panel can be found on the lower pedestal to the right of the throttle quadrant.

![ATC-TCAS Panel](../../assets/a32nx-briefing/pedestal/ATC-TCAS.jpg "ATC-TCAS Panel")

Make sure that the ATC system is on `AUTO` or `ON` and the `ALT RPTG` knob is in position `ON`. The TCAS mode switch should be in position `TA/RA` when entering the runway for takeoff.

For more information on how to ensure TCAS is active for your flight and the corresponding controls, please see the [ATC TCAS PANEL](../../a32nx-briefing/flight-deck/pedestal/atc-tcas.md) page.

## Traffic Advisory

This advisory is generated when TCAS detects an intruder along the current flight path it would consider a potential threat. Flight crews will receive multiple cues from TCAS that identify a TA. No specific action is mandatory during a TA, but the flight crew should remain vigilant of intruders and anticipate a potential RA.

- "*Traffic, Traffic*" aural warning
- Visual amber cues on the navigation display (ND) providing information about the potential threat.
    - See [ND Symbology](#nd-symbology)

Once a TA is triggered, the AP/FD TCAS will arm itself to notify the crew with the traffic displayed on the ND. The TA will remain active for as long as the threat remains, resulting in one of two things:

- Once the predicted flight paths of the aircraft or the aircraft themselves are no longer in proximity, TCAS will issue a "Clear of Conflict".
- If the threat increases because the aircraft are predicted to approach too close to each other, TCAS will upgrade the Traffic Advisory to a Resolution Advisory.

### TA Pilot Actions

As soon as the "*Traffic, Traffic*" aural warning is heard, pilots should begin analyzing the potential threat. **Corrective maneuvers should not be performed in response to a TA.**

- Confirm the TCAS panel is correctly configured
- Confirm that TCAS is armed in <span style=color:cyan>cyan</span> on the PFD's FMA (AP/FD TCAS feature)
    - If TCAS is not armed, the flight crew should be mentally prepared to disconnect the autopilot and manually follow TCAS commands
- Ensure A/THR is set to `ON`
- Pilot monitoring (PM):
    - Check the ND for the potential threat
        - It may be necessary to set the zoom level to 40 NM or below
    - Contact ATC about any nearby aircraft
    - Keep pilot flying (PF) informed about the status of the threat
    - Confirm the PF takes the correct actions if the TA upgrades to an RA
    - Consider turning on additional exterior lighting for increased visibility
    
## Resolution Advisory

When a traffic advisory becomes a collision threat, an RA is generated. RA actions require the flight crew to promptly follow any commanded actions by TCAS and notify ATC. According to the Airbus Flight Crew Techniques Manual (FCTM) the flight crew **must follow TCAS RA commands** even in the following situations:

- TCAS RA issues commands that conflict with ATC instructions
- Aural warnings such as "Climb, Climb" or "Increase Climb" exceed max ceiling altitude
- Results in crossing altitude of intruder

AP/FD TCAS shines in this regard, allowing for fully automated flight in the case of an RA. Pilots will now have additional information provided to them on the primary flight display (PFD) and navigation display (ND) depending on what actions the flight crew needs to perform to clear the conflict.

- Aural commands instructing the pilot of what type of vertical maneuver to perform
    - See [Aural Messages](#aural-messages) for a list
- Visual red cues on the ND, providing information about the potential threat
    - See [ND Symbology](#nd-symbology)
- Visual green and red zones on the vertical speed indicators on the PFD
    - See [Flight Instrument Indicators](#flight-instrument-indicators)

There are generally two types of behaviors associated with an RA - preventative and corrective.

### Preventative

This behavior starts with the vertical speed in the <span style=color:green>green zone</span> of the VSI. It requires the flight crew or commands the autopilot to maintain the current vertical speed and is coupled with an audible alert such as "Monitor V/S". This would help increase the safety margin before any further measures would need to be taken and allow for safe capture of a selected flight level clear of any conflicts.

The following conditions will apply:

- TCAS will maintain a safe V/S target
- Longitudinal modes previously armed will automatically be disarmed except ALT^*^
- In the situation that conditions for altitude capture are met, a preventative RA will allow for safe capture of the targeted altitude
    - This prevents the aircraft from exceeding a commanded altitude in the FCU
- The audible alert "Adjust V/S" will play and TCAS will avoid conflicts by maintaining a safe vertical speed when attempting to level-off at a targeted altitude
- To ensure a safe speed during any maneuvers, A/THR will engage SPEED/MACH

### Corrective

This behavior starts with the vertical speed in the <span style=color:red>red zone</span> of the VSI. As the behavior denotes, this RA will require active corrective measure either automatically via the autopilot or manually from the flight crew to fly out of the red zone towards the edge of the green / red zone on the VSI. It is usually coupled with audible alerts such as "Climb, Descend".

The following conditions will apply:

- TCAS will engage and modify vertical guidance to avoid conflict targeting the <span style=color:green>green zone</span>.
- Targets a V/S of 200 ft/min inside the green band on the VSI
- Longitudinal modes previously armed will automatically be disarmed except ALT^*^
    - This prevents the aircraft from exceeding a commanded altitude / prevents excursions
    - In this type of RA, a V/S of 0 ft/min is always within the safe zone to prevent commanded altitude excursions, allowing for TCAS to reach a targeted flight level if capture conditions are met. Sample scenario:
    ![tcas level off](../../assets/advanced-guides/flight/tcas-level-ra.png)
- To ensure a safe speed during any maneuvers, A/THR will engage SPEED/MACH

### RA Pilot Actions

As soon as the threat upgrades to an RA, TCAS will engage and provide corrective action based on the types discussed above. While there are many benefits to having AP/FD TCAS installed and having the autopilot perform any corrective maneuvers, the flight crew should still monitor all actions taken by the system and prepare to take manual control at any time.

**AP/FD TCAS Actions**

- Ensure TCAS is now the active mode on the FMA
- Ensure the AP is targeting the <span style=color:green>green zone</span> on the VSI
- Notify ATC

**Manual TCAS Actions**

- Set AP to `OFF`
- Ensure both FDs set to `OFF`
- Fly the aircraft into the <span style=color:green>green zone</span> on the VSI smoothly and promptly
    - TCAS aural commands will also play at this time

!!! info "Additional Considerations with AP/FD TCAS"
    Please be aware that there are certain scenarios that happen during a TCAS RA that affects how flight crews should react depending on the conditions of the flight deck.

    ---

    **AP + FD Engaged**

    Any vertical mode will revert to `TCAS` in the FMA, and the autopilot will fly the TCAS maneuver.

    ---

    **AP Disengaged / FD Engaged**

    TCAS mode will be engaged and supersede the flight directory guidance. Flight crews should ensure they are centered on the pitch bar and bring the vertical speed of the aircraft into the green zone indicated on the vertical speed indicator on the PFD.

    ---

    **AP + FD Disengaged**
    
    The FD bars will appear automatically. TCAS mode will be engaged and provide guidance and flight crews should perform actions as stated in above.

## Clear of Conflict

TCAS will notify the flight crew via the aural warning "Clear of Conflict" when separation and range from a threat is adequate. At this time, the flight crew should perform the following actions:

If maneuver performed using AP/FD TCAS:

- Monitor AP/FD TCAS returns aircraft to previously assigned ATC clearance
- Notify ATC - clear of conflict

If manual actions were taken during the TCAS RA:

- Engage Flight Directors
- Set new commands on the FCU
- Engage the Autopilot
- Notify ATC - clear of conflict

---

## AP/FD TCAS

!!! warning "Manual Flight Assumptions"
    The operating flight crew should always be able to take command of the aircraft manually by disconnecting the autopilot and flight directors to respond to a TCAS RA by flying the aircraft at a vertical speed outside the red zone in the vertical speed indicator.

AP/FD TCAS includes vertical guidance as part of the Auto Flight System (AFS) to support pilots during a TCAS RA. It provides control of the vertical speed via the AFS, which is specifically tailored to each target that generated an RA. 

Essentially, this feature allows the flight crew to resolve TCAS RAs using the autopilot. It is also entirely possible to complete a TCAS RA maneuver manually by using the flight director guidance with the autopilot switched off as well. The major benefit of this system is to provide optimal maneuvers when a conflict arises.

---

## Flight Instrument Indicators

### PFD during TCAS RA

!!! block ""
    ![pfd-tcas](../../assets/advanced-guides/flight/pfd-tcas.png){width=50% align=left}

    This image showcases an aircraft experiencing a TCAS RA during cruise to "descend". 

    There are two critical elements to pay attention to in this image:

    - The Flight Mode Annunciators (FMA) in the highlighted box
    - The Vertical speed indicator (VSI) to the right of the PFD.

As a conflict occurs and the AP/FD TCAS system kicks in, typically you will see:

- TCAS in the FMA:
    - TCAS will be armed in <span style=color:cyan>cyan</span> below the current vertical guidance mode. (Not Pictured).
    - A mode revision and TCAS will engage with a box around it. (Pictured).
    - TCAS in <span style=color:green>green</span> after 10s.
- The aircraft will also target a safe vertical speed in the VSI as seen below.

!!! block ""
    ![pfd vsi](../../assets/advanced-guides/flight/pfd-vsi.png){align=left}

    This is an example of the PFD's vertical speed indicator during a TCAS RA. It showcases a corrective measure to "descend" the aircraft to prevent a collision. These zones can also indicate a positive vertical speed change in the case of a corrective measure to "climb".

    There are two notable indications in this example. 

    - <span style=color:green>Green Zone</span> which indicates the proper and safe vertical speed during the TCAS maneuver.
    - <span style=color:red>Red Zone</span> which indicates a forbidden vertical speed during the TCAS maneuver.

### ND Symbology

The following chart explains the various symbols displayed on the navigation display (ND) when TCAS detects potential threats (increasing in severity):

|                                            Symbol on ND                                             |     Type of Traffic      | Information                                                                 |
|:---------------------------------------------------------------------------------------------------:|:------------------------:|:----------------------------------------------------------------------------|
|       ![tcas other traffic](../../assets/advanced-guides/flight/other-traffic.png){width=75%}       |      Other Traffic       | Not a threat.<br>Visible within the surveillance field.                     |
|       ![tcas proximate traffic](../../assets/advanced-guides/flight/proximate.png){width=75%}       |    Proximate Traffic     | Not a threat.<br>Identified as a possible intruder within 6 NM and 1200 ft. |
|    ![tcas traffic advisory](../../assets/advanced-guides/flight/traffic-advisory.png){width=75%}    |  Traffic Advisory (TA)   | Possible threat.                                                            |
| ![tcas resolution advisory](../../assets/advanced-guides/flight/resolution-advisory.png){width=75%} | Resolution Advisory (RA) | Collision threat.                                                           |

This next chart includes additional symbology when traffic is seen on the ND.

|                                          Symbol                                           | Information                                                                                                                                      |
|:-----------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------|
|  ![tcas other traffic](../../assets/advanced-guides/flight/tcas-arrow-up.png){width=75%}  | This arrow represents climbing traffic.                                                                                                          |
| ![tcas other traffic](../../assets/advanced-guides/flight/tcas-arrow-down.png){width=75%} | This arrow represents descending traffic.                                                                                                        |
|  ![tcas other traffic](../../assets/advanced-guides/flight/tcas-traffic.png){width=75%}   | Complete picture of traffic on the ND.<br>This example showcases Proximate Traffic that is 1000 ft above the aircraft and is currently climbing. |

## Aural Messages

The following table includes a list of auditory messages when a TA/RA is detected.

|               Aural Messages               | Description                                                                                              |
|:------------------------------------------:|----------------------------------------------------------------------------------------------------------|
|              Traffic Traffic               | Traffic Alert Detected.                                                                                  |
|                Climb Climb                 | Perform climb indicated in the green zone on the VSI.                                                    |
|      Climb, Crossing Climb<br>(twice)      | *See above*. Additionally, indicates you are crossing the altitude of the intruder.                      |
|         Increase Climb<br>(twice)          | Warning is played after CLIMB warning when vertical speed is still insufficient.                         |
|              Descend Descend               | Perform descent indicated in the green zone on the VSI.                                                  |
|    Descend, Crossing Descend<br>(twice)    | *See above*. Additionally indicates you are crossing the altitude of the intruder.                       |
|        Increase Descend<br>(twice)         | Warning is played after DESCEND warning when vertical speed is still insufficient.                       |
|            Level off, Level off            | Set vertical speed to 0.                                                                                 |
|         Climb Climb Now<br>(twice)         | Warning is played after DESCEND warning when the trajectory of the intruder has changed.                 |
|       Descend Descend Now<br>(twice)       | Warning is played after the CLIMB warning when the trajectory of the intruder has changed.               |
|           Monitor Vertical Speed           | Warning is played in the case of preventative RA. Ensure aircraft is not within the red zone on the VSI. |
|     Maintain Vertical Speed, Maintain      | Maintain vertical speed in the green zone of the VSI.                                                    |
| Maintain Vertical Speed, Crossing Maintain | *See above*. Additionally, indicates you are crossing the altitude of the intruder.                      |
|             Clear of Conflict              | Return to assigned ATC clearance. Separation is adequate and the threat has passed.                      |

---

## External Resources

Airbus' Safety First publication has great resources further explaining their systems in-depth with supporting graphics and statistics. We've provided a link below to a great article detailing TCAS Alert Prevention (TCAP) and the AP/FD TCAS function.

[Safe Handing of TCAS Alerts](https://safetyfirst.airbus.com/safe-handling-of-tcas-alerts/){.md-button primary target=new}

---

## Compatibilities and Known Issues

### Compatible Networks

Our implementation of TCAS supports the following networks:

- VATSIM
- IVAO
- Live Traffic in MSFS
- FSLTL Traffic Injection

### Known Issues

[//]: # (- Broken support for FSLTL Traffic &#40;sim issue&#41;)

[//]: # (    - FSLTL traffic is not visible to TCAS but auditory warnings are still played)

[//]: # (    !!! info "Root Cause for FSLTL + TCAS Issues")

[//]: # (        Unfortunately this is an issue with how injected traffic uses certain APIs from MSFS. Asobo seems to be aware of the issue and you can track it on the dev support )

[//]: # (        forum link below:)

[//]: # ()
[//]: # (        [AI aircraft generated airborne do not get returned with the GET_AIR_TRAFFIC Coherent call]&#40;https://devsupport.flightsimulator.)

[//]: # (        com/questions/12949/ai-aircraft-generated-airborne-do-not-get-returned.html&#41;)
  
- No support for offline AI traffic (sim limitation)
- No support of multiplayer (MSFS) traffic (sim limitation)
- Possible false detection of ground traffic
- Possible ghost TA / RA due to jumping traffic (*improvements and changes expected*)

!!! tip "A Quick Note on TCAS Performance"
    TCAS relative altitude is now based on plane altitude (true altitude) for both airplanes. This should work exactly as intended for MSFS airplanes relative to one another (though not as the IRL TCAS works). It can still be somewhat of an issue when on a network with non-MSFS airplanes.

    This is because MSFS is the only sim that should correctly compute the true altitude. Depending on the atmospheric conditions, an MSFS airplane flying in the same weather and with the same baro setting as a non-MSFS airplane may be at a different true altitude than the non-MSFS airplane. Said differently, each aircraft could be at the same altitude in their respective simulator, but TCAS would show them at different altitudes.

    {==

    This is not just a TCAS issue. It is an issue that VATSIM and all the other networks are struggling with so that ATC sees all airplanes, regardless of sim, at the right altitudes, at least relative to one another.

    ==}