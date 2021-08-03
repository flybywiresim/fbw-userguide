# Autopilot / Fly-By-Wire

!!! warning "Important"

    * The custom autopilot system needs at least stable 17 fps to work properly. Any lower performance may result in unexpected behaviour.
    * Use modern flight model (legacy flight model is not supported)
    * It's crucial for the Autothrust system to have properly setup detents. Ensure that you have enough dead zone around the detents.
    * Typical issues when this is not done properly: constantly flashing "LVR CLB", FLX / TOGA not engaging or ATHR not holding speed correctly (the latter can also happen when in CLB/OP CLB or DES/OP DES and flying manually -> in that case you need to take care of holding speed with pitch)
    * Any mod or add-on that changes the physics or has impact on the flight model are **not supported**

***

## Reporting issues

When reporting issues please take the following into account:

* read the known and typical issues to be sure it's not already known or can be solved that way
* have a look at your fps
* note down which flight condition you are (in flight, on ground)
* note down what the FMA showed (or even better: take a screenshot or make a video)
* you can press the DFDR button (right of the throttle levers and above the TCAS panel) to mark an event
* if you ask for support you might be asked for a FDR file, those can be found in the work folder (see below)

***

### Work folder location

#### Microsoft Store Version

The work folder can be found here:

`%LOCALAPPDATA%\Packages\Microsoft.FlightSimulator_8wekyb3d8bbwe\LocalState\packages\flybywire-aircraft-a320-neo\work\`

#### Steam Version

The work folder can be found here:

`%APPDATA%\Microsoft Flight Simulator\Packages\flybywire-aircraft-a320-neo\work\`

***

## Custom Autopilot and Autothrust System incl. new Engine model

⚠️ This is work in progress, there are still issues, see the [Known Issues](#known-issues)

⚠️ When throttle sensitivity is changed, the throttle configuration needs to be adapted in most cases.

:information_source: It is recommended that the sidestick uses a linear sensitivity with only dead zone set appropriately.

:information_source: It is recommended to use a linear sensitivity for the throttle axis.

:information_source: The throttle configuration can be adapted using the EFB.

### Typical issues and how to solve them

???+ info "FMA keeps blinking with message `LVR CLB`"

    If this is the case your throttle calibration is not properly. The values of the throttle axis range from -1.0 to 1.0 independently if you're using reverse on axis or not. When the current throttle position is larger or equal then the start position and smaller or equal than the end position of a detent, the throttles are considered to be in that detent.

    Ensure that:

    * detents are large enough defined so hardware inaccuracy is taken into account (i.e. detents on the Thrustmaster TCA are not that hard and values can quite differ even one thinks it's in the detent
    * there is enough range between the detents (meaning end position of detent and start position of next detent are at least wide as the detents)

    **Important**: if you have issues, don't look at the animation part to check if it's in the detent. Check the values in the EFB, those are relevant and not the animation.

??? info "Autothrust does not hold target speed in manual flight"

    Important rule is to always monitor the FMA. If you're in manual flight and you're in `CLB`, `OP CLB`, `DES` or `OP DES` the autothrust applies either `THR CLB` (limited by the throttle levers) or `THR IDLE`. The speed needs to be controlled by pitch and in manual flight the pilot is responsible to do so by following the flight director orders.

    If this is not your desired mode, you can do two things:

    * engage another vertical mode (i.e. V/S or FPA)
    * disengage both flight directors, this will force the Autothrust into SPEED mode

    **Reminder**: Speed is only controlled properly using thrust when Autothrust is engaged and active, thrust levers are in detent CLB, active FMA mode is `SPEED` or `MACH`.

??? info "`SRS` does not engage on take-off"

    `SRS` mode needs at least a V2 entered on TO PERF page. Additionally it does only engage when the detents are set properly. If no FLX temperature is set, this needs to be TOGA. If a FLX temperature is set, it's FLX/MCT or TOGA.

    Other conditions:

    * plane needs to be at least 30 s on ground
    * Flaps extended at least in position 1+F

??? info "`RWY` does not engage on take-off"

    There is currently no auto-tune available for the LOC on take-off. You need to enter the right frequency manually. Beside that `RWY` mode only engages with the following conditions:

    * LOC signal valid
    * LOC deviation smaller than 1/2 dot
    * Deviation between plane heading and LOC bearing is < 20°
    * Plane needs to be at least 30 s on ground
    * Flaps extended at least in position 1+F

??? info "`LVR CLB` flashes immediately after lift-off"

    Ensure that both thrust reduction and acceleration altitude on TO PERF page are properly setup.

??? info "`LAND` mode does not engage"

    Before reaching 400 ft radio altitude the FMA needs to show `LOC` and `G/S`. If one of them is still in capture mode (`LOC*` or `G/S*`) you need to perform a go around maneuver or land manually, LAND will not engage that way.

??? info "Autoland does not perform as expected"

    The Autoland system is quite complex and is dependent on multiple environmental conditions to work properly, such as:

    * LOC accuracy in terms of
      * alignment of heading to runway heading
      * alignment on runway centerline
      * availability down to 0 ft and also during roll-out
    * G/S accuracy in terms of
      * alignment to correct height (50 ft over runway threshold)
      * availability down to 50 ft
    * ground in front of runway threshold needs to be more or less stable (no fast raising terrain) beginning 200 ft radio altitude

    **Reminder:** If the autoland warning light goes on it's IRL procedure to go around!

    Unfortunately a lot of runways (either using Navigraph or not) have issues for LOC and/or G/S, either in terms of alignment or availability. On many runways you loose the LOC during `ROLL OUT`. In that case the roll out has to be performed manually by disengaging the AP.

??? info "Flight controls are not working after reload of the sim or airplane"

    Ensure that no `SimConnect.cfg` is in the Documents folder of your user profile. An older version of Kinetic Assistant installed that file and it's causing issues with SimConnect connection between our custom systems and the sim. 

??? info "Autopilot is oscillating on approach or in flight"

    Ensure that you get enough frames per second (see on top).

??? info "Climb performance is not satisfying or plane drops or increases nose heavily on approach"

    Ensure that you're using modern flight model (Options -> General -> Flight Model). Beside that also ensure that you don't have any mods or add-ons installed that have influence on the flight model or other physics.

??? info "Autopilot oscillates when using time compression"

    Time compression is not fully supported yet, this applies also to fuel burn (time compression is not taken into account).

    The reason why it can work for some and not for others is how time compression is working. For example when using time compression of 2x for the custom systems it's like having 1/2 of your displayed fps, when you're using 4x it's like 1/4 of it. So taking into account the 17 fps requirement it means you need ~ 30 fps and ~ 45 fps for 4x to work somehow, at least for smooth cruise.

    When you encounter heavy turbulence it might be needed that time compression is reduced.

    For the time being we do not recommend using it.

??? info "Ailerons are not working when using the keyboard"

    There is currently an issue with the associated events and there is currently no way to solve it.

    We highly recommend using a controller with an axis assigned to use the plane.
    
    A possible workaround is by using a tool like FSUIPC. Assign the correct events to the keys you want to use. The events that work are (mind the 's' behind aileron):
    
    * AILERONS_LEFT
    * AILERONS_RIGHT

***

### Known issues

#### Requirements and Incompatibilities

* ❌ Legacy flight model of MSFS is not supported
* ❌ Minimum performance requirement is stable 17 fps
* ❌ No support for AI copilot
* ❌ Proper throttle calibration via EFB

#### Not solved or missing (this list is not conclusive)

##### Fly-By-Wire
* ❌ Alternative Law
* ❌ Direct Law (in flight)
* ❌ Simulation of hydraulic system missing -> when engines are off / electric pump is off control surfaces should not work
* ❌ Ailerons cannot be controlled using the keyboard at the moment (issue with SimConnect events)
* ❌ Pitch attitude and load factor limitation are currently not applied in high angle of attack (AoA) protection

##### Flight Management

* ❌ Due to lack of LNAV, the flaws of the default flight plan manager still apply (bank to left or right shortly after TO etc)
* ❌ Due to lack of VNAV, DES mode is currently only using SPD/MACH
* ❌ Due to lack of VNAV, RNAV approaches are not supported yet

##### Autopilot

* ❌ AP disconnect does not trigger master warning etc.
* ❌ NAV mode being armed might show dashes in the FCU instead of selected HDG
* ❌ Engine out operations are not yet considered
* ❌ AP is not disconnected due to turbulence
* ❌ Time compression is not supported

##### Engines

* ❌ Realistic start-up procedure is missing
* ❌ Realistic Descent/ Approach idle parameters / drag.
* ❌ Time compression is not supported (fuel burn is not adapted for time compression)

##### Autothrust

* ❌ N1 thrust limit displayed and achieved may differ slightly in certain situations

#### First implementation available

* 🔸 V_LS, V_alpha_prot, V_alpha_max are not finished and will be further improved
* 🔸 Some transitions might not be as they should or are missing
* 🔸 Engines can now be started, realistic start-up procedure is in work
* 🔸 principle go-around mode has been added but not all conditions are respected yet
* 🔸 NAV mode is for the time being using default flight plan manager until the custom is ready
* 🔸 altitude constraints seem to work with CLB and DES (there are many situations out there, so there can still be unknown bugs)
* 🔸 FLEX thrust limit is still rough and is also not adapted for Mach yet
* 🔸 Thrust limits are already very good but might be improved in the future (they are currently lacking adaptation for Mach)
* 🔸 Thrust limits are now corrected for air-conditioning and anti-ice yet
* 🔸 Flare Law has been improved to handle fast raising ground before the runway; when in 200 ft RA, the ground should in the area of the runway slope, otherwise issues are to be expected
* 🔸 AP performance when flying turbulence might not be satisfying in all cases
* 🔸 During start, no fuel flow is shown
* 🔸 ROLL OUT law is more sensitive to fps than other laws which can cause oscillations
* 🔸 ROLL OUT law can cause a divert from the runway when the runway is short (i.e. EDNY)

#### Considered solved

* ✔️ In case the default AP is for any reason engaged it will be automatically disconnected
* ✔️ In manual approach LOC and G/S might be lost too fast with mode reversion to HDG + V/S
* ✔️ FMA indications for ATHR system are missing
* ✔️ due to this workaround, the engine EGT can go into read area when in (OP) CLB/DES (see workaround above)
* ✔️ due to missing custom ATHR system, the (OP) CLB/DES modes might need manual thrust control
* ✔️ FD off/on does not deactivate all FMA items
* ✔️ Engagement of AP with FD off is incorrect
* ✔️ Flight Director (FD) guidance in pitch is not fully satisfying yet
* ✔️ Fuel used since start is not shown correctly on ECAM fuel page, it's basically 0
* ✔️ AP is disconnected due to sidestick or rudder input
* ✔️ EWD has been improved to correctly display N2 > 100
* ✔️ Fuel flow is currently always in KG
* ✔️ Pause and slew detection should be ok now
* ✔️ SPD/MACH hold might when flying in curves has been improved
* ✔️ Fuel burn should be correct in flight
* ✔️ ATHR implementation is already quite complete
* ✔️ Switched to different default input source for LNAV, transitions are now much better
* ✔️ LOC* has been improved in capturing performance
* ✔️ Normal Law (Pitch) creates a too small pitch rate on low speed or g-load on higher speeds
* ✔️ Rotation Law including tailstrike protection
* ✔️ pitch normal law (C* law) sometimes oscillates on low speed
* ✔️ yaw damper / rudder control missing
* ✔️ pitch attitude protections can oscillate
* ✔️ nose-down pitch attitude protection sometimes kicks-in too early
* ✔️ transformation from ground to flight mode might take longer than intended (nose might drop after releasing the stick)
* ✔️ auto-trim feature locks trim wheel completely
* ✔️ flare mode might be stronger than expected, needs to be investigated
* ✔️ after landing sometimes a slight pitch up moment is introduced, needs to be investigated
* ✔️ strange interaction with default auto thrust system -> thrust lever sometimes does not move, fix is to manually disable ATHR
* ✔️ after a longer pause the fbw system goes crazy
* ✔️ High speed protection
* ✔️ High angle of attack (AoA) protection
* ✔️ Increasing thrust rapidly while being in high alpha protection may additionally trigger alpha floor

***

### Mapping of events to control autopilot / autothrust

⚠️ Not all events are working and it's also difficult to map all default events because there is no 100% match.

The recommendation is to use a combination of default events and the custom events to trigger the FCU. This has been tested with the Honeycomb Bravo Throttle using SPAD.next or FSUIPC.

:information_source: An event file is required for FSUIPC. This needs to be placed in the FSUIPC folder beside the ini-file to be recognized. Then you can select those custom events for button press (for FS Control).

:information_source: A profile xml is required for SPAD.neXt. This needs to be placed in your configured SPAD.neXt profile folder. Then you can create a new profile based on that or by editing the XML files you can take-over the custom events in your existing profile.

You can grab the required files with the links below.

[:fontawesome-brands-github:{: .github } FSUIPC Event File](https://github.com/flybywiresim/a32nx/tree/master/docs/FSUIPC){ .md-button } [:fontawesome-brands-github:{: .github } SPAD.neXt Profile](https://github.com/flybywiresim/a32nx/tree/master/docs/SPAD.neXt){ .md-button }

***

#### Default events

| Event | Function |
| ---: | --- |
| AP_MASTER | Toggles AP 1 master
| AUTOPILOT_OFF | Disconnect AP (like red button on sidestick)
| AUTOPILOT_DISENGAGE_TOGGLE | Same as AP_MASTER
| AP_SPD_VAR_INC | Clockwise dial Speed knob on FCU
| AP_SPD_VAR_DEC | Anti-clockwise dial Speed knob on FCU
| HEADING_BUG_INC | Clockwise dial Heading knob on FCU
| HEADING_BUG_DEC | Anti-clockwise dial Heading knob on FCU
| AP_ALT_VAR_INC | Clockwise dial ALT knob on FCU
| AP_ALT_VAR_DEC | Anti-clockwise dial ALT knob on FCU
| AP_VS_VAR_INC | Clockwise dial V/S knob on FCU
| AP_VS_VAR_DEC | Anti-clockwise dial V/S knob on FCU
| AP_APR_HOLD | Push APPR button on FCU
| AP_LOC_HOLD | Push LOC button on FCU
| AUTO_THROTTLE_ARM | Push A/THR button on FCU
| AUTO_THROTTLE_DISCONNECT | Disconnect A/THR (like red button on throttle levers)
| AUTO_THROTTLE_TO_GA | Apply TOGA thrust

#### Custom events

| Event | Function |
| ---: | --- |
| A32NX.FCU_AP_1_PUSH | Push AP1 on FCU
| A32NX.FCU_AP_2_PUSH | Push AP2 on FCU
| A32NX.FCU_AP_DISCONNECT_PUSH | Disconnect AP (like red button on sidestick)
| A32NX.FCU_ATHR_PUSH | Push A/THR on FCU
| A32NX.FCU_ATHR_DISCONNECT_PUSH | Disconnect A/THR (like red button on throttle levers)
| A32NX.FCU_SPD_INC | Clockwise dial Speed knob on FCU
| A32NX.FCU_SPD_DEC | Anti-clockwise dial Speed knob on FCU
| A32NX.FCU_SPD_SET | Set Speed value on FCU (when in MACH mode 78 == M0.78)
| A32NX.FCU_SPD_PUSH | Push Speed knob on FCU
| A32NX.FCU_SPD_PULL | Pull Speed knob on FCU
| A32NX.FCU_SPD_MACH_TOGGLE_PUSH | Push SPD/MACH toggle on FCU
| A32NX.FCU_HDG_INC | Clockwise dial Heading knob on FCU
| A32NX.FCU_HDG_DEC | Anti-clockwise dial Heading knob on FCU
| A32NX.FCU_HDG_SET | Set Heading value on FCU
| A32NX.FCU_HDG_PUSH | Push Heading knob on FCU
| A32NX.FCU_HDG_PULL | Pull Heading knob on FCU
| A32NX.FCU_TRK_FPA_TOGGLE_PUSH | Push TRK/FPA toggle on FCU
| A32NX.FCU_ALT_INC | Clockwise dial Altitude knob on FCU (parameter 0 = use FCU increment, 100 = 100, 1000 = 1000)
| A32NX.FCU_ALT_DEC | Anti-clockwise dial Altitude knob on FCU (parameter 0 = use FCU increment, 100 = 100, 1000 = 1000)
| A32NX.FCU_ALT_SET | Set Altitude value on FCU
| A32NX.FCU_ALT_PUSH | Push Altitude knob on FCU
| A32NX.FCU_ALT_PULL | Pull Altitude knob on FCU
| A32NX.FCU_VS_INC | Clockwise dial V/S knob on FCU
| A32NX.FCU_VS_DEC | Anti-clockwise dial V/S knob on FCU
| A32NX.FCU_VS_SET | Set Speed value on FCU (when in TRK/FPA mode 10 == 1.0°)
| A32NX.FCU_VS_PUSH | Push V/S knob on FCU
| A32NX.FCU_VS_PULL | Pull V/S knob on FCU
| A32NX.FCU_LOC_PUSH | Push LOC button on FCU
| A32NX.FCU_APPR_PUSH | Push APPR button on FCU
| A32NX.FCU_EXPED_PUSH | Push EXPED button on FCU

#### FCU variables

The following gives an overview of the used variables in relation to the FCU. For more detailed explanation of the values please refer to this page:

[:fontawesome-brands-github:{: .github } SimVars Documentation](https://github.com/flybywiresim/a32nx/blob/master/docs/a320-simvars.md){ .md-button }

##### Common

| Variable | Function |
| ---: | --- |
| L:A32NX_AUTOPILOT_1_ACTIVE | Indicates if Autopilot 1 is enaged
| L:A32NX_AUTOPILOT_2_ACTIVE | Indicates if Autopilot 2 is enaged
| L:A32NX_AUTOTHRUST_STATUS | Indicates the current status of the ATHR system
| L:A32NX_FCU_LOC_MODE_ACTIVE | Indicates if LOC button on the FCU is illuminated
| L:A32NX_FCU_APPR_MODE_ACTIVE | Indicates if APPR button on the FCU is illuminated
| L:A32NX_TRK_FPA_MODE_ACTIVE | Indicates if TRK/FPA mode is active

##### Speed

| Variable | Function |
| ---: | --- |
| AUTOPILOT AIRSPEED HOLD VAR | Current Airspeed target (can be selected or managed)
| L:A32NX_FCU_SPD_MANAGED_DASHES | Indicates if managed speed/mach mode is active and a numerical value is not displayed
| L:A32NX_FCU_SPD_MANAGED_DOT | Indicates if managed speed/mach mode is active

##### Heading

| Variable | Function |
| ---: | --- |
| L:A32NX_AUTOPILOT_HEADING_SELECTED | Selected Heading in FCU
| L:A32NX_FCU_HDG_MANAGED_DASHES | Indicates if managed heading mode is active and a numerical value is not displayed
| L:A32NX_FCU_HDG_MANAGED_DOT | Indicates if managed heading mode is active or armed

##### Altitude + V/S

| Variable | Function |
| ---: | --- |
| AUTOPILOT ALTITUDE LOCK VAR:3 | Selected Altitude in FCU
| L:A32NX_FCU_ALT_MANAGED | Indicates if managed altitude mode is active (dot)
| L:A32NX_AUTOPILOT_FPA_SELECTED | Selected FPA in FCU
| L:A32NX_AUTOPILOT_VS_SELECTED | Selected V/S in FCU
| L:A32NX_FCU_VS_MANAGED | Indicates if managed VS/FPA mode is active
| L:A32NX_FMA_EXPEDITE_MODE | Indicates if expedite mode is engaged
