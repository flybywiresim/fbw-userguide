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
    - When active it is green, otherwise white.

    !!! note ""
         If the takeoff shift or the runway is changed after V1, V2 or VR insertion, but the origin airport remains the same, the MCDU message “CHECK TAKEOFF DATA” is displayed, but all takeoff parameters are retained.

- V1 (1L) VR (2L) V2 (3L):
    - The boxes remain amber, as long as the pilot does not make entries in them. The pilot can modify any entry, as long as the takeoff phase is not active.

    !!! note ""
        If the pilot does not enter V2, the SRS mode will not be available at takeoff.

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
    - Acceleration altitude is the altitude at which the climb phase is triggered.
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

## CRUISE

![PERF CRUISE Page](../../assets/a32nx-briefing/mcdu/perf-cruise-page.png "PERF CRUISE Page"){loading=lazy}

## DESCENT

![PERF DES Page](../../assets/a32nx-briefing/mcdu/perf-des-page.png "PERF DES Page"){loading=lazy}

## APPRAOCH

![PERF APPR Page](../../assets/a32nx-briefing/mcdu/perf-appr-page.png "PERF APPR Page"){loading=lazy}

## GO-AROUND

![PERF GO AROUND Page](../../assets/a32nx-briefing/mcdu/perf-goaround-page.png "PERF GO AROUND Page"){loading=lazy}
