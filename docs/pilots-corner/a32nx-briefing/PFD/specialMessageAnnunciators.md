---
hide:
    - navigation
---

# Common Mode and Special Message Annunciators

These two types of annunciators are displayed on both columns two and three. 

Special Message annunciators displays three types of messages (in the order of priority):

- Flight controls messages
- Vertical flight management messages
- EFIS reconfiguration messages

Common mode annunciators display the common flight modes. 

---

## Special Message Annunciators

### MAN PITCH TRIM ONLY

Displayed with red text. Displayed when there is a loss of both left and right elevators. 

### USE MAN PITCH TRIM

Displayed with amber text. Displayed when the flight controls are in direct law. 

### CHECK APP SEL

Displayed with white text. Displays when the aircraft is in cruise at less than 100 nautical miles from the top of descent or in descent or in approach and:

- A non ILS approach has been selected.
- An ILS frequency is tuned on the radio navigation page. 

### SET MANAGED SPD

Displayed with white text. Displays when the speed target is selected but a preselected speed does not exist for the next flight phase. 

### SET GREEN DOT SPD

Displayed with white text. Displays when the aircraft is in engine out mode and the speed target is selected. This message will be displayed if the FCU selected speed is:

- Less than or equal to the green dot speed minus 10kts or
- Greater than or equal to the green dot speed plus 10kts (except when the aircraft is in ALT\* mode or ALT mode).

### SET HOLD SPD

Displayed with white text. Displays when the aircraft is in selected speed control, a holding pattern has been inserted into the MCDU flight plan and the aircraft is 30 seconds out from the deceleration point to the the computed hold speed. 

### DECELERATE

Displayed with white text. Displays if the thrust is not reduced when the aircraft is passing the top of descent point, and the aircraft is above the descent profile. 

### MORE DRAG

Displayed with white text. Displays when descent mode is engaged, idle is selected, and:

- Either the aircraft is above the vertical profile and the predicted intercept point of the profile is at less than 2 nautical miles away from the next altitude constraint or
- In auto speed control and the aircraft enters a speedbrake decelerating segment. 

### VERT DISCON AHEAD

Displayed in amber text. Displays when descent mode is engaged and:

- A vertical path too steep exists on the next leg .
- The aircraft is less than 30 seconds from the path that is too steep. 

---

## Common Mode Annunciators

### LAND 

Displayed with green text. Displays when land mode is engaged below 400 feet (radio altitude).

### FLARE 

Displayed with green text. Displays when flare mode is engaged. 

### ROLL OUT 

Displayed with green text. Displays when roll out mode is engaged. 

### FINAL APP

Displayed with green text. Displays when APP NAV and Final modes are engaged during a non ILS approach. 

---

[Back to Flight Mode Annunciators](..\PFD\FMA.md){ .md-button }





