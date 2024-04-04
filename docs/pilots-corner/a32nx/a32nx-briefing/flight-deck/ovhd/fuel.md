# Fuel Control Panel

---

[Back to Flight Deck](../index.md){ .md-button }

---

![FUEL Control Panel](../../../assets/a32nx-briefing/overhead-panel/Fuel-Panel.jpg "FUEL Control Panel")

!!! note "API Documentation: [Fuel Panel API](../../../../../aircraft/a32nx/a32nx-api/a32nx-flightdeck-api.md#fuel-panel)"

## Description

Total Fuel Capacity:

- Two outer tanks: 1760 liters (1408 kg)
- Two inner tanks: 13 849 liters (11 079 kg)
- One center tank: 8250 liters (6600 kg)

The tanks empty in the following sequence :

1. Center tank
2. Inner tanks (down to 750 kg in each inner tank)
3. Outer tanks (fuel transferred into the inner tanks)

Each engine is fed by their corresponding center and wing tanks. The pumps stay turned on during the flight.

Both engines can be fed from one side, or both sides can feed only one engine.

## Usage

###  L + R TK PUMPS 1 + 2

- ON:
    - Pump is on.
- OFF:
    - Pump is OFF and the button lights up a white OFF.
- FAULT:
    - Amber light and ECAM caution appear, when the pressure drops and the pump is not OFF.

### MODE SEL

- AUTO:
    - Automatic control of transfer valves from center to inner tanks, if the CTR TK PUMP are set to ON/AUTO
        - Valves open if inner tank level is 500 kg below inner tank capacity.
        - Valves close when the inner tank is full or 5 minutes after the center tank low fuel level (130 kg) is reached.
- MAN:
    - Manual control of center tank valve to inner tanks with center tank pumps button switches.
- FAULT:
    - Amber light and ECAM caution appear, when the left or right-wing tank has less than 5000 kg (11 000 lb) and the center tank has more than 250 kg (550 lb).

### CTR TK PUMP 1 + 2

!!! note ""
     The A320NEO doesn't have traditional pumps for the center tank anymore. These have been replaced with jet pumps. Only the valves to the pumps can be controlled by the flight crew. The current aircraft model used by the FlyByWire A32NX has incorrect labels.

- ON/AUTO:
    - Valve is open if MAN mode is selected with the MODE SEL pushbutton switch. The pump is automatically controlled when AUTO mode is selected.
- OFF:
    - Valve is closed and the OFF button lights up white.

### X FEED

- OFF:
    - Valve closes (no light).
- ON:
    - Valve opens.
- OPEN:
    - When the valve is fully open, a green light comes on.

---

[Back to Flight Deck](../index.md){ .md-button }

