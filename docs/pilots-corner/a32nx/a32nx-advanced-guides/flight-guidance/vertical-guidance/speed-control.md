# Speed/Mach Control
In flight, either the AP/FD pitch control, or Autothrust may acquire and hold a target speed or Mach number, depending on the engaged modes.

Speed control is:

‐ Managed when the target comes from the FMGS.
‐ Selected when the target comes from the SPD/MACH FCU window.

## Managed Speed/Mach Target
Managed Speed/Mach target is engaged when:

- the SPD/MACH knob is pushed
- EXP mode engaged
- V2 is inserted into the MCDU PERF page
- SRS mode is engaged (SRS will not engage if V2 is not set in the MCDU PERF page)
- The TCAS mode is engaged.

Managed Speed/Mach disengages if a target speed is selected in the FCU by pulling the knob, or if a preselected speed was configured in the MCDU PERF pages.

Managed speed accounts for all speed constraints in the flight plan when the lateral navigation NAV is enabled.
Otherwise, any speed constraints are ignored.

The speed profile when NAV is enabled is as follows: V2, SPD LIM, SPD CSTR (if applicable), ECON CLB SPD/MACH, ECON CRZ MACH, ECON or preset DES MACH/SPD, SPD LIM, SPD CSTR (if applicable), HOLD SPD (if applicable), V~APP~.

The speed profile when NAV is not enabled is as follows: V2, SPD LIM, ECON CLB SPD/MACH, ECON CRZ MACH, ECON or preset DES MACH/SPD, SPD LIM - V~APP~.

In managed mode the AP and FD pitch modes can control a target SPD/MACH or a vertical trajectory, and the A/THR mode can control a fixed thrust or a target SPD/MACH. However, the AP/FD and the A/THR cannot both control a target SPD/MACH simultaneously.

Therefore, the AP/FD pitch modes and A/THR mode are coordinated as follows:

‐ If an AP/FD pitch mode controls a vertical trajectory, the A/THR mode controls the target SPD/MACH.
‐ If an AP/FD pitch mode controls a target SPD or MACH, the A/THR mode controls the thrust.
‐ If no AP/FD pitch mode is engaged, the A/THR mode reverts to controlling the SPD/MACH mode.

| AP/FD Pitch Modes                               | A/THR Modes          |
|-------------------------------------------------|----------------------|
| V/S - FPA                                       | SPEED/MACH MODE      |
| DES (geometric path)                            | SPEED/MACH MODE      |
| ALT*, ALT, ALT CRZ*. ALT CRZ, ALT CST*, ALT CST | SPEED/MACH MODE      |
| G/S*, G/S                                       | SPEED/MACH MODE      |   
| FINAL. FINAL APP                                | SPEED/MACH MODE      |
| TCAS                                            | SPEED/MACH MODE      |
| FD/AP OFF                                       | SPEED/MACH MODE      |
| CLB/DES (idle path)                             | THR (CLB, IDLE) MODE |
| OP CLB/OP DES                                   | THR (CLB, IDLE) MODE |
| EXP CLB/EXP DES                                 | THR (CLB, IDLE) MODE |
| SRS                                             | THR (CLB, IDLE) MODE |
| FLARE                                           | RETARD (IDLE)        |

## Selected Speed/Mach Target
To use a selected Speed/Mach target, the flight crew uses the knob on the FCU to set the target speed, which is then displayed in the FCU window. It is also displayed in blue on the PFD speed scale.

Selected speed has priority over managed speed. The only automatic change-over from selected to managed speed target may occur at go-around mode engagement. In flight, if the situation calls for managed speed, both the PFD and the MCDU display a message proposing a manual change to managed speed (for example, SET MANAGED SPEED, SET HOLD SPEED, or SET GREEN DOT SPEED).

The selected Speed/Mach target mode activates when:

- the SPD/MACH knob is pulled
- both AP/FDs are off
- the next phase has a preselected speed configured in the corresponding MCDU PERF page
- the flight management target is lost or the FMGC is powered up during flight

