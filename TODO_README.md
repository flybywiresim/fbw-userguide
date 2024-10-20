## List of pages/section that need to be migrated from the A32NX docs or completed in general
Changes have been made to this list to better reflect meeting alignment with core team and A380 team. The lists below are "MUST HAVES" before we move forward with a release pipeline (at least on the docs side of things). It will be structured as follows:

- P1 - High Priority (for RC and general public)
  - Requires assistance from dev, pilot insight, and general collaboration to get out the door.
- P2 - Ongoing work
  - As aircraft develops this can be done in tandem or shortly after RC and general release.
- Docs Team - Manadatory for docs team to complete before RC and general release.
  - Clean up and docs structure that will be handled by Docs Maintainers. Contributors can focus on content.

Let's try and avoid duplication where possible.

### P1

- [x] Homepage (serviceable)
- [x] FlyByWire Aircraft Overview
- [ ] FAQ - Further Pending (Val)
- [ ] Installation Guide - cleanup, split section if required, etc.
  - [ ] Overview
  - [x] Versions
    - Add simple versioning table
  - [ ] Installation (TODO: Part 2)
    - Add A380X specific installation links / steps 
  - [x] Settings (minor changes possibly required)
  - [ ] Liveries (TODO)
- [ ] A32NX
  - [x] Overview
  - [ ] Feature Guides - split into a32nx/a380x specific features and common features
  - [x] API
- [ ] A380X
  - [x] Overview - Interim Docs Started
  - [x] Feature Guides (need a list of available features for early documentation)
  - [ ] Hardware Guides - **Coming Soon OK (Limited/Initial)**
- [ ] Pilot's Corner
  - [x] Overview
  - [x] A32NX Corner
    - [x] Beginner Guide - Keeping the Same
      - [ ] Add Flow Patterns - **Optional**
    - [x] A320X Pilot Briefing
      - [x] Flight-Deck
      - [x] MFD
      - [x] PFD
      - [ ] ND
      - [x] EWD
      - [x] SD
      - [ ] FCU
  - [ ] A380X Corner
    - [ ] Beginner Guide - **Important** 
    - [ ] Minor Advanced Guides? - **SEE P2**
    - [ ] A380X Pilot Briefing - **Initial Progress Only / Coming Soon Sections Valid**
      - [ ] Flight-Deck - Basic with all links
      - [ ] Limitations - **IMPORTANT**
      - [ ] MFD - Coming soon OK
      - [ ] PFD - Coming soon OK
      - [ ] ND - Coming Soon OK
      - [ ] EWD - Coming soon OK
      - [ ] SD - Coming soon OK
      - [ ] FCU - Coming soon OK
  - [x] Airliner Corner
    - [x] Airliner Flying Guide
    - [x] Terms and Abbreviations

#### P1 Additional for Beginning Guide
Section is for additional content to match P1 requirements for **Beginner Guide Specifically**.

**Overview**
- [X] Overview page for the A380X Beginner Guide

**Preflight**
Minor internal linking requirements and restructuring.

- [ ] SimBrief guide needs update + New Page
  - [ ] Note: Would exist in `aircraft/A380x/new page here`
- [ ] Discontinuities
  - [ ] Has a page in A380X corner needs updates
  - How is this handled?
- [ ] Payload Management
  - [ ] Fuel and weight - needs guide + new page

**Cockpit Preparation**

Pre-Checks
- [ ]  Flight Deck Overview Link (Add)

Initial Power Up
- [ ]  Image of how to do so (overhead → See Panels)

Fire Test and APU Startup
- [ ]  Location

**Panels**

