# Primary Flight Display (PFD)

## Description

The Primary Flight Display (PFD) is the main aviation instrument for the pilots. It provides information for:

- Attitude
- Sideslip Indication
- Airspeed (Knots or Mach) and speed trend
- Altitude (baro and radio)
- Vertical Speed
- Heading and Track
- Autopilot / Flight Director Guidance
- Sidestick Order Indication
- Flight Mode Annunciator and Flight Modes FMGS
- Deviations (vertical and lateral)
- Radio navigation (ILS, DME, etc.)
- Various scales and limits (bank limits, max sidestick deflection, pitch, etc.)

## Interactive PFD

<style>
.imagemap {
    position: relative;
    display: inline-block;
    /*background-color: rgba(255, 0, 0, .4);
    border: 1px solid yellow;*/
}
.imagemap .imagemapname {
  visibility: hidden;

  background-color: rgba(29, 30, 38,.8);
  color: rgba(212, 212, 213, 1);
  text-align: center;
  padding: 5px 0;
  border-radius: 6px;

  /* Position the tooltip text - see examples below! */
  position: absolute;
  z-index: 1;
  width: 120px;
  top: 0%;
  left: 50%;
  margin-left: -60px; /* Use half of the width (120/2 = 60), to center the tooltip */
}
.imagemap:hover .imagemapname {
    visibility: visible;
}
.imagemap:hover {
    background-color: rgba(10, 144, 153, 0.30);
    border: 1px solid black;
}
</style>
<div style="position: relative;">
    <img src="../../assets/a32nx-briefing/front/primaryfd.jpg" style="width: 100%; height: auto;">
    <!-- OVHD AFT -->
    <a href="/pilots-corner/a32nx-briefing/pfd/fma/"><div class="imagemap" style="position: absolute; left: 0%; top: 0%; width: 100%; height: 13.6%;"><span class="imagemapname">Flight Mode Annunciators</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/altitude-indicator/"><div class="imagemap" style="position: absolute; left: 72.6%; top: 22.60%; width: 15.28%; height: 56.0%;"><span class="imagemapname">Altitude Indicator</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/vertical-speed/"><div class="imagemap" style="position: absolute; left: 91.25%; top: 18.15%; width: 8.46%; height: 64.2%;"><span class="imagemapname">Vertical Speed Indicator</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/baro-ref/"><div class="imagemap" style="position: absolute; left: 74.04%; top: 82.8%; width: 19.44%; height: 4.01%;"><span class="imagemapname">Barometric Reference</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/artificial-horizon/"><div class="imagemap" style="position: absolute; left: 18.74%; top: 20.62%; width: 48.81%; height: 56.68%;"><span class="imagemapname">Attitude and Guidance</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/speedtape/"><div class="imagemap" style="position: absolute; left: 0%; top: 20.17%; width: 15.35%; height: 57.86%;"><span class="imagemapname">Actual Airspeed Reference Line and Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/heading-ref/"><div class="imagemap" style="position: absolute; left: 19.58%; top: 86.09%; width: 47.48%; height: 12.17%;"><span class="imagemapname">Heading Reference Line and Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/ils-indicator/"><div class="imagemap" style="position: absolute; left: 22.70%; top: 78.4%; width: 42.88%; height: 5.34%;"><span class="imagemapname">Loc and G/S Deviation Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/pfd/ils-indicator/"><div class="imagemap" style="position: absolute; left: 68.10%; top: 29.41%; width: 4.01%; height: 41.10%;"><span class="imagemapname">Loc and G/S Deviation Scale</span></div></a>
</div>

---

## Chapters

- [Flight Mode Annunciators](fma.md)
- [Actual Airspeed Reference Line and Scale](speedtape.md)
- [Attitude and Guidance](artificial-horizon.md)
- [Altitude Indicator](altitude-indicator.md)
- [Barometric Reference](baro-ref.md)
- [Heading Reference Line and Scale](heading-ref.md)
- [Vertical Speed indicator](vertical-speed.md)
- [Flags and Messages](flags-messages.md)
