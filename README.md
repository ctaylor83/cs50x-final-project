# CS50x PICO Survival Server
#### Video Demo:  <URL HERE>
#### Description: A self contained web server for outdoor activities!

This project features a simple chat and Morse code server running on the Raspberry Pi Pico. It uses MicroPython and the `phew` web framework to provide a web-based interface for sending and viewing chat messages and converting text to Morse code signals using the Pico's LED.

## Features

- Web-based chat application.
- Morse code conversion and signaling using the Pico's LED.
- Basic HTML rendering for chat messages.
- Timestamps for each chat message.

## Hardware Requirements

- Raspberry Pi Pico
- Micro USB cable for power and programming

## Software Requirements

- MicroPython firmware for Raspberry Pi Pico
- `phew` web framework

## Installation

### Setting Up MicroPython

1. Download the latest MicroPython firmware for Raspberry Pi Pico from [the official website](https://micropython.org/download/rp2-pico/).
2. Follow the instructions to install the firmware on your Raspberry Pi Pico.

### Installing Dependencies

Copy the `phew` framework files to your Pico. You can find the necessary files and instructions at [phew's repository](https://github.com/pimoroni/phew).

## Usage

1. Connect the Raspberry Pi Pico to a power source.
2. Access the Pico's wifi network which will open the Pico's html site or prompt the user to open.

### Chat Interface

- Enter your callsign and message in the provided fields.
- Click 'Send' to post your message to the chat.
- Messages will be displayed with timestamps and callsigns.

### Morse Code Generator

- Enter text to be converted to Morse code.
- The Morse code will be signaled using the Pico's onboard LED or an external LED if configured.

### Considerations

- In addition to the above I had considered the possibility of adding in storage so that any chat messages could be saved and rendered when the Pico is powered on.
- I decided against doing so in this iteration, on review of Pico's documentation it seems that while there is some onboard memory the flash memory only has a limited number of write cycles so frequent use could wear it out.
- There is the possibility of using something like an SD card with the Pico however that creates more complexity with additoinal hardware and I wanted this to be a fairly light project in terms of what the user needs.
