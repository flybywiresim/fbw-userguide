---
title: FlyByWire Installer - Known Issues
description: Explore reported issues and known bugs for the FlyByWire Installer.
---

!!! danger "STOP"
    [Read this first before reporting any issues on Discord or GitHub.](./known-issues.md#read-this-first)

## Use the Browser's Search Function

On Desktop, press ++ctrl+'F'++ to search for an issue within the current page.

## Legend

!!! bug "Breaking Issue / Bug"
!!! warning "Non-Breaking Issue / Inconvenience"
!!! tip "Config Issue / Usage Issue"

---

<!--
TEMPLATE

??? issue "Issue Headline"
    ### Issue Headline

    !!! tip ""
        *Affected versions: Stable, Development*

    ^^Description^^
    ^^Root Cause^^
    ^^Possible Solution or Workaround^^
    ^^Additional Information^^
-->

## FBW Installer Known Issues

??? bug "Download Issues - FBW Products"
    ### Download Issues - FBW Products

    ^^Description^^

    In certain situations, your ISP may block our CDN (Content Distribution Network) served by Cloudflare. Cloudflare allows us to save costs when users download our aircraft from our installer to 
    provide a seamless installation process for a variety of our products.

    Additionally, any disturbance to the stability of your connection may cause any downloads to fail and may need to be retried when you have a more stable connection.

    ^^Common Error Codes^^

    - ECONNRESET
    - ETIMEDOUT
    - ENOTFOUND
    - HTTP 403

    ^^Possible Solution or Workaround^^

    We recommend one of the following actions:

    1. TEMPORARY Solution: Try a VPN - a great free one that's reliable is [ProtonVPN](https://protonvpn.com/).
        - Please do your own due diligence and research when utilizing a VPN, even with our recommended one above.
    2. Download a full build from our website [here]() - Please ensure you follow our [manual installation instructions](../install/installation.md#manual-installation).
    3. Contact your ISP to check with them if there are any existing issues utilizing Cloudflare on their network.

    ^^Additional Information^^

    Below is a list of countries that are possibly affected by this issue. Please note that it may not be *every* ISP in the country.

    - Brazil
    - China
    - Iberia
    - Portugal
    - Saudi Arabia
    - Spain

??? bug "Installer Permission Problems"
    ### Installer Permission Problems

    ^^Description^^

    During installation of a product a "Windows Permission Error" with the error code EPERM shows up and the installation is aborted.

    ^^Root Cause^^
    
    Sometimes the permissions of the community folder are set to not allow the current user to install addons in it.
    This might be set since the installation of MSFS or MSFS might have changed it at some point.
    
    ^^Possible Solution or Workaround^^

    One of the following solutions usually lets the desired addon be installed

    * Check the permissions of the community folder and correct them.
    * Rename the current community folder, create a new one with the same name and move your installed addons into the new community folder.
    * Start the installer with admin permissions.