<link rel="stylesheet" href="../../../../../stylesheets/pfd-interactive.css">

# Autopilot Status Annunciations
<div style="position: relative; width: 413px; height: auto; margin-left: auto;  margin-right: auto;">
    <img src="/pilots-corner/a32nx/assets/a32nx-briefing/pfd/pfd-small.png" style="width: 413px; height: auto;">
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/fma/">               <div class="imagemap highlighted" style="position: absolute; left:     0%; top:     0%; width:   100%; height: 15.00%;"><span class="imagemapname">Flight Mode Annunciators</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/altitude-indicator/"><div class="imagemap"             style="position: absolute; left: 72.60%; top: 20.00%; width: 16.00%; height: 58.00%;"><span class="imagemapname">Altitude Indicator</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/vertical-speed/">    <div class="imagemap"             style="position: absolute; left: 89.00%; top: 18.15%; width: 11.00%; height: 64.20%;"><span class="imagemapname">Vertical Speed Indicator</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/baro-ref/">          <div class="imagemap"             style="position: absolute; left: 74.04%; top: 81.00%; width: 19.44%; height:   5.8%;"><span class="imagemapname">Barometric Reference</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/artificial-horizon/"><div class="imagemap"             style="position: absolute; left: 18.74%; top: 20.62%; width: 48.81%; height: 56.68%;"><span class="imagemapname">Attitude and Guidance</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/speedtape/">         <div class="imagemap"             style="position: absolute; left:     0%; top: 20.17%; width: 15.35%; height: 57.86%;"><span class="imagemapname">Actual Airspeed Reference Line and Scale</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/heading-ref/">       <div class="imagemap"             style="position: absolute; left: 19.58%; top: 86.09%; width: 47.48%; height: 12.17%;"><span class="imagemapname">Heading Reference Line and Scale</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/ils-indicator/">     <div class="imagemap"             style="position: absolute; left: 22.70%; top: 78.40%; width: 42.88%; height:  5.34%;"><span class="imagemapname">Loc and G/S Deviation Scale</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/ils-indicator/">     <div class="imagemap"             style="position: absolute; left: 68.10%; top: 29.41%; width:  4.01%; height: 41.10%;"><span class="imagemapname">Loc and G/S Deviation Scale</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/ils-indicator/">     <div class="imagemap"             style="position: absolute; left:     0%; top: 85.00%; width: 16.00%; height: 13.00%;"><span class="imagemapname">ILS Information</span></div></a>
</div>

## Flight Mode Annunciator Columns (Interactive)

<div style="position: relative;">
    <img src="/pilots-corner/a32nx/assets/a32nx-briefing/pfd/fma.png" style="width: 100%; height: 100%;">
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/first-column">                <div class="imagemap" style="position: absolute; left:     0%; top:    0%; width: 20.77%; height:  95%;"><span class="imagemapname">First Column: Autothrust</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/second-column">               <div class="imagemap" style="position: absolute; left: 21.22%; top:    0%; width: 20.35%; height:  66%;"><span class="imagemapname">Second Column: Vertical Guidance</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/third-column">                <div class="imagemap" style="position: absolute; left: 41.40%; top:    0%; width: 22.90%; height:  66%;"><span class="imagemapname">Third Column: Lateral Guidance</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/fourth-column">               <div class="imagemap" style="position: absolute; left: 64.50%; top:    0%; width: 19.70%; height:  95%;"><span class="imagemapname">Fourth Column: Approach</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/fifth-column">                <div class="imagemap highlighted" style="position: absolute; left: 84.25%; top:    0%; width: 15.80%; height:  95%;"><span class="imagemapname">Fifth Column: Autoflight Engagement Status</span></div></a>
    <a href="/pilots-corner/a32nx/a32nx-briefing/pfd/special-message-annunciators"><div class="imagemap" style="position: absolute; left: 21.22%; top:   67%; width: 43.08%; height:  31%;"><span class="imagemapname">Special Message and Common Mode Annunciators</span></div></a>
</div>

## Description

This column displays the autothrust modes that are armed or active, as well as any requested pilot actions.

---

### AP

- AP1: Autopilot One is active.
- AP2: Autopilot Two is active.
- AP1+2: Both Autopilots are active.

### FD

- 1FD-: Flight Director One is active (Captain's side).
- -FD2: Flight Director Two is active (FO's side).
- 1FD2: Both Flight Directors are active.
- 1FD1: Flight Director Two has failed, but both Flight Directors are selected on.
- 2FD2 : Flight Director One has failed, but both flight directors are selected on.

### A/THR

When A/THR is displayed in blue text, autothrust is armed but not active. This means that thrust will be controlled by the thrust lever position.

Autothrust is armed by:

- Setting the thrust levers to the TO/GA position if at least one Flight Director is active.
- Setting the thrust levers to the FLEX position if at least one Flight Director is active and a FLEX temperature has been entered in the MCDU.
- Pushing the A/THR button when the thrust levers are not in the Climb Position.

When A/THR is displayed in white, autothrust is Active. This means that thrust will be controlled by the FADEC.

!!! note ""
    In Airbus autothrust systems, the thrust levers do not move by themselves. This is different from autothrottle systems in other aircraft vendors (e.g., Boeing).

Autothrust is engaged by:

- Setting the thrust levers to the engagement detent when the autothrust system is armed.
- Pushing the A/THR button when the thrust levers are in the engagement range (below climb detent with both engines or below MCT with one engine out).
- Activating Alpha Floor protection.

---

[Back to Flight Mode Annunciators](fma.md){ .md-button }
