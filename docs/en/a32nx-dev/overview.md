# A32NX Development Guide Overview

## Introduction

This guide has the objective of teaching you how to contribute efficiently to the FlyByWire A32NX project.

You will learn how to:

- Setup a functional development environment
- Get familiar with the technologies involved
- Understand our build process
- Integrate into our development cycle and best practices

## Setting up a development environment

Working on the addon will require at a minimum the following software:

- A code editor (with at least syntax highlighting, search and replace, and support for workspaces)
- A `git` client (along with any editor integrations of your choice)
- Docker Desktop (either WSL2 or HyperV backend work, but the latter is faster)

Most of our team works with either Visual Studio Code or IntelliJ IDEA-based IDEs for development. Obviously, your choice is yours as long as the resulting code conforms to our standards.

## Used technologies

Our tech stack includes the following:

- Systems development for aircraft uses Rust and the [`msfs-rs`](https://github.com/flybywiresim/msfs-rs) library
- Avionics programming is done using JavaScript or TypeScript (depending on the project), with the `React.js` rendering library.
- Front-end web or desktop app development uses the same technologies outlined above
- Server-side development uses `nest.js` for the API and `MySQL` for the database backend

Knowledge of all items on this list is obviously not necessary, but this can hopefully give you a better insight into what your skills can fit into.

## Build process

Due to how Microsoft Flight Simulator package building works, it is necessary for us to maintain our own bespoke build tools.

The high-level goal of the build process is to eventually have all code in the `src/` directory.

Commonly, the following items will be found in the source:

```
- src/
    - instruments/                  Avionics code built using the rollup config
        - rollup.config.js
    - behavior/                     Compiled and verified ModelBehavior code
    - model/                        Model source files to be merged at build time
    - <directories for systems>     Rust/C++ source code for systems
    ... more to come
```

Each directory will usually contain a build.js/build.sh file that is called from a central build script located in `scripts/build.sh`.

A Docker container is used to ship pre-configured build environments to developers. It contains necessary library headers and compilers, and requires no user intervention at all.

This build process is optimized to be run in cloud CI pipelines on GitHub Actions. This allows us to automatically distribute development master builds to thousands of users without any manual intervention. It lets the team deploy critical fixes to production in a matter of minutes.

The automatic CI pipeline is sometimes manually added to other branches in order to provide the community with experimental versions.

An automatic system that allows us to enable CI for specific branches might be considered in the future.

### Reference material

Creating a high-fidelity aircraft is a serious task that requires focus and dedication. But more importantly, it's a strive for accuracy and realism. Therefore, any change that affects the appearance or behavior of a plane needs to reference real documentation.

The maintainer team has the role of deciding if references are suitable for a change. It is understandable that new developers do not have access to in-depth resource material.

While material like that is generally not in the possession of new contributors, the development team is always available to confirm your changes or provide you with necessary info.

Our extensive pool of IRL A320/A380 pilots and aircraft maintenance engineers are also able to answer your questions whenever needed.

## Useful tools

A number of tools make development in Microsoft Flight Simulator easier.

- [`msfs-webui-devkit`](https://github.com/dga711/msfs-webui-devkit/) - simple avionics overlay allowing cache-breaking live reload and basic console view
