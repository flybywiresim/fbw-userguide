# Experimental Version

!!! danger "No Support for Experimental - use at own risk"
    Please do not seek support for the Experimental Version on Discord and only report issues if you have read this page and the reported and known issues. You can report issues in the Discord channel "#ata-22-fms" in the thread "[CFMS LNAV ONLY Bugs + Issues](https://discord.com/channels/738864299392630914/876140343735771147/882442909918584862){ target=new }".

---

## FlyByWire Custom Flight Management System (cFMS)

### Features

- Flight plan manager overhaul
- Edit SID/STAR/APPR waypoints
- Cross-track error indicator
- USR waypoints are gone
- Multiple leg types
    - TF: Track to a Fix defines a great circle track over ground between two known databases fixes.
    - RF: Constant Radius Arc defines a constant radius turn between two database fixes, lines tangent to the arc and a center fix.
    - VM: Heading to a manual termination defines a specified heading until a Manual termination.
- LNAV turn prediction
- Roll anticipation distance
- Correct procedure and direct-to sequencing
- Improved flight plan rendering / drawing

### Known Issues

*Last Update: {{git_revision_date_localized}}*

- Approach Phase must be manually activated (MCDU PERF)
- Only 3 leg types (TF, RF and VM) are supported at this time
- WX and TERR on ND INOP
- ARPT, VOR, NDB, WPTs filters INOP on ND
- May encounter runaway sequencing issues
- Sequencing also may not be aggressive enough at times
- Rendering of terminal procedure legs may be incorrect during flight
- No traffic shown, TCAS is INOP, elements are cosmetic only
- EFB Rate of descent now no longer syncs with ND
- MCDU flight plan INIT DEPARTURE/ARRIVAL page is sometimes cleared when DIRECT-TO is used
- Defining both from/to in MSFS Flight Planner (World Map) do show in the from/to init page but do not populate the airport list in METAR
- Flight plans defined in the MSFS Flight Planner (World Map) are loaded to the cFMS
- Any changes to the cFMS flight plan will not be synced back to the MSFS flight plan manager for now
- Built-in ATC will not be supported with the cFMS for now.

### How to Report Issues

At this time please only report issues via our Discord channel "#ata-22-fms" in the thread "[CFMS LNAV ONLY Bugs + Issues](https://discord.com/channels/738864299392630914/876140343735771147/882442909918584862){ target=new }".

!!! warning
    Please read the above Known Issues list and also use the search of  Discord to see if your issue has already been reported.

**Do not open any issues on Github for the Experimental Version!**

<!--### Download and Install-->

<!--See [Installation Guide](../installation.md#downloads).-->

---

!!! danger "No Support for Experimental - use at own risk"
    Please do not seek support for the Experimental Version on Discord and only report issues if you have read this page and the reported and known issues. You can report issues in the Discord channel "#ata-22-fms" in the thread "[CFMS LNAV ONLY Bugs + Issues](https://discord.com/channels/738864299392630914/876140343735771147/882442909918584862){ target=new }".
