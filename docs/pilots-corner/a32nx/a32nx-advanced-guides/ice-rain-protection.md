# Ice and Rain Protection

The A320 is exposed to many types of weather and atmospheric conditions, both in flight and on the ground. These include icing conditions and heavy rain, both of which could be potentially dangerous to the aircraft if they are not managed appropriately.

!!! note "Definition of Icing Conditions"  

    - Icing conditions exist when the OAT (on ground or after takeoff) or the TAT (in flight) is at or below 10 °C and visible moisture in any form is present (such as clouds, fog with visibility of 1600 m (1 sm) or less, rain, snow, sleet or ice crystals).   
    - Icing conditions also exist when the OAT on the ground and for takeoff is at or below 10 °C and operating on ramps, taxiways, or runways where surface snow, standing water or slush may be ingested by the engines, or freeze on engines, nacelles, or engine sensor probes.
    
To ensure safe and unrestricted operation of the aircraft in these conditions, the ice, and rain protection system has been implemented. This comprises the subsystems listed below:

- [Wing Anti-Ice](#wing-anti-ice)
- [Engine Anti-Ice](#engine-anti-ice) 
- [Window Heat](#window-heat) 
- [Probes Heat](#probes-heat)
- [Rain Removal](#rain-removal)
- [Ice Detection](#ice-detection)

Jump to [Usage of the Ice and Rain Protection System](#usage-of-the-ice-and-rain-protection-system)

## Wing Anti-Ice  

- In flight, hot air from the pneumatic system heats the three outboard slats (3-4-5) of each wing.  
- Air is supplied through one valve in each wing.  
- The WING pushbutton on the ANTI-ICE panel controls the valves.  
- When the aircraft is on the ground, the flight crew can initiate a 30-second test sequence by turning the system ON.  
- If the system detects a leak during normal operation, the affected side’s wind anti-ice valve automatically closes.  
- When wing anti-ice is selected, the N1 or EPR limit is automatically reduced, and the idle N1 or EPR limit is automatically increased.  
- If the electrical power supply fails, the valves close.

## Engine Anti-Ice 

- An independent air bleed from the high-pressure compressor protects each engine nacelle from ice. Air is supplied through a two-position (open and closed) valve that the flight crew controls with two pushbuttons, one for each engine.  
- The valve automatically closes if air is unavailable (engine not running).  
- When an engine anti-ice valve is open, the N1 or EPR limit is automatically reduced and, if necessary, the idle N1 or EPR limit is automatically increased for both engines to provide the required pressure.  
- If electrical power fails, the valves open.

## Window Heat  

- The aircraft uses electrical heating for anti-icing each windshield and demisting the cockpit side windows.  
- Two independent Window Heat Computers (WHCs), one on each side, automatically regulate the system, protect it against overheating, and indicate faults.  

- Window heating comes on:  

      - Automatically when at least one engine is running, or when the aircraft is in flight  
      - Manually, before engine start, when the flight crew switches ON the PROBE/WINDOW HEAT pushbutton

- Windshield heating operates at low power on the ground and at normal power in flight. The changeover is automatic.
- Only one heating level exists for the windows.

## Probes Heat  

- Electrical heating protects:  

      - Pitot heads  
      - Static ports  
      - Angle of Attack (AOA) probes  
      - Total Air Temperature (TAT) probes  

- Three independent Probe Heating Computers (PHCs) automatically control and monitor:  
 
      - Captain probes   
      - F/O probes  
      - STBY probes  

- They protect against overheating and indicate faults.  
- The probes are heated:  

      - Automatically when at least one engine is running, or when the aircraft is in flight  
      - Manually, when the flight crew switches ON the PROBE/WINDOW HEAT pushbutton  

- On the ground, the TAT probes are not heated and pitot heating operates at a low level. The changeover to normal power is automatic.

## Rain Removal

### Wipers

- Each front windshield has a two-speed electric wiper.
- A rotary selector controls each wiper.
- Wipers must never be used on a dry windshield.

### Rain Repellent

- In moderate to heavy rain, the flight crew can spray a rain repellent liquid on the windshield to improve visibility.
- After about 30 seconds, the windows are covered with spray.
- Separate pushbuttons control the rain repellent application on each side of the windshield.
- Rain repellent must never be used to wash the windshield and must never be used on a dry windshield.

## Ice Detection

### Visual Ice Indicator
- An external visual ice indicator is installed between the two windshields. There can also be an external ice detector light.

### Ice Detection System
- The ice detection system has two separate ice detector probes on the forward lower section of the fuselage. The probes detect ice accretion.  
- They also indicate, through the MEMO display, that icing conditions have disappeared. The system logic generates ECAM messages according to the ice detector signals and the flight crew’s selection of engine or wing anti-icing systems.  
- The ice detection system does not control the ENG or WING anti-icing systems.  

## Usage of the Ice and Rain Protection System

See also [Anti Ice Panel](../a32nx-briefing/flight-deck/ovhd/anti-ice.md) and [Wiper Panels](../a32nx-briefing/flight-deck/ovhd/wipers.md)

### WING Anti-Ice pushbutton  

- ON GROUND:  
      - Can only be used for a 30-second test sequence  
- IN FLIGHT: 
      - Must be ON when there is visible airframe icing, either on the visual ice indicator or the wipers  

### ENG 1 + 2 Anti-Ice pushbuttons

- ON GROUND:  
      - Must be ON during all ground operations where icing conditions exist or are anticipated  
- IN FLIGHT:  
      - Must be ON during all flight operations where icing conditions exist or are anticipated, except during climb or cruise when the SAT is below - 40 ᵒC  

### PROBE/WINDOW HEAT pushbutton  

- ON GROUND:  
      - Windows and probes (except TAT probes) are automatically heated when at least one engine is running
- IN FLIGHT:  
      - Windows and probes are automatically heated

### WIPERS  

- ON GROUND:  
      - Set to SLOW/FAST as required if raining  
- IN FLIGHT:  
      - Set to SLOW/FAST as required if raining  

### RAIN RPLNT pushbutton

- ON GROUND:  
      - PUSH as required in moderate to heavy rain
      - Inhibited on ground if engines are not running  
- IN FLIGHT:  
      - PUSH as required in moderate to heavy rain  

!!! info ""
    RAIN RPLNT is currently not available or INOP in the FBW A32NX for Microsoft Flight Simulator

### Other Procedures
- If taxiing in icing conditions, delay the flaps extension until the runway holding point. This prevents contamination in the mechanism.  
- If an approach is made in icing conditions, delay the flaps retraction until the ground crew confirms the flaps and slats are clear of ice.

