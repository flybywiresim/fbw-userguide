---
title: A380X Flight Deck API
description: Documentation for the FlyByWire A32NX FlightDeck API.
hide:
    - navigation
---

# A380X Flight Deck API

<H1><span style="color: #ff0000;">TODO: Change content</span></H1>

[A380 Pilot Briefing](../../../pilots-corner/a380x/a380x-briefing/index.md){ .md-button }
[Clickable Flight Deck](../../../pilots-corner/a380x/a380x-briefing/flight-deck/index.md){ .md-button }

Find the complete list of Custom Event and Custom LVARS of the A380X:

- [Custom LVARs](https://github.com/flybywiresim/aircraft/blob/master/fbw-a380x/docs/a380-simvars.md){target=new}
- [Custom Input Events](https://github.com/flybywiresim/aircraft/blob/master/fbw-a380x/docs/a380x-input-events.md){target=new}

[//]: # (- [Custom Events]&#40;https://github.com/flybywiresim/aircraft/blob/master/fbw-a380x/docs/a380-events.md&#41;{target=new})


## "How to read the tables"

- **Function**: The name of the switch or button on the panel.
- **API Usage**: The name of the API variable or event.
- **Values**: The possible values the API variable or event can have.
- **Read/Write**: Whether the API variable or event can be read or written.
- **Type**: The type of the API variable or event (see [below](#api-var-and-event-types)).
- **Remark**: Additional information about the API variable or event.

To shorten the length of the table we use the following placeholders for the API disignations:

- `{SIDE}`: Replace with `L` for left, `R` for right (and sometimes `C` for Center).
- `{NUM}`: Replace with `1` for the first, `2` for the second, `3` for the third, `4` for the fourth.

### "API Var and Event Types"

| Type                 | Description                                                                                                           |
|----------------------|-----------------------------------------------------------------------------------------------------------------------|
| **Custom LVAR**      | are custom variables created by the FlyByWire team to control the aircraft (aka Named Vars).                          |
| **MSFS VAR**         | are variables that are part of the default MSFS SDK (aka A Vars).                                                     |
| **SIMCONNECT VAR**   | are variables that are part of the default MSFS SDK (aka A Vars).                                                     |
| **MSFS EVENT**       | are events that are part of the default MSFS SDK (aka K-Events).                                                      |
| **SIMCONNECT EVENT** | are events that are part of the default MSFS SDK (aka K Events).                                                      |
| **CUSTOM EVENT**     | are custom events created by the FlyByWire team to control the aircraft.                                              |
| **H EVENT**          | are events that are part of the default MSFS SDK (aka H Events).                                                      |
| **INPUT EVENT**      | are events that are part of the default MSFS SDK used mainly for cockpit interaction inputs (aka B Vars or B Events). |

_[MSFS Avionics Framework on SimVars](https://microsoft.github.io/msfs-avionics-mirror/docs/interacting-with-msfs/simvars){target=new}_<br/>
_[MSFS Avionics Framework on Events](https://microsoft.github.io/msfs-avionics-mirror/docs/interacting-with-msfs/key-events){target=new}_<br/>
_[MSFS Avionics Framework on H Events](https://microsoft.github.io/msfs-avionics-mirror/docs/interacting-with-msfs/receiving-h-events){target=new}_

!!! note ""
    The below table might lag behind the current developments of the A380X. It is based on the A380X Development
    version, and we try to keep it updated as best as possible.

    You can help us keep this up to date and improve this by reporting any errors or omissions on our 
    [:fontawesome-brands-discord:{: .discord } - **Discord**](https://discord.gg/flybywire){target=new} in the 
    **#a380x-support** channel or by creating an issue report here: 
    [Docs Issues](https://github.com/flybywiresim/docs/issues){target=new}.

!!! note "The order of the panels below is roughly done after the standard cold & dark setup procedure."

## Overhead Forward

### ELEC Panel

Flight Deck:  [ELEC Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/ovhd/elec.md)

| Function         | API Usage                                     | Values     | Read/Write | Type             | Remark                                                                      |
|:-----------------|:----------------------------------------------|:-----------|:-----------|:-----------------|:----------------------------------------------------------------------------|
| BAT {NUM}        | A32NX_OVHD_ELEC_BAT_{NUM}_PB_IS_AUTO          | 0..1       | R/W        | Custom LVAR      |                                                                             |
|                  | A32NX_OVHD_ELEC_BAT_{NUM}_PB_HAS_FAULT        | 0..1       | R/W        | Custom LVAR      |                                                                             |
| BAT ESS+APU      | A32NX_OVHD_ELEC_BAT_{ESS\|APU}_PB_IS_AUTO     | 0..1       | R/W        | Custom LVAR      |                                                                             |
|                  | A32NX_OVHD_ELEC_BAT_{ESS\|APU}_PB_HAS_FAULT   | 0..1       | R/W        | Custom LVAR      |                                                                             |
|                  |                                               |            |            |                  |                                                                             |
| EXT PWR {NUM}    | SET_EXTERNAL_POWER                            | 1..4, 0..1 | -          | MSFS EVENT       | This event takes 2 parameters - the number of the index 1..4 and OFF/ON=0/1 |
|                  | EXTERNAL POWER AVAILABLE:{NUM}                | 0..1       | R          | MSFS VAR         |                                                                             |
|                  | EXTERNAL POWER ON:{NUM}                       | 0..1       | R          | MSFS VAR         |                                                                             |
|                  |                                               |            |            |                  |                                                                             |
| GEN {NUM}        | TOGGLE_ALTERNATOR:{NUM}                       | -          | -          | SIMCONNECT EVENT |                                                                             |
|                  | GENERAL ENG MASTER ALTERNATOR:{NUM}           | 0..1       | R/W        | SIMCONNECT VAR   |                                                                             |
|                  | A32NX_OVHD_ELEC_ENG_GEN_{NUM}_PB_HAS_FAULT    | 0..1       | R          | Custom LVAR      |                                                                             |
|                  |                                               |            |            |                  |                                                                             |
| APU GEN          | APU_GENERATOR_SWITCH_TOGGLE                   | 1..2       | -          | SIMCONNECT EVENT |                                                                             |
|                  | APU_GENERATOR_SWITCH_SET                      | 0..1       | -          | SIMCONNECT EVENT |                                                                             |
|                  | APU GENERATOR SWITCH                          | 0..1       | R/W        | SIMCONNECT VAR   |                                                                             |
|                  | A32NX_OVHD_ELEC_APU_GEN_{NUM}_PB_HAS_FAULT    | 0..1       | R          | Custom LVAR      |                                                                             |
|                  |                                               |            |            |                  |                                                                             |
| BUS TIE          | A32NX_OVHD_ELEC_BUS_TIE_PB_IS_AUTO            | 0..1       | R/W        | Custom LVAR      |                                                                             |
|                  | A32NX_OVHD_ELEC_BUS_TIE_PB_HAS_FAULT          | 0..1       | R          | Custom LVAR      |                                                                             |
|                  |                                               |            |            |                  |                                                                             |
| AC ESS FEED      | A32NX_OVHD_ELEC_AC_ESS_FEED_PB_IS_NORMAL      | 0..1       | R/W        | Custom LVAR      |                                                                             |
|                  | A32NX_OVHD_ELEC_AC_ESS_FEED_PB_HAS_FAULT      | 0..1       | R          | Custom LVAR      |                                                                             |
| AC ESS FEED LOCK | A32NX_OVHD_ELEC_AC_ESS<br/>_FEED_PB_IS_NORMAL_LOCK | 0..1       | R          | Custom LVAR      |                                                                             |
|                  |                                               |            |            |                  |                                                                             |
| DRIVE {NUM}      | A32NX_OVHD_ELEC_IDG_{NUM}_PB_IS_RELEASED      | 0 -> 1     | R/W        | Custom LVAR      | Cannot be undone - flight restart required                                  |
|                  | A32NX_OVHD_ELEC_IDG_{NUM}_PB_HAS_FAULT        | 0..1       | R          | Custom LVAR      |                                                                             |
|                  |                                               |            |            |                  |                                                                             |
| GALY & CAB       | A32NX_OVHD_ELEC_GALY_AND_CAB_PB_IS_AUTO       | 0..1       | R/W        | Custom LVAR      | Current connected with PAX SYS                                              |
|                  | A32NX_OVHD_ELEC_GALY_AND_CAB_PB_HAS_FAULT     | 0..1       | R          | Custom LVAR      |                                                                             |
|                  |                                               |            |            |                  |                                                                             |
| COMMERCIAL       | A32NX_OVHD_ELEC_COMMERCIAL_PB_IS_AUTO         | 0..1       | R/W        | Custom LVAR      | Currently 1+2 and ELMU are connected                                        |
|                  | A32NX_OVHD_ELEC_COMMERCIAL_PB_HAS_FAULT       | 0..1       | R          | Custom LVAR      | Currently 1+2 and ELMU are connected                                        |
|                  |                                               |            |            |                  |                                                                             |

### External Lights Panel

Flight Deck:  [EXT LT Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/ovhd/ext-lt.md)

| Function     | API Usage            | Values | Read/Write | Type           | Remark                        |
|:-------------|:---------------------|:-------|:-----------|:---------------|:------------------------------|
| STROBE       | LIGHTING_STROBE_0    | 0..2   | R/W        | INPUT EVENT    | 2=OFF, 1=AUTO, 0=ON           |
|              | STROBES_SET          | 0..1   | -          | INPUT EVENT    | OFF and ON (no AUTO)          |
|              | STROBES_ON           | -      | -          | INPUT EVENT    | OFF and ON (no AUTO)          |
|              | STROBES_OFF          | -      | -          | INPUT EVENT    | OFF and ON (no AUTO)          |
|              | STROBES_TOGGLE       | -      | -          | INPUT EVENT    | OFF and ON (no AUTO)          |
|              | LIGHT STROBE         | 0..1   | R          | SIMCONNECT VAR | OFF and ON (no AUTO)          |
|              | STROBE_0_AUTO        | 0..1   | R/W        | Custom LVAR    | AUTO only when STROBES are ON |
|              |                      |        |            |                |                               |
| BEACON       | LIGHTING_BEACON_0    | -      | R/W        | INPUT EVENT    |                               |
|              | BEACON_LIGHTS_SET    | 0..1   | -          | INPUT EVENT    |                               |
|              | BEACON_LIGHTS_ON     | -      | -          | INPUT EVENT    |                               |
|              | BEACON_LIGHTS_OFF    | -      | -          | INPUT EVENT    |                               |
|              | TOGGLE_BEACON_LIGHTS | -      | -          | INPUT EVENT    |                               |
|              | LIGHT BEACON         | 0..1   | R          | SIMCONNECT VAR |                               |
|              |                      |        |            |                |                               |
| WING         | LIGHTING_WING_0      | -      | R/W        | INPUT EVENT    |                               |
|              | WING_LIGHTS_SET      | 0..1   | -          | INPUT EVENT    |                               |
|              | WING_LIGHTS_ON       | -      | -          | INPUT EVENT    |                               |
|              | WING_LIGHTS_OFF      | -      | -          | INPUT EVENT    |                               |
|              | TOGGLE_WING_LIGHTS   | -      | -          | INPUT EVENT    |                               |
|              | LIGHT WING           | 0..1   | R          | SIMCONNECT VAR |                               |
|              |                      |        |            |                |                               |
| NAV          | LIGHTING_NAV_0       | -      | R/W        | INPUT EVENT    |                               |
|              | NAV_LIGHTS_SET       | 0..1   | -          | INPUT EVENT    |                               |
|              | NAV_LIGHTS_ON        | -      | -          | INPUT EVENT    |                               |
|              | NAV_LIGHTS_OFF       | -      | -          | INPUT EVENT    |                               |
|              | TOGGLE_NAV_LIGHTS    | -      | -          | INPUT EVENT    |                               |
|              | LIGHT NAV            | 0..1   | R          | SIMCONNECT VAR |                               |
|              |                      |
| LOGO         | LIGHTING_LOGO_0      | -      | R/W        | INPUT EVENT    |                               |
|              | LOGO_LIGHTS_SET      | 0..2   | -          | INPUT EVENT    |                               |
|              | LOGO_LIGHTS_ON       | -      | -          | INPUT EVENT    |                               |
|              | LOGO_LIGHTS_OFF      | -      | -          | INPUT EVENT    |                               |
|              | TOGGLE_NAV_LIGHTS    | -      | -          | INPUT EVENT    |                               |
|              | LIGHT LOGO           | 0..2   | R          | SIMCONNECT VAR |                               |
|              |                      |
| RWY TURN OFF | LANDING_TAXI_2       | 0..1   | R/W        | INPUT EVENT    |                               |
|              | TOGGLE_TAXI_LIGHTS   | -      | -          | INPUT EVENT    |                               |
|              | LIGHT TAXI:2         | 0..1   | R          | SIMCONNECT VAR |                               |
|              |                      |        |            |                |                               |
| LAND         | LIGHTING_LANDING_2   | 0..1   | R/W        | INPUT EVENT    | 0=OFF, 1=ON                   |
|              |                      |        |            |                |                               |
| NOSE         | LIGHTING_LANDING_1   | 0..2   | R/W        | INPUT EVENT    | 0=T.O, 1=TAXI, 2=OFF          |

### Interior Lights Panel

Flight Deck: [INT LT Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/ovhd/int-lt.md)

| Function               | API Usage                                               | Values | Read/Write | Type             | Remark                                 |
|:-----------------------|:--------------------------------------------------------|:-------|:-----------|:-----------------|:---------------------------------------|
| ICE IND & STBY COMPASS | L:A380X_OVHD_EXTLT_STBY<br/>_COMPASS_ICE_IND_SWITCH_POS | 0..1   | R/W        | Custom LVAR      | 0=OFF, 1=ICI IND ON, 2=STBY COMPASS ON |
|                        |                                                         |        |            |                  |                                        |
| STORM                  | N/A                                                     |        |            |                  |                                        |
|                        |                                                         |        |            |                  |                                        |
| ANN LT                 | A32NX_OVHD_INTLT_ANN                                    | 0..2   | R/W        | Custom LVAR      | 2=DIM, 1=BRT, 0=TEST                   |

### Signs Panel

Flight Deck: [Signs Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/ovhd/signs.md)

| Function     | API Usage                                   | Values | Read/Write | Type             | Remark              |
|:-------------|:--------------------------------------------|:-------|:-----------|:-----------------|:--------------------|
| SEAT BELTS   | CABIN_SEATBELTS_ALERT_SWITCH_TOGGLE         | -      | -          | SIMCONNECT EVENT |                     |
|              | CABIN SEATBELTS ALERT SWITCH                | 0..1   | R          | SIMCONNECT VAR   |                     |
|              | XMLVAR_SWITCH_OVHD_INTLT_SEATBELT_Position  | 0..2   | R          | Custom LVAR      | 0=ON, 1=AUTO, 2=OFF |
|              |                                             |        |            |                  |                     |
| NO SMOKING   | XMLVAR_SWITCH_OVHD_INTLT_NOSMOKING_POSITION | 0..2   | R/W        | Custom LVAR      | 0=ON, 1=AUTO, 2=OFF |
|              |                                             |        |            |                  |                     |
| EMER EXIT LT | XMLVAR_SWITCH_OVHD_INTLT_EMEREXIT_POSITION  | 0..2   | R/W        | Custom LVAR      | 0=ON, 1=AUTO, 2=OFF |

### ADIRS Panel

Flight Deck: [ADIRS Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/ovhd/adirs.md)

| Function                 | API Usage                                    | Values  | Read/Write | Type        | Remark              |
|:-------------------------|:---------------------------------------------|:--------|:-----------|:------------|:--------------------|
| ADIR {NUM} knob          | A32NX_OVHD_ADIRS_IR_{NUM}_MODE_SELECTOR_KNOB | 0..2    | R/W        | Custom LVAR | 0=OFF, 1=NAV, 2=ATT |
|                          |                                              |         |            |             |                     |
| IR {NUM}                 | A32NX_OVHD_ADIRS_IR_{NUM}_PB_IS_ON           | 0..1    | R/W        | Custom LVAR |                     |
|                          | A32NX_OVHD_ADIRS_IR_{NUM}_PB_HAS_FAULT       | 0..1    | R          | Custom LVAR |                     |
|                          |                                              |         |            |             |                     |
| ADR {NUM}                | A32NX_OVHD_ADIRS_ADR_{NUM}_PB_IS_ON          | 0..1    | R/W        | Custom LVAR |                     |
|                          | A32NX_OVHD_ADIRS_ADR_{NUM}_PB_HAS_FAULT      | 0..1    | R          | Custom LVAR |                     |
|                          |                                              |         |            |             |                     |
| Remaining Alignment Time | A32NX_ADIRS_REMAINING_IR_ALIGNMENT_TIME      | seconds | R          | Custom LVAR |                     |

### APU Panel

Flight Deck: [APU Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/ovhd/apu.md)

| Function  | API Usage                             | Values | Read/Write | Type        | Remark |
|:----------|:--------------------------------------|:-------|:-----------|:------------|:-------|
| MASTER SW | A32NX_OVHD_APU_MASTER_SW_PB_IS_ON     | 0..1   | R/W        | Custom LVAR |        |
|           | A32NX_OVHD_APU_MASTER_SW_PB_HAS_FAULT | 0..1   | R          | Custom LVAR |        |
|           |                                       |        |            |             |        |
| START     | A32NX_OVHD_APU_START_PB_IS_ON         | 0..1   | R/W        | Custom LVAR |        |
|           | A32NX_OVHD_APU_START_PB_IS_AVAILABLE  | 0..1   | R          | Custom LVAR |        |

### RCDR Panel

Flight Deck: [RCDR Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/ovhd/rcdr-evac.md)

| Function  | API Usage                    | Values | Read/Write | Type        | Remark |
|:----------|:-----------------------------|:-------|:-----------|:------------|:-------|
| GND CTL   | A32NX_RCDR_GROUND_CONTROL_ON | 0..1   | R/W        | Custom LVAR |        |

### Oxygen Panel

Flight Deck: [Oxygen Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/ovhd/oxygen.md)

| Function    | API Usage                       | Values | Read/Write | Type        | Remark        |
|:------------|:--------------------------------|:-------|:-----------|:------------|:--------------|
| MASK MAN ON | A32NX_OXYGEN_MASKS_DEPLOYED     | 0..1   | R/W        | Custom LVAR |               |
|             |                                 |        |            |             |               |
| PASSENGER   | A32NX_OXYGEN_PASSENGER_LIGHT_ON | 0..1   | R/W        | Custom LVAR |               |
|             |                                 |        |            |             |               |
| CREW SUPPLY | PUSH_OVHD_OXYGEN_CREW           | 0..1   | R/W        | Custom LVAR | 0=AUTO, 1=OFF |

### Fire Panel

Flight Deck: [APU Fire Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/ovhd/apu-fire.md)<br/>
Flight Deck: [ENG Fire Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/ovhd/eng-fire.md)

| Function                      | API Usage                                                 | Values | Read/Write | Type        | Remark                                          |
|:------------------------------|:----------------------------------------------------------|:-------|:-----------|:------------|:------------------------------------------------|
| APU FIRE GUARD                | A32NX_FIRE_GUARD_APU1                                     | 0..1   | R/W        | Custom LVAR |                                                 |
| APU FIRE                      | A32NX_FIRE_BUTTON_APU1                                    | 0..1   | R/W        | Custom LVAR |                                                 |
| APU AGENT ARMED               | A32NX_FIRE_SQUIB_1_APU_1_IS_ARMED                         | 0..1   | R          | Custom LVAR |                                                 |
| APU AGENT PRESSED             | A32NX_OVHD_FIRE_AGENT_1_APU_1_IS_PRESSED                  | 0..1   | R/W        | Custom LVAR | When pressed, SQUIB discharges. Can't be reset. |
| APU AGENT DISCH               | A32NX_OVHD_FIRE_AGENT_1_APU_1_IS_DISCHARGED               | 0..1   | R          | Custom LVAR | Can't be reset.                                 |
|                               |                                                           |        |            |             |                                                 |
| ENG {NUM} FIRE GUARD          | A32NX_FIRE_GUARD_ENG{NUM}                                 | 0..1   | R/W        | Custom LVAR |                                                 |
| ENG {NUM} FIRE                | A32NX_FIRE_BUTTON_ENG{NUM}                                | 0..1   | R/W        | Custom LVAR |                                                 |
| ENG {NUM} AGENT {NUM} ARMED   | A32NX_FIRE_SQUIB_{NUM}\_ENG_{NUM}_IS_ARMED                | 0..1   | R          | Custom LVAR |                                                 |
| ENG {NUM} AGENT {NUM} PRESSED | A32NX_OVHD_FIRE_AGENT<br/>_{NUM}\_ENG_{NUM}_IS_PRESSED    | 0..1   | R/W        | Custom LVAR | When pressed, SQUIB discharges. Can't be reset. |
| ENG {NUM} AGENT {NUM} DISCH   | A32NX_OVHD_FIRE_AGENT<br/>_{NUM}\_ENG_{NUM}_IS_DISCHARGED | 0..1   | R          | Custom LVAR | Can't be reset.                                 |
|                               |                                                           |        |            |             |                                                 |
| FIRE TEST                     | A32NX_OVHD_FIRE_TEST_PB_IS_PRESSED                        | 0..1   | R/W        | Custom LVAR |                                                 |

### Fuel Panel

Flight Deck: [Fuel Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/ovhd/fuel.md)

The A380X Fuel Panel is split into several parts, the crossfeeds, the left and right fuel tanks, the trim tanks and
the x-feeds.

The individual pumps are controlled via circuit connections. The corresponding circuit connection numbers are as 
follows:

``` title="Fuel and Trim Tank CIRCUIT CONNECTION NUMBERS"
|    | 2  | 3  | 64 | 65 |    |    | 66 | 67 | 68 | 69 |    |   
| 70 | 71 | 72 | 73 | 74 |    |    | 78 | 79 | 76 | 77 | 75 |
|    |    |    |    |    | 80 | 81 |    |    |    |    |    |
```

```rpn title="Example Reverse Polish Notation (RPN) for Fuel Pump Circuit Connection"
2 1 (>K:2:ELECTRICAL_BUS_TO_CIRCUIT_CONNECTION_TOGGLE)
```

| Function               | API Usage                                           | Values         | Read/Write | Type        | Remark                       |
|:-----------------------|:----------------------------------------------------|:---------------|:-----------|:------------|:-----------------------------|
| FUEL PUMP              | ELECTRICAL_BUS_TO_CIRCUIT_CONNECTION_TOGGLE         | see above      | -          | MSFS EVENT  | Fuel pumps connection toggle |
|                        |                                                     |                |            |             |                              |
| CROSSFEED Valve        | FUELSYSTEM_VALVE_TOGGLE                             | 46, 47, 48, 49 | -          | MSFS EVENT  |                              |
| CROSSFEED 1 PRESSED    | XMLVAR_Momentary_PUSH_OVHD_FUEL_XFEED_Pressed       | 0..1           | R          | Custom LVAR |                              |
| CROSSFEED 2..4 PRESSED | XMLVAR_Momentary_PUSH_OVHD_FUEL_XFEED{1..3}_Pressed | 0..1           | R          | Custom LVAR |                              |
|                        |                                                     |                |            |             |                              |
| OUTR TK XFR            | A380X_OVHD_FUEL_OUTRTK_XFR_PB_IS_AUTO               | 0..1           | R/W        | Custom LVAR |                              |
|                        | A380X_OVHD_FUEL_OUTTTK_XFR_PB_IS_AUTO_LOCK          | 0..1           | R          | Custom LVAR |                              |
| MID TK XFR             | A380X_OVHD_FUEL_MIDTK_XFR_PB_IS_AUTO                | 0..1           | R/W        | Custom LVAR |                              |
|                        | A380X_OVHD_FUEL_MIDTK_XFR_PB_IS_AUTO_LOCK           | 0..1           | R          | Custom LVAR |                              |
| INR TK XFR             | A380X_OVHD_FUEL_INRTK_XFR_PB_IS_AUTO                | 0..1           | R/W        | Custom LVAR |                              |
|                        | A380X_OVHD_FUEL_INRTK_XFR_PB_IS_AUTO_LOCK           | 0..1           | R          | Custom LVAR |                              |
| TRIM TK XFR            | A380X_OVHD_FUEL_TRIMTK_XFR_PB_IS_AUTO               | 0..1           | R/W        | Custom LVAR |                              |
|                        | A380X_OVHD_FUEL_TRIMTK_XFR_PB_IS_AUTO_LOCK          | 0..1           | R          | Custom LVAR |                              |

### Air Condition Panel

Flight Deck: [AC Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/ovhd/air.md)

| Function          | API Usage                                                     | Values | Read/Write | Type           | Remark                                                  |
|:------------------|:--------------------------------------------------------------|:-------|:-----------|:---------------|:--------------------------------------------------------|
| APU BLEED         | A32NX_OVHD_PNEU_APU_BLEED_PB_IS_ON                            | 0..1   | R/W        | Custom LVAR    |                                                         |
|                   | A32NX_OVHD_PNEU_APU_BLEED_PB_HAS_FAULT                        | 1      | R          | Custom LVAR    |                                                         |
|                   | XMLVAR_Momentary_PUSH<br/>_OVHD_AIRCOND_APUBLEED_Pressed      | 0..1   | R/W        | SIMCONNECT VAR | Button position                                         |
|                   | BLEED AIR APU                                                 | 0..1   | R          | SIMCONNECT VAR |                                                         |
|                   |                                                               |        |            |                |                                                         |
| ENG {NUM} BLEED   | ENGINE_BLEED_AIR_SOURCE_TOGGLE                                | {NUM}  | -          | MSFS EVENT     |                                                         |
|                   | BLEED AIR ENGINE:{NUM}                                        | 0..1   | R          | SIMCONNECT VAR |                                                         |
|                   | A32NX_OVHD_PNEU_ENG_{NUM}_BLEED_PB_HAS_FAULT                  | 0..1   | R/W        | Custom LVAR    |                                                         |
|                   | XMLVAR_Momentary_PUSH<br/>_OVHD_AIRCOND_ENG{NUM}BLEED_Pressed | 0..1   | R/W        | Custom LVAR    |                                                         |
|                   |                                                               |        |            |                |                                                         |
| X BLEED knob      | A32NX_KNOB_OVHD_AIRCOND_XBLEED_POSITION                       | 0..2   | R/W        | Custom LVAR    | 0=Close, 1=AUTO, 2=Open                                 |
|                   | A32NX_PNEU_XBLEED_VALVE_{SIDE}_OPEN                           | 0..1   | R          | Custom LVAR    | SIDE=C, L, R                                            |
|                   |                                                               |        |            |                |                                                         |
| PACK {NUM}        | A32NX_OVHD_COND_PACK_{NUM}_PB_IS_ON                           | 0..1   | R/W        | Custom LVAR    |                                                         |
|                   | A32NX_OVHD_COND_PACK_{NUM}_PB_HAS_FAULT                       | 0..1   | R/W        | Custom LVAR    |                                                         |
|                   | A32NX_COND_PACK_{NUM}_FLOW_VALVE_1_IS_OPEN                    | 0..1   | R          | Custom LVAR    |                                                         |
|                   | A32NX_COND_PACK_{NUM}_FLOW_VALVE_2_IS_OPEN                    | 0..1   | R          | Custom LVAR    |                                                         |
|                   |                                                               |        |            |                |                                                         |
| AIR FLOW knob     | A32NX_KNOB_OVHD_AIRCOND_PACKFLOW_POSITION                     | 0..3   | R/W        | Custom LVAR    | 0=MAN, 1=LO, 2=NORM, 3=HI                               |
|                   |                                                               |        |            |                |                                                         |
| COCKPIT knob      | A32NX_OVHD_COND_CKPT_SELECTOR_KNOB                            | 0..300 | R/W        | Custom LVAR    |                                                         |
|                   | A32NX_COND_CKPT_TEMP                                          | °      | R          | Custom LVAR    |                                                         |
|                   | A32NX_COND_CKPT_DUCT_TEMP                                     | °      | R          | Custom LVAR    |                                                         |
|                   |                                                               |        |            |                |                                                         |
| CABIN knob        | A32NX_OVHD_COND_FWD_SELECTOR_KNOB                             | 0..400 | R/W        | Custom LVAR    | 0..350 Cabin Temp, 400=PURS SEL                         |
|                   | A32NX_COND_{DECK}\_DECK_{NUM}_TEMP                            | °      | R          | Custom LVAR    | DECK=MAIN or UPPER, MAIN has 8 zones, UPPER has 7 zones |
|                   | A32NX_COND_{DECK}\_DECK_{NUM}_DUCT_TEMP                       | °      | R          | Custom LVAR    | DECK=MAIN or UPPER, MAIN has 8 zones, UPPER has 7 zones |
|                   |                                                               |        |            |                |                                                         |
| HOT AIR           | A32NX_OVHD_COND_HOT_AIR_{NUM}_PB_IS_ON                        | 0..1   | R/W        | Custom LVAR    |                                                         |
|                   | A32NX_OVHD_COND_HOT_AIR_{NUM}_PB_HAS_FAULT                    | 0..1   | R/W        | Custom LVAR    |                                                         |
|                   |                                                               |        |            |                |                                                         |
| RAM AIR           | A32NX_OVHD_COND_RAM_AIR_PB_IS_ON_LOCK                         | 0..1   | R          | Custom LVAR    | Switch Guard                                            |
|                   | A32NX_OVHD_COND_RAM_AIR_PB_IS_ON                              | 0..1   | R/W        | Custom LVAR    |                                                         |
|                   |                                                               |        |            |                |                                                         |
| CABIN AIR EXTRACT | A32NX_OVHD_VENT_AIR_EXTRACT_PB_IS_ON_LOCK                     | 0..1   | R          | Custom LVAR    | Switch Guard                                            |
|                   | A32NX_OVHD_VENT_AIR_EXTRACT_PB_IS_ON                          | 0..1   | R/W        | Custom LVAR    |                                                         |

### Anti Ice Panel

Flight Deck: [Anti Ice Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/ovhd/anti-ice.md)

| Function          | API Usage                                                | Values | Read/Write | Type             | Remark                                |
|:------------------|:---------------------------------------------------------|:-------|:-----------|:-----------------|:--------------------------------------|
| WING              | TOGGLE_STRUCTURAL_DEICE                                  | -      | -          | SIMCONNECT EVENT | Function & Button light               |
|                   | STRUCTURAL DEICE SWITCH                                  | 0..1   | R/W        | SIMCONNECT VAR   | Function & Button light               |
|                   | XMLVAR_MOMENTARY_PUSH<br/>_OVHD_ANTIICE_WING_PRESSED     | 0..1   | R/W        | Custom LVAR      | Button state                          |
|                   |                                                          |        |            |                  |                                       |
| ENG {NUM}         | ANTI_ICE_SET_ENG{NUM}                                    | 0..1   | -          | SIMCONNECT EVENT | Function & Button light               |
|                   | ENG ANTI ICE:{NUM}                                       | 0..1   | R/W        | SIMCONNECT VAR   | Function & Button light               |
|                   | XMLVAR_MOMENTARY_PUSH<br/>_OVHD_ANTIICE_ENG{NUM}_PRESSED | 0..1   | R/W        | Custom LVAR      | Button state                          |
|                   |                                                          |        |            |                  |                                       |
| PROBE/WINDOW HEAT | A32NX_MAN_PITOT_HEAT                                     | 0..1   | R/W        | Custom LVAR      | Panel is on the left side of the OVHD |
|                   | XMLVAR_MOMENTARY_PUSH<br/>_OVHD_PROBESWINDOW_PRESSED     | 0..1   | R/W        | Custom LVAR      | Button state                          |

### Calls Panel

Flight Deck: [Calls Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/ovhd/calls.md)

| Function | API Usage                | Values | Read/Write | Type        | Remark |
|:---------|:-------------------------|:-------|:-----------|:------------|:-------|
| EMER     | A32NX_CALLS_EMER_ON_LOCK | 0..1   | R          | Custom LVAR |        |
|          | A32NX_CALLS_EMER_ON      | 0..1   | R/W        | Custom LVAR |        |

### Wiper Panel

Flight Deck: [Wiper Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/ovhd/wiper.md)

| Function     | API Usage                                | Values     | Read/Write | Type       | Remark                                               |
|:-------------|:-----------------------------------------|:-----------|:-----------|:-----------|:-----------------------------------------------------|
| WIPER L knob | CIRCUIT SWITCH ON:141                    | 0..1       | R/W        | MSFS VAR   | Turns the wiper on/off - slow/fast via power setting |
|              | ELECTRICAL_CIRCUIT_TOGGLE:141            |            |            | MSFS Event |                                                      |
|              | ELECTRICAL_CIRCUIT_POWER_SETTING_SET:141 | 0..75..100 |            | MSFS Event | 0=off, 75=slow, 100=fast                             |           |
|              |                                          |            |            |            |                                                      |
| WIPER R knob | CIRCUIT SWITCH ON:143                    | 0..1       | R/W        | MSFS       | Turns the wiper on/off - slow/fast via power setting |
|              | ELECTRICAL_CIRCUIT_TOGGLE:143            |            |            | MSFS VAR   |                                                      |
|              | ELECTRICAL_CIRCUIT_POWER_SETTING_SET:143 | 0..75..100 |            | MSFS Event | 0=off, 75=slow, 100=fast                             |

### Flight Control Panel

Flight Deck: [Flight Control Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/ovhd/flt-ctl.md)

| Function      | API Usage                           | Values | Read/Write | Type        | Remark |
|:--------------|:------------------------------------|:-------|:-----------|:------------|:-------|
| PRIM {NUM} PB | A32NX_PRIM_{NUM}_PUSHBUTTON_PRESSED | 0..1   | R/W        | Custom LVAR |        |
| SEC {NUM} PB  | A32NX_SEC_{NUM}_PUSHBUTTON_PRESSED  | 0..1   | R/W        | Custom LVAR |        |

## Glareshield

### Lighting Knobs

Flight Deck: [Glareshield Lighting Knobs](../../../pilots-corner/a380x/a380x-briefing/flight-deck/glareshield/glare-underside.md)

To control the lighting knobs, the following API usage is available:

SIMCONNECT EVENT: `SIMCONNECT:LIGHT_POTENTIOMETER_SET`

| Function                    | API Usage              | Values | Read/Write | Type     | Remark |
|:----------------------------|:-----------------------|:-------|:-----------|:---------|:-------|
| Glareshield Integral Lights | LIGHT POTENTIOMETER:84 | 0..100 | R          | MSFS VAR |        |
|                             |                        |        |            |          |        |
| Glareshield LCD Lights      | LIGHT POTENTIOMETER:87 | 0..100 | R          | MSFS VAR |        |
|                             |                        |        |            |          |        |
| Table Light Capt.           | LIGHT POTENTIOMETER:10 | 0..100 | R          | MSFS VAR |        |
|                             |                        |        |            |          |        |
| Table Light F.O.            | LIGHT POTENTIOMETER:11 | 0..100 | R          | MSFS VAR |        |

### EFIS Control Panel

Flight Deck: [EFIS Control Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/glareshield/efis.md)

| Function           | API Usage                               | Values           | Read/Write | Type             | Remark                                                        |
|:-------------------|:----------------------------------------|:-----------------|:-----------|:-----------------|:--------------------------------------------------------------|
| Baro Display       | KOHLSMAN SETTING MB:1                   | 948-1084 (hPa)   | R          | MSFS VAR         |                                                               |
|                    | KOHLSMAN SETTING HG:1                   | 27.99-32.01 (Hg) | R          | MSFS VAR         |                                                               |
|                    |                                         |                  |            |                  |                                                               |
| Baro knob          | KOHLSMAN_INC                            | -                | -          | SIMCONNECT EVENT |                                                               |
|                    | KOHLSMAN_DEC                            | -                | -          | SIMCONNECT EVENT |                                                               |
|                    | XMLVAR_Baro1_Mode                       | 0..2             | R/W        | Custom LVAR      | 0=QFE, 1=QNH, 2=STD                                           |
|                    |                                         |                  |            |                  |                                                               |
| inHG / hPa         | XMLVAR_Baro_Selector_HPA_1              | 0..1             | R/W        | Custom LVAR      | 0=Hg, 1=hPa                                                   |
|                    |                                         |                  |            |                  |                                                               |
| LS                 | A380X_EFIS_{SIDE}_LS_BUTTON_IS_ON       | 0..1             | R/W        | Custom LVAR      |                                                               |
|                    |                                         |                  |            |                  |                                                               |
| VV                 | A380X_EFIS_{SIDE}_VV_BUTTON_IS_ON       | 0..1             | R/W        | Custom LVAR      |                                                               |
|                    |                                         |                  |            |                  |                                                               |
| ND MODE            | A32NX_EFIS_{SIDE}_ND_MODE               | 0..4             | R          | Custom LVAR      | 0=ROSE ILS, 1=ROSE VOR, 2=ROSE NAV. 3=ARC, 4=PLAN             |
|                    |                                         |                  |            |                  |                                                               |
| ND RANGE           | A32NX_EFIS_{SIDE}_ND_RANGE              | 0..7             | R/W        | Custom LVAR      | 0=ZOOM, 1=10, ..., 7=640                                      |
|                    |                                         |                  |            |                  |                                                               |
| OANS RANGE         | A32NX_EFIS_{SIDE}_OANS_RANGE            | 0..4             | R/W        | Custom LVAR      | 0=MAX, ..., 4=MIN; ND RANGE must be 0 to turn on OANS display |
|                    |                                         |                  |            |                  |                                                               |
| ND DATA Display pb | A380X_EFIS_{SIDE}_CSTR_BUTTON_IS_ON     | 0..1             | R/W        | Custom LVAR      |                                                               |
|                    | A380X_EFIS_{SIDE}_WPT_BUTTON_IS_ON      | 0..1             | R/W        | Custom LVAR      |                                                               |
|                    | A380X_EFIS_{SIDE}_VORD_BUTTON_IS_ON     | 0..1             | R/W        | Custom LVAR      |                                                               |
|                    | A380X_EFIS_{SIDE}_NDB_BUTTON_IS_ON      | 0..1             | R/W        | Custom LVAR      |                                                               |
|                    | A380X_EFIS_{SIDE}_ARPT_BUTTON_IS_ON     | 0..1             | R/W        | Custom LVAR      |                                                               |
|                    | A380X_EFIS_{SIDE}_NAVAID_1_BUTTON_IS_ON | 0..2             | R/W        | Custom LVAR      | 0=OFF, 1=ADF, 2=VOR1                                          |
|                    | A380X_EFIS_{SIDE}_ACTIVE_OVERLAY        | 0..1             | R/W        | Custom LVAR      | 0=WX/TERR OFF, 1=WX ON, 2=TERR ON                             |
|                    | A380X_EFIS_{SIDE}_TRAF_BUTTON_IS_ON     | 0..1             | R/W        | Custom LVAR      |                                                               |
|                    | A380X_EFIS_{SIDE}_NAVAID_2_BUTTON_IS_ON | 0..2             | R/W        | Custom LVAR      | 0=OFF, 1=ADF, 2=VOR2                                          |

### FCU Panel

Flight Deck: [FCU Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/glareshield/afs.md)

| Function          | API Usage                           | Values       | Read/Write | Type             | Remark                                                                   |
|:------------------|:------------------------------------|:-------------|:-----------|:-----------------|:-------------------------------------------------------------------------|
| SPD knob          | A32NX_AUTOPILOT_SPEED_SELECTED      | 0..399       | R          | Custom LVAR      |                                                                          |
|                   | A32NX.FCU_SPD_INC                   | -            | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_SPD_DEC                   | -            | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_SPD_SET                   | 0..399       | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_SPD_PUSH                  | -            | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_SPD_PULL                  | -            | -          | Custom EVENT     |                                                                          |
|                   | AP_AIRSPEED_ON                      | -            | -          | SIMCONNECT EVENT | Push                                                                     |
|                   | AP_AIRSPEED_OFF                     | -            | -          | SIMCONNECT EVENT | Pull                                                                     |
|                   | AP_SPD_VAR_INC                      | -            | -          | SIMCONNECT EVENT |                                                                          |
|                   | AP_SPD_VAR_DEC                      | -            | -          | SIMCONNECT EVENT |                                                                          |
|                   | AP_MACH_VAR_INC                     | -            | -          | SIMCONNECT EVENT |                                                                          |
|                   | AP_MACH_VAR_DEC                     | -            | -          | SIMCONNECT EVENT |                                                                          |
|                   |                                     |              |            |                  |                                                                          |
| HDG knob          | A32NX_AUTOPILOT_HEADING_SELECTED    | 0..359       | R          | Custom LVAR      |                                                                          |
|                   | A32NX.FCU_HDG_INC                   | -            | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_HDG_DEC                   | -            | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_HDG_SET                   | 0..359       | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_HDG_PUSH                  | -            | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_HDG_PULL                  | -            | -          | Custom EVENT     |                                                                          |
|                   | AP_HDG_HOLD_ON                      | -            | -          | SIMCONNECT EVENT | Push                                                                     |
|                   | AP_HDG_HOLD_OFF                     | -            | -          | SIMCONNECT EVENT | Pull                                                                     |
|                   | HEADING_BUG_INC                     | -            | -          | SIMCONNECT EVENT |                                                                          |
|                   | HEADING_BUG_DEC                     | -            | -          | SIMCONNECT EVENT |                                                                          |
|                   |                                     |              |            |                  |                                                                          |
| LOC               | A32NX_FCU_LOC_MODE_ACTIVE           | 0..1         | R          | Custom LVAR      |                                                                          |
|                   | A32NX.FCU_LOC_PUSH                  | -            | -          | Custom EVENT     |                                                                          |
|                   | AP_LOC_HOLD                         | -            | -          | SIMCONNECT EVENT |                                                                          |
|                   |                                     |              |            |                  |                                                                          |
| ALT knob          | AUTOPILOT ALTITUDE LOCK VAR:3       | 100..49000   |            | MSFS VAR         |                                                                          |
|                   | A32NX.FCU_ALT_INC                   | 0..100..1000 | R          | Custom EVENT     | 0=Use FCU Setting, 100=100, 1000=1000                                    |
|                   | A32NX.FCU_ALT_DEC                   | 0..100..1000 | R          | Custom EVENT     | 0=Use FCU Setting, 100=100, 1000=1000                                    |
|                   | A32NX.FCU_ALT_SET                   | 100..49000   | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_ALT_PUSH                  | -            | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_ALT_PULL                  | -            | -          | Custom EVENT     |                                                                          |
|                   | AP_ALT_HOLD_ON                      | -            | -          | SIMCONNECT EVENT | Push                                                                     |
|                   | AP_ALT_HOLD_OFF                     | -            | -          | SIMCONNECT EVENT | Pull                                                                     |
|                   | AP_ALT_VAR_INC                      | -            | -          | SIMCONNECT EVENT |                                                                          |
|                   | AP_ALT_VAR_DEC                      | -            | -          | SIMCONNECT EVENT |                                                                          |
|                   |                                     |              |            |                  |                                                                          |
| ALT INC 100-1000  | A32NX.FCU_ALT_INCREMENT_TOGGLE      | -            | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_ALT_INCREMENT_SET         | 100..1000    | -          | Custom EVENT     |                                                                          |
|                   | XMLVAR_AUTOPILOT_ALTITUDE_INCREMENT | 100..1000    | R          | Custom LVAR      |                                                                          |
|                   | AP_ALT_HOLD                         | -            | -          | SIMCONNECT EVENT | Repurposed event as Simconnect has no standard event for this otherwise. |
|                   |                                     |              |            |                  |                                                                          |
| ALT               | N/A                                 |              |            |                  | Not yet implemented                                                      |
|                   |                                     |              |            |                  |                                                                          |
| V/S FPA knob      | A32NX_AUTOPILOT_VS_SELECTED         | -6000..6000  | R          | Custom LVAR      |                                                                          |
|                   | A32NX.FCU_VS_INC                    | -            | -          | Custom LVAR      | FPA: -9.9..9.9                                                           |
|                   | A32NX.FCU_VS_DEC                    | -            | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_VS_SET                    | -6000..6000  | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_VS_PUSH                   | -            | -          | Custom EVENT     | FPA: -9.9..9.9                                                           |
|                   | A32NX.FCU_VS_PULL                   | -            | -          | Custom EVENT     |                                                                          |
|                   | AP_VS_HOLD_ON                       | -            | -          | SIMCONNECT EVENT | Push                                                                     |
|                   | AP_VS_HOLD_OFF                      | -            | -          | SIMCONNECT EVENT | Pull                                                                     |
|                   | AP_VS_VAR_INC                       | -            | -          | SIMCONNECT EVENT |                                                                          |
|                   | AP_VS_VAR_DEC                       | -            | -          | SIMCONNECT EVENT |                                                                          |
|                   |                                     |              |            |                  |                                                                          |
| APPR              | A32NX_FCU_APPR_MODE_ACTIVE          | 0..1         | R          | Custom LVAR      |                                                                          |
|                   | A32NX.FCU_APPR_PUSH                 | -            | -          | Custom EVENT     |                                                                          |
|                   | AP_APR_HOLD                         | -            | -          | SIMCONNECT EVENT |                                                                          |
|                   |                                     |              |            |                  |                                                                          |
| FD                | AUTOPILOT FLIGHT DIRECTOR ACTIVE    | 0..1         | R          | SIMCONNECT VAR   |                                                                          |
|                   | TOGGLE_FLIGHT_DIRECTOR              | -            | -          | SIMCONNECT EVENT |                                                                          |
|                   |                                     |              |            |                  |                                                                          |
| AP 1 + 2          | A32NX_AUTOPILOT_1_ACTIVE            | 0..1         | R          | Custom LVAR      |                                                                          |
|                   | A32NX_AUTOPILOT_2_ACTIVE            | 0..1         | R          | Custom LVAR      |                                                                          |
|                   | A32NX.FCU_AP_1_PUSH                 | -            | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_AP_2_PUSH                 | -            | -          | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_AP_DISCONNECT_PUSH        | -            |            | Custom EVENT     |                                                                          |
|                   | AP_MASTER                           | 1            | -          | SIMCONNECT EVENT | Toggles                                                                  |
|                   | AUTOPILOT_ON                        | -            | -          | SIMCONNECT EVENT | 1st call AP1, 2nd call AP2                                               |
|                   | AUTOPILOT_OFF                       | -            | -          | SIMCONNECT EVENT | Turns off any AP                                                         |
|                   | AUTOPILOT_DISENGAGE_SET             | -            | -          | SIMCONNECT EVENT | 1 for OFF                                                                |
|                   | AUTOPILOT_DISENGAGE_TOGGLE          | -            | -          | SIMCONNECT EVENT | Toggles                                                                  |
|                   |                                     |              | -          |                  |                                                                          |
| A/THR             | A32NX_AUTOTHRUST_STATUS             | 0..2         | R          | Custom LVAR      | 0=Disengaged, 1=Armed, 2=Active                                          |
|                   | A32NX.FCU_ATHR_PUSH                 | -            |            | Custom EVENT     |                                                                          |
|                   | A32NX.FCU_ATHR_DISCONNECT_PUSH      | -            | -          | Custom EVENT     |                                                                          |
|                   | AUTO_THROTTLE_ARM                   | -            | -          | SIMCONNECT EVENT |                                                                          |
|                   | AUTO_THROTTLE_DISCONNECT            | -            | -          | SIMCONNECT EVENT |                                                                          |
|                   | AUTO_THROTTLE_TO_GA                 | -            | -          | SIMCONNECT EVENT |                                                                          |
|                   |                                     |              |            |                  |                                                                          |
| SPD/MACH          | AUTOPILOT MANAGED SPEED IN MACH     | 0..1         | R          | MSFS VAR         |                                                                          |
|                   | A32NX.FCU_SPD_MACH_TOGGLE_PUSH      | -            | -          | Custom EVENT     |                                                                          |
|                   | AP_MACH_HOLD                        | -            | -          | SIMCONNECT EVENT | Repurposed event as Simconnect has no standard event for this otherwise. |
|                   |                                     |              |            |                  |                                                                          |
| HDG-TRK / V/S-FPA | A32NX_TRK_FPA_MODE_ACTIVE           | 0..1         | R          | Custom LVAR      |                                                                          |
|                   | A32NX.FCU_TRK_FPA_TOGGLE_PUSH       | -            | -          | Custom EVENT     |                                                                          |
|                   | AP_VS_HOLD                          | -            | -          | SIMCONNECT EVENT | Repurposed event as Simconnect has no standard event for this otherwise. |
|                   |                                     |              |            |                  |                                                                          |
| TRUE MAG pb       | H:A320_Neo_FCU_TRUEMAG_PUSH         | -            | -          | H: Event         |                                                                          |
|                   |                                     |              |            |                  |                                                                          |
| METER pb          | A32NX_METRIC_ALT_TOGGLE             | 0..1         | R/W        | Custom LVAR      |                                                                          |

### Glareshield Side Panel

Flight Deck: [Glareshield Side Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/glareshield/glare-side.md)

| Function            | API Usage                         | Values | Read/Write | Type                     | Remark                 |
|:--------------------|:----------------------------------|:-------|:-----------|:-------------------------|:-----------------------|
| MASTER CAUTION      | PUSH_AUTOPILOT_MASTERCAUT_{SIDE}  | 0..1   | R/W        | Custom LVAR              | 0=not pushed, 1=pushed |
|                     |                                   |        |            |                          |                        |
| MASTER WARNING      | PUSH_AUTOPILOT_MASTERAWARN_{SIDE} | 0..1   | R/W        | Custom LVAR              | 0=not pushed, 1=pushed |
|                     |                                   |        |            |                          |                        |
| CHRONO              | H:A32NX_EFIS_{SIDE}_CHRONO_PUSHED | -      | -          | HTML Event (aka H Event) |                        |
|                     |                                   |        |            |                          |                        |
| SIDE STICK PRIORITY | N/A                               |        |            |                          |                        |
|                     |                                   |        |            |                          |                        |
| AUTOLAND WARNING    | A32NX_AUTOPILOT_AUTOLAND_WARNING  | 0..1   | R          | Custom LVAR              |                        |
|                     |                                   |        |            |                          |                        |
| ATC MSG             | N/A                               |        |            |                          |                        |

## Instrument Panel

### Switching Panel

Flight Deck: [Switching Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/main-panel/switching.md)

| Function    | API Usage                        | Values | Read/Write | Type        | Remark                |
|:------------|:---------------------------------|:-------|:-----------|:------------|:----------------------|
| ATT HDG     | A32NX_ATT_HDG_SWITCHING_KNOB     | 0..2   | R/W        | Custom LVAR | 0=CAPT, 1=NORM, 2=F/O |
| AIR DATA    | A32NX_AIR_DATA_SWITCHING_KNOB    | 0..2   | R/W        | Custom LVAR | 0=CAPT, 1=NORM, 2=F/O |
| EIS DMC     | A32NX_EIS_DMC_SWITCHING_KNOB     | 0..2   | R/W        | Custom LVAR | 0=CAPT, 1=NORM, 2=F/O |

### ISIS

Flight Deck: [ISIS Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/main-panel/isis.md)

| Function | API Usage                        | Values | Read/Write | Type     | Remark                                      |
|:---------|:---------------------------------|:-------|:-----------|:---------|:--------------------------------------------|
| PLUS pb  | H:A32NX_ISIS_PLUS_PRESSED        | -      | -          | H: EVENT | Temporary until ISIS is refactored to A380X |
|          | H:A32NX_ISIS_PLUS_RELEASED       | -      | -          | H: EVENT | Temporary until ISIS is refactored to A380X |
|          |                                  |        |            |          |                                             |
| MINUS pb | H:A32NX_ISIS_MINUS_PRESSED       | -      | -          | H: EVENT | Temporary until ISIS is refactored to A380X |
|          | H:A32NX_ISIS_MINUS_RELEASED      | -      | -          | H: EVENT | Temporary until ISIS is refactored to A380X |
|          |                                  |        |            |          |                                             |
| MODE pb  | H:A32NX_ISIS_BUGS_PRESSED        | -      | -          | H: EVENT | Temporary until ISIS is refactored to A380X |
|          | H:A32NX_ISIS_BUGS_RELEASED       | -      | -          |          |                                             |
|          |                                  |        |            |          |                                             |
| LS pb    | H:A32NX_ISIS_LS_PRESSED          | -      | -          | H: EVENT | Temporary until ISIS is refactored to A380X |
|          | H:A32NX_ISIS_LS_RELEASED         | -      | -          |          |                                             |
|          |                                  |        |            |          |                                             |
| MENU pb  | H:A32NX_ISIS_RST_PRESSED         | -      | -          | H: EVENT | Temporary until ISIS is refactored to A380X |
|          | H:A32NX_ISIS_RST_RELEASED        | -      | -          | H: EVENT | Temporary until ISIS is refactored to A380X |
|          |                                  |        |            |          |                                             |
| KNOB     | H:A32NX_ISIS_KNOB_PRESSED        | -      | -          | H: EVENT | Temporary until ISIS is refactored to A380X |
|          | H:A32NX_ISIS_KNOB_RELEASED       | -      | -          | H: EVENT | Temporary until ISIS is refactored to A380X |
|          | H:A32NX_ISIS_KNOB_ANTI_CLOCKWISE | -      | -          | H: EVENT | Temporary until ISIS is refactored to A380X |
|          | H:A32NX_ISIS_KNOB_CLOCKWISE      | -      | -          | H: EVENT | Temporary until ISIS is refactored to A380X |

### Landing Gear Gravity Panel

Flight Deck: [Gravity Geary Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/main-panel/gravity-gear.md)

| Function            | API Usage                          | Values | Read/Write | Type        | Remark                 |
|:--------------------|:-----------------------------------|:-------|:-----------|:------------|:-----------------------|
| MASTER SWITCH GUARD | A32NX_LG_GRVTY_MASTER_SWITCH_GUARD | 0..1   | R          | Custom LVAR |                        |
| SWITCH GUARD LEFT   | A32NX_LG_GRVTY_SWITCH_GUARD_1      | 0..1   | R/W        | Custom LVAR |                        |
| SWITCH GUARD RIGHT  | A32NX_LG_GRVTY_SWITCH_GUARD_2      | 0..1   | R/W        | Custom LVAR |                        |
| MASTER SWITCH POS   | A32NX_LG_GRVTY_SWITCH_POS          | 0..2   | R/W        | Custom LVAR | 0=RESET, 1=OFF, 2=DOWN |

### Display Unit Control Panel

Flight Deck: [Display Unit Control Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/main-panel/efis-reconf.md)

To control the lighting knobs, the following API usage is available:

SIMCONNECT EVENT: `SIMCONNECT:LIGHT_POTENTIOMETER_SET`

| Function            | API Usage              | Values  | Read/Write | Type     | Remark |
|:--------------------|:-----------------------|:--------|:-----------|:---------|:-------|
| PFD Brt Cpt.        | LIGHT POTENTIOMETER:88 | 0..100  | R          | MSFS VAR |        |
| PFD/ND Cpt.         | N/A                    |         |            |          |        |
| ND Brt Cpt.         | LIGHT POTENTIOMETER:89 | 0..100  | R          | MSFS VAR |        |
| WX/Terrain Brt Cpt. | LIGHT POTENTIOMETER:94 | 0..100  | R          | MSFS VAR |        |
| OIT Brt. Cpt.       | N/A                    |         |            |          |        |
| RECONF Cpt.         | N/A                    |         |            |          |        |
| MFD Brt Cpt.        | LIGHT POTENTIOMETER:98 | 0..100  | R          | MSFS VAR |        |
|                     |                        |         |            |          |        |
| PFD Brt F.O.        | LIGHT POTENTIOMETER:90 | 0..100  | R          | MSFS VAR |        |
| PFD/ND F.O.         | N/A                    |         |            |          |        |
| ND Brt F.O.         | LIGHT POTENTIOMETER:91 | 0..100  | R          | MSFS VAR |        |
| WX/Terrain Brt F.O. | LIGHT POTENTIOMETER:95 | 0..100  | R          | MSFS VAR |        |
| OIT Brt. F.O.       | N/A                    |         |            |          |        |
| RECONF F.O.         | N/A                    |         |            |          |        |
| MFD Brt F.O.        | LIGHT POTENTIOMETER:99 | 0..100  | R          | MSFS VAR |        |

### Autobrake, Gear Lever and Gear Annunciation

Flight Deck: [Center Right Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/main-panel/center-right.md)

| Function              | API Usage                             | Values  | Read/Write | Type             | Remark                                                              |
|:----------------------|:--------------------------------------|:--------|:-----------|:-----------------|:--------------------------------------------------------------------|
| Gear lever            | GEAR_UP                               | -       | -          | SIMCONNECT EVENT |                                                                     |
|                       | GEAR_DOWN                             | -       | -          | SIMCONNECT EVENT |                                                                     |
|                       | GEAR HANDLE POSITION                  | 0..1    | R/W        | SIMCONNECT VAR   |                                                                     |
|                       | A32NX_GEAR_HANDLE_POSITION            | 0.0-1.0 | R/W        | Custom LVAR      |                                                                     |
|                       |                                       |         |            |                  |                                                                     |
| LDG GEAR Annunciators | GEAR LEFT POSITION                    | 0..100  | R          | SIMCONNECT VAR   |                                                                     |
|                       | GEAR CENTER POSITION                  | 0..100  | R          | SIMCONNECT VAR   |                                                                     |
|                       | GEAR RIGHT POSITION                   | 0..100  | R          | SIMCONNECT VAR   |                                                                     |
|                       |                                       |         |            |                  |                                                                     |
| REJECTED T.O          | A32NX_OVHD_AUTOBRK_RTO_ARM_IS_PRESSED | 0..1    | R/W        | Custom LVAR      |                                                                     |
|                       | A32NX_AUTOBRAKES_RTO_ARMED            | 0..1    | R          | Custom LVAR      |                                                                     |
|                       |                                       |         |            |                  |                                                                     |
| AUTO BRK KNOB         | A32NX_AUTOBRAKES_SELECTED_MODE        | 0..5    | R/W        | Custom LVAR      | 0=DIS, 1=BTV, 2=LO, 3=L2, 4=L3, 5=HI                                |
|                       | A32NX_AUTOBRAKES_ARMED_MODE           | 0..6    | R          | Custom LVAR      | 0=DIS, 1=BTV, 2=LO, 3=L2, 4=L3, 5=HI, 6=RTO                         |
|                       | A32NX_AUTOBRAKES_DISARM_KNOB_REQ      | 0..1    | R          | Custom LVAR      | true(1) when autobrake knob solenoid resets knob position to DISARM |
|                       |                                       |         |            |                  |                                                                     |
| A/SKID & N/W STRG     | ANTISKID_BRAKES_TOGGLE                | -       | -          | SIMCONNECT EVENT |                                                                     |
|                       | ANTISKID BRAKES ACTIVE                | 0..1    | R/W        | SIMCONNECT VAR   |                                                                     |

### Clock

Flight Deck: [Chrono Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/main-panel/center-right.md)

| Function            | API Usage                  | Values | Read/Write | Type        | Remark                       |
|:--------------------|:---------------------------|:-------|:-----------|:------------|:-----------------------------|
| ELAPSED TIME SWITCH | A32NX_CHRONO_ET_SWITCH_POS | 0..2   | R/W        | Custom LVAR | 0 = RUN, 1 = STOP, 2 = RESET |
| RST pb              | H:A32NX_CHRONO_RST         | -      | -          | H: Event    |                              |
| CHR pb              | H:A32NX_CHRONO_TOGGLE      | -      | -          | H: Event    |                              |
| DATE pb             | H:A32NX_CHRONO_DATE        | -      | -          | H: Event    |                              |

## Pedestal

### Lighting  Panel

Flight Deck: [Lighting Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/pedestal/cockpit-lighting.md)

To control the lighting knobs, the following API usage is available:

SIMCONNECT EVENT: `SIMCONNECT:LIGHT_POTENTIOMETER_SET`

| Function          | API Usage              | Values | Read/Write | Type     | Remark      |
|:------------------|:-----------------------|:-------|:-----------|:---------|:------------|
| INTEG LT          | LIGHT POTENTIOMETER:85 | 0..100 | R          | MSFS VAR |             |
| MAIN PNL FLOOD LT | LIGHT POTENTIOMETER:83 | 0..100 | R          | MSFS VAR |             |
| PEDESTAL FLOOD LT | LIGHT POTENTIOMETER:76 | 0..100 | R          | MSFS VAR |             |
| AMBIENT LT        | LIGHT POTENTIOMETER:7  | 0..100 | R          | MSFS VAR | aka DOME Lt |

### KCCU Panel

Flight Deck: [KCCU Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/pedestal/kccu.md)

| Function  | API Usage                    | Values | Read/Write | Type        |   | Remark         |
|:----------|:-----------------------------|:-------|:-----------|:------------|:--|:---------------|
| KEY Press | H:A32NX_KCCU_{SIDE}_{KEY}    | -      | -          | H: EVENT    |   | See list below |
|           |                              |        |            |             |   |                |
| KBD sw    | A32NX_KCCU_{SIDE}_KBD_ON_OFF | 0..1   | R/W        | Custom LVAR |   |                |
| CCD sw    | A32NX_KCCU_{SIDE}_CCD_ON_OFF | 0..1   | R/W        | Custom LVAR |   |                |

??? note "KCCU Keys"
    - KBD
    - CCD
    - 0..9
    - DOT
    - PLUSMINUS
    - A..Z
    - ESC
    - UP
    - RIGHT
    - DOWN
    - SIDE
    - DIR
    - PERF
    - INIT
    - NAVAID
    - MAILBOX
    - FPLN
    - DEST
    - SECINDEX
    - SURV
    - ATCCOM
    - ND
    - SLASH
    - ESC2
    - KBD
    - REWIND
    - FORWARD
    - ENT
    - BACKSPACE
    - SP
    - CLRINFO

### Thrust Lever 

Flight Deck: [Thrust Lever Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/pedestal/throttle.md)

| Function              | API Usage                   | Values        | Read/Write | Type             | Remark  |
|:----------------------|:----------------------------|:--------------|:-----------|:-----------------|:--------|
| Throttle {NUM} Axis   | THROTTLE{NUM}_AXIS_SET_EX1  | -16383..16384 | -          | MSFS EVENT       |         |
|                       |                             |               |            |                  |         |
| AUTO THRUST DISENGAGE | AUTO_THROTTLE_ARM           | -             | -          | SIMCONNECT EVENT | Toggles |
|                       | A32NX_AUTOTHRUST_DISCONNECT | 0..1          | R          | Custom LVAR      |         |

### RMP

Flight Deck: [RMP Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/pedestal/rmp.md)

The RMP panel consequently uses InputEvents (aka B: Events) to control the RMPs.

See the [RMP API developer documentation](https://github.com/flybywiresim/aircraft/blob/master/fbw-a380x/docs/a380x-input-events.md#23---communications){target=_blank}.

### ENG Panel

Flight Deck: [ENG Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/pedestal/engine.md)

| Function       | API Usage                      | Values | Read/Write | Type       |   | Remark                 |
|:---------------|:-------------------------------|:-------|:-----------|:-----------|:--|:-----------------------|
| ENG 1+2 MASTER | FUELSYSTEM_VALVE_OPEN          | -      | -          | MSFS EVENT |   | Activates the switch   |
|                | FUELSYSTEM_VALVE_CLOSE         | -      | -          | MSFS EVENT |   | Deactivates the switch |
|                | FUELSYSTEM VALVE SWITCH:1      | 0..1   | R          | MSFS VAR   |   |                        |
|                | FUELSYSTEM VALVE SWITCH:2      | 0..1   | R          | MSFS VAR   |   |                        |

### ECAM Control Panel

Flight Deck: [ECAM Control Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/pedestal/ecam-cp.md)

!!! note "The below LVARs are momentary buttons - they need to be reset to 0 by the API user." 

| Function         | API Usage                        | Values | Read/Write | Type        | Remark     |
|:-----------------|:---------------------------------|:-------|:-----------|:------------|:-----------|
| ECAM SD Page pb  | A32NX_ECAM_SD_CURRENT_PAGE_INDEX | -1..12 | R/W        | Custom LVAR | See below. |
|                  |                                  |        |            |             |            |
| T.O. CONFIG pb   | A32NX_BTN_TOCONFIG               | 0..1   | R/W        | Custom LVAR |            |
| C/L  pb          | A32NX_BTN_CL                     | 0..1   | R/W        | Custom LVAR |            |
| CHECK L pb       | A32NX_BTN_CHECK_LH               | 0..1   | R/W        | Custom LVAR |            |
| CHECK R pb       | A32NX_BTN_CHECK_RH               | 0..1   | R/W        | Custom LVAR |            |
| ABNPROC  pb      | A32NX_BTN_ABNPROC                | 0..1   | R/W        | Custom LVAR |            |
| EMERCANC  pb     | A32NX_BTN_EMERCANC               | 0..1   | R/W        | Custom LVAR |            |
|                  |                                  |        |            |             |            |
| UP pb            | A32NX_BTN_UP                     | 0..1   | R/W        | Custom LVAR |            |
| DOWN pb          | A32NX_BTN_DOWN                   | 0..1   | R/W        | Custom LVAR |            |
|                  |                                  |        |            |             |            |
| Left CLR  button | A32NX_BTN_CLR                    | 0..1   | R/W        | Custom LVAR |            |
| RCL button       | A32NX_BTN_RCL                    | 0..1   | R/W        | Custom LVAR |            |
| MORE button      | A32NX_BTN_MORE                   | 0..1   | R/W        | Custom LVAR |            |
| Right CLR button | A32NX_BTN_CLR2                   | 0..1   | R/W        | Custom LVAR |            |
|                  |                                  |        |            |             |            |
| EWD DU BRT       | LIGHT POTENTIOMETER:92           | 0..100 | R          | MSFS VAR    |            |
| SD DU BRT        | LIGHT POTENTIOMETER:93           | 0..100 | R          | MSFS VAR    |            |

A32NX_ECAM_SD_CURRENT_PAGE_INDEX:

<style>
.md-typeset li {
    line-height: 1.0
}
</style>

- None = -1,
- Eng = 0,
- Apu = 1,
- Bleed = 2,
- Cond = 3,
- Press = 4,
- Door = 5,
- ElecAc = 6,
- ElecDc = 7,
- Fuel = 8,
- Wheel = 9,
- Hyd = 10,
- Fctl = 11,
- Cb = 12,
- Crz = 13,
- Status = 14,
- Video = 15,

### Speed Brake

Flight Deck: [Speed Brake Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/pedestal/speedbrake.md)

| Function         | API Usage                      | Values   | Read/Write | Type             | Remark                           |
|:-----------------|:-------------------------------|:---------|:-----------|:-----------------|:---------------------------------|
| SPEED BRAKE AXIS | SPOILER SET                    | 0..16384 | -          | SIMCONNECT EVENT |                                  |
|                  | A32NX_SPOILERS_HANDLE_POSITION | 0.0..1.0 | R          | Custom LVAR      | (add. SIMCONNECT VARS available) |
|                  |                                |          |            |                  |                                  |
| GND SPOILER ARM  | SPOILERS_ARM_TOGGLE            | -        | -          | SIMCONNECT EVENT |                                  |
|                  | SPOILERS ARMED                 | 0..1     | R/W        | SIMCONNECT VAR   |                                  |
|                  | A32NX_SPOILERS_ARMED           | 0..1     | R          | Custom LVAR      |                                  |

### Surveillance Panel

### Flaps

Flight Deck: [Speed Brake Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/pedestal/flaps.md)

| Function   | API Usage                  | Values   | Read/Write | Type             | Remark                        |
|:-----------|:---------------------------|:---------|:-----------|:-----------------|:------------------------------|
| Flaps Axis | FLAPS_SET                  | 0..16384 | -          | SIMCONNECT EVENT | 0=FLAPS UP, 16384=FLAPS FULL  |
|            | FLAPS_UP                   | -        | -          | SIMCONNECT EVENT |                               |
|            | FLAPS_1                    | -        | -          | SIMCONNECT EVENT |                               |
|            | FLAPS_2                    | -        | -          | SIMCONNECT EVENT |                               |
|            | FLAPS_3                    | -        | -          | SIMCONNECT EVENT |                               |
|            | FLAPS_DOWN                 | -        | -          | SIMCONNECT EVENT |                               |
|            | FLAPS_INCR                 | -        | -          | SIMCONNECT EVENT |                               |
|            | FLAPS_DECR                 | -        | -          | SIMCONNECT EVENT |                               |
|            |                            |          |            |                  |                               |
|            | A32NX_FLAPS_HANDLE_INDEX   | 0..4     | R          | Custom LVAR      | 0=UP, 4=FULL                  |
|            | A32NX_FLAPS_HANDLE_PERCENT | 0.0..1.0 | R          | Custom LVAR      | 0.0=UP, 1.0=FULL (0.25 steps) |
|            |                            |          |            |                  |                               |
|            | FLAPS HANDLE INDEX         | 0..5     | R          | SIMCONNECT VAR   | 0=UP, 5=FULL, 1 is not used.  |
|            | FLAPS HANDLE PERCENT       | 0.0..1.0 | R          | SIMCONNECT VAR   | 0.0=UP, 1.0=FULL (0.2 steps)  |

### Parking Brake

Flight Deck: [Parking Brake Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/pedestal/parking-brake.md)

| Function      | API Usage                  | Values | Read/Write | Type        | Remark |
|:--------------|:---------------------------|:-------|:-----------|:------------|:-------|
| PARKING BRAKE | A32NX_PARK_BRAKE_LEVER_POS | 0..1   | R/W        | Custom LVAR |        |

### Rudder Trim

Flight Deck: [Rudder Trim Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/pedestal/rudder-trim.md)

| Function | API Usage         | Values      | Read/Write | Type             | Remark                                                                            |
|:---------|:------------------|:------------|:-----------|:-----------------|:----------------------------------------------------------------------------------|
| Display  | RUDDER TRIM PCT   | -1.0..1.0   | R          | SIMCONNECT VAR   | -1.0=20° left, 1.0=20° right                                                      |
|          | RUDDER TRIM       | -0.35..0.35 | R          | SIMCONNECT VAR   | Radians: 0.3490×180°/π = 19.99°                                                   |
|          |                   |             |            |                  |                                                                                   |
| RESET    | RUDDER_TRIM_RESET | -           | .          | SIMCONNECT EVENT |                                                                                   |
|          |                   |             |            |                  |                                                                                   |
| RUD TRIM | XMLVAR_RUDDERTRIM | 0 .. 2      | R/W        | Custom LVAR      | ~~Knob jumps back. Needs to be set repeatably until the target value is reached~~ |

### Cockpit Door

Flight Deck: [Cockpit Door Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/pedestal/cockpit-door.md)

| Function     | API Usage                 | Values | Read/Write | Type        | Remark |
|:-------------|:--------------------------|:-------|:-----------|:------------|:-------|
| COCKPIT DOOR | A32NX_COCKPIT_DOOR_LOCKED | 0..1   | R/W        | Custom LVAR |        |
|              |                           |        |            |             |        |
| VIDEO        | PUSH_DOORPANEL_VIDEO      | 0..1   | R/W        | Custom LVAR |        |



### WX Radar

Flight Deck: [WX Radar Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/pedestal/radar.md)

| Function   | API Usage                       | Values | Read/Write | Type        | Remark                      |
|:-----------|:--------------------------------|:-------|:-----------|:------------|:----------------------------|
| SYS        | XMLVAR_A320_WEATHERRADAR_SYS    | 0..2   | R/W        | Custom LVAR | 0=1, 1=OFF, 2=2             |
|            |                                 |        |            |             |                             |
| PWS        | A32NX_SWITCH_RADAR_PWS_POSITION | 0..1   | R/W        | Custom LVAR | 0=OFF, 1=AUTO               |
|            |                                 |        |            |             |                             |
| MODE       | XMLVAR_A320_WEATHERRADAR_MODE   | 0..3   | R/W        | Custom LVAR | 0=WX, 1=WX+T, 2=TURB, 3=MAP |
|            |                                 |        |            |             |                             |
| GAIN       | N/A                             |        |            |             |                             |
|            |                                 |        |            |             |                             |
| MULTISCANS | N/A                             |        |            |             |                             |
|            |                                 |        |            |             |                             |
| GCS        | N/A                             |        |            |             |                             |
|            |                                 |        |            |             |                             |
| TILT       | N/A                             |        |            |             |                             |

### ATC-TCAS

Flight Deck: [ATC-TCAS Panel](../../../pilots-corner/a380x/a380x-briefing/flight-deck/pedestal/atc-tcas.md)

| Function     | API Usage                          | Values      | Read/Write | Type             | Remark                      |
|:-------------|:-----------------------------------|:------------|:-----------|:-----------------|:----------------------------|
| ATC MODE     | A32NX_TRANSPONDER_MODE             | 0..2        | R/W        | Custom LVAR      | 0=STBY, 1=AUTO, 2=ON        |
|              |                                    |             |            |                  |                             |
| ATC SYSTEM   | A32NX_TRANSPONDER_SYSTEM           | 0..1        | R/W        | Custom LVAR      | 0 = System 1, 1 = System 2  |
|              |                                    |             |            |                  |                             |
| ALT RPTG     | A32NX_SWITCH_ATC_ALT               | 0..1        | R/W        | Custom LVAR      | 0=OFF, 1=ON                 |
|              |                                    |             |            |                  |                             |
| SQUAWK       | TRANSPONDER CODE:1                 | 0000...7777 | R/W        | SIMCONNECT VAR   |                             |
|              |                                    |             |            |                  |                             |
| IDENT        | XPNDR_IDENT_ON                     | -           | -          | SIMCONNECT EVENT |                             |
|              |                                    |             |            |                  |                             |
| TCAS MODE    | A32NX_SWITCH_TCAS_TRAFFIC_POSITION | 0..3        | R/W        | Custom LVAR      | 0=THRT, 1=ALL, 2=ABV, 3=BLW |
|              |                                    |             |            |                  |                             |
| TCAS TRAFFIC | A32NX_SWITCH_TCAS_POSITION         | 0..2        | R/W        | Custom LVAR      | 0=STBY, 1=TA, 2=TA/RA       |



## Side Stick

| Function             | API Usage                 | Values        | Read/Write | Type             | Remark                  |
|:---------------------|:--------------------------|:--------------|:-----------|:-----------------|:------------------------|
| Aileron              | AILERON_SET               | -16383..16384 | -          | SIMCONNECT EVENT |                         |
|                      | AILERON POSITION          | -1.0..1.0     | R          | SIMCONNECT VAR   |                         |
|                      |                           |               |            |                  |                         |
| Elevator             | ELEVATOR_SET              | -16383..16384 | -          | SIMCONNECT EVENT |                         |
|                      | ELEVATOR POSITION         | -1.0..1.0     | R          | SIMCONNECT VAR   |                         |
|                      |                           |               |            |                  |                         |
| TAKE OVER pushbutton | A32NX_PRIORITY_TAKEOVER:1 | 0..1          | R          | Custom LVAR      | Causes AP disconnection |
|                      | A32NX_PRIORITY_TAKEOVER:2 | 0..1          | R          | Custom LVAR      | Causes AP disconnection |

## Tiller

See [Nose Wheel and Tiller Operation](../feature-guides/nw-tiller.md)

## Rudder Pedals

| Function | API Usage                      | Values        | Read/Write | Type             | Remark |
|:---------|:-------------------------------|:--------------|:-----------|:-----------------|:-------|
| Rudder   | RUDDER_SET                     | -16383..16384 | -          | SIMCONNECT EVENT |        |
|          | RUDDER POSITION                | -1.0..1.0     | R          | SIMCONNECT VAR   |        |
|          |                                |               |            |                  |        |
| Brakes   | A32NX_LEFT_BRAKE_PEDAL_INPUT   | 0..100        | R          | Custom LVAR      |        |
|          | A32NX_RIGHT_BRAKE_PEDAL_INPUT  | 1..100        | R          | Custom LVAR      |        |
|          | SIMCONNECT:AXIS_LEFT_BRAKE_SET | -16383..16384 | -          | SIMCONNECT EVENT |        |
|          | SIMCONNECT:AXIS_LEFT_BRAKE_SET | -16383..16384 | -          | SIMCONNECT EVENT |        |

## flyPad EFB

| Function                                     | API Usage                             | Values    | Read/Write | Type                     | Remark                                                                                 |
|:---------------------------------------------|:--------------------------------------|:----------|:-----------|:-------------------------|:---------------------------------------------------------------------------------------|
| Hardware Power Button                        | A32NX_EFB_POWER                       | -         | -          | HTML Event (aka H Event) | Toggles EFB Power                                                                      |
| EFB Brightness                               | A32NX_EFB_BRIGHTNESS                  | 0..100    | R/W        | Custom LVAR              | Overwrites automatic setting                                                           |
| Load Lighting Preset                         | A32NX_LOAD_LIGHTING_PRESET            | 1..8      | R/W        | Custom LVAR              | Aircraft must be powered. Will be reset to 0 after the preset has been loaded.         |
| Save Lighting Preset                         | A32NX_SAVE_LIGHTING_PRESET            | 1..8      | R/W        | Custom LVAR              | Aircraft must be powered. Will be reset to 0 after the preset has been saved.          |
| Load Aircraft Preset                         | A32NX_LOAD_AIRCRAFT_PRESET            | 1..5      | R/W        | Custom LVAR              | Will be reset to 0 after the preset has been loaded.                                   |
| Current Progress for Aircraft Preset Loading | A32NX_LOAD_AIRCRAFT_PRESET_PROGRESS   | 0.0..1.0  | R          | Custom LVAR              | Percent done of the Aircraft State to be loaded.                                       |
| Current Aircraft Preset Loading Step         | A32NX_LOAD_AIRCRAFT_PRESET_CURRENT_ID | 0..999    | R          | Custom LVAR              | ID of the current step.                                                                |

### Pushback API

| Function                 | API Usage                     | Values    | Read/Write | Type        | Remark                                                                                  |
|:-------------------------|:------------------------------|:----------|:-----------|:------------|:----------------------------------------------------------------------------------------|
| Pushback System          | A32NX_PUSHBACK_SYSTEM_ENABLED | 0..1      | R/W        | Custom LVAR | To turn off the Pushback System completely to not interfere with other pushback add-ons |
| Pushback Movement Factor | A32NX_PUSHBACK_SPD_FACTOR     | -1.0..1.0 | R/W        | Custom LVAR | Set the speed of the pushback tug in percent. Negative values are backwards movements.  |
| Pushback Heading Factor  | A32NX_PUSHBACK_HDG_FACTOR     | -1.0..1.0 | R/W        | Custom LVAR | Set the turning factor from max left (-1.0) to max right (1.0)                          |

??? tip "Pushback API HowTo"
    #### Pushback API HowTo
    Using the Pushback API is relatively easy, but you also might need some additional sim events/vars to make it work. 
    The following step-by-step description helps you to use buttons on a controller or a Stream Deck to control the 
    pushback.  

    * Set the Pushback System to enabled ==> set L:A32NX_PUSHBACK_SYSTEM_ENABLED to 1
    * Use the sim var `PUSHBACK STATE` to check if the pushback tug is connected to the aircraft
        - PUSHBACK STATE == 3 ==> Pushback tug is **not** connected
        - PUSHBACK STATE < 3 ==> Pushback tug is connected
        - Alternatively there is also the sim var `Pushback Attached` which can also be used.
    * Call the Pushback Tug via the SimConnect Event `K:TOGGLE_PUSHBACK`
    * Wait until the Pushback Tug is connected to the aircraft
        - Should be immediately and is independent of the actual visual pushback tug being attached to the aircraft 
        - This is a sim issue, as MSFS will not wait for the pushback tug model to be attached before setting the 
        corresponding sim vars
    * Set the Pushback Movement Factor via the LVAR `L:A32NX_PUSHBACK_SPD_FACTOR` to the desired value
    * Set the Pushback Heading Factor via the LVAR `L:A32NX_PUSHBACK_HDG_FACTOR` to the desired value
    * Set the Pushback Movement Factor via the LVAR `L:A32NX_PUSHBACK_SPD_FACTOR` to `0` to stop the pushback tug
    * To disconnect the pushback tug, call the SimConnect Event `K:TOGGLE_PUSHBACK` again

    #### Pushback API Example

    ![img.png](../assets/api-guide/pushback-api-example.png){loading=lazy}
    
    | Button                      | Pseudo Code                                                                 | Remark                    |
    |-----------------------------|-----------------------------------------------------------------------------|---------------------------|
    | PUSHBACK<br/>SYSTEM         | toggle `L:A32NX_PUSHBACK_SYSTEM_ENABLED`                                    | 0 or 1                    |
    | Forward                     | `L:A32NX_PUSHBACK_SPD_FACTOR` = oldvalue + 0.1                              | -1.0..1.0, 0 = not moving |
    | TUG                         | call `K:TOGGLE_PUSHBACK`                                                    |                           |
    | Left                        | `L:A32NX_PUSHBACK_HDG_FACTOR` = oldvalue - 0.1                              | -1.0..1.0, 0 = straight   |
    | PUSHBACK<br/>STOPPED/MOVING | `L:A32NX_PUSHBACK_SPD_FACTOR` = 0.0<br/>`L:A32NX_PUSHBACK_HDG_FACTOR` = 0.0 |                           |
    | Right                       | `L:A32NX_PUSHBACK_HDG_FACTOR` = oldvalue + 0.1                              |                           |
    | STRAIGHT                    | `L:A32NX_PUSHBACK_HDG_FACTOR` = 0.0                                         |                           |
    | Backward                    | `L:A32NX_PUSHBACK_SPD_FACTOR` = oldvalue - 0.1                              |                           |
    | 30% back                    | `L:A32NX_PUSHBACK_SPD_FACTOR` = -0.3                                        |                           |
        
