# FlyByWire A32NX API

This section is aimed at sim pilots who want to use external hardware or software to connect to the FlyByWire A32NX to read values and control the aircraft.

## General

Many sim pilots want to use dedicated hardware or specific software to control their aircraft which goes beyond just the normal flight stick and maybe controller for thrust.

The hardware alone is not sufficient to control aircraft in Microsoft Flight Simulator (or any sim). A software is required to tell the sim what the different levers (axis) and buttons shall do.

Most hardware (or software) vendors therefore ship their products with a driver for their hardware which translates hardware input into software commands which are then sent to the simulator.

The problem with this approach is that for this to work all aircraft need to actually use the same software commands (API) for this to work on any aircraft. For Microsoft Flight Simulator this has been achieve by most default aircraft delivered with MSFS itself.

Unfortunately the API used (Simconnect, MSFS API) is not able to handle more complex aircraft and in addition there are other limitations which would go beyond this guide to explain.

To make it possible for 3rd party aircraft to go beyond these limitation Microsoft Flight Simulator enables aircraft builders to create their own API, most commonly in the form of so called LVARS and Events.

All of the major custom aircraft on the market use this possibility. So not only the FlybyWire A32NX does this but e.g. the Aerosoft CRJ, PMDG DC-6, Working Titles CJ4 mod, Justflight PA-28 Arrow, etc.

All these advanced aircraft have in common that any standard drivers for hardware (or software) controllers are not able to use the additional aircraft APIs (variables and events).

Therefore, much to the frustration of users many hardware controllers do not correctly work with these aircraft.

But there are solutions to this problem.

## Solutions

To solve the issue described above there are several software solutions which basically replace any default hardware drivers. These solutions take the hardware inputs and translate them into the correct software requests to the simulator for the current aircraft.

The main feature of these solutions is that the hardware/software mapping is highly configurable and even programmable and in some cases even with a nice and user friendly interface.

**Example:**

So, for example the standard software command for the landing lights is the Simconnect event "LANDING_LIGHTS_ON".

But the Aerosoft CRJ aircraft requires these variables:

```
    - set ASCRJ_OVHD_LDG_LEFT -> 1  
    - set ASCRJ_OVHD_LDG_NOSE -> 1  
    - set ASCRJ_OVHD_LDG_RIGHT -> 1
```

The mentioned software solutions would then enable the user to map a hardware landing light button to these three aircraft specific variables instead of using the default Simconnect event.

The FlyByWire A32NX also requires specific variables to control its advanced features. The documentation for these variables and events can be found here: [A32NX API Documentation](lvars-events.md)

The most common software solutions are:

- [SPAD.neXt](https://www.spadnext.com/home.html){target=new}
- [FSUIPC](http://www.fsuipc.com/){target=new}
- [Axis and Ohs](https://axisandohs.weebly.com/){target=new}

For SPAD.neXt we have some example configurations for common hardware controllers: [Common hardware with SPAD](hardware.md)

## Common Hardware Controllers

See [Common Hardware](hardware.md)







