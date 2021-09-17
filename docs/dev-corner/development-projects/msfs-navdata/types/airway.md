# Airway
Airport data can be loaded through `Database.getAirways(idents: string[]): Airway[]`

property                | type              | example   | description
------------------------| ------------------|-----------|-----------
ident                   | `string`          | A1        | Identifier of the airway
databaseId              | `string`          | ERJ    A1 | Unique database item identifier
icaoCode                | `string`          | RJ        | Region code of the airway (2 Letter)
level                   | `AirwayLevel`     | 0: All    | Level of the airway (All, High, or Low)
fixes                   | `Waypoint[]`      | [...]     | Array of fixes within the given airway
turnRadius?             | `NauticalMiles`   | undefined | Turn radius of transitions between legs within the given airway
rnp?                    | `NauticalMiles`   | undefined |
direction               | `AirwayDirection` | 0: Either | Direction through which the airway can be flown(Either, Forward, Backward)
minimumAltitudeForward  | `Feet`            | 8000      | Minimum altitude when flying the airway forward
minimumAltitudeBackward | `Feet`            | null      | Minimum altitude when flying the airway backward
maximumAltitude         | `Feet`            | 99999     | Maximum altitude when flying the airway  
