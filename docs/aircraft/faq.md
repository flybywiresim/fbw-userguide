---
title: FlyByWire Aircraft - Common Questions 
description: Frequently Asked Questions about the FlyByWire Aircraft, detailing features, installation, and troubleshooting.
---

## General

<p style="color:yellow; font-size:18px;">TODO: Add 380 directory/filenames</p>

???+ info "Q: Where is the plane in-sim?"
    Both of our aircraft are searchable in the aircraft selection menu. 

    - The A32NX is listed as `FlyByWire Simulations A320neo (LEAP)`

    - The A380X is listed as `TBD`

    !!! tip "A32NX"
        The A32NX is a separate aircraft from the default Asobo A320. 

        Please esnure you have selected aircraft `FlyByWire Simulations A320neo (LEAP)` instead of the Asobo variant in the 'aircraft selection' menu before loading the flight.

??? info "Q: Can I download the aircraft in the current state?"
    Yes, see [Downloads](install/installation.md#downloads).

??? info "Q: How do I install this aircraft?"
    Visit our [Installation Guide](install/installation.md).

??? info "Q: What liveries are available?"
    We recommend downloading compatible liveries from [Flightsim.to](https://flightsim.to/c/liveries/flybywire-a32nx/){target=new}.

    **NOTE:** Liveries for the default A320neo are incompatible with the A32NX. 
<p style="color:yellow; font-size:18px;">TODO: Verify other directories for airframe or if we're moving this</p>
??? info "Q: Do we have a simBrief profile for our aircraft?"
    Yes, there is one available for all versions of our aircraft. You can find how to use it [here](a32nx/feature-guides/simbrief.md##simbrief-airframe).

??? info "Q: When will it be released?"
    The project is an ongoing rolling release. See [Downloads](install/installation.md#downloads).

??? info "Q: When is the next update?"
    We don't know when the next update will be, however you can keep track of development via commit logs and Stable release logs.

    [A32NX Information](install/fbw-versions.md){.md-button}

    [A380X Information](#){.md-button}

<p style="color:yellow; font-size:18px;">TODO: Joining team restructure</p>
??? info "Q: How do I join the team?"
    Head over to [A32NX Development Overview](../dev-corner/dev-guide/index.md) and join our Discord to get started.

??? info "Q: Is it payware?"
    No, it is a completely free and open-source aircraft.

<p style="color:yellow; font-size:18px;">TODO: Change this depending on Server restructure</p>
??? info "Q: How do we report bugs?"
    Report bugs to us in the [Discord server](https://discord.gg/flybywire){target=new}, under the `#a32nx-support` channel, or by creating a [GitHub issue](https://github.com/flybywiresim/aircraft/issues/new/choose){target=new}.

    Just make sure to search for existing issues first before creating a new one.

??? info "Q: Why is my version not the same as what I see others using?"
    We have two versions: Stable and Development.

    **Stable**

    The Stable version is a 'snapshot' of the development which we regard as stable with the current version of the simulator. See [Downloads](installation.md#downloads).

    **Development**

    The Development build is updated daily and is a constant work in progress and although we test each update thoroughly, minor issues may occur from time to time. See [Downloads](installation.md#downloads).

[//]: # (??? info "Q: What is the Experimental Version?")

[//]: # (    Please read more [here]&#40;support/exp.md&#41;.)

---

## A32NX Quick FAQ

???+ info "Q: I cannot hear the Flaps or PTU in the cockpit anymore?"
    This change was made due to feedback from IRL A320 pilots who identified the sounds could not be heard from the cockpit IRL as they currently are in the simulator.

    The PTU has a toggleable switch on the EFB (flyPad) settings that allows you to hear it in the cockpit when it is running.

[//]: # (??? info "Q: Which lights should I turn on during taxi/takeoff/flight?")

[//]: # (    There are many fantastic tutorials online which demonstrate the proper use of lighting on the A320neo, take a look at this video from 320 Sim Pilot:)

[//]: # ()
[//]: # (    ![video-embed]&#40;https://www.youtube.com/embed/L9XUHepoFDg&#41;)

??? info "Q: Is the Hold function implemented yet?"
    Yes - the Hold function is available in the MCDU. 

??? info "Q: Why is the overall interior lighting different? (Blue light effect on pedestal and displays)"
    Based on IRL A320 pilot feedback, the blue light effect can only be seen from images. Also, the pedestal should be dark at night to improve pilots' vision at night.

??? info "Q: Why does light bleed into the cockpit? Can this be fixed?"
    Unfortunately, no - This is a more profound issue which will require work from the Asobo team.

??? info "Q: The new sounds are different from the default ones, why?"
    The default sounds were shared sounds from other default aircrafts. The new sounds are accurate and very well-developed based on the A320 and A320neo pilot feedback.

