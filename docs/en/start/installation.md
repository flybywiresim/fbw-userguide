# Installation guide

Please follow the information on this page to install the FlyByWire Simulations A32NX addon for Microsoft Flight Simulator 2020

*Last Update: {{git_revision_date_localized}}*

!!! warning "Important Notice"

    All FlyByWire Simulations A32NX versions are now independent from the default A320neo.

    We’d like to remind all users of the following two **important changes**:

    The folder in the Community directory is now:

      - `flybywire-aircraft-a320-neo`

    The airplane in the simulator is now titled:

      - `FlyByWire Simulations - A320neo (LEAP)`

!!! info "Marketplace Version Incompatibility"
    The A32NX on the MSFS  marketplace is incompatible with any of our installer / standalone versions.

    You must **choose** one of the options below:

    - The marketplace version installed
    - One of the branches from our installer/website.  

    If you're an existing user and want to benefit from our regular updates, you should stay on the version you fly already or download using the options below to keep the plane up to date:

    - [FlyByWire Installer](#flybywire-installer)
    - [FlyByWire Simulations website](https://flybywiresim.com)

---

## Downloads

### FlyByWire Installer

Download the new FlyByWire installer where you can select either the Stable, Development, or Experimental build. Our installer downloads and installs the mod directly into your community folder.

The following commands can be used:

++ctrl+f5++ - Refreshes Installer

++ctrl+f12++ - Opens the debug tool

You can send us logs to our [Discord](https://discord.gg/flybywire) for support if you encounter issues with the installer. Please follow the steps below:

  * In the debug tool find and select ++"Console"++ in the top menu.

  * `Right Click` anywhere in the log displayed.

  * Click ++"Save as"++ and send the log to us.

[Download Installer](https://api.flybywiresim.com/installer){ .md-button }

---

### Traditional Download Methods

!!! info "Methods"

    === "Latest Stable Version"

        **How to download**:

        **Current Stable Version - v0.6.1**

          Stable is our variant that has the least bugs and best performance. This version will not always be up to date but we gurantee its compatibility with each major patch from MSFS. 

          [Download Stable](https://api.flybywiresim.com/api/v1/download?url=https://flybywiresim-packages.b-cdn.net/stable/A32NX-stable.zip){ .md-button }

          You can see the changelog on the releases page: [View Here](https://github.com/flybywiresim/a32nx/releases)


    === "Development Version"

        **How to download**:

        Development will have the latest features that will end up in the next stable. Bugs are to be expected. 

        It updates whenever something is added to the 'master' branch on GitHub. 

         [Download Development](https://api.flybywiresim.com/api/v1/download?url=https://flybywiresim-packages.b-cdn.net/vmaster/A32NX-master.zip){ .md-button }
         
         [**IMPORTANT:** View information on Autopilot / Fly-By-Wire here](autopilot-fbw.md)

    === "Experimental Version"

        **How to download**:

        This version is similar to the development version, but contains custom systems. 

        Experimental is currently on **hold**. 

        **No support will be provided via Discord.**

        [Download Experimental](https://api.flybywiresim.com/api/v1/download?url=https://flybywiresim-packages.b-cdn.net/vmaster-cfbw-cap/A32NX-master-cfbw-cap.zip){ .md-button }

        [**IMPORTANT:** view warnings and info for the experimental version here](https://github.com/flybywiresim/a32nx/tree/autopilot/docs)

---
## Manual Installation

**Please follow ALL steps in this section if you encounter any issues with installation before seeking support.**

Open the zip that you downloaded from one of the links above, and drag the `flybywire-aircraft-a320-neo` folder inside the zip into your Community folder.

See below for the location of your Community folder:

---

### Microsoft Store and/or Game Pass edition

- Copy the `flybywire-aircraft-a320-neo` folder into your community package folder.

It is located in:

* `C:\Users\[YOURUSERNAME]\AppData\Local\Packages\Microsoft.FlightSimulator_<RANDOMLETTERS>\LocalCache\Packages\Community`.

---

### Steam edition

- Copy the `flybywire-aircraft-a320-neo` folder into your community package folder.

It is located in:

* `C:\Users\[YOUR USERNAME]\AppData\Roaming\Microsoft Flight Simulator\Packages\Community`.

---

### Boxed edition

- Copy the `flybywire-aircraft-a320-neo` folder into your community package folder.

It is located in:

* `C:\Users\[YOUR USERNAME]\AppData\Local\MSFSPackages\Community`.

---

### Troubleshooting

If the above methods do not work:

- You can find your community folder by going into Microsoft Flight Simulator general options and enabling developer mode. You will see a menu appear on top.
    - Go to tools and virtual file system.
    - Click on watch bases and your community folder will be listed in one of the folders.

If your issue is not related to installation visit - [**Reported Issues**](reported-issues.md)

---

## Clean Install Steps

To perform a clean install you simply have to delete the `flybywire-aircraft-a320-neo` folder from your community folder.

We do however store additional information related to the aircraft in a separate directory. Delete the contents of this folder but not the folder itself.

These locations can be found below.

![localstate folder](https://cdn.discordapp.com/attachments/838062729398976522/869736690695172156/unknown.png){ width=70% }

!!! info "Work Folder"
    The locations below contain a "work" folder. We store two important things here that you may not want to delete:

    - Your EFB throttle configuration.
    - Our flight data recorder (for debugging purposes which we may ask you to provide).

    **It is up to you to keep this folder or not.**

To access the folders below:

- Press start.
- Type in run into the start menu and press ++enter++
- Type into the box either `%localappdata%` or `%appdata%` depending on your game version below.
- Press ++"OK"++

If the folders are hidden to you follow the directions on [Microsoft's support site](https://support.microsoft.com/en-us/windows/view-hidden-files-and-folders-in-windows-10-97fbc472-c603-9d90-91d0-1166d1d9f4b5).

### Microsoft Store Version

The folder can be found here:

`%LOCALAPPDATA%\Packages\Microsoft.FlightSimulator_8wekyb3d8bbwe\LocalState\packages\flybywire-aircraft-a320-neo\`

!!! warning ""
    This is not your community directory

### Steam Version

The folder can be found here:

`%APPDATA%\Microsoft Flight Simulator\Packages\flybywire-aircraft-a320-neo\`

!!! warning ""
    This is not your community directory

***

## Contributing

[:fontawesome-brands-github:{: .github } **GitHub Contributing.md**](https://github.com/flybywiresim/a32nx/blob/master/.github/Contributing.md){ .md-button }

More info [A32NX Development Overview](../en/a32nx-dev/overview.md)

***

## SimBrief Airframe

SimBrief now has a dedicated airframe for the A320neo.

- Select `A20N - A320-251N` for your aircraft type.

You may also select the FlyByWire Simulations SimBrief airframe with correct weights which is available below.

✈ [SimBrief Airframe Link](https://www.simbrief.com/system/dispatch.php?sharefleet=eyJ0cyI6IjE2MjAyMTYxMzY2MjciLCJiYXNldHlwZSI6IkEyME4iLCJjb21tZW50cyI6IkZCVyBBMzJOWCIsImljYW8iOiJBMjBOIiwibmFtZSI6IkEzMjBORU8gRkJXIiwiZW5naW5lcyI6IkxFQVAtMUEyNiIsInJlZyI6IkQtQUZCVyIsImZpbiI6IiIsInNlbGNhbCI6IiIsImhleGNvZGUiOiIiLCJjYXQiOiJNIiwicGVyIjoiQyIsImVxdWlwIjoiU0RFMkUzRkdISUoxUldYWSIsInRyYW5zcG9uZGVyIjoiTEIxIiwicGJuIjoiQTFCMUMxRDFPMVMyIiwiZXh0cmFybWsiOiIiLCJtYXhwYXgiOiIxODAiLCJ3Z3R1bml0cyI6IktHUyIsIm9ldyI6IjQxMDA1IiwibXpmdyI6IjY0MzAwIiwibXRvdyI6Ijc5MDAwIiwibWx3IjoiNjc0MDAiLCJtYXhmdWVsIjoiMTkwNDUiLCJwYXh3Z3QiOiIxMDQiLCJkZWZhdWx0Y2kiOiIiLCJmdWVsZmFjdG9yIjoiUDAwIiwiY3J1aXNlb2Zmc2V0IjoiUDAwMDAifQ--) Credits: [@viniciusfont](https://github.com/viniciusfont)

Pilot ID can be found in the Optional Entries section of the Dispatch Options page.

