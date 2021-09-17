# Database

The database class is the interface between the FMS and the navdata backend. When Initialising a Database you must parse in a Backend for the database to use.
`Please Note: All functions on the database class are asyncronous`

### `getAirportByIdent(ident: string): Airport`
This will load the first airport found from the current Backend with a given identifier

### `getRunways(airportIdentifier: string, procedure?: Departure | Arrival): Runway[]`
This will load all runways at a given airport, this result can be narrowed down by parsing in a Departure or Arrival procedure in order to return only runways which are compatible with the given procedure.

### `getDepartures(airportIdentifier: string, runwayIdentifier?: string): Departure[]`
This will load all departures at a given airport, this result can be narrowed down by parsing in a runwayIdentifier in order to only return departures which are compatible with the given runway.

### `getArrivals(airportIdentifier: string, approach?: Approach): Arrival[]`
This will load all arrivals at a given airport, this result can be narrowed down by parsing in an Approach in order to only return arrivals compatible with the given Approach

### `getApproaches(airportIdentifier: string, arrival?: Arrival): Approach[]`
This will load all approaches at a given airport, this result can be narrowed down by parsing in an Arrival in order to only return Approaches compatible with the given Arrival
