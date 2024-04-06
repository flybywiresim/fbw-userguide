---
title: flyPadOS 3 EFB - Dashboard
description: A comprehensive guide on how to use the Dashboard widgets in flyPadOS 3 for the FlyByWire A32NX.
---

<link rel="stylesheet" href="/stylesheets/efb-interactive.css">

# flyPad Dashboard

<div style="position: relative;">
    <img src="/aircraft/a32nx/assets/flypados3/flypad-dashboard.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

## Description

The Dashboard is the default flyPad page after starting it.
    
## Usage

### Widgets

The Dashboard provides several widgets to allow quick access to specific information and pages.

The provided widgets are: 

- Weather:
    - METAR weather information - see [Weather Widget](#weather-widget)
- Pinned Charts:
    - Navigation charts from the [Navigation page](charts.md) can be pinned and displayed here
- Checklists:
    - Specific checklists according to the current flight phase ([Checklists page](checklists.md))
- Maintenance:
    - Shows active failures from the [Failures page](failures.md) 

![Widgets Rearrange](../../assets/flypados3/widgets-rearrange.png)

By clicking on the edit symbol (pen) the widgets can be rearranged as required by the user. 

### Weather Widget

The Weather widget shows the current METAR information of either the simBrief imported airports or manually entered airports.

You can type in any airport ICAO-code into the input fields to get the corresponding METAR information. To get back to the simBrief imported airports, simply delete the manually entered ICAO.

You can switch between the weather summary which shows the most important METAR parts with icons or a raw view of the METAR information.

Selected METAR information is updated every 5 minutes.

![ICAO Input to Weather Widget](../../assets/flypados3/weather-widget-input.png "ICAO Input to Weather Widget"){loading=lazy}

We have applied a helpful coloring scheme a large European airline uses to point out significant parts of the raw METAR information to the pilots. This coloring uses the following colors:

- Cyan: Chosen airport ICAO
- White: standard value with no special concern
- Amber: highlights significant values as a caution to the pilot
- Red: highlights very significant values as a warning to the pilot
- Grey: additional information and remarks

### Pinned Charts Widget

![img_4.png](../../assets/flypados3/pinned-charts-widget.png)

Any pinned charts from the [Navigation page](charts.md#pinned-charts) will be shown here. 
Clicking on a chart card brings up the corresponding chart. 

### Checklist and Maintenance Widget

![img_5.png](../../assets/flypados3/checklist-maintenance-widget.png)

This shows relevant checklists in relation to the current flight phase.
Clicking on a checklist card brings up the corresponding checklist.

### Load From simBrief

![From simBrief](../../assets/flypados3/load-from-simbrief.png)

If you have [configured](settings.md) your simBrief account correctly, you can click the above button to load your last simBrief flight plan into the flyPad. This does not load the flight plan into the MCDU - you need to load it there separately (see [MCDU simBrief Integration](../../../../pilots-corner/a32nx/a32nx-beginner-guide/preparing-mcdu.md#a32nx-simbrief-integration)).

It is also possible to configure the flyPad to automatically load the latest SimBrief data.<br/>
See [ATSU / AOC Settings](settings.md#atsuaoc)

### After loading of a simBrief flight plan 

<div style="position: relative;">
    <img src="/aircraft/a32nx/assets/flypados3/flypad-dashboard-simbrief.png" style="width: 100%; height: auto;" loading="lazy">
    <a href="../dashboard/">   <div class="imagemap" style="position: absolute; left: 1.7%; top:  6.9%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dashboard</span></div></a>
    <a href="../dispatch/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 14.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Dispatch</span></div></a>
    <a href="../ground/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 21.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Ground</span></div></a>
    <a href="../performance/"> <div class="imagemap" style="position: absolute; left: 1.7%; top: 28.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Performance</span></div></a>
    <a href="../charts/">      <div class="imagemap" style="position: absolute; left: 1.7%; top: 35.6%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Navigation & Charts</span></div></a>
    <a href="../online-atc/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 43.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Online ATC</span></div></a>
    <a href="../failures/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 50.1%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Failures</span></div></a>
    <a href="../checklists/">  <div class="imagemap" style="position: absolute; left: 1.7%; top: 57.3%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Checklists</span></div></a>
    <a href="../presets/">     <div class="imagemap" style="position: absolute; left: 1.7%; top: 64.7%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Presets</span></div></a>
    <a href="../settings/">    <div class="imagemap" style="position: absolute; left: 1.7%; top: 85.0%; width: 5.8%; height: 7.0%;"><span class="imagemapname">Settings</span></div></a>
    <span class="imagesub">Click on the menu icons in this image to see other flyPad pages.</span>
</div>

