---
title: Resources
description: Resources for working with and on the A32NX and A380X code.
---

# Resources

On this page, you will find all the necessary resources, links, and documentation you might need to work with and on the
A32NX code.

## GitHub Repositories

The main GitHub repository for the A32NX aircraft is:

**[https://github.com/flybywiresim/aircraft](https://github.com/flybywiresim/aircraft){target=new}**

The Development version of the FlyByWire A32NX is done in the master branch. Whenever something is merged into the 
master branch, an automatic build process builds the newest Development version and uploads it to our CDN, so users can 
download the latest Development version via the FlyByWire Installer. We have a very strict development, review and QA 
process for this version.

The Stable version is a snapshot (in git terms, a [Tag](https://github.com/flybywiresim/aircraft/tags){target=new}) of 
the development branch.

The FlyByWire project has other repositories for subprojects like api, msfs-rs, installer, website, docs, etc. Find them
[here](https://github.com/orgs/flybywiresim/repositories){target=new}.

## Support from the FlyByWire Team on Discord

To get additional information and support, please make sure you join our Discord. There are various channels dedicated 
to supporting developers (in fact, most channels).

[:fontawesome-brands-discord:{: .discord } - **Discord Link**](https://discord.gg/flybywire){target=new}

First get yourself the "programmer" role in 
[#roles](https://discord.com/channels/738864299392630914/751780817772216401/816730253543604224){target=new}.

The most general channel for getting help for development is [#dev-support](https://discord.gg/v3jAxJpwZm){target=new}.

There are many other channels for specific systems or subprojects. If you are working on the flyPad EFB for example, the
#efb channel would be an important channel for collaborating and support.

## Tech Stack

Our tech stack includes the following:

!!! info "Tech Stack / Language Summary"
    Below you can find a table summary of the languages and technologies used in the A32NX project.

    | Category                      | Language / Technology                                     |
    |:------------------------------|-----------------------------------------------------------|
    | General                       | React                                                     |
    | flyPadOS                      | Tailwind CSS, Redux                                       |
    | Autopilot / Flight Controls   | MATLAB / C++                                              |
    | Systems / Physics Simulations | Rust                                                      |
    | Displays / Avionics           | Typescript / React (deprecated) / MSFS Avionics Framework |

- Systems development for aircraft uses Rust and the `msfs-rs` library.
- Avionics programming is done using JavaScript or TypeScript (depending on the project), with the `React.js` rendering 
  library.
- Front-end web or desktop app development uses the same technologies outlined above.
- Server-side development uses `nest.js` for the API and `MySQL` for the database backend.

Knowledge of all items on this list is obviously not necessary, but this can hopefully give you a better insight into 
what your skills can fit into.

## Tools

A number of tools make development in Microsoft Flight Simulator easier.

- [WebUI-DevKit](https://github.com/dga711/msfs-webui-devkit){target=new} - In-game development overlay for html-ui 
  content. Provides fast reload, console output, and more!
- [devtools-backend-refurb](https://github.com/dga711/devtools-backend-refurb){target=new} - Chrome DevTools server 
  targeting Coherent GT. Gives you DevTools for html-ui content. WARNING: This is still a work in progress, and tends to 
  be very finicky.

## Additional resources

- [P3D XML Gauge Reference](http://www.prepar3d.com/SDK/SimObject%20Creation%20Kit/Panels%20and%20Gauges%20SDK/creating%20xml%20gauges.html)
  still applies to FS2020.