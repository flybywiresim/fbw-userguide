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
    <img src="../../assets/a32nx-briefing/front/PFDLS.jpg" style="width: 100%; height: auto;">
    <!-- OVHD AFT -->
    <a href="/pilots-corner/a32nx-briefing/PFD/fma/"><div class="imagemap" style="position: absolute; left: 8.7%; top: 4%; width: 82.7%; height: 11.8%;"><span class="imagemapname">Flight Mode Annunciators</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/PFD/altitude-indicator/"><div class="imagemap" style="position: absolute; left: 68.4%; top: 23.4%; width: 14.2%; height: 53%;"><span class="imagemapname">Altitude Indicator</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/PFD/vertical-speed/"><div class="imagemap" style="position: absolute; left: 84%; top: 19%; width: 7.2%; height: 60%;"><span class="imagemapname">Vertical Speed Indicator</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/PFD/baro-ref/"><div class="imagemap" style="position: absolute; left: 70%; top: 79.4%; width: 17.7%; height: 3.9%;"><span class="imagemapname">Barometric Reference</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/PFD/artificial-horizon/"><div class="imagemap" style="position: absolute; left: 24.4%; top: 22.6%; width: 40.5%; height: 51.6%;"><span class="imagemapname">Attitude and Guidance</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/PFD/speedtape/"><div class="imagemap" style="position: absolute; left: 8.5%; top: 21%; width: 12.6%; height: 55.5%;"><span class="imagemapname">Actual Airspeed Reference Line and Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/PFD/heading-ref/"><div class="imagemap" style="position: absolute; left: 24.6%; top: 83%; width: 40.5%; height: 11.6%;"><span class="imagemapname">Heading Reference Line and Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/PFD/ils-indicator/"><div class="imagemap" style="position: absolute; left: 26.3%; top: 75.6%; width: 37%; height: 5.9%;"><span class="imagemapname">Loc and G/S Deviation Scale</span></div></a>
    <a href="/pilots-corner/a32nx-briefing/PFD/ils-indicator/"><div class="imagemap" style="position: absolute; left: 65%; top: 31%; width: 3.2%; height: 39%;"><span class="imagemapname">Loc and G/S Deviation Scale</span></div></a>
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
