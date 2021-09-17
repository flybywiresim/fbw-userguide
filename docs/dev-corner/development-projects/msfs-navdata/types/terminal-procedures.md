# Terminal Procedures
Terminal Procedures are procedures in and out of airports: Departure(sids), Arrival(stars), Approach(iaps)

### ProcedureTransition
property | type             | example | description
---------|------------------|---------|------
ident    | `string`         | LAM     | Identifier of the transition
legs     | `ProcedureLeg[]` | [...]   | Array of legs in the transition

property            | type                                 | example      | description
--------------------|--------------------------------------|--------------|----------
ident               | `string`                             | LAM          | Leg Identifier
databaseId          | `string`                             | PEGEGLLI27L5 | Unique database identifier of the leg
icaoCode            | `string`                             | EG           | Region code of the leg (2 Letter)
procedureIdent      | `string`                             | I27L         | Identifier of the procedure this leg is part of
type                | `LegType`                            | 10: FD       | The type of leg, Path and Termination
overfly             | `boolean`                            | false        | Is this an overfly waypoint leg
waypoint?           | `Waypoint`                           | {...}        | The reference Waypoint of the leg if the Leg Type requires one
recommendedNavaid   | `VhfNavaid or NdbNavaid or Waypoint` | undefined    | Navaid used as reference for arc or fixed radius turns
rho?                | `NauticalMiles`                      | 0            | Distance from the recommended navaid, to the waypoint
theta?              | `DegreesMagnetic`                    | 0            | Magnetic bearing from the recommended navaid, to the waypoint
arcCentreFix?       | `Waypoint`                           | null         | Defines the arc for RF legs
arcRadius?          | `NauticalMiles`                      | 11           | Defines the radius for RF legs
lenght?             | `NauticalMiles`                      | null         | Defines the radius for RF legs
lengthTime?         | `Minutes`                            | undefined    | length if it is specified in distance, exact meaning depends on the leg type, mutually exclusive with lengthTime
rnp?                | `NauticalMiles`                      | null         |
transitionAltitude? | `Feet`                               | null         | Transition Altitude in the location of this leg(Only present on IF legs)
altitudeDescriptor  | `AltitudeDescriptor`                 | 1: AtAlt1    | Specifies the meaning of the altitude1 and altitude2 properties
altitude1?          | `Feet`                               | 7000         | altitudeDescriptor property specifies the meaning of this property
altitude2?          | `Feet`                               | null         | altitudeDescriptor property specifies the meaning of this property
speed?              | `Knots`                              | 220          | The exact meaning of this is coded in the speedDescriptor property
speedDescriptor?    | `SpeedDescriptor`                    | 2: Maximum   | Specifies the meaning of the speed property
turnDirection?      | `TurnDirection`                      | 0: Unknown   |
magneticCourse?     | `DegreesMagnetic`                    | 273          | Heading/Course to be flown during Legs which require a specific heading/course


### Approach
property    | type                      | example     | description
------------|---------------------------|-------------|-----------
ident       | `string`                  | I27L        | Identifier of the Approach
icaoCode    | `string`                  | EG          | Region code of the approach (2 Letter)
databaseId  | `string`                  | PEGEGLLI27L | Unique database item identifier
type        | [ApproachType](common.md) | 5: ILS      | The type of the Approach
transitions | `ProcedureTransition[]`   | [...]       | Array of transitions into the Approach
legs        | `ProcedureLeg[]`          | [...]       | Array of Common legs in the approach
missedLegs  | `procedureLeg[]`          | [...]       | Array of missed approach legs in the approach

### Departure
property           | type                    | example      | description
-------------------|-------------------------|--------------|----------------------------
ident              | `string`                | BPK7F        | Identifier of the departure
databaseId         | `string`                | PEGEGLLBPK7F | Unique databaseId of the departure
icaoCode           | `string`                | EG           | region code of the departure (2 Letter)
runwayTransitions  | `ProcedureTransition[]` | [...]        | List of runway transitions on the departure
commonLegs         | `ProcedureLeg[]`        | []           | Legs present on the departure not dependant on transitions
enrouteTransitions | `ProcedureTransition[]` | []           | List of enroute transitions on the departure
engineOutLegs      | `ProcedureLeg[]`        | []           | List of engine out legs on the departure

### Arrival
property           | type                    | example      | description
-------------------|-------------------------|--------------|----------------------------
ident              | `string`                | LAM1X        | Identifier of the Arrival
databaseId         | `string`                | PEGEGLLLAM1X | Unique databaseId of the Arrival
icaoCode           | `string`                | EG           | region code of the Arrival (2 Letter)
enrouteTransitions | `ProcedureTransition[]` | []           | List of enroute transitions on the Arrival
commonLegs         | `ProcedureLeg[]`        | []           | Legs present on the Arrival not dependant on transitions
runwayTransitions  | `ProcedureTransition[]` | [...]        | List of runway transitions on the Arrival
