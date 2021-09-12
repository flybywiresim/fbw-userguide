# Autopilot Status Annunciators

## Description

This column tells the pilot which Autopilot and which Flight Director is activated. It will also display the status of the Autothrust. 

---

### AP 

This will show which Autopilot is active.

-   AP1  : Autopilot One is active.
-   AP2  : Autopilot Two is active.
-  AP1+2 : Both Autopilots are active.


### FD

This will show which Flight Director is active. 

- 1FD- : Flight Director One is active (Captain's Side).
- -FD2 : Flight Director Two is active (FO's Side).
- 1FD2 : Both Flight Directors are active.
- 1FD1 : Flight Director Two has failed but both Flight Directors are selected on. 
- 2FD2 : Flight Director One has failed but both flight directors are selected on. 

### A/THR

When A/THR is displayed in Cyan text, Autothrust is armed but not active. This means that thrust will be controlled by the thrust lever position. 

Autothrust is armed by:

- Setting the thrust levers to the TO/GA position if at least one Flight Director is active.
- Setting the thrust levers to the FLEX position if at least one Flight Director is active and a FLEX temperature has been entered in the MCDU.
- Pushing the A/THR button when the thrust levers are not in the Climb Position. 

When A/THR is displayed in White Text, Autothrust is Active. This means that thrust will be controlled by the FADEC. (Note: The thrust levers do not move when autothrust is active). 

Autothrust is engaged by:

- Setting the thrust levers to the engagement detent when the Autothrust system is armed.
- Pushing the A/THR button when the thrust levers are in the engagement range (below climb detent with both engines or below MCT with one engine out).
- Activating Alpha Floor.

---

[Back to Flight Mode Annunciators](fma.md){ .md-button }