# A32NX flyPad Development Guide Overview

[**Development Guide Overview**](https://docs.flybywiresim.com/dev-corner/development-guide){.md-button target=new}
[:fontawesome-brands-github:{: .github } **GitHub Contributing.md**](https://github.com/flybywiresim/a32nx/blob/master/.github/Contributing.md){.md-button target=new}


## Introduction

This guide has the objective of teaching you how to set up your development environment to efficiently contribute to the flyPad/EFB in the A32NX. This guide follows on from [A32NX Development Guide Overview](https://docs.flybywiresim.com/dev-corner/development-guide/) and 
[GitHub Contributing.md](https://github.com/flybywiresim/a32nx/blob/master/.github/Contributing.md){target=new}. Please familiarise yourself with the information, steps and requirements listed there before reading further.

## Setting up a Development Environment inside MSFS

Before you can load the project to test in your simulator, you first need to ensure you've created a fork of the [A32NX project on GitHub](https://github.com/flybywiresim/a32nx){target=new} and have cloned this in your code editor/IDE.
We recommend when making changes on your fork, you create a new branch, titled with the change you're looking to make or something similar.
Make sure you have also run the setup and build scripts shown below and explained in detail on [GitHub Contributing.md](https://github.com/flybywiresim/a32nx/blob/master/.github/Contributing.md){target=new}.


```
git clone https://github.com/flybywiresim/a32nx.git
cd a32nx
.\scripts\dev-env\run.cmd ./scripts/setup.sh
.\scripts\dev-env\run.cmd ./scripts/build.sh
```

## Creating a Symlink and Setting up Instant-Reload

Once you have the A32NX built, you'll need to link your newly compiled A32NX to your community folder to enable you to quickly update the flyPad with new changes made to your local branch without copying everything over manually again and reloading MSFS.
This is commonly referred to as a 'Symlink'.

To create your Symlink, open your command terminal and run the below command, substituting the correct file paths with your community folder, and the 'flybywire-aircraft-a320' folder from your new project.

!!! warning "Important step!"
    Make sure you remove any existing copy of the aircraft from your community folder before doing this.

```
mklink /J [MSFS Community folder/flybywire-aircraft-a320-neo] [Project folder path]
```
Example:
``` 
mklink /J C:\Users\USERNAME\AppData\Local\Packages\Microsoft.FlightSimulator_8wekyb3d8bbwe\Community\flybywire-aircraft-a320-neo C:\Users\USERNAME\IdeaProjects\a32nx\flybywire-aircraft-a320-neo
```

If this works, you'll receive the response:

"Junction created for [Community folder] [Project Folder]" from the terminal.

Now you've compiled and symlinked your Github fork to your community folder, you should be able to load into the aircraft as normal. Open MSFS and check everything is working with your compiled branch before progressing.

## Quick Reloading the flyPad

As the aircraft in your project folder is now connected to your MSFS community folder via the Symlink you created in the previous step, each time you load in to the A32NX on MSFS, any changes you've made since the sim was last opened should be updated.

Rather than reloading MSFS each time you wish to test your changes, you can enable quick reloading directly from your code editor/IDE, then with each change you make in the code, you can save and reload only the flyPad, and keep MSFS running throughout.

!!!info ""
    From here on, if you're coming back to continue working on your flyPad project, you would only need to run the following quick reload steps again to get everything up and running again!


To start quick reloading the project:

- In your code editor/IDE, run the command:

```
npx rollup -wc src/instruments/buildSrc/simulatorBuild.mjs
```

- Navigate to **[http://127.0.0.1:19999](http://127.0.0.1:19999)** in your browser. You should see several options appear, select the following option: 

```
VCockpit16 - EFB_TEMPLATE [coui://html_UI/Pages/VCockpit/Core/VCockpit.html]
```

- A page similar to the below should be shown. The refresh button at the top of the page will reload your flyPad, causing the display to switch off for a few moments. Once turned back on, any changes made and saved in your EFB project file will be updated to the EFB in your simulator session.

![image](../dev-corner/assets/EFBLoader.png){loading=lazy}

## Getting Started with the EFB Code

Now you're set up with your own fork, which you can reload instantly and test in MSFS, you're ready to get started making changes. When getting started it's a good idea to spend some time looking around the project and wrapping your head around the structure.

- You'll find the main EFB content under ` src/instruments/src/EFB ` of your Github fork, try making small changes at first to test, such as changing the colour of an icon, or changing a few words to make sure the reloading is working. 
- Take a look at previous commits made to the flyPad on the [A32NX Github Repository](https://github.com/flybywiresim/a32nx/commits/master){target=new} and see what changes were made to get the desired result.

!!!info "Top tip!"
    When working on your project, make sure to reload the flyPad and test regularly to catch issues as soon as they happen.
    If many changes are made between tests, it may be difficult to find the cause of any problems that arise.

## Troubleshooting 

If there is anything wrong with the code/files in your local branch, when reloading the flyPad, several issues may occur:

- The flyPad will turn on, but switch off and remain off when clicking on an affected page (Reloading the build in the browser will bring this back).
- Everything may show as normal but none of your changes have been applied. 
- The flyPad doesn't turn on at all.

This would generally indicate an issue with the code in your project.
In these cases, it's best to take a look back through changes you've made so far and track down the cause, or revert the last change made if that was the cause.

!!! warning "Unique Error"
    If you receive the error `Ineffective mark-cmpacts near heap limit Allocation failed - Javascript heap out of memory` when attempting the npx rollup command, run the below command to increase Node's memory limit.
    This should enable you to continue with the quick reloading process.

    ```
    $env:NODE_OPTIONS='--max_old_space_size=8192
    ```