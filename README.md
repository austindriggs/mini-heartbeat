# Mini Heartbeat

A MicroPython project for the Raspberry Pi Pico that drives a MAX7219 8x8 LED Matrix that features heartbeat animations, custom-designed fonts, and a terminal interface.

<a href="https://youtu.be/J6t5J2ZZkJU?si=F_Cc42BRk_-zXlft" target="_blank">
  <img src="/support/mini-heartbeat.jpg" alt="Mini Heartbeat YouTube Demo" width="1000" style="border:0;">
</a>

> Click the image above to see a video demo on YouTube.


## FILE STRUCTURE

- main.py: Entry point for the main annimation loop and terminal interface.
- drawings.py: High-level animation functions.
- alphabet.py: Dictionary containing 6-bit wide character bitmasks.
- hearts.py: Bitmask frames for the pulsing heart animation.
- max7219.py: Driver library for the LED matrix.
- support: Useful files, documents, and firmware for the project.


## WIRING DIAGRAM

| PICO | GPIO | FUNCTION       | MATRIX |
|------|------|----------------|--------|
| 2    | GP1  | SPI0 CS (CSN)  | CS     |
| 4    | GP2  | SPI0 SCK (CLK) | CLK    |
| 5    | GP3  | SPI0 TX (MOSI) | DIN    |
| 38   | -    | Ground         | GND    |
| 40   | -    | VBUS           | VCC    |


## INSTALLATION

1. Download MicroPython: Get the latest `.uf2` firmware from the [official MicroPython website](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html) for the Pico (or your choice of microcontroller). The version I'm running is in the `support` directory.
2. Flash the Pico: Hold the `BOOTSEL` button on while plugging it into your USB port. It will appear as a drive named RPI-RP2. Drag and drop the `.uf2` file onto the drive.
3. Reboot: Unplug and plug the Pico back in normally.


## RUN IN VSCODE

1. Install Extension: Install the [Raspberry Pi Pico](https://open-vsx.org/extension/raspberry-pi/raspberry-pi-pico) extension from the VS Code Marketplace.
2. Connect: Plug in your Pico. Click the Pico Connected button in the VS Code status bar to establish a REPL connection.
3. Sync: Use the MicroPico: Sync (Local -> Remote) command from the Command Palette (Ctrl+Shift+P) to upload your project files.
4. Run: Open main.py and press the `run` icon on the status bar to start the animation loop.


## AI DISCLOSURE

I wrote this code myself **without** the use of AI.
