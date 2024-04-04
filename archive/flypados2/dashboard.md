<link rel="stylesheet" href="../../../../stylesheets/efb-interactive.css">

# flyPad Dashboard

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados2/flypad-dashboard.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.3%; top:  7.7%; width: 5.8%; height: 7.6%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 15.6%; width: 5.8%; height: 7.6%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.3%; top: 23.5%; width: 5.8%; height: 7.6%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.3%; top: 31.4%; width: 5.8%; height: 7.6%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.3%; top: 39.3%; width: 5.8%; height: 7.6%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.3%; top: 47.2%; width: 5.8%; height: 7.6%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 55.1%; width: 5.8%; height: 7.6%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 84.1%; width: 5.8%; height: 7.6%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>


## Description

The Dashboard is the default flyPad page after starting it.

It has three sections:

- Left:
    - Shows the currently loaded flight plan or dashes if none is loaded.
- Right Top:
    - Shows current METAR information for the loaded origin and destination airports.
- Right Bottom:
    - Moving map with your current location marked by a blue plane symbol.
    - Shows the current weather on the map.

## Usage

### METAR Information

The METAR widget on the top right shows the current METAR information of either the simBrief imported airports or manually entered airports.

You can type in any airport ICAO code into the input fields to get the corresponding METAR information. To get back to the simBrief imported airports simply delete the manually entered ICAO.

You can switch between the weather summary which shows the most important METAR parts with icons or a raw view of the METAR information.

![ICAO Input to Weather Widget](../assets/flypados2/weather-widget-input.png "ICAO Input to Weather Widget"){loading=lazy}

We have applied a helpful coloring scheme a large European airline uses to point out significant parts of the raw METAR information to the pilots. This coloring uses the following colors:

- Cyan: Chosen airport ICAO
- White: standard value with no special concern
- Amber: highlights significant values as a caution to the pilot
- Red: highlights very significant values as a warning to the pilot
- Grey: additional information and remarks

### Load From simBrief

![From simBrief](../assets/flypados2/load-from-simbrief.png)

If you have [configured](settings.md) your simBrief account correctly, you can click the above button to load your last simBrief flight plan into the flyPad. This does not load the flight plan into the MCDU - you need to load it there separately (see [MCDU simBrief Integration](../../docs/pilots-corner/a32nx/a32nx-beginner-guide/preparing-mcdu.md#a32nx-simbrief-integration)) .

### Map Zoom and Tools

!!! block ""
    ![Zoom Map](../assets/flypados2/zoom-map.png "Zoom Map"){align=left}

    Zooms the map in (+) and out (-).

!!! block ""
    ![Map Tools](../assets/flypados2/map-tools.png "Map Tools"){align=left}

    Distance measurement tools.

    !!! info ""
        Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.

### After loading of a simBrief flight plan

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados2/flypad-dashboard-simbrief.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.3%; top:  7.7%; width: 5.8%; height: 7.6%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 15.6%; width: 5.8%; height: 7.6%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.3%; top: 23.5%; width: 5.8%; height: 7.6%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.3%; top: 31.4%; width: 5.8%; height: 7.6%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.3%; top: 39.3%; width: 5.8%; height: 7.6%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.3%; top: 47.2%; width: 5.8%; height: 7.6%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 55.1%; width: 5.8%; height: 7.6%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.3%; top: 84.1%; width: 5.8%; height: 7.6%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

