# Local Files

SimBridge allows files outside the simulator to be accessed by our aircraft. Notably, the [flyPadOS 3 Charts](../../fbw-a32nx/feature-guides/flypados3/charts.md#local-files) feature, and the [Company Routes](./coroute.md) feature utilize the Local Files functionality of SimBridge. Please refer to the respective documentation on how these features work and their requirements.

## Where to store Local Files?

!!! warning "Important Note" As of version 6.0.0 of SimBridge, the path for the Local Files has changed. If you are using older versions (Not recommended), you will have to use the `/path/to/<SimBridge Install Directory>/resources` folder.

SimBridge will read files from a special file in your computer documents folder. You can find it by going to `Documents > FlyByWireSim > SimBridge`. Each feature that uses Local Files, will have its own folder. For formatting and what files are available by each feature, please its documentation.
