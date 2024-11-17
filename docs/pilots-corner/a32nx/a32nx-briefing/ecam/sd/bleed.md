# ECAM Bleed page

[Back to ECAM System Display Overview](index.md){ .md-button }

![ECAM SD Bleed page](../../../assets/a32nx-briefing/ecam/bleed.png "ECAM SD Bleed page")

| Number | Name                               | Variation        | Meaning                                                                                                                                               |
|:-------|:-----------------------------------|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1      | Pack outlet temperature            | Green color      | It is in the normal temperature range.                                                                                                                |
|        |                                    | Amber color      | The temperature is higher than 90 °C.                                                                                                                 |
| 2      | Pack RAM AIR inlet                 | Green crossline  | The flap is closed.                                                                                                                                   |
|        |                                    | Amber in transit | The flap is partially open.                                                                                                                           |
|        |                                    | Amber inline     | The flap is fully open on ground.                                                                                                                     |
|        |                                    | Green inline     | The flap is fully open in flight.                                                                                                                     |
| 3      | Pack turbine bypass valve position | C                | The valve is closed (Cold).                                                                                                                           |
|        |                                    | H                | The valve is open (hot).                                                                                                                              |
| 4      | Pack compressor outlet temperature | Green color      | The temperature is in the normal range.                                                                                                               |
|        |                                    | Amber color      | The temperature is above 230 °C.                                                                                                                      |
| 5      | Pack flow                          | Green color      | Pack flow control valve is open.                                                                                                                      |
|        |                                    | Amber Color      | Pack flow control valve is closed.                                                                                                                    |
| 6      | Pack flow control valve            | Green inline     | Pack flow control valve is open.                                                                                                                      |
|        |                                    | Amber inline     | Pack flow control valve is open but isn’t coordinated with the control position.                                                                      |
|        |                                    | Green crossline  | Pack flow control valve is fully closed.                                                                                                              |
|        |                                    | Amber crossline  | Pack flow control valve is fully closed but is not coordinated with the control position.                                                             |
| 7      | User indication                    | Green color      | The RAM air flap is fully open, and both pack flow controls valves are open.                                                                          |
|        |                                    | Amber color      | The RAM air flap is not fully open, and both pack flow controls valves are closed.                                                                    |
| 8      | High-Pressure valves               | Green crossline  | The high-pressure valve is fully closed.                                                                                                              |
|        |                                    | Amber crossline  | The high-pressure valve position is not coordinated with the control position.                                                                        |
|        |                                    | Green inline     | The high-pressure valve is partially closed.                                                                                                          |
| 9      | Engine bleed valves                | Green crossline  | The bleed valve is fully closed                                                                                                                       |
|        |                                    | Amber crossline  | The bleed valve is not coordinated with the control position.                                                                                         |
|        |                                    | Green inline     | The bleed valve is open.                                                                                                                              |
|        |                                    | Amber inline     | The bleed valve is not coordinated with the control position.                                                                                         |
| 10     | Precooler inlet pressure           | Green color      | The pressure is within normal operation range.                                                                                                        |
|        |                                    | Amber color      | The pressure is either under 4 psi, or if the pressure is over 57 psi.                                                                                |
| 11     | Precooler outlet temperature       | Green color      | The temperature is within normal operation range.                                                                                                     |
|        |                                    | Amber color      | The temperature is lower than 150 °C, or exceeds temperature over 290 °C for 5 seconds, or 270 °C for 15 seconds, or 257 °C for 55 seconds.           |
| 12     | APU Bleed valve                    | Green crossline  | The APU master switch is ON, and the APU valve is partially open.                                                                                     |
|        |                                    | Amber crossline  | The APU master switch is ON, the APU bleed switch is ON, and the APU valve is closed.                                                                 |
|        |                                    | Green inline     | The APU master switch is ON, and the APU valve is open.                                                                                               |
| 13     | Crossbleed valve                   | Green crossline  | The crossbleed valve is closed.                                                                                                                       |
|        |                                    | Amber crossline  | The crossbleed valve is not coordinated with the control position.                                                                                    |
|        |                                    | Green inline     | The crossbleed valve is open.                                                                                                                         |
|        |                                    | Amber inline     | The crossbleed valve is not in the control position.                                                                                                  |
|        |                                    | Amber transit    | The crossbleed valve is in transit.                                                                                                                   |
| 14     | High-Pressure ground connection    | Green            | The high-pressure ground connection is connected.                                                                                                     |
|        |                                    | Hidden           | The high-pressure ground connection is not connected.                                                                                                 |
| 15     | Anti-Ice indication                | Appear in white  | The wing pushbutton on the anti-ice panel is ON.                                                                                                      |
|        |                                    | Hidden           | The wing pushbutton on the anti-ice panel is off.                                                                                                     |
| 16     | Arrow                              | Appear in green  | The corresponding valve is open.                                                                                                                      |
|        |                                    | Appear in amber  | The corresponding valve is open and the air pressure is low or high, or the aircraft is on the ground and the valve is open for more than 10 seconds. |
|        |                                    | Hidden           | The corresponding valve is closed.                                                                                                                    |
| 17     | Engine indication                  | White            | The corresponding engine is in normal operation.                                                                                                      |
|        |                                    | Amber            | The corresponding engine N2 is below idle.                                                                                                            |

