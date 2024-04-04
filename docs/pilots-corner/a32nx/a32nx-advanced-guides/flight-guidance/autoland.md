# Autoland

## Introduction

The FlyByWire A32NX has implemented the Airbus A320 Autoland feature. This guide shall give you a realistic description of when and how to use it correctly and successfully.

!!! info "Standard Operation"
    The focus of this guide is on standard operations without failures, as these are not yet implemented in the A32NX.

In flight simulation, the Autoland feature is an often requested feature, as many simmers use it as a substitute to learning how to land manually. And for recreational flight simulation, this is of course ok.

In real life, Autoland is very rarely used and requires special considerations and extra training and certifications by the flight crew. In fact, many pilots feel it's more stressful to use Autoland as they are not in control but need to monitor the systems very closely, so they can take manual control at any time.

This is on top of the fact that Autoland is mostly used in very bad visual situations where the pilots have little to no visual references and have to trust the autopilot to successfully perform the Autoland.

In summary:

- Autoland is not a replacement for learning and training how to land manually.
- Special training and certification is required for real pilots.
- Aircraft and airport must have the appropriate capability.
- It requires a high amount of preparation and limiting conditions need to be checked constantly (e.g. maximum crosswind).
- Autoland requires high focus from the flight crew monitoring the systems and to always be ready to take over for a go around. Pilot flying (PF) will usually look outside the aircraft, while pilot monitoring (PM) will watch the instruments.

## Real-World Considerations

### When to Use Autoland

When low visibility operations (LVO) CAT III are enforced, the use of Autoland is required. LVO operations are either announced via ATIS or ATC. 

Performing an Autoland is permissible for CAT II / CAT III runways even when low visibility operations (LVO) are not enforced, and this may even extend to CAT I runways. 

Autoland can also be subject to local procedures and authorities.

### When Not to Use Autoland

- ATC restrictions.
- Airport capabilities missing or restrictions in place.
- Aircraft capabilities missing or limitations exceeded.
- If CAT1 is displayed on the FMA, Autoland is not authorized.

### Crew Requirements

Airbus requires an operator to be Low Visibility Operation (LVO) certified to perform an Autoland. 

Other training may also be required before being able to perform an Autoland. It is also the responsibility of the operator to maintain the LVO certification or any approval by airworthiness authorities to perform automatic landings.

### Airport Requirements

The airport must be equipped with the appropriate ILS CAT (category) capability. 

- CAT III - LVP (Low Visibility Procedure) enforced
- CAT II / CAT III - LVP (Low Visibility Procedure) not enforced
- CAT I - Operators have a list of runways that are authorized to use Autoland with CAT I

!!! danger "Low Visibility Operations (LVO) Not Enforced"
    If the flight crew opts to perform an Autoland on a CAT II / CAT III capable runway when LVO is not enforced (checked with ATIS or ATC) the runway **must be considered a CAT I runway**.

    Crews should be alert to ILS beam / signal contamination, since the LOC/GS signal strength may not be guaranteed.

CAT I runway considerations before using Autoland:

- Pilots must be ready to disconnect the AP if any ILS fluctuations are detected.
- CAT II should at least be indicated on the FMA and the flight crew should apply the respective CAT II / CAT III.
  FCOM procedures.
- Visual contact should be established at the CAT I Minimum at the latest.

### Aircraft Limitations

All Airbus aircraft are certified to land automatically. However, limitations and conditions specified in the FCOM must be considered. Be aware that other not-so-obvious Autoland limitations, such as maximum airfield altitude, maximum (minimum) GS angle or maximum runway slope, must also be considered. 

In addition, the flight crew must monitor possible day-to-day technical restrictions, or the consequence(s) of a failure that may have occurred during the flight and that may downgrade landing capability.

Autoland many not be performed outside these limitations:

- Max. Crosswind: 20 kt
- Max. Headwind: 30 kt
- Max. Tailwind: 10 kt
- Glide slope angle smaller than - 2.5° or greater than - 3.25°
- Airport elevation above 9200 ft
- Aircraft weight below 44 000 kg (97 004 lb)
- Aircraft weight above the maximum landing weight
- Automatic landing is not allowed below - 2 000 ft pressure altitude

Minima: 

- ILS CAT II: MDH 100 ft
- ILS CAT III SINGLE: MDH 50 ft
- ILS CAT III DUAL: no DH (minimum RVR 75 m)

## Autoland How-To

### Preparations

- Check aircraft capability and limitations
- Check airport capability and limitations
- Check aircraft status
- Check Minima

### ILS Approach

- An Autoland procedure is very similar to a normal ILS approach and landing
- Follow the Beginner Guide procedure until the end of this [chapter](../../a32nx-beginner-guide/landing.md#3-preparation-and-checklist-for-landing)
- Instead of what is described in the [Beginner Guide for manual landing](../../a32nx-beginner-guide/landing.md#4-landing), you will not deactivate the Autopilot AP1, but instead you will activate the AP2 if you haven't done so already when activating APPR mode on the FCU.

### FMA Annunciations

The following FMA annunciations will be displayed during the approach and landing:

- SPEED
- G/S
- LOC
- CAT 3 DUAL (triple click sound when downgraded)
- AP 1+2
- 1 FD 2
- A/THR
- MINIMUM (or NO DH)
- At 350 ft: LAND
- At 40 ft: FLARE
- At 30 ft: THRUST IDLE
- ROLL OUT (main gear touchdown)

### Flow From 1000ft

Autoland is technically not much different from a normal ILS landing apart from the fact that the Autopilot(s) will not be turned off for the landing but stay on and the flight crew "only" monitors the landing via the instruments.

Assuming that we are fully configured for landing at 1000 ft above ground, with CONFIG 3 or CONFIG FULL, V~appr~ speed, gear down, autobrake armed, ground spoilers armed, ECAM landing memo no blue, landing checklist complete.

See [Beginner Guide Preparation and Checklist for Landing](../../a32nx-beginner-guide/landing.md#3-preparation-and-checklist-for-landing)

- At 1000 ft: callout "one thousand".
- At 500 ft: now callouts every hundred feet.
- Shortly after the 400 callout and before 350 ft, the FMA must show LAND in green to signal that the aircraft is now 
  in landing mode.
- At 350 ft: check the ILS course on the PFD.
- At 150 ft: The white line signifying the ground on the PFD attitude indicator starts to move up.
- At 100 ft: callout "hundred".
- At 50 ft: callout "fifty" and now callouts every 10 ft.
- At 40 ft: the FMA must show FLARE or otherwise the flight crew needs to either perform a manual landing if 
  visual references are acquired or perform a go around.
- Autothrust FMA should switch to THRUST IDLE.
- Between about 20 ft and 10 ft, the aircraft corrects its crosswind crab angle to bring its longitudinal axis in line 
  with the runway.
- At 10 ft: callout "Retard" commands the PF to set the throttle levers to idle.
- At touchdown:
    - FMA shows ROLL OUT - autopilot keeps aircraft on center line.
    - PF sets both thrust levers to reverse thrust (idle or up to max as appropriate).
    - PM checks and calls out: "touchdown", "spoilers", "reversers", "auto brake", "decel".
- At 70 kt: PM announces "70 knots" and PF will set the throttle to reverse idle if reverse max was used. 
- Before 20 kt: the PF manually brakes to deactivate the autobrake.
- At taxi speed: PF will set both thrust levers to idle and will disengage autopilots.
- From here on it is a normal [runway exit](../../a32nx-beginner-guide/landing.md#5-vacate-runway) and 
  [taxi procedure](../../a32nx-beginner-guide/after-landing.md).

### When Things go Wrong

Always remember the Golden Rules: Fly, Navigate, Communicate!

- Fly the aircraft manually!
- Perform a [Go-Around](#go-around)
- Inform ATC and follow instructions

### What could go wrong and how to react 

This is a non-exhaustive collection of things which could go wrong and how to handle them.

- FMA not showing `LAND` at 350 ft: 
    - Perform a go-around, or
    - A transition to a manual landing may be possible during a CAT II approach and at or above 80 ft if visual 
      references are acquired
- [Autoland Warning Light](#autoland-warning-light) at or below 200 ft:
    - Perform a go-around
    - A transition to a manual landing may be possible during a CAT II approach and at or above 80 ft if visual 
     references are acquired
- FMA not showing `FLARE` at 40 ft:
    - Perform a go-around
- FMA not showing `ROLL OUT` at touchdown:
    - Disconnect the autopilot and track the center line using visual references or localizer signal down to taxi speed.

If below 1000 ft AAL (above airport level) but higher than 100 ft RA (radio altitude):

- Perform a **go-around** in case of:
    - AP loss (cavalry charge)                
    - Amber caution (single chime)            
    - [Autoland Warning Light](#autoland-warning-light) (below 200 ft RA)  
    - Triple click (downgrading of capability)
- Proceed in case of:
    - Fire (red warning: Engine or APU)       
    - Smoke (red warning: Avionics, Cargo, Lavatory)
    - Smokes/Fumes in the Cockpit/Cabin

If below 100ft RA (radio altitude):

- Perform a **go-around** in case of:
    - [Autoland Warning Light](#autoland-warning-light)
    - Aircraft deviates from safe trajectory (Loc or Glide)
 
### Autoland Warning Light

See [Cockpit Glareshield Warning Panel](../../a32nx-briefing/flight-deck/glareshield/warning.md#5--autoland-warning-light).

With `LAND` or `FLARE` on FMA and at least one `AP` engaged, the Autoland Warning Light (red) will appear when the aircraft is below 200Fft RA (radio altitude) and one of the following events occurs:
 
- Both APs are lost
- The difference between both RA indications is greater than 15 ft
- Loss of LOC and/or GS signals:
    - Loss of LOC signal above 15 ft (transmitter or receiver)
    - Loss of GS signal above 100 ft (transmitter or receiver)
- The aircraft gets too far off the beam (LOC and/or GS scales flashes on PFD and ND rose ILS):
    - LOC deviation > 1/4 dot (above 15 ft)
    - GS deviation > 1 dot (above 100 ft)
- The FMGS detects a long flare

When the Autoland Warning Light (red) comes on, the automatic landing must be discontinued. 
For a Cat 2 app, a transition to a manual landing may be possible, but takeover should be made at or above 80 ft.

### Go-Around

!!! tip "We are planning an advanced guide for the Go-Around procedure. Stay tuned."

- Simultaneously apply the following three actions:
    - Thrust levers to TOGA to ensure SRS GA mode and then to FLX/MCT for a GA SOFT mode.
    - Rotate the aircraft towards 15° pitch up.
    - Announce "Go Around".
- Flaps: retract one step or as required.
- Check the FMA: MAN GA SOFT / SRS / GA TRK or NAV / A/THR (in blue).
    - If FMA does not display MAN GA SOFT or MAN TOGA set thrust levers to TOGA.
- Check positive climb and retract gear.
- Use NAV or HDG mode as required.
- Engage AP as required.
- At Go-Around Thrust Reduction Altitude set thrust levers to CL.
- At Go-Around Acceleration Altitude monitor that the target speed increases to green dot.
- Set flaps as required.
- At S speed: `FLAPS 0`, disarm `GND SPLRS`, turn off `NOSE` light, `RWY TURN OFF`, `LAND LIGHTS` as required. 
- Complete `After TakeOff Checklist`. 

See also [Beginner Guide Initial Climb](../../a32nx-beginner-guide/takeoff-climb-cruise.md#3-initial-climb).

## Additional Reading

See this excellent real-world pilot LVO Guide (low visibility operations) for more information:
[LVO Study Guide on this page](https://studygouge.blogspot.com/){target=new}

## Autoland Video

![video-embed](https://www.youtube.com/embed/Q1hACfew68Y)

