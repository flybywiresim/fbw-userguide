# PERF: Performance Page

![PERF Page](../../assets/a32nx-briefing/mcdu/perf-page.jpg "PERF Page"){loading=lazy}

## Description

The Airbus A320neo divides each flight into these flight phases:

PREFLIGHT, TAKEOFF, CLIMB, CRUISE, DESCENT, APPROACH, GO-AROUND, DONE.

Except for the preflight and done phases, each flight phase has a performance page. These display performance data, speeds related to the various phases, and predictions. When pressing the PERF key the page for the currently active phase brought up. Pages for already completed flight phases are not available any more. In the preflight and done phases, pressing the PERF key brings up the takeoff performance page.

Prompts on each PERF page:

- PREV PHASE (6L):
    - To switch to the page for the previous phase. Not available on the takeoff performance page or already completed phases.
- ACTIVATE APPR PHASE (&L):
    - Replaces the PREV PHASE prompt when the current phase is active.
    - To activate the APPR phase (needs a second push for confirmation).
- NEXT PHASE (&R):
    - To review the performance page for the next phase.

## TAKE OFF

![PERF TAKE OFF](../../assets/a32nx-briefing/mcdu/perf-takeoff-page.png "PERF TAKE OFF"){loading=lazy}

- TITLE TAKE OFF:
    - Green when active, white when inactive.

    !!! note ""
         If the takeoff shift or the runway is changed after V1, V2 or VR insertion, but the origin airport remains the same, the MCDU message “CHECK TAKEOFF DATA” is displayed, but all takeoff parameters are retained.

- V1 (1L) VR (2L) V2 (3L):
    - The boxes remain amber, as long as the pilot does not make entries in them. The pilot can modify any entry, as long as the takeoff phase is not active.

    !!! note ""
        If the pilot does not enter V2, the SRS mode will not be available at takeoff.

    !!! tip
        In the FlyByWire A32NX you can click on the LSK next to V1, VR, V2, to let the aircraft calculate the correct V-Speed for you. This calculated value is placed in the Scratchpad and can be move to the V-Speed field with a second click.
        In real life this value us usually calculated by a specific airline application on the EFB.

- TRANS ALT (4L)
    - This field displays the navigation database default transition altitude (if defined) once the origin airport is entered. The pilot can modify it.

    !!! attention ""
        Currently no default database entry if filled in the FBW A32NX for Microsoft Flight Simulator.

- THR RED (5L)
    - The thrust reduction altitude is the altitude at which the pilot should reduce the thrust from TOGA/FLX to MAX CLIMB (CL detent).
    ‐ The thrust reduction altitude defaults to 1.500 ft above the runway elevation, or to the altitude set by the airline.
    !!! note ""
        Can be set in the flyPad settings.
    - The pilot can modify this altitude: The minimum is 400 ft above the runway elevation.

- ACC (5L)
    - Passing acceleration altitude triggers the climb phase.
    - The target speed changes to the initial climb speed
    - The default value is 1.500 ft above runway elevation
    - The flight crew can modify the value. The minimum value is 400 ft above runway elevation, though it is always higher than, or equal to, THR RED.
    !!! note ""
        - A clearing action reverts both values to the defaulted ones.
        - When the flight crew selects an altitude on the FCU that is below THR RED, it brings THR RED and ACC down to this altitude. (The 400 ft minimum still applies).

- UPLINK TO DATA (6L)
    - This key calls up the UPLINK TO DATA REQ page. It is only displayed in the preflight and done phases.

    !!! attention ""
        Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.

- TO SHIFT (2R)
    - Distance in meters or feet between the beginning of the runway and the aircraft's takeoff position. The flight crew should insert this value when taking off from an intersection to ensure a correct update of the FM position. The takeoff shift value must be positive, and cannot be greater than the runway length.

    !!! attention ""
        Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.

- FLAPS/THS (3R)
    - Positions of the flaps and the trimmable horizontal stabilizer (THS) at takeoff to be entered by the crew.
    - Can be edited until takeoff, by entering “UP X.X” or “X.X UP”, or “DN X.X” or “X.X DN” for the THS.

- FLX TO TEMP (4R)
    - Flight crew inserts the FLX TO temperature in Celsius for FLX takeoff setting purposes. It can only be entered during preflight. This value will be sent to the FADEC and displayed on the upper ECAM display.

- ENG OUT ACC (5R)
    - Engine-out acceleration altitude, as defined in the database, or manually entered by the flight crew. This is for display only, as a reminder. It cannot be cleared. The above ACC altitude rules of (5L) apply to this field.

## CLIMB

![PERF CLIMB Page](../../assets/a32nx-briefing/mcdu/perf-climb-page.png "PERF CLIMB Page"){loading=lazy}

- TITLE CLB:
    - Green when active, white when inactive.

- ACT MODE (1L):
    - Displays the preselected or active speed mode: SELECTED or MANAGED. Can't be modified from this field.

- CI (2L):
    - Cost index, as initialized either on the INIT A page, defaulted from the database, or inserted in this field by the pilot.

- MANAGED (3L):
    - This field displays the FMGS computed ECON speed/Mach.
    - Before CLIMB phase is active, a star is displayed next to the MANAGED speed, if the preselected speed mode is SELECTED. Pressing the 3L key in this case preselects MANAGED speed, and 4L reverts to brackets.

    !!! attention ""
        Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.

- PRESEL or SELECTED (4L):
    - Climb phase is not active:
        - As long as the climb phase is not active this field displays PRESEL. A preselected speed can be entered.
    - Climb phase is active:
        - Title becomes SELECTED.
        - Displays selected (or preselected) SPD or MACH target.
        - Cannot be modifed directly in this field, but with the SPD/MACH selection knob on the FCU.
        - If the FCU SPD/MACH selection knob if pushed it reverts to managed speed and the system selects/reselects ECON SPD/MACH and (4L) is blank.

<!--- Blank or EXPEDITE (5L):-->
<!--    - Blank as long as the aircraft is in preflight.-->
<!--    - Displays this legend when the takeoff or climb phase is active.-->
<!--    - The flight crew cannot engage EXPEDITE from this field. It indicates the time and distance required to reach the altitude displayed in the 2R field, in case of climb at green dot.-->

<!--    !!! attention ""-->
<!--        Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.-->

<!--- EO CLR (1R):-->
<!--    - The system displays the EO CLR prompt in case of engine out in climb.-->

<!--    !!! attention ""-->
<!--        Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.-->

<!--- PRED TO... (2R):-->
<!--    - This field displays the target altitude for the predictions shown in 3R, 4R, or 5L. It defaults to FCU altitude, but the pilot can modify it to any altitude below   CRZ FL.-->

<!--    !!! attention ""-->
<!--        Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.-->

<!--- (3R) (4R) (5R):-->
<!--    - These fields show time and distance predictions for the target altitude selected in (2R), computed for the current vertical mode and speed mode (MANAGED, SELECTED). These fields are displayed only while the takeoff, or climb phase is active.-->

<!--    !!! attention ""-->
<!--        Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.-->

## CRUISE

![PERF CRUISE Page](../../assets/a32nx-briefing/mcdu/perf-cruise-page.png "PERF CRUISE Page"){loading=lazy}

## DESCENT

![PERF DES Page](../../assets/a32nx-briefing/mcdu/perf-des-page.png "PERF DES Page"){loading=lazy}

## APPRAOCH

![PERF APPR Page](../../assets/a32nx-briefing/mcdu/perf-appr-page.png "PERF APPR Page"){loading=lazy}

## GO-AROUND

![PERF GO AROUND Page](../../assets/a32nx-briefing/mcdu/perf-goaround-page.png "PERF GO AROUND Page"){loading=lazy}
