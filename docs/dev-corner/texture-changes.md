# Texture Map Changes

Changes made to the A32NX external model texturing will be documented below. The intended audience for this page is livery creators.

## Sharklet Un-Mirror

The A32NX sharklet model previously mapped both sharklets to the same location on the livery decal texture, despite a second set of sharklets existing on the texture. We have corrected the UV map to utilize the second set of sharklets, to allow accurate depictions of liveries with text, or other items that cannot be mirrored. It was necessary to make use of the existing decals from the original Asobo model because no method has been developed yet to attach new decals to animation bones, so the decals would move with the wing flex.

Some existing liveries using the `A320NEO_AIRFRAME_LIVERY_ALBD.png.dds` texture for sharklets did not paint the second set of sharklets. The left wing sharklet will appear unpainted, or partially painted, in this case.

If you are the author of an affected livery, please reference the following:

- Add the second set of sharklets to your `A320NEO_AIRFRAME_LIVERY_ALBD.png.dds` texture.
- For convenience, here is a copy of the [new sharklet UV map](assets/a32nx-dev/sharklet_uv_4k.png){target=new} that can be added as a layer in your workflow. The decals should be painted un-mirrored.

!!! warning ""
    For further context, you can review [pull request #5490](https://github.com/flybywiresim/aircraft/pull/5490){target=new} on our GitHub if necessary.

## Registration Decal

The A32NX has a [toggle option in the EFB to disable the dynamic registration number decal,](../aircraft/a32nx/feature-guides/flypados3/settings.md#sim-options) normally located near the rear of the aircraft. The intention of this option is to remove the need for livery designers to include a `panel.cfg` file in their livery packages.

!!! warning "Avoid Using panel.cfg"
    Overriding `panel.cfg` creates future conflicts with A32NX development.

    Please avoid using `panel.cfg` to disable the registration number decal, and instead advise users to [disable the dynamic decal in the EFB settings](../fbw-a32nx/feature-guides/flypados3/settings.md#sim-options).

## Mirrored Wheel Texture

The A32NX model previously used a single UV for all wheels. This caused the right main gear wheel to appear mirrored. We have flipped the UV for the right wheel texture, so now any texture on the right wheel will appear correct.

If you are the author of a livery that has textured wheels, with text or anything else orientation critical.

- No action is required. The current wheel texture will appear correct on the right main gear wheel.

!!! warning ""
    For further context, you can review [pull request #6931](https://github.com/flybywiresim/aircraft/pull/6931) on our GitHub if necessary.

## Cargo Hinges

The A32NX model previously mapped both cargo door hinges to the same location on the livery decal texture. We have added a new mesh to make each hinge have individual textures.

If you are the author of a livery that needs individual texturing of these hinges, please reference the following:

- Add a new *512x512px* texture called `DECALS_DOOR_CARGO_HINGES_ALBD.PNG.DDS` to your livery.
- We provide a `DECALS_DOOR_CARGO_HINGES_COMP.PNG.DDS`, but this could also be replaced if needed.

For convenience, here is a copy of the 
[cargo door UV Map](assets/a32nx-dev/cargo-door-uv.png){target=new} that can be added as a layer in your workflow.

## Bandit / Racoon Mask
The bandit/racoon mask is disabled by default.
To enable the mask, in any color of your choice, use the `DECALS_BANDIT_WINDOW_ALBD.PNG.DDS` texture (you need all three files incl. the Flags and json) and fill the 
associated square referenced in the [UV map legend](assets/textures/uv-map-legend.png).

Note that the UV legend is 1024x1024, for readability, while the real texture only is 64x64.

## Elevator Trim Scale
The fill and outline color of the elevator trim scale, is configured in the `DECALS_BANDIT_WINDOW_ALBD.PNG.DDS` texture (you need all three files incl. the Flags and json).
See the [UV map legend](assets/textures/uv-map-legend.png) for reference. 

Note that the UV legend is 1024x1024, for readability, while the real texture only is 64x64.

## Logo / Sticker / Alliance Decal
We have added a mesh between the forward doors and the cockpit, to ease with high-quality logos, stickers, etc.
The texture for logo / stickers / alliance is transparent by default.
To enable this texture, add a 2048x2048 `DECAL_LOGO_FRONT_COMP.PNG.DDS` texture and add your graphics in the 
associated square referenced in the image below. 

![](assets/textures/logo-mesh.png)