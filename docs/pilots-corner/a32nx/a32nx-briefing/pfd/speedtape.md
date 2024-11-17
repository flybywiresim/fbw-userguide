<link rel="stylesheet" href="../../../../../stylesheets/pfd-interactive.css">

# Airspeed


<div style="position: relative; width: 413px; height: auto; margin-left: auto;  margin-right: auto;">
    <img src="/pilots-corner/a32nx/assets/a32nx-briefing/pfd/pfd-small.png" style="width: 413px; height: auto;">
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/fma/">               <div class="imagemap"             style="position: absolute; left:     0%; top:     0%; width:   100%; height: 15.00%;"><span class="imagemapname">Flight Mode Annunciators</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/altitude-indicator/"><div class="imagemap"             style="position: absolute; left: 72.60%; top: 20.00%; width: 16.00%; height: 58.00%;"><span class="imagemapname">Altitude Indicator</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/vertical-speed/">    <div class="imagemap"             style="position: absolute; left: 89.00%; top: 18.15%; width: 11.00%; height: 64.20%;"><span class="imagemapname">Vertical Speed Indicator</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/baro-ref/">          <div class="imagemap"             style="position: absolute; left: 74.04%; top: 81.00%; width: 19.44%; height:   5.8%;"><span class="imagemapname">Barometric Reference</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/artificial-horizon/"><div class="imagemap"             style="position: absolute; left: 18.74%; top: 20.62%; width: 48.81%; height: 56.68%;"><span class="imagemapname">Attitude and Guidance</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/speedtape/">         <div class="imagemap highlighted"             style="position: absolute; left:     0%; top: 20.17%; width: 15.35%; height: 57.86%;"><span class="imagemapname">Actual Airspeed Reference Line and Scale</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/heading-ref/">       <div class="imagemap"             style="position: absolute; left: 19.58%; top: 86.09%; width: 47.48%; height: 12.17%;"><span class="imagemapname">Heading Reference Line and Scale</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/ils-indicator/">     <div class="imagemap"             style="position: absolute; left: 22.70%; top: 78.40%; width: 42.88%; height:  5.34%;"><span class="imagemapname">Loc and G/S Deviation Scale</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/ils-indicator/">     <div class="imagemap"             style="position: absolute; left: 68.10%; top: 29.41%; width:  4.01%; height: 41.10%;"><span class="imagemapname">Loc and G/S Deviation Scale</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/ils-indicator/">     <div class="imagemap"             style="position: absolute; left:     0%; top: 85.00%; width: 16.00%; height: 13.00%;"><span class="imagemapname">ILS Information</span></div></a>
</div>

## Description

See also: [V-Speeds](../../../airliner/abbreviations.md#v-speeds)

### Actual Airspeed Reference Line and Scale

A white scale on a gray background moves in front of a fixed yellow reference line next to a yellow triangle to show airspeed. The minimum airspeed indication is 30 knots.

### Speed trend

This is shown in yellow and starts at the speed symbol. It is an arrow that extends upwards or downwards from the speed symbol, depending on the trend of the aircraft's speed (whether accelerating or decelerating).

The tip shows the speed the aircraft will reach in 10 seconds if the rate of change remains constant. The pointer will only appear when it exceeds 2 knots and disappears when it is 1 knot.

It will also disappear if the FACs fail.

### Target Airspeed

This is displayed in either magenta or blue depending on whether managed or selected speed is commanded. It is a triangle coming off from the right side of the speedtape. If the target airspeed is the FMGC computed airspeed, it will be displayed as a magenta triangle. If it is selected from the FCU by the pilots, it will be blue.

The target speed will be a magenta double bar when it is associated with the ECON speed range.

If the target speed is off the scale, the value is displayed as a number above or below the scale.

### Mach Number

This is displayed in green and is shown if the Mach number reaches above 0.5. It is displayed underneath the scale.

### Speed Protection

This is displayed in green and shows the speed at which overspeed protections become active.

This speed is V~MO~ (maximum operating speed) + 6 knots or M~MO~ (maximum Mach speed) + 0.01

### ECON Speed Range

This appears in descent mode with ECON/AUTO SPD mode active. Two magenta half triangles will represent the upper and lower limits calculated by the FMGC. This replaces the target speed symbol.

The upper speed is equal to the target speed + 20 knots, limited to V~MAX~, V~MO~ - 3 knots or M~MO~ - 0.006, whichever is the lowest.

If a speed constraint or limit applies, then the upper margin is limited to ECON SPD + 5 kt.

The lower speed margin is the target speed - 20 knots. It is limited to green dot, F, S or V~LS~ speeds, whichever is higher.

### Minimum Selectable Speed (V~LS~)

The top of the amber strip along the speed scale represents this speed. It shows the lowest selectable speed and provides an appropriate margin to the stall speed. This information is inhibited from touchdown until 10 seconds after liftoff.

### Alpha Protection Speed

The top of the black and amber striped strip along the speed scale represents this speed. It shows the speed corresponding to the angle of attack at which the alpha protections will become active. It is displayed when the aircraft is in normal pitch law.

### Alpha Max Speed

The top of a red strip along the speed scale indicates this speed. It represents the speed corresponding to the maximum angle of attack that the aircraft can achieve in normal pitch law.

### V~MAX~

The lower end of a red and black strip along the speed scale represents this speed. It is the lowest of:

- V~MO~ or the corresponding to M~MO~
- V~LE~
- V~FE~

### Stall Warning Speed (V~SW~)

The top of the red and black strip along the speed scale represents this speed. It is the speed at which the stall warning will occur. This information is inhibited from touchdown until 5 seconds after liftoff and is displayed only when operating in pitch alternate or pitch direct law.

### V~1~

It is shown as blue numeral one (1) at a speed that the pilot inserted manually in the takeoff performance page in the MCDU. When it is off the scale, the upper part of the scale shows the speed in numbers. It disappears after liftoff.

### Minimum Flap Retraction Speed (F)

This is displayed with a green letter F. It appears when the flap selector is in position 2 or 3.

### Minimum Slat Retraction Speed (S)

This is displayed with a green letter S. It appears when the flap selector is in position 1.

### V~FE~ NEXT

It is displayed with an amber double bar (=) and shows the V~FE~ corresponding to the next flap lever position. It appears when the aircraft altitude is below 15 000 feet or 20 000 feet depending upon the FAC standard.

### V~R~ (Rotation Velocity)

This is a blue dot on the right side of the speedtape. It displays the speed at which the aircraft can rotate.

### V~2~

This is a magenta triangle on the right side of the speedtape. It displays the V~2~ speed which has been set in the TAKE OFF PERF page of the MCDU. V~2~ is the minimum speed that needs to be maintained in the event of an engine failure after V~1~ up to acceleration altitude.

V~2~+10 provides better climb performance (before acceleration altitude and during noise abatement program departures).

!!! info "Engine Loss V~2~ Speeds"
    After takeoff, **V~2~+10** is the targeted speed you should reach and maintain by the time you attain a height of 35 ft after takeoff until reaching the acceleration altitude.

    When an engine failure occurs (shortly before or after takeoff), V~2~ is the minimum allowable speed. Pilots should aim to meet the criteria below at the point of engine loss:

    - In a situation where the engine is lost before reaching V~2~ the targeted speed is V~2~.
    - If the aircraft speed is higher than V~2~ then pilots should maintain the higher speed but not exceed V~2~+15.

---

[Back to Interactive PFD](index.md){ .md-button }
