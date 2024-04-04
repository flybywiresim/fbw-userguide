# Powering Down

This guide will explain the correct procedures to power down the aircraft when at the gate after arriving at the destination and taxi to the designated gate.

Obviously, this is not strictly required in a simulator, but for interested sim pilots this might be an interesting process for a more realistic experience.

!!! warning "Disclaimer"
    The level of detail in this guide is meant to help a FlyByWire A320neo beginner to correctly shut down the aircraft.

    A *beginner* is defined as someone familiar with flying a GA aircraft or different types of airliners. Aviation terminology and know-how is a requirement to fly any airliner, even in Microsoft Flight Simulator.

    Check out the FlyByWire YouTube Channel as well: [FlyByWire on YouTube](https://www.youtube.com/c/FlyByWireSimulations/playlists){target=new}

    You will find many great videos on YouTube on how to fly the FlyByWire A32NX.<br/>

---

## Prerequisites

- Aircraft is at the gate after landing and taxi as per previous chapters.

[Download FlyByWire Checklist](../assets/sop/A32NX%20Documentation/FBW%20A32NX%20Checklist.pdf){ .md-button }

## Chapters / Phases

This guide will cover these phases:

1. [Parking at the Gate](#1-parking-at-the-gate)
2. [Disembarking Passengers and Baggage](#2-disembarking-passengers-and-baggage)
3. [Securing the Aircraft](#3-securing-the-aircraft)

---

## Preface
Shutting down and securing an aircraft is an important part of the overall procedure. Obviously, less important in a simulator, as the next flight will have the aircraft start in a cold and dark state again.

If we want to actually do a turn around and start a new flight directly, the procedure will be a little different, as we would not turn off certain systems and at some point simply start with the preparation of the aircraft procedure again.

## 1. Parking at the Gate

**Situation**

- We arrived at the designated gate after taxiing from the runway where we landed.
- Aircraft is in taxi state as per previous chapters.
- Engines are still running.
- Lights are still in taxi configuration (`RWY TURN OFF` set to on and `NOSE` is to taxi, `LAND`-ing lights are off).
- `APU` has been turned on during taxi and is `AVAIL`, `APU BLEED` is off.
- **After Landing** checklist is completed.


**At the gate:**

![EDDM at gate](../assets/beginner-guide/powering-down/eddm-at-the-gate.png "EDDM at gate"){loading=lazy}

**Steps after arriving at the gate:**

- Set parking brake (`PARK BRK`).

    ![Parking Brake](../assets/beginner-guide/powering-down/parking-brk.png "Parking Brake"){loading=lazy}

- `NOSE TAXI` and `RWY TURN OFF` lights are usually turned off even before we turn into the gate to not blind the ground personnel. This, of course, is only done if enough lighting is available to safely park into the gate. Turn them off if they were used while parking.

    ![Taxilights off](../assets/beginner-guide/powering-down/lights-taxi-off.png "Taxilights off"){loading=lazy}

- Turn on `APU BLEED` before we turn off the engines.

    ![APU BLEED ON](../assets/beginner-guide/powering-down/apu-bleed-on1.png "APU BLEED ON"){loading=lazy width=20%}

- Shut down the engines by setting the `ENG 1` and `ENG 2` master switches to off.

    ![Engines off](../assets/beginner-guide/powering-down/engine-off.png "Engines off"){loading=lazy }

- Wait until `N1` is below 5 %.

    ![Engines N1 under 5 %](../assets/beginner-guide/powering-down/ENG-N1-u5.png "Engines N1 under 5 %"){loading=lazy width=50%}

- Turn off `Seat Belt` sign.

    ![Seat Belt Sign off](../assets/beginner-guide/powering-down/seatbelts-off.png "Seat Belt Sign off"){loading=lazy width=20%}

- Turn off `BEACON` (leave `NAV & LOGO` on as long as the aircraft has power from external or APU, `STROBES` can remain on AUTO).

    ![All_Ext_LT_off](../assets/beginner-guide/powering-down/beacons-off.png){width=20%}

- Complete **Parking** checklist.

    ![Parking Checklist](../assets/beginner-guide/powering-down/Parking-checklist.png "Parking Checklist"){loading=lazy width=50%}

If external power were available, the ground crew would have connected it by now, and we can turn on `EXT PWR`. Turning off the APU depends on the turn around time. For a shutdown, we do this after the passengers have disembarked to still have airflow in the cabin. See last chapter.

This concludes *Parking at the Gate*.

## 2. Disembarking Passengers and Baggage

**Situation:**

- **Parking** checklist is completed.

In real life, there are many things that begin automatically after parking at the gate. The Jetway is connected to the aircraft, doors are opened, passengers disembark, cargo is unloaded, etc. The pilots don't have to do much to trigger these steps.

In the simulator, though, we would have to trigger them by ourselves. For this, we use the FlyByWire flyPad's ground functionality or the Microsoft Flight Simulator's built-in ATC to start these procedures. There are also some nice add-on tools out there which help with this.

Taking care of passengers and luggage with the FlyByWire flyPad:

- Go to the flyPad (view can be activated by `Ctrl+0`).
- Connect the Jetway (PAX).
- Call cargo/baggage (Baggage).

![flyPad Ground page](../../../aircraft/a32nx/assets/flypados3/flypad-ground.png){loading=lazy}

Obviously, this would take a while in real life, and we would not be able to shut down the aircraft before everybody is disembarked.

For a turn around we would start preparing the aircraft for the next flight and the cabin crew would coordinate everything from disembarking the passengers, cleaning and resetting the cabin.

After refueling, the pilot would signal the cabin crew that they could let the new passengers board the aircraft once the cabin is ready.

This concludes *Disembarking Passengers and Baggage*.

## 3. Securing the Aircraft

**Situation:**

- **Parking** checklist is completed.
- Aircraft is empty (no passengers or cargo).
- Cabin is cleaned and ready for shutdown.

**To secure the aircraft, we follow these steps: **

- Turn off all fuel pumps.

    ![Fuel pumps off](../assets/beginner-guide/powering-down/fuel-pumps-off.png "Fuel pumps off"){loading=lazy width=80%}

- Turn off the `ADIRS`.

    ![ADIRS OFF](../assets/beginner-guide/powering-down/adirs-off.png "ADIRS OFF"){loading=lazy }

- Turn off `OXYGEN`.

    ![OXYGEN Crew Supply off](../assets/beginner-guide/powering-down/crewoxyhighlight.png "OXYGEN Crew Supply off"){loading=lazy}

- Turn off `APU BLEED`.

    ![APU BLEED OFF](../assets/beginner-guide/powering-down/apu-bleed.png "APU BLEED OFF"){loading=lazy width=20%}

- Turn off emergency exit lights `EMER EXIT LT` and no smoking lights `NO SMOKING`.

    ![Signs off](../assets/beginner-guide/powering-down/passenger-signs.png "Signs off"){loading=lazy}

- Optional or depending on airline SOPs: Reset air conditioning, lighting, and screen brightness.
- Turn off `APU MASTER` (expect the APU to still be AVAIL for a few minutes if you also had APU Bleed on shortly before, as it needs a cool down period).

    ![APU Master off](../assets/beginner-guide/powering-down/apu-master-off1.png "APU Master off"){loading=lazy width=20%}

- Wait 2 minutes for the APU FLAP door to close before you turn off the power, as this requires either APU or external power.
- Turn off `EXT PWR` if it has been turned on before

    ![External Power off](../assets/beginner-guide/powering-down/ext-power-off.png "External Power off"){loading=lazy width=20%}

- Turn off `NAV & LOGO` lights (as the aircraft no longer has power).

    ![NAV & LOGO off](../assets/beginner-guide/powering-down/nav-logo-off-1.png "NAV & LOGO off"){loading=lazy width=20%}

- Turn off `BAT 1` and `BAT 2`.

    ![Batteries off](../assets/beginner-guide/powering-down/batteries-off.png "Batteries off"){loading=lazy width=70%}

Now the aircraft is back in a cold and dark state.

This concludes *Securing the Aircraft*

