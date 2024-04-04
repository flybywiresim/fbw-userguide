# Engine Manual Start and N1 Mode Panel

---

[Back to Flight Deck](../index.md){ .md-button }

---

![Engine Manual Start an N1 Mode](../../../assets/a32nx-briefing/overhead-panel/eng-man-start.jpg "Engine Manual Start an N1 Mode")

## Usage

!!! info ""
    Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.

### ENG MAN START

!!! info ""
    Currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator.

- ON:
    ‐ Starts manual start sequence of the associated engine, if the ENG MODE selector is set to IGN/START, or
    ‐ Starts wet crank process of the associated engine, if the ENG MODE selector is set to CRANK and the ENG MASTER lever is set to ON, or
    ‐ Starts dry crank process of the associated engine, if the ENG MODE selector is set to CRANK and the ENG MASTER lever is set to OFF.

- Off:
    ‐ Stops the manual start sequence of the associated engine, if the ENG MODE selector is set to IGN/START and the ENG MASTER lever is set to OFF, or
    ‐ Stops the dry crank process of the associated engine, if the ENG MODE selector is set to CRANK and the ENG MASTER lever is set to OFF.

### ENG N1 MODE

!!! info ""
    These buttons do not exist in an A320neo with LEAP or PW1100 engines. They are exclusively for the CEO IAE V2500 engines. As these buttons are part of Asobo's Default A320 3D model, they are still visible and can't be removed at this time.

    They are INOP in the FlyByWire A32NX. 

If the aircraft is equipped with IAE engines, there are two additional guarded N1 MODE indicator switches. N1 mode is used for changing the thrust control between EPR and N1 (abnormal situation).

- N1 RATED MODE:
    - In the N1 rated mode, the FADEC controls engine N1 as a function of thrust lever position, temperature, and altitude while preventing the engine from exceeding operating limits. Thrust is controlled in the same manner as in the normal mode, without auto-thrust. Place the thrust lever in the TO/GA detent to obtain TO/GA thrust, the MCT detent to obtain MCT thrust, and the CL detent to obtain climb thrust.

- N1 UNRATED MODE:
    - In the N1 unrated mode (N1 DEGRADED mode on ECAM) the FADEC controls engine N1 as a function of thrust lever position only. The thrust lever detents do not provide limit protections; over boost is possible. With one engine in the N1 rated mode, the N1 of the unrated engine should be matched with the N1 of the rated engine (the thrust levers may not be aligned). If both engines degrade to the N1 unrated mode, N1 limit values in the Takeoff Performance, Climb Performance, and Landing Performance chapters must be used.

---

[Back to Flight Deck](../index.md){ .md-button }
