# Company Routes
Stored Company Routes allow you to save routes you regularly fly to your PC. It uses simBrief XML Datafiles format, so you can easily use your simBrief planning to create a stored company route.

!!! warning Notice
    SimBridge *must* be [running](../install-configure/start-simbridge.md) to access local files.

    See [Autostart](../install-configure/start-simbridge.md#autostart) documentation on how to start it. 

    Check [Troubleshooting](../troubleshooting.md) if you are having issues.

### Generating a Stored Company Route Using simBrief

- Generate a flight plan using simBrief.
- Download the `XML Datafile' from simBrief.

    ![simBrief Datafile Download](../assets/simbrief-datafile-download.png){loading=lazy}

- Save the simBrief XML Datafile to the coroutes folder in the [resources folder](../install-configure/installation.md#resources-folder).
- Rename the simBrief XML Datafile to any name with maximal 9 characters. E.g., the airport's IATA codes `STRCPH1.xml`.

### How to Use a Saved Company Route

There are two methods available:

- [Entering the Company Route Name](#entering-the-company-route-name)
- [Entering a FROM/TO Pair](#entering-a-fromto-pair)

!!! warning "Important Note"
     When utilizing a stored company route, please be aware of the following data that is not included:

    - <span style= "color:red;">Does not include</span> the flight number, cost index or cruise level.
    - <span style= "color:red;">Does not include</span> SID/STAR and APPR or any other flight-specific data (pax, cargo, etc.).
    
    You can complete the flight plan setup by entering the missing data manually.

#### Entering the Company Route Name 
- Start a flight at the appropriate departure airport and follow the standard setup procedure.
- When setting up the flight management system in the MCDU, you can directly head to the INIT A page.
- Enter the name of your company route into the `CO RTE` field.

    ![MCDU INIT A Loading CoRoute](../assets/mcdu-init-a-load.png){loading=lazy}

- This populates FROM/TO and also the basic flight plan. 


#### Entering a FROM/TO Pair
- **Alternatively**, you can enter the FROM/TO pair of routes you have stored, which will bring up the co-route selection page.
    
    ![MCDU Co Route Selection Page](../assets/mcdu-coroute-selection-page.png){loading=lazy}

- The co-route selection page shows a summary of each stored route.
- You can navigate between the routes with the horizontal slew keys.
- For long routes, you can scroll the page by using the vertical slew keys.
- You can choose and insert a route by pressing the LSK 6L next to `INSERT*`