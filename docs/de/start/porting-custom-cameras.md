# Porting Custom Cameras

---

!!! warning "Disclaimer"

    This guide is provided with no guarantee of compatibility and meant for the porting of custom cameras for personal use.

    **No support will be provided**

The FlyByWire Simulations A32NX has now been separated from the default Asobo A320neo which has resulted in changes to some file structures.

To be able to use your previously set custom camera views with the FBW A32NX follow the steps below.

!!! info "Step One"

    Find CAMERAS.CFG in `..\LocalCache\SimObjects\Airplanes\Asobo_A320_NEO`

    Copy the file above (using CTRL + C or Right Click + Copy)

!!! info "Step Two"

    Find CAMERAS.CFG in directory `..\LocalCache\SimObjects\Airplanes\FlyByWire_A320_NEO`

    Paste the file you copied in step one, and replace/overwrite when asked to.

    If the folder FlyByWire_A320_NEO does not exist, create a new one with the name FlyByWire_A320_NEO.

Ready to go! Launch the sim and load into the new A32NX. Use the same keybinds you used before to load your custom camera views.