Requires images in block format for each specific module to include in the cockpit preparation (can be reused later but would be handy to have.

Can see the requirements in the A380X pilot briefing. **All Modules In block format**

- [ ]  Overhead Panel
  - [ ]  Left
  - [ ]  Center
  - [ ]  Right
- [ ]  Main Instrument Panel
- [ ]  Pedestal
- [ ]  Glareshield
- [ ]  Lateral Consoles

Takeoff Briefing

- [ ]  Need before runway Image
- [ ]  Vertical and Lateral Guidance on PFD Image
- [ ]  A380X speedband with V speeds
- [ ]  FCU standard screenshot

Preparing FMS
Straks should be preparing this

Descent Planning

- [ ]  Verify Landing Calc Present in FMS - use simbrief UPDATE NOTICE
- [ ]  BTV Documentation Written
- [ ]  Remove notice to update links in V/S not recommended

Landing

- [ ]  Update aircraft exterior screenshot exiting runway entry markers with full length of the aircraft

After Landing + Powering Down

- [ ]  Repeat of imagery based on landing


### P2

- [ ] Pilot's Corner
    - [x] Advanced Guide
      - [ ] ... / split into a32nx/a380x specific features and common features
  - [ ] A380X Corner
    - [ ] Advanced Guides
      - [ ] Add Go-Around
      - [ ] Add OANS
      - [ ] A380X specific features
    - [ ] A380X Pilot Briefing - **Continue P1 Work**
      - [ ] Flight-Deck
      - [ ] Limitations
      - [ ] MFD
      - [ ] PFD
      - [ ] ND
      - [ ] EWD
      - [ ] SD
      - [ ] FCU
- [ ] A380X
  - [ ] API
  - [ ] Hardware Guides (FULL)

### Docs Team All Phases

- [x] Update and add redirects for pages that have been moved or renamed
- [x] Fix broken links and images
- [ ] Support Guide - cleanup, split section if required, etc.
- [ ] Common Features - Check structure and move if necessary. Also change into card format.
  - [ ] EFB
  - [ ] Tiller
  - [ ] ...
- [x] Release Notes
  - [x] Overview
  - [x] A32NX
  - [x] A380X - No Stable yet Page is ready but hidden
- FlyByWire Tools
  - [x] SimBridge
  - [x] Installer
- [ ] Development Corner
  - check what changes are required in this section
    - Push that back up to P1/P2

## Master List

- [ ] Homepage
- [ ] FlyByWire Aircraft Overview
- [ ] FAQ - Further Pending (Val)
- [ ] Installation Guide - cleanup, split section if required, etc.
  - [ ] Overview
  - [ ] Versions
  - [ ] Installation (TODO: Part 2)
  - [x] Settings
  - [ ] Liveries (TODO)
- [ ] Support Guide - cleanup, split section if required, etc.
- [ ] A32NX
  - [x] Overview
  - [ ] Feature Guides - split into a32nx/a380x specific features and common features
  - [x] API
- [ ] A380X
  - [ ] Overview
  - [ ] Feature Guides
  - [ ] API
- [ ] Common Features
  - [ ] EFB
  - [ ] Tiller
  - [ ] ...
- [ ] Pilot's Corner
  - [x] Overview
  - [x] A32NX Corner
    - [ ] Beginner Guide
      - [ ] Add Flow Patterns
    - [x] Advanced Guide
      - [ ] ... / split into a32nx/a380x specific features and common features
    - [x] A320X Pilot Briefing
      - [x] Flight-Deck
      - [x] MFD
      - [x] PFD
      - [ ] ND
      - [x] EWD
      - [x] SD
      - [ ] FCU
  - [ ] A380X Corner
    - [ ] Beginner Guide
    - [ ] Advanced Guides
      - [ ] Add Go-Around
      - [ ] Add OANS
      - [ ] A380X specific features
    - [ ] A380X Pilot Briefing
      - [ ] Flight-Deck
      - [ ] Limitations
      - [ ] MFD
      - [ ] PFD
      - [ ] ND
      - [ ] EWD
      - [ ] SD
      - [ ] FCU
  - [x] Airliner Corner
    - [x] Airliner Flying Guide
    - [x] Terms and Abbreviations
  - [ ] Development Corner
    - check what changes are required in this section
  - FlyByWire Tools
    - [x] SimBridge
    - [ ] Installer
  - [ ] Release Notes
    - [ ] Overview
    - [x] A32NX
    - [ ] A380X

- [ ] Update and add redirects for pages that have been moved or renamed

