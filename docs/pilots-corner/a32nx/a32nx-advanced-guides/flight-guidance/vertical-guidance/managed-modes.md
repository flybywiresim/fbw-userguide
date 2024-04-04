# Managed Vertical Modes
Managed modes guide the aircraft along the vertical profile according to the data the pilot inserts into the MCDU. Flight Management (in the Flight Management and Guidance Computer) computes the corresponding guidance targets.

Managed modes account for altitude constraints at waypoints and also for speed constraints at waypoints when speed is in managed mode.

## Takeoff SRS (Speed Reference System)
The SRS mode controls pitch at takeoff to steer the aircraft along a path in the vertical plan at a speed defined by the SRS guidance law.

In SRS mode, the aircraft maintains a speed target equal to V2+10 kt in normal engine configuration. When the FMGS detects an engine failure, the speed target becomes the highest of V2 or current speed, limited by V2+15 kt.

The SRS mode engages automatically when the thrust levers are set to the TOGA or FLX/MCT detent (when a Flex takeoff temperature has been selected), if:

- V2 has been inserted in the MCDU PERF TAKEOFF page
- the slats are extended
- the aircraft has been on the ground for at least 30 seconds

The SRS mode disengages:

- automatically, at the acceleration altitude (ACC ALT), or if ALT* or ALT CST* mode engages (above 400 ft RA)
- if the flight crew engages another vertical mode
- if the flight crew selects a speed while in SRS mode: SRS reverts to OP CLB mode, and a triple-click aural warning is heard
- if the TCAS mode engages

The SRS guidance law also includes:

- Attitude protection to reduce aircraft nose-up effect during takeoff (18° or 22.5° maximum in case of windshear)
- Flight path angle protection that ensures a minimum vertical speed of 120 ft/min
- A speed protection, limiting the target speed to V2+15 kt.

## CLB (Climb)

CLB mode guides the aircraft in a managed climb, at either a managed or a selected target speed, to an FCU selected altitude, considering altitude constraints at waypoints. The system also considers speed constraints if the target speed is managed.

The AP/FD pitch controls the speed or Mach number target and the A/THR is in thrust mode (CLB) corresponding to maximum climb thrust. The flight path may include several segments. The flight crew can arm the CLB mode during the takeoff, go-around, climb, and cruise phases and engage it during the climb and cruise phases.

The CLB mode can be armed under the following conditions:

- On ground or when in SRS mode
    - if no other vertical mode is activated
    - the acceleration altitude defined in the MCDU PERF TO or GA page is below the lowest altitude constraint and
      also below the altitude selected in the FCU
- In flight in climb or go-around phase
    - if lateral navigation (NAV) is engaged
    - if the altitude selected in the FCU is above the current altitude and the aircraft captures or flies an
      altitude constraint

The CLB mode can be engaged when:

- the aircraft has been in flight for more than 5 seconds
- the altitude selected in the FCU is above the current altitude
- not in descent, approach, or go-around phase
- Lateral navigation (NAV) is engaged
- Not in G/S mode

It is automatically engaged at acceleration altitude (ACC ALT) or when a waypoint with an altitude constraint is passed while CLB mode was armed.

It can be manually engaged by pushing the FCU ALT knob while the CLB mode is not armed and the current altitude is not at an altitude constraint.

- When CLB mode is engaged, the system arms ALT and displays the applicable target altitude on the ALT scale.
    - Magenta for another altitude constraint
    - Blue for a FCU selected altitude
- The guidance does **not** modify the target speed in order to satisfy an altitude constraint. Therefore, the
  constraint may not be met and may be predicted as missed
- When the aircraft levels off at the ALT CSTR, CLB mode arms automatically, then engages when the aircraft passes the constrained waypoint (if the FCU altitude is above the constraint altitude).

## Altitude Acquire Mode (ALT CST^*^)
ALT CST* guides the aircraft to acquire an altitude constraint provided by Flight Management. Once the aircraft has reached the altitude, the altitude mode (ALT or ALT CST) engages.

The mode engages when the aircraft reaches the altitude capture zone, defined by the aircraft vertical speed (among other parameters).

## Altitude Hold Mode (ALT CST, ALT CRZ)
The ALT mode maintains a target altitude. This target altitude is either the FCU selected altitude or an altitude constraint delivered by Flight Management.

The ALT mode arms automatically whenever the aircraft climbs or descends toward the target altitude.

When ALT is armed, the FMA displays the ALT message on its second line:

- Blue when the target altitude is the FCU selected altitude
- Magenta if the target altitude is an altitude constraint.

The ALT mode is engaged automatically when the difference between the present altitude and the target altitude becomes less than 20 ft with ALT* engaged.

The altitude that ALT mode holds is the altitude it memorized when engaged. It is not affected by a change of reference in the ALT window or by a change in the barometric correction.

When ALT is engaged, the FMA displays ALT in green (FCU altitude hold), ALT CST in green if it is an altitude constraint, or ALT CRZ in green if cruise flight level is held.

## DES (Descent)

The managed descent mode guides the aircraft along the FMS computed vertical flight path. The DES mode is preferred when conditions permit, since it ensures the management of altitude constraints and reduces the operating cost when flying at ECON DES speed.

The DES mode is only available when the aircraft flies on the FMS lateral flight plan, i.e., when the aircraft uses the NAV horizontal guidance mode.

The FMGS computes the flight path backwards from the deceleration point (D) up to the top of descent (T/D), with respect to the speed and altitude constraints at the deceleration point, the guidance begins the deceleration to V~APP~, to be reached at 1000 ft above touchdown on the final descent path.

This computation starts with an idle power segment down to the first constraint, followed by geometric segments between constraints until reaching the deceleration point. The FMGS accounts for wind and data from the vertical and lateral flight plan and bases its computations on the managed speed profile. Holding patterns are not considered.

Each descent can have the following segments:

- Idle path segment:
    - Autothrust uses idle thrust, while the AF/FD controls speed by adjusting the vertical trajectory (pitch)
- Geometric path segment:
    - AP/FD controls the required vertical path while Autothrust controls speed.
- Re-pressurization segment:
    - If required, this ensures a specific rate of pressurization for the cabin during descent. It is calculated from the destination airport altitude and the selected cabin rate (default - 350 ft/min, which can be modified)

!!! warning "Re-pressurization segments are not yet implemented in the A32NX"

If the aircraft levels off at an ALT CSTR, the DES mode arms and remains armed until the aircraft passes the constraint, then reengages (if the FCU altitude is set below the altitude of the constraint).

### Engaging DES Mode
The DES mode can be engaged when:

- the altitude selected in the FCU is lower than the present altitude
- either NAV, LOC^*^, LOC are active
- takeoff, climb, or go-around phase are not active
- vertical flight path is valid
- not in TO, G/S, LAND, FINAL, or GA mode
- Either
    - an ALT CSTR waypoint is sequenced (passed) and DES mode is armed (DES will activate automatically), or
    - pilot presses the ALT knob (ALT CST^*^, ATL CST may not be active), or
    - pilot presses the ALT knob when ALT^*^ or ALT is active and current altitude is not a constraint

During the descent, approach and landing, the managed speed is equal to either:

- ECON DES speed or the descent speed manually entered in the PERF DES page of the FMS, or
- The speed constraint, speed limit, or
- The maneuvring speed of the current aircraft configuration, or
- V~APP~.

### Initiating Decent
Descent initiation is not started automatically in the Airbus A320. To start the descent, the flight crew sets the ATC cleared altitude into the FCU and pushes the ALT knob. If the aircraft has not yet reached the top of descent point, it will start descent immediately at a constant V/S until intercepting the computed descent path. If the aircraft is at or beyond the top of descent point, it descents at idle thrust.

After initiating the descent, the aircraft shows a vertical deviation symbol (green dot) next to the altitude scale on the PFD so that the flight crew can monitor the aircraft's position relative to the descent path.

When the speed is managed, a target speed range is displayed in the speed band on the PFD (magenta bars) which defines acceptable speed variations around the nominal descent speed target.

Associated with the VDEV displayed on PFD, the ND shows an intercept point (zigzag symbol) on the flight plan. It indicates the position where the system predicts that the aircraft will intercept the descent profile.

See all symbols below: [Vertical Guidance Symbology](nd-symbols.md).

### Vertical Path Deviation
If the aircraft is above the descent profile, the speed will increase toward the upper limit of the managed speed range. If the speed reaches the upper limit, the aircraft will maintain the speed but will deviate from the profile (Autothrust at idle).

The navigation display presents a pseudo waypoint (intercept point) along the flight plan that assumes the aircraft will return to the profile using:

- Idle thrust
- 1/2 speedbrake extension
- ECON speed plus a margin (until intercepting the profile).

If necessary, the message “MORE DRAG” comes up on the PFD and the MCDU, and remains there as long as more drag (speedbrakes) is still required. The flight crew should respond to this message by deploying half speedbrakes.

If the aircraft is below the descent profile, its speed will be maintained at target speed until it reaches the descent profile. The lower margin becomes effective when the aircraft is on the descent profile, but has to lose speed to stay on it.

!!! warning "The MORE DRAG message is not yet implemented in the A32NX"

## Approach modes

### G/S, G/S*
Glideslope capture (G/S^*^) and glideslope (G/S) modes are used in precision approaches (ILS, MLS).

### FINAL / FINAL APP
APP NAV and FINAL modes are used in non-precision approaches (VOR/DEM, VOR, NDB, RNAV).

!!! warning "FINAL and FINAL APP are not yet implemented in the A32NX"

### LAND
LAND mode automatically engages when the LOC and G/S modes are engaged, and the aircraft is below 400 ft RA. The FMA displays “LAND”, indicating that LOC and G/S are locked. LAND mode can only be disengaged by a go-around. FLARE and ROLL OUT modes will successively engage.

### FLARE
FLARE mode engages once the aircraft reaches approximately 40 ft RA (the precise value is a function of V/S). The FMA displays “FLARE” in green.

At 30 ft RA, the AP/FD aligns the yaw axis with the runway center line and the aircraft flares on the pitch axis. If the Autothrust is active, thrust is automatically reduced to IDLE (callout "retard").
When both AP/FDs are disengaged, FLARE mode disengages. After main landing gear touchdown, the autopilot (if engaged) sends a nose down order.

## TCAS Mode
The TCAS mode is an Auto Flight System (AFS) guidance mode that provides vertical guidance in the case of a Traffic Alert and Collision Avoidance System (TCAS) Resolution Advisory (RA). When a Traffic Advisory (TA) is triggered, the TCAS mode arms.

When a RA is triggered, the TCAS mode engages. The TCAS mode provides vertical guidance in accordance with the TCAS RA order.

When clear of conflict (the “CLEAR OF CONFLICT” aural alert sounds), the TCAS mode disengages.

The AFS provides guidance toward the latest target altitude set on the FCU.

See or detailed guide for TCAS: [Traffic Alert and Collision Avoidance System](../tcas.md)

