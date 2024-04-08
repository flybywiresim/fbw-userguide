# MCDU Web Interface

<link rel="stylesheet" href="/../../stylesheets/web-mcdu.css">

!!! danger "STOP"
    This documentation is applicable for **STABLE** versions only. If you are using the Development or Experimental version please refer to our SimBridge Documentation instead.

    ---

    **Development/Experimental Version**

    [SimBridge Guides](../../../simbridge){.md-button}
    
    [Remote MDCU (Updated Version of this Page)](../../simbridge/remote-displays/remote-mcdu.md){.md-button} 

## Overview

The MCDU Web Interface allows you to display and control the MCDU on a browser including browsers on mobile devices like phones or tablets.

See list of compatible and tested browsers: [Compatible Browsers](#compatible-browsers)

!!! note "MCDU Web Interface"
    ![Web MCDU Interface](../docs/aircraft/a32nx/assets/mcdu-server/web-mcdu-ipad.webp "Web MCDU Interface"){loading=lazy}

It also allows you to use your real printer as a cockpit printer for the MCDU.

## Starting the MCDU Web Interface

### Start the MCDU Web Interface Server

To be able to use the MCDU Web Interface you need to start the web server which will provide the application to your browser.

To do this locate the `flybywire-aircraft-a320-neo` folder in your MSFS Community folder. Within this folder you will find a folder called `MCDU SERVER`. Open this folder.

![MCDU Server Folder](../docs/aircraft/a32nx/assets/mcdu-server/mcdu-server-folder.png "MCDU Server Folder"){loading=lazy}

![MCDU Server Executable](../docs/aircraft/a32nx/assets/mcdu-server/mcdr-server.exe.png "MCDU Server Executable"){loading=lazy}

Double-click on the `server.exe` file to start the MCDU Server.

!!! tip "You can also use the command prompt to start the server manually"
    See advanced startup options below: [Advanced Start Options](#advanced-start-options)

Once started the MCDU Server application will ask if you want to use your real printer instead of the virtual printer in the cockpit.

If you choose to use your real printer then press ++y++, after which you need to select which printer you want to use. The MCDU Server will list all printers available in your Windows.

If you do not want to use your printer select ++n++.

After this the MCDU Server will start and will provide you with links for your local browser to access the MCDU Web Interface.

**You will need to keep this window open and the MCDU Server running to use the MCDU Web Interface**.

![MCDU Server Command Window](../docs/aircraft/a32nx/assets/mcdu-server/mcdu-server-cmd-window.png "MCDU Server Command Window"){loading=lazy}

### MCDU Server Connection Attempts Timeout

Due to issues in the Microsoft Flight Simulator Coherent Engine (Javascript Engine) continuous connection attempts lead to performance problems for some users because of how the engine handles unsuccessful connections.

Therefore, a timeout mechanism has been built into the MCDU limiting the number of connection attempts the MCDU will execute.

A setting in the fylPad EFB Sim Options page has been introduced to allow users to restart the connection attempts or to turn off the attempts to connect to the MCDU Server completely.

![flyPad EFB Settings Sim Options](../docs/aircraft/a32nx/assets/mcdu-server/efb-setting-simoptions.png)

The three settings are:

- Auto:
    - The MCDU attempts to connect to the MCDU Server for 5min after pressing "Ready to Fly" (`Active` is shown).
    - If this setting is selected the MCDU will try to connect to the MCDU Server for 5min after every start of a new flight.
    - After 5min of unsuccessful connection attempts the MCDU will stop any further attempts and `Inactive` will be
      shown.
    - If `Inactive` is shown but you want to connect to the MCDU server just click on `Off` and then `Auto` again.
- Off:
    - The MCDU will not make any attempts to connect to the MCDU Server.

### Browser on Local PC

If you want to use a browser on the same machine on which you are running the Microsoft Flight Simulator and the MCDU Server it is very easy to connect to the MCDU Web Interface.

Just use ++ctrl+"Left Click"++ on the `localhost` link in the command window and it should open the MCDU Web Interface in your default browser.

[http://localhost:8125](http://localhost:8125){target=new}

If you want to start with only the MCDU display and not the whole MCDU panel then add "/fullscreen" to the url.

[http://localhost:8125/fullscreen](http://localhost:8125/fullscreen){target=new}

### Browser on Remote Device

If you want to use the MCDU Web Interface from a remote device (e.g. tablet, phone, 2nd PC, etc.) you need to first make sure you can access the MCDU Web Interface on your PC
by allowing incoming network connections to the server through your Windows Firewall. See how to do this here: [Firewall Configuration](#firewall-configuration).

The MCDU Server command window tries to detect your IP address. Use the `http://xxx.xxx.xxx.xxx:8125` address and enter it into your browser on the remote device.

??? note "Unknown IP Address (click to expand)"
    Sometimes the MCDU Server is not able to detect your IP address.
    To find your correct IP address follow this guide: [How to Find Your IP Address on Windows 11](https://www.howtogeek.com/744082/how-to-find-your-ip-address-on-windows-11/){target=new}

    The port is set to 8125 per default and can be changed be command line options (see [Advanced Start Options](#advanced-start-options)) .

    Enter the correct IP address and port into the remote device's browser address line and hit enter.

    Example: http://192.168.16.1:8125

If you want to start with only the MCDU display without the MCDU panel then add "/fullscreen" to the url.

## How to Use the MCDU Web Interface

The MCDU Web Interface can then be used by mouse or touch depending on your device.

It is also possible to click on the MCDU screen items themselves to actually click the corresponding LSK (Line Select Key).

You can hold the CLR key for >1.5sec to clear all of the scratchpad's content as it is possible in the cockpit itself.

Changes done in the MCDU Web Interface will be reflected immediately in the cockpit and vice versa. Any change in the cockpit will be immediately shown in the MCDU Web Interface.

### Fullscreen Display
If you only want the MCDU display to be shown then tap on the top-most part of the MCDU display. To return to the full MCDU view tap anywhere on the display.

If you want to start with only the MCDU display visible then add `/fullscreen` to the url.

### Sound
You can enable click sounds when pressing buttons on the MCDU by adding `/sound` to the url.

### Day and Night Mode
It is possible to switch between a day and night mode MCDU visualization be clicking/touching the BRT/DIM button in the Web MCDU.

### 4:3 Aspect Ratio Compatibility Mode
If you are using MCDU hardware with a 4:3 display, you can use the 4:3 aspect ratio compatibility mode to improve the formatting so that the lines align better with your hardware.

To use this mode, add `/43` to the url.

## Using Your Local Printer

If you chose a local printer when starting the MCDU Server, every print you will make from the MCDU to the cockpit printer will also be printed using your previously selected printer.

The printers available are those known to the PC where you run Microsoft Flight Simulator and the MCDU Server is on. It is not relevant if your remote device where you use the MCDU Web Interface actually knows this printer.

For different printers and paper size the server allows to specify the paper size and font size. See [Advanced Start Options](#advanced-start-options)

### Websocket Port

The websocket port is the port where the MCDU Web Interface will communicate with the actual MCDU. It sends and receives data through this connection.

This will allow to have different UI implementations or even hardware MCDUs in the future. We plan to eventually also create separate documentation for using this websocket connection directly.

!!! warning "We recommend to **not** change the default port for the websocket if not required. If you have to change this port because it is already occupied on your machine you need to change it as well in the EFB Sim Options Settings page."

## Compatible Browsers

With hundreds of different browsers available today it is not possible to test and support all browsers and their different versions.

In general we expect this feature to work with the common modern standard browsers on Windows, iOS, Android.

However, there will be browsers where this will not work. In this case we recommend to use a standard browser.

We have tested these browsers (current versions) during the development and these should therefore work ok:

- Windows: Edge, Firefox, Chrome
- iOS: Safari, Firefox, Edge, Chrome, duckduckgo, Brave, Bing
- Android: Chrome, Edge
- Mac OS: Safari, Firefox, Edge, Chrome
- Samsung phone: Chrome, Firefox, duckduckgo
- Linux: Firefox
- Amazon Kindle Fire HD 10 : Silk <br/>(App Version 94.2.2.4606.119.10 Android 5.1.1, Fire OS 5.6.9.0)

{==

Always use the latest versions of the operating system and the browser.

We have not tested older operating systems or browsers and can't support them. They might or might not work.

==}

Known unsupported operating systems or browsers:

- Samsung Internet Browser
- iOS 9.x, iOS 10.x
- Very old browsers not supporting Web Sockets. See [Can I use Web Sockets](https://caniuse.com/?search=web%20sockets){target=new}

## Advanced Configuration

### Advanced Start Options

The MCDU Server application has several additional command line options to control the startup configuration.

``` cmd title="Windows Command Line"
>server.exe -h

Usage:
server [options]

Options:
--debug              shows full error details and logs websocket traffic
--font-size=...      sets font size for printing (default: 19)
-h, --help           print command line options
--http-port=...      sets port for http server (default: 8125)
--margin=...         sets margin for printing in points
--no-printer         skips prompt to select printer
--paper-size=...     sets paper size for printing (default: A4)
--printer=...        enables printing to the specified printer
--websocket-port=... sets port for websocket server (default: 8380)
```

- debug:
    - Additional error output and logs websocket traffic
- font-size
    - This defines the font size the printer out will use.
    - Default is 19 but for smaller printouts (e.g. thermal printer) a smaller size may be required.
- http-port:
    - This is the port you need to add to your URL in the browser to access the MCDU Web Interface.
    - E.g. 8125 for this URL: http://localhost:**==8125==**
- margin:
    - This defines the margins for the print out
- no-printer:
    - To skip the prompt asking to choose a printer and not have a local printer configured. This option is required if you want to start the server without any manual interaction (e.g. starting it with the sim).
- paper-size:
    - This defines the paper size the printer out uses.
    - See a list of all supported paper sizes below.
- printer:
    - To skip the prompt asking to choose a printer and have a specific local printer configured. This option is required if you want to start the server without any manual interaction (e.g. starting it with the sim).
- websocket-port:
    - The port where the MCDU Web Interface will communicate with the MCDU itself.
    - ~~This is not the port you need to access the MCDU Web Interface with your browser.~~
    - ~~We recommend to **only** change this if absolutely required (e.g. port is already occupied). See [Websocket Port](#websocket-port) for details.~~

??? info "Supported Paper Sizes (click to expand)"
    Based on this list: [PDFKIT Paper Sizes](https://pdfkit.org/docs/paper_sizes.html){target=new}

    - A-series: A0 ... A10
    - B-series: B0 ... B10
    - C-series: C0 ... C10
    - RA-series: RA0 ... RA4
    - SRA-series: SRA0 ... SRA4
    - Common U.S. sizes
        - EXECUTIVE
        - LEGAL
        - LETTER
        - TABLOID
    - Other
        - 4A0
        - 2A0
        - FOLIO

    The exact size can be found here:
    [Overview_of_ISO_paper_sizes](https://en.wikipedia.org/wiki/Paper_size#Overview_of_ISO_paper_sizes){target=new}

To use advanced startup options you can use a Windows Powershell or Windows Command Prompt.

![Windows Command Prompt](../docs/aircraft/a32nx/assets/mcdu-server/windows-command-prompt.png "Windows Command Prompt"){loading=lazy}

Alternatively you can create a Windows Shortcut for the server.exe file and add the parameters to the target field.

![Windows Shortcut Dialog](../docs/aircraft/a32nx/assets/mcdu-server/windows-shortcut-dialog.png "Windows Shortcut Dialog"){loading=lazy}


### Network Configuration

To access the MCDU Server from a remote device you need to make sure that this device is on the same network as the PC running the MCDU Server.

This is typically the case if both, the PC and the device use the same Internet router and the same WiFi.

To check this you can look at the IP address the MCDU server has listed in its command window.

![MCDU Server Command Window](../docs/aircraft/a32nx/assets/mcdu-server/mcdu-server-cmd-window.png "MCDU Server Command Window"){loading=lazy}

In the example above the IP address is `192.168.1.19`.

Your device should typically also have an IP address starting with `192.168.1.x` in this case.

You can check this in the device's network configuration.

??? tip "Examples for Device Network Information (click to expand)"
    **iPad:**

    ![iPad Network Info](../assets/mcdu-server/ipad-network-info.png "iPad Network Info"){loading=lazy}

    **Samsung Android:**

    ![Samsung Network Info](../assets/mcdu-server/samsung-network-info.png "Samsung Network Info"){loading=lazy}

If you still can't connect to the MCDU server your firewall might block the traffic. See next chapter.

### Firewall Configuration

!!! danger "Disclaimer"
    Changing Windows settings, especially security settings like the firewall comes with certain risks. Please do not change these settings if you are not comfortable doing so. FlyByWire Simulations cannot take any responsibility for any issues caused by your changes to Windows or security settings.

If you can't reach your MCDU server from your browser on your device or on your local PC then it is very likely that your PC firewall is blocking this network traffic.

To test and confirm this turn off your firewall and try again to reach your MCDU via your browser. If you now can access your MCDU from your browser you have confirmed that it is indeed the firewall that blocks this access.

{==

**Turn the firewall back on again.**<br/>
*(never run a PC without a firewall)*

==}

We now know we need to open the ports we want to use. The default ports are **TCP 8125** and **TCP 8380** and these must be allowed to pass the firewall.

There are several ways to open ports on your PC firewall.

For the Windows Firewall you can follow this guide here:

[Opening a Port on Windows Firewall Instructions](https://www.howtogeek.com/394735/how-do-i-open-a-port-on-windows-firewall/){target=new  .md-button }

Alternatively you can open a Command Line prompt as Administrator and use this command:

``` cmd title="Windows Powershell"
netsh advfirewall firewall add rule name="MCDU Server" dir=in action=allow protocol=TCP localport=8380,8125
```

For an advanced guide of this command see the Microsoft documentation:<br/>
[netsh advfirewall firewall](https://docs.microsoft.com/en-US/troubleshoot/windows-server/networking/netsh-advfirewall-firewall-control-firewall-behavior){target=new}

??? warning "Remove Autogenerated Rules (click to expand)"
    Sometimes Windows has already automatically generated some rules after showing you a firewall dialog when starting the MCDU Server.

    If you still can't connect to the MCDU Server these rules might be the cause. After adding your own rule as described above you don't need these anymore and they can be deleted.

    They usually look like this:

    ![Windows Automatic Firewall Rules](../assets/mcdu-server/mcdu-firewall-automatic-rules.png "Windows Automatic Firewall Rules")

    ![Windows Automatic Firewall Rules](../assets/mcdu-server/mcdu-firewall-automatic-rules-2.png "Windows Automatic Firewall Rules")

    Windows Dialog creating these automatic rules looks likes like this:
    ![Windows Firewall Dialog](../assets/mcdu-server/mcdu-windows-auto-fwrules-dialog.png "Windows Firewall Dialog")

This should now allow access from your browser to the MCDU.

### Occupied Port

Sometimes the default ports 8380 or 8125 are already used by other services on your PC.

In this case you should get error messages similar to this:

``` cmd title="Windows Command Line"
Error: Port 8125 is already in use
```
or
``` cmd title="Windows Command Line"
Error: Port 8380 is already in use
```

??? tip "How To Check If a Port is Already In Use? (click to expand)"
    You can see if a port is occupied by making sure the MCDU Server is off and then running this command:

    Windows Command Line:
    ``` cmd title="Windows Command Line"
    netstat -ano | find "8380"
    ```
    or
    Windows Powershell:
    ``` cmd title="Windows Powershell"
    netstat -aon | findstr 8380
    ```

    If the corresponding port is already in use the output should be similar to this:
    ``` cmd title="Output"
      TCP    0.0.0.0:8380       0.0.0.0:0              LISTENING       4
      TCP    [::]:8380          [::]:0                 LISTENING       4
      ...
    ```

#### Webserver Port is Occupied

If the port for the webserver 8125 is already in use you can simply start the MCDU server with a different web server port with this option:

``` cmd title="Windows Command Line"
server.exe --http-port=8126
```

Of course now the firewall might need to be opened for this new port.

#### Websocket Port is Occupied

If the port for the MCDU Websocket Server is occupied you need to first change this port in the [flyPad EFB Sim options page](../docs/aircraft/common/flypados3/settings.md#sim-options).

You can then start the MCDU server using the new websocket port with this option:

``` cmd title="Windows Command Line"
server.exe --websocket-port=8381
```

Of course now the firewall might need to be opened for this new port.

## Starting the MCDU Server with Microsoft Flight Simulator

Microsoft Flight Simulator has the possibility to automatically start external applications during its own startup.

We can use this feature to also automatically start the MCDU Server.

!!! warning "Be aware that this feature has some drawbacks and we do not offer support for this MSFS feature"

For this configuration we need to edit a file called `exe.xml` in the MSFS configuration folder.

You can find this folder here:

``` title="Sim from MS Store"
%localAppData%\Packages\Microsoft.FlightSimulator_8wekyb3d8bbwe\LocalCache
```

``` title="Sim from Steam"
%appData%\Microsoft Flight Simulator
```

This file should similar to this although it already might have entries not shown in this example:

``` xml title="exe.xml"
<?xml version="1.0" encoding="Windows-1252"?>
<SimBase.Document Type="SimConnect" version="1,0">
	<Descr>SimConnect</Descr>
	<Filename>SimConnect.xml</Filename>
	<Disabled>False</Disabled>
	
	<!-- NEW APPLICATIONS TO START HERE -->
	
</SimBase.Document>
```

Add the following section before the `</SimBase.Document>` tag and change the `YOUR_COMMUNITY_FOLDER` placeholder with the path to your Community folder.

``` xml title="exe.xml (partial)"
	<Launch.Addon>
		<Name>FlyByWire MCDU Server</Name>
		<Disabled>False</Disabled>
		<Path>YOUR_COMMUNITY_FOLDER\flybywire-aircraft-a320-neo\MCDU SERVER\server.exe</Path>
		<CommandLine>--no-printer</CommandLine>
	</Launch.Addon>
```
Now every time Microsoft Flight Simulator starts it will also start the MCDU Server.

!!! warning ""
    Unfortunately MSFS does not stop the automatically stated applications after shutting down and you need to close the MCDU Server window manually.

    If you do not do this there will be an error message the next time you start MSFS or the MCDU Server as it is already running.

## MCDU Server Architecture

![MCDU Server Architecture](../docs/aircraft/a32nx/assets/mcdu-server/mcdu-server-architecture.png "MCDU Server Architecture"){loading=lazy}

The MCDU Server uses a web application running in the browser to send and receive data via the Web Socket protocol from the MCDU.

To open the web application the browser will connect to the MCDU Server's webserver via http protocol (default port 8125) and download and run the MCDU Web Interface application (HTML/CSS/JavaScript).

The MCDU Web Interface application will open a data connection to the MCDU via Web Socket protocol (default port 8380) and receive data (screen content) and send data (user input like button pushes) from and to the MCDU.

For this to work the browser must be able to reach the MCDU Server via the two TCP ports 8380 and 8125 (these defaults can be changed) which means users might need to reconfigure their network and firewall settings accordingly (see documentation above).

## Troubleshooting

??? warning "No MCDU SERVER Folder"
    The MCDU Server is only available in the Development Version.

??? warning "MCDU Server Error: Port 8125 is already in use"
    The http port 8125 is already in use.

    Solution: [Webserver Port is Occupied](#webserver-port-is-occupied)

??? warning "MCDU Server Error: Port 8380 is already in use"
    The web socket port 8380 is already in use.

    Solution: [Websocket Port is Occupied](#websocket-port-is-occupied)

??? warning "MCDU Server: `Waiting for Simulator...` Although Flight is Started"
    The MCDU Server continues to show `Waiting for simulator ...` although the flight is started and aircraft is loaded.

    Two known causes:
    
    - The web socket port 8380 is already in use.
    - MCDU Server Connection Timeout 

    Solution: 

    - [Websocket Port is Occupied](#websocket-port-is-occupied)
    - [MCDU Server Connection Timeout](#mcdu-server-connection-attempts-timeout)

??? warning "MCDU Server Error: Failed to load printers"

    If you you start the server and get this error messages:

    ``` cmd title="Windows Command Line"
    Error: Failed to load printers.
    Make sure the "Print Spooler" Windows service is running.
    ```
    Solution: Make sure the "Printer Spooler" Windows service is turned on:

    ![mcdu-windows-service-printer](../assets/mcdu-server/mcdu-windows-service-printer.png){loading=lazy}

    You can find the Services Manager by pressing ++windows+r++ and then type `services.msc`.

??? warning "MCDU Server Error: `...Encoding not recognized...`"

    When you start the server and and it crashes immediately with an error message mentioning `...Encoding not recognized...` you Windows most likely uses a rare UTF-8 based encoding.

    Solution:

    - Open Windows Control Panel -> Region.
    - Go to the Administrative tab and click Change system locale
    - Make sure the check mark next to Beta: Use UTF-8 for worldwide language support is selected.
    - Click OK and restart your computer.

??? warning "Browser Can't Connect to MCDU Web Interface"
    Your browser can't connect to the MCDU Web Interface and times out eventually.

    Cause: This is most likely a network or firewall issue.

    Solutions:

    - [Network Configuration](#network-configuration)
    - [Firewall Configuration](#firewall-configuration)

??? warning "Browser Shows MCDU Web Interface but Display Remains Black"
    Your browser can't connect to the MCDU Web Socket port.

    Cause: This is most likely a network or firewall issue.

    Solutions:

    - [Network Configuration](#network-configuration)
    - [Firewall Configuration](#firewall-configuration)

    Cause: Aircraft has no Power / MCDU is still off.

    Solution: Power up the aircraft.

??? warning "Browser Shows MCDU Web Interface only partly or garbled"
    Your browser can connect to the server but does not show the MCDU Web Interface correctly or not at all.

    Cause: This is most likely an incompatible browser.

    Solutions:

    - Use a different browser.
    - See tested browsers: [Compatible Browsers](#compatible-browsers)

??? warning "Printout format incorrect / receipt printer"
    The default format the printer uses is paper size A4 and font size 19.

    For some printer especially receipt printer a different paper size and font size must be used to make the output look good.

    We recommend to experiment with this a bit to find good values for your printer. In our tests we found paper size C8 and font size 10 a good starting point.
