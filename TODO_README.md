# How

- avoid screenshots for now - use placeholders instead (exception is flight-deck overview)   
  - text, dummy-image or similar A32NX images
- do not add notes to features if available or not. These will still change a lot and we will do it 
  shortly before release
- otherwise use the A32NX docs as a guide for the content - if you think you can improve on the pages 
  in the A32NX docs, feel free to do so for the A380X docs. But we recommend to not make your life 
  unnecessarily difficult

# TODO

1. Navigation restructuring for multiple aircraft
2. Content restructuring for common content for both aircraft
3. Create scaffolding navigation for new aircraft sections
4. Create scaffolding content for new aircraft sections
5. Content creation for new aircraft sections in roughly this priority order:
   1. Beginner Guide 
   2. Update common pages to refer to both projects and aircraft 
      - (e.g. homepage, Overview pages, FAQ, Support Guide, release notes, common questions, Install Guide, etc.)
   3. Common Features (depending on structure) - e.g. EFB, Tiller, and such...)
   4. List will be updated as needed
6. Apply new CSS style to all existing pages


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
  - [ ] Versions
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
  - [ ] Overview
  - [ ] Feature Guides (need a list of available features for early documentation)
  - [ ] Hardware Guides (Limited/Initial)
- [ ] Pilot's Corner
  - [x] Overview
  - [x] A32NX Corner
    - [ ] Beginner Guide
      - [ ] Add Flow Patterns
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

- [ ] Update and add redirects for pages that have been moved or renamed
- [ ] Fix broken links and images
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
  - [ ] Installer
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

