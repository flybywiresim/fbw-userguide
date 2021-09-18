# Appendix A - Fuel and Weight

## Overview

This short appendix describes appropriate loading of fuel and weights for the A32NX to ensure that you have the correct center of gravity (CG) configured for the aircraft.

## Zero Fuel Weight - CG

The A32NX simBrief integration's auto-loading feature allows for automated CG configuration. The auto population of ZFW and ZFWCG on the INIT B page will accurately reflect what simBrief has configured when you have generated an OFP. You can read about INIT B configuration [here](preparing-mcdu.md#init-b).

While trimming the aircraft can be optional, we recommend pilots continue to trim their aircraft based on the reported CG value on INIT B or on your simBrief OFP prior to takeoff. Doing this can prevent any sort of early nose-up action during takeoff roll.

!!! warning "Mistrimming"
    It is a requirement that attempting a takeoff with the maximum amount of mistrim that would not result in a takeoff configuration warning must not result in unsafe flight characteristics or a marked increase in takeoff distance (generally interpreted as a 1% increase).

## Center of Gravity

An acceptable range of ZFWCG in the A32NX is between 16-40%. Ideally, anything less than 25% CG is considered FWD load, and anything more than 25% is considered an AFT load.

!!! info "Demerits of FWD Favoring Load"
    The more forward the CG (25 or less):

    - The higher the tail down force.
    - The higher the lift necessary to maintain the flight.
    - The higher the minimum speed (Vs1g) necessary to maintain the flight.
    - The higher the drag.
    - The higher the fuel consumption.
    - The lower the takeoff and landing performance.

    These demerits coincidentally describe the counter benefits of having an AFT favored load.

For a single-aisle aircraft like the A32NX there is virtually no effect of CG position on fuel consumption. ==Having an AFT favored load does provide better takeoff / landing performance.==  

    