# Airport
Airport data can be loaded through `Database.getAirportByIdent(ident: string): Airport`

property                 | type                           | example                 | description
-------------------------|--------------------------------|-------------------------| -------
ident                    | `string`                       | KDFW                    | 4 Letter identifier of the airport
databaseId               | `string`                       | A      KDFW             | Unique database item identifier
icaoCode                 | `string`                       | K4                      | ICAO region Code (2 letter)
airportName              | `string`                       | DALLAS-FT WORTH INTL    | Public name of the airport
location                 | `Location`                     | lat: 33 lon: alt: 606   | Reference location of the airport
speedLimit?              | `Knots`                        | 250                     | Airspeed limit at airport
speedLimitAltitude?      | `Feet`                         | 10000                   | Altitude up until which the speed limit applies
transitionAltitude?      | `Feet`                         | 18000                   | Transition Altitude in the airports location
transitionLevel?         | `FlightLevel`                  | 180                     | Transition Level in the airports location
longestRunwaySurfaceType | [RunwaySurfaceType](common.md) | 1: Hard                 | Surface type of the longest runway at airport
