# Selected Vertical Modes

Selected modes guide the aircraft according to target values that the pilot selects and the FCU windows display.

Selected modes disregard all altitude constraints.

## OP CLB (Open Climb)
The OPEN CLB mode specifically wants (and commands) Climb Thrust. The target speed/mach is maintained by the AP/FD system by adjusting the pitch with the elevator, whereas thrust is maintained either by the Autothrust system, or manually by the flight crew. Speed target may either be selected or managed.

The OPEN CLB mode disregards all altitude constraints up to the FCU selected altitude.

OPEN CLB mode can be engaged when:

- the aircraft has been in flight for more than 5 seconds.
- LAND mode is not engaged.
- the altitude selected in the FCU is higher than the present altitude.

It is activated when:

- the flight crew pulls the FCU ALT knob.
- guidance reverts to speed protection.
- acceleration altitude is reached with CLB armed and lateral navigation (NAV) not engaged.

## Altitude Acquire Mode (ALT^*^)
ALT* mode guides the aircraft to acquire the FCU selected altitude.

The mode engages when the aircraft reaches the altitude capture zone, defined by the aircraft vertical speed (among other parameters).

## Altitude Hold Mode (ALT)
The ALT mode maintains the FCU selected target altitude.

The ALT mode arms automatically whenever the aircraft climbs or descends toward the target altitude.

When ALT is armed, the FMA displays the ALT message on its second line in blue (when in OP CLB/DES).

The ALT mode is engaged automatically when the difference between the present altitude and the target altitude becomes less than 20 ft with ALT^*^ engaged.

The altitude that ALT mode holds is the altitude it memorized when engaged. It is not affected by a change of reference in the ALT window or by a change in the barometric correction.

When ALT is engaged after OP CLD/DES, the FMA displays ALT in green (FCU altitude hold).

## OP DES (Open Descent)
The OPEN DES mode is specifically designed for IDLE thrust. The target speed/mach is maintained by the AP/FD system by adjusting the pitch with the elevator, whereas thrust is maintained either by the Autothrust system, or manually by the flight crew. Speed target may either be selected or managed.

The OPEN DES mode disregards all altitude constraints.

OP DES mode can be engaged when:

- the aircraft has been in flight for more than 5 seconds.
- LAND mode is not engaged.
- the altitude selected in the FCU is lower than the present altitude.

It is activated when:
- the flight crew pulls the FCU ALT knob.
- Selecting a manual speed when EXPEDITE mode is engaged.

## V/S and FPA (Vertical Speed and Flight Path Angle)
The V/S-FPA mode acquires and holds the vertical speed or the flight path angle displayed in the V/S-FPA window of the FCU. The HDG V/S-TRK FPA push button on the FCU allows the flight crew to select vertical speed or flight path angle to be used.

The FMGC pitch mode guides the aircraft to the target V/S or FPA. The corresponding A/THR mode is SPEED or MACH. The FMA displays V/S (FPA).

{--

The V/S (FPA) guidance has priority over the speed guidance. If the selected target V/S or FPA is too high (relative to the current thrust condition and speed), the FMGC will steer the aircraft to the target V/S or FPA, but the aircraft will also accelerate or decelerate.

When the speed reaches its authorized limit, V/S or FPA automatically decreases to maintain the minimum or maximum speed limit.

--}

V/S-FPA can be manually engaged when:

- the aircraft has been in flight for more than 5 seconds.
- the AP or FD are activated when they have been off before.
- changing target altitude by > 250 ft when in ALT^*^ mode.
- selecting a higher altitude when in any descent mode.
- selecting a lower altitude when in any climb mode.

It engages automatically when:

- no other vertical mode is engaged after 5 seconds after lift off.
- loss of G/S* or G/S mode.
- loss of FINAL mode.
- loss of LOC* or LOC mode.
- loss of NAV mode when DES mode is engaged.
- loss of vertical flight path in DES mode.
- TCAS mode disengagement.

To immediately level off the aircraft, the flight crew can push the FCU V/S-FPA knob or set the V/S-FPA to 0.

Note: If AP is engaged while a V/S is selected with only FD ON, the V/S will synchronize to the current aircraft V/S.

## EXP (Expedite)
Expedite mode is used in climb or descent to reach the desired altitude with the maximum vertical gradient.

When the aircraft is in EXP CLB, the target speed is Green Dot, which is maintained with pitch control. If Autothrust is active, it sets the thrust to CLB THRUST automatically.

When the aircraft is in EXP DES, the target speed is 340 kt or 0.8 Mach, which is maintained with pitch control.
If Autothrust is active, it sets the thrust to IDLE automatically.

When EXPEDITE is engaged, the system disregards speed constraints (SPD CSTR), altitude constraints (ALT CSTR), and speed limits (SPD LIM).

EXPEDITE can be engaged when

‐ the aircraft has been in flight for more than 5 s.
‐ managed speed is available.

It is engaged manually only when

‐ the FCU selected altitude is higher than present altitude, EXP CLB mode engages.
‐ the FCU selected altitude is lower than present altitude, EXP DES mode engages.


