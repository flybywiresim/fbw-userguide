---
title: flyPadOS 3 EFB - Ground
description: A comprehensive guide on how to use the ground services provided by flyPadOS 3 in the FlyByWire A32NX.
---

<link rel="stylesheet" href="../../../../stylesheets/efb-interactive.css">

# flyPad Ground

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-ground.png" style="width: 100%; height: auto;" loading="lazy">
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

## Ground Service

This page allows managing ground operation similar to the in-sim ATC ground services, but without having to use the in-sim ATC.

### Connect Jet Bridge

When standing at a gate, this connects and disconnects the gate's Jetway if one is available at the current gate.

### Door Fwd

Opens and closes the forward door.

### Call Fuel Truck

Calls the fuel truck if available at the current airport. It will take quite a while until the fuel truck arrives. 5-10 minutes is not unusual. When the fuel truck arrives, the MSFS fuel page appears.

!!! warning ""
    We have deactivated the MSFS Fuel Page and you can't use it with the FlyByWire A32NX.
    Fuel and payload should be loaded through the [Fuel](#fuel-page) page only. 

### Call Baggage Truck

Calls the baggage service if available at the current airport and gate. Baggage service will open the cargo door, load baggage and then close the cargo door automatically.

### Connect External Power

Calls a ground power unit (GPU) if available at the current airport and gate or stand. This can be used if there is otherwise no external power available.

### Door Aft

Opens and closes the aft door.

### Call Catering Truck

Calls the catering service if available at the current airport and gate. The catering service will open the aft door and automatically closes it after it has virtually supplied the aircraft.

### Ground Equipment 

See [Wheel Chocks and GSE Safety Cones](../wheel-chocks-cones.md)

For settings, see: [flyPad Sim Options Settings](settings.md#sim-options)

## Fuel Page

The fuel page provides accurate information about the quantity of fuel in the different tanks of the aircraft. It also allows fueling or defueling the aircraft to the desired fuel quantity.

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-ground-fuel.png" style="width: 100%; height: auto;" loading="lazy">
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

### Fuel and De-Fuel

![flyPad Fuel Page Refuel](../../assets/flypados3/fuel-refuel.png "flyPad Fuel Page Refuel")

To set the fuel quantity, simply click into the input field and change the value to the desired quantity.

If you have loaded a SimBrief flight plan, you can import the required fuel directly by pressing the import symbol (cloud with down arrow). 

Press the "play" symbol to start the refueling process (defueling if the new quantity is lower than the current).

### Realism Settings for Fuel Time

![flyPad Fuel Page Fuel Time](../../assets/flypados3/fuel-time.png "flyPad Fuel Page Fuel Time")

Set this setting to the desired duration of refueling. Either instant refueling (Instant - but unrealistic), realistic refuel time (Real) or a middle ground (Fast).

After starting the engines, only "Instant" is available. 

## Payload Page

The Payload page allows setting up the payload of the aircraft, board and deboard passengers and load cargo. 

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-ground-payload.png" style="width: 100%; height: auto;" loading="lazy">
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

See our [Fuel and Weight](../loading-fuel-weight.md#development-version) page for more information on how to set 
up the payload.

### Setting Up Payload
![flypad-ground-payload-values](../../assets/flypados3/flypad-ground-payload-values.png)

This widget allows setting up the payload of the aircraft.

1. Planning
     - Enter the planned number of passengers and weight of cargo here. 
     - You can also enter the planned ZFW (zero fuel weight) here, which will change the other values accordingly.
2. Current
    - Shows the current number of passengers, weight of cargo and ZFW.
    - This will change as passengers board and deboard and cargo is loaded and unloaded.
3. Per Passenger Values
    - Enter the weight of each passenger and the respective baggage weight per passenger.
    - This is used for the calculation of the total weight of passengers and baggage/cargo.
    - Default values (also for SimBrief) are 80 kg for passengers and 24 kg for baggage.
4. Start Boarding/DeBoarding
    - Click on this button to start the boarding/deboarding process.
    - The process will take 5 s/1 s/0 s per passenger depending on the [Boarding/Loading Time setting](#configure-boardingloading-time).
    - The current number of passengers and weight of cargo will change accordingly. 
5. Deboard Now
    - Click on this button to deboard all passengers and unload all cargo.
    - The process will take 5 s/1 s/0 s per passenger depending on the [Boarding/Loading Time setting](#configure-boardingloading-time).
6. Load Payload Values from SimBrief
    - The values for the number of passengers, weight of cargo and ZFW can be imported from the SimBrief flight plan.
    - Make sure to have imported the flight plan on the [flyPad Dashboard page](dashboard.md).
7. Switch Zero-Fuel-Weight and Gross Weight
    - This will switch between ZFW/ZFWCG and GW/GWCG, the percentage for calculation is changed automatically.

### Configure Boarding/Loading Time
![flypad-ground-payload-loadingtime](../../assets/flypados3/flypad-ground-payload-loadingtime.png)

This widget allows configuring the boarding/loading time.

* Instant: will directly load all passengers and cargo without any delay.
* Fast: will load 1 passenger every 1 s.
* Real: will load 1 passenger every 5 s.

### Center of Gravity Diagram
![flypad-ground-payload-cgenvelope](../../assets/flypados3/flypad-ground-payload-cgenvelope.png)

This shows the CG and ZFWCG envelope of the aircraft. The current CG is sown in cyan and the ZFWCG is shown in white.

These current value indicators move during boarding and deboarding and loading and unloading of cargo.

### Interactive Seating and Cargo Diagram
![flypad-ground-payload-seatscargo](../../assets/flypados3/flypad-ground-payload-seatscargo.png)

This widget shows the planned and current loading of the cabin and cargo visually. 

It also allows changing the loading by clicking on the seats or cargo areas.

- Click on seats to plan to board/deboard individual passengers.
- Click on the cargo areas to plan to change cargo and cargo distribution.
- Click on the boarding/deboarding button to start the process.

The current cabin and cargo area layout of the A32NX consists of:

- 174 Seats in 4 passenger areas 
    - A = rows 1-6
    - B = rows 7-13
    - C = rows 14-21
    - D = rows 22-29
- 4 Cargo areas
    - Forward Baggage Container
    - Aft Baggage Container
    - Aft Baggage
    - Aft Bulk Loose
## Pushback

{--

The flyPadOS 3 pushback system is, in general, incompatible with other pushback add-ons as they all use the same sim variables and will conflict with each other.

See [Pushback System On/Off](#pushback-system-onoff).

--}

<div style="position: relative;">
    <img src="/fbw-a32nx/assets/flypados3/flypad-ground-pushback.png" style="width: 100%; height: auto;" loading="lazy">
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

The flyPad pushback system provides comfortable pushback from within the cockpit using buttons or controllers and the built-in map.

!!! tip
    Use your controller's rudder and elevator axis to steer!

!!! tip
    The flyPad's pushback system can be remotely controlled by using the A32NX's API. 
    See [Pushback API](../../a32nx-api/a32nx-flightdeck-api.md#pushback-api).

### Pushback System On/Off

As pushback add-ons all use the same sim variables to control and move the aircraft during pushback the flyPad pushback system and these add-ons usually cannot not be used at the same time. Because of this, the flyPad pushback system can be disabled completely to avoid any interference with other pushback add-ons.

!!! block ""
    ![img.png](../../assets/flypados3/flypad-pushback-system-off.png){align=center width=49% loading=lazy}
    ![img_1.png](../../assets/flypados3/flypad-pushback-system-on.png){align=center width=49% loading=lazy}

A warning message will appear if you enable the system to remind users of these potential incompatibilities.

External add-ons can recognize the flyPad pushback system and also deactivate it if they choose to do so by reading/setting this LVAR variable: `L:A32NX_PUSHBACK_SYSTEM_ENABLED`.

### Call/Release Tug

Pressing this button will call and attach the pushback tug or release it in case it was already attached.

!!! warning "Tug Animation"
    From the perspective of the aircraft, the tug appears to be immediately attached. This is a sim issue, as the tug's animation is not in sync with the tug-attached signal to the aircraft. This also allows to pushback immediately, although the visual tug is not yet connected to the aircraft.
    <p />
    To overcome this limitation the sim's pushback tug model would need to be changed which would conflict with other pushback add-ons which use this method. We have therefore decided not to implement this at this time.

When releasing the tug, the button will stay amber until the pushback pin is removed and the ECAM memo "NW STRG DISC" has disappeared (~15sec). The aircraft cannot be steered with the nose wheel steering pin installed.

!!! block ""
    ![img.png](../../assets/flypados3/flypad-pushback-tugcall.png){align=center width=32% loading=lazy}
    ![img_2.png](../../assets/flypados3/flypad-pushback-tugwait.png){align=center width=32% loading=lazy}
    ![img_1.png](../../assets/flypados3/flypad-pushback-tugrelease.png){align=center width=32% loading=lazy}

### Parking Brake

Convenience button to set or release the parking brake while using the pushback system.

### Forward/Backward

The forward and backward buttons control the speed of the pushback tug.

The `Forward` button changes the speed in forward direction:

- increase speed when already moving forwards
- decrease speed when moving backwards

The `Backward`button is vice versa.

### Pause Movement

Pauses all movement and resets speed and direction to zero.

### Left/Right

The `Left` and `Right` buttons control the direction of the tug-aircraft movement.

`Left` changes the direction towards the left:

- more left when already in a left turn
- less right when in a right turn

`Right` is vice versa.

### Tug Direction Slider

The tug direction slider can be dragged with the mouse to quickly set the desired direction.

### Tug Speed Slider

The tug speed slider can be dragged with the mouse to quickly set the desired speed.

### Using Rudder and Elevator Control for Pushback

You can use the standard sim rudder axis control for steering left and right.

You can use the standard elevator axis (pitch) for controlling the speed of the pushback tug.

### Map

The pushback map allows executing the pushback without leaving the cockpit view. It depicts the airport and ground markings so that a precise pushback can be accomplished.

!!! block ""
    ![img_5.png](../../assets/flypados3/flypad-pushback-mapzoom.png){align=left width=5% loading=lazy}    
    <p />
    The map allows zooming in and out as require using the zoom buttons.


!!! block ""
    ![img_7.png](../../assets/flypados3/flypad-pushback-map-aircraft-icon-filled.png){align=left width=5% loading=lazy}
    ![img_8.png](../../assets/flypados3/flypad-pushback-map-aircraft-icon-outlined.png){align=left width=5% loading=lazy}
    <p />
    If the aircraft symbol is filled, the map is in centered aircraft mode and moves with the aircraft movement.
    If it is outlined, the map is fixed and the aircraft symbol is moving.
    <p />
    The map can also be dragged and moved with the mouse. To reset the map to be centered on the aircraft, press the aircraft symbol.

!!! block ""
    ![img_6.png](../../assets/flypados3/flypad-pushback-map-turn-prediction.png){align=left width=15% loading=lazy}
    <p />
    The map also features a turn prediction indicator, providing a visual aid while turning. 

### Pushback API

See [Pushback API](../../a32nx-api/a32nx-flightdeck-api.md#pushback-api) for details.
