# SimBrief Integration

## Flight Planning

Flying IFR (Instrument Flight Rules) even in a simulation like Microsoft Flight Simulator always requires some level of flight planning.

In addition to the obvious route planning there are several other aspects which are critical to any good flight plan:

- Route Planning
    - Origin and Destination
    - Runways, SID and STAR
    - Compliance with ATC Requirements
    - Routing and Constraints
- Fuel Calculation
- Weather Forecast
- Cost and Time Optimization

See [Flight Planning](https://en.wikipedia.org/wiki/Flight_planning){target=new} on Wikipedia for more information.

Microsoft Flight Simulator tries to offer a simple way to do route planning (World Map before starting a flight) this is falls short, especially for users wanting a more realistic experience for airliner flying.

In real life airlines and pilots use dedicated software alongside various sources and services for creating their flight plans.

In the world of flight simulation simBrief does all that for the users based on real word databases and sources. SimBrief provides on average ~40.000 flight plans to users each day and is the most commonly used tool for flight planning for non-professional flight simulation.

It is absolutely possible to use the simBrief OFP (Operational Flight Plan) to configure and program the aircraft based on it without any special integration into the flight sim software or aircraft.

But as in real world aircraft it is common in flight simulation aircraft to integrate these systems directly with the aircraft's flight management system to be able to import all the relevant planning data. This includes the route, altitudes, constraints, fuel, payload (passengers, cargo), and other data points.

This is why FlyByWire has implemented our simBrief integration and will continue to improve this experience even further in the future.

### Flight Planning with SimBrief

This is best explained by simBrief itself: [simBrief User Guide](https://www.simbrief.com/system/guide.php){target=new}

---

## Using the flyPad simBrief Integration

### Setup A32NX simBrief Integration

See [Setup simBrief Integration](flyPad/settings.md#simbrief-integration)

### Importing the simBrief OFP to the flyPad

See [flyPad Guide - Load from simBrief](flyPad/dashboard.md#load-from-simbrief)

See [flyPad Guide - OFP](flyPad/dispatch.md#ofp-page) on how to view the simBrief Operational Flight Plan.

---

## Using the FMS (MCDU) and simBrief Integration

### Importing the simBrief OFP to the FMS (MCDU)

We've included a quick method to have your simBrief OFP automatically loaded into the MCDU. Please do not select an arrival airport on the MSFS world menu otherwise the integration will not work.

This portion of the guide assumes that you understand how to generate a simBrief OFP.

#### ^^SimBrief MCDU Setup^^

Enter your simBrief username. Upon entering your username the MCDU will convert it into an ID number. Please ensure you have no special characters in your username OR use the ID number found before generating your OFP.

* Click on `MCDU MENU`
* Click on `OPTIONS`
* Click on `AOC`
* Click on `SIMBRIEF`

#### ^^Request Data from simBrief^^

* Return to `MCDU MENU`
* Click on `ATSU`
* Click on `AOC MENU`
* Click on `INIT/PRESS`
* Click on `INIT DATA REQ`

![mcdu2](../../pilots-corner/assets/beginner-guide/mcdu/mcdu2.png){loading=lazy}

This will prepare the MCDU to input the flight plan.

#### ^^Load Fuel and Payload^^

Go back to the AOC menu.

* Click on `PERF/W&B`

![mcdu3](../../pilots-corner/assets/beginner-guide/mcdu/mcdu3.png){loading=lazy}

Here you can automatically load your fuel + passenger / cargo weights. You are presented with the `Fuel Page` first then the `Weights and Balance` page.

* Press LSK5L to instantly load your planned simBrief fuel. (The load button will flash momentarily).
* You can verify fuel has loaded by looking at your upper ECAM FOB.

Using the horizontal slew keys you can switch to the weights and balance page.

* Again press LSK5L to instantly load your planned payload and pax.
* You can verify the weight has changed by looking at the lower ECAM towards the lower right-hand side.

!!! info "Customizing Fuel and Weights"

    You can adjust the amount of fuel or payload weight manually on these pages. Type in your desired amounts and press the relevant LSK to input it into that field. 

    When you are happy with your changes press `LOAD` using LSK5L to load your custom fuel and weight.

#### ^^Initialize Flight Plan^^

Head over to the `INIT A` page.

* Select `INIT REQUEST` by pressing LSK2R

This will load your flight plan from simBrief directly into the MCDU

![mcdu1b](../../pilots-corner/assets/beginner-guide/mcdu/mcdu1b.png){loading=lazy}

To learn how to set up the MCDU you can read the [**^^F^^**LIGHT PLAN](../../pilots-corner/beginner-guide/preparing-mcdu.md#flight-plan) section in our beginner's guide.