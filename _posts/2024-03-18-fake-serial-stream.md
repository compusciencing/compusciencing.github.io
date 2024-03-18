---
layout: post
title: "Fake Serial Data Stream"
tags: ["python", "serial", "arduino", "sensor", "com", "virtual", "pseudoterminal", "windows"]
author: "Anthony J. Clark"
---

Here is the scenario:

> I would like to visualize Arduino sensor data using a web page and the [Web Serial API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Serial_API). The Arduino is connected to the computer via USB, and they are communicating using serial data. On the other hand, I want to test the web page without connecting an Arduino to the computer.

My solution is to

1. Capture some real data from the Arduino and its sensor, and save this data to a text file.
2. Create a Python script that reads the text file and sends it over a virtual serial port.
3. Connect the web page to the virtual serial port.

I normally develop on my Macbook, but it would not allow me to easily connect a virtual serial port to a web page. So, I opted to use a Windows machine.

## Capture Real Data

This part is farily straightforwrd. On my Macbook, I connected the Arduino, uploaded a sketch in which the Arduino wrote sensor data to serial, and then used screen to capture the data to a file.

~~~bash
# -L     : log to file
# 115200 : baud rate
screen -L /dev/cu.usbserial-02857203 115200
~~~

By default, the log file is named `screenlog.0` (more generally, `screenlog.n`), but you can change the output filename with the `-Logfile` option.

## Send Data Over Virtual Serial Port

I used [`com0com`](https://com0com.sourceforge.net/) to create a pair of virtual serial ports named: `COM3` and `COM4` on Windows, and [`pyserial`](https://pyserial.readthedocs.io/en/latest/pyserial.html) library to write to a virtual port.

~~~python
from time import sleep

from serial import Serial

channel = Serial("COM3", 115200)

with open("screenlog.0", "r") as f:
    i = 0
    for line in f:
        channel.write(line.encode("utf-8"))
        print(i, line, end="")
        sleep(0.1)
        i += 1

print("Done!")
~~~

Data was read on the browser side with:

~~~javascript
const port = await navigator.serial.requestPort( { filters: portFilters } )
await port.open( { baudRate: baudRate } )

const textDecoder = new TextDecoderStream()
const readableStreamClosed = port.readable.pipeTo( textDecoder.writable )
const reader = textDecoder.readable.getReader()

async function readForever( reader, logContainer )
{
    try {

        while ( true ) {

            const { value, done } = await reader.read()

            if ( done ) {
                logContainer.textContent += "Done reading!";
                reader.releaseLock();
                break;
            }

            if ( value ) {
                logContainer.textContent += value + "\n";
                logContainer.scrollTop = logContainer.scrollHeight;
            }

        }

    } catch ( e ) {

        logContainer.textContent = `ERROR: ${ e }\n`;
        console.error( e )

    }
}


// logContainer is a <pre> element
readForever( reader, logContainer )
    .then( response =>
    {
        console.log( response, 'readLoop done' )
    } )
    .catch( e =>
    {
        logContainer.textContent = `ERROR: ${ e }\n`;
        logContainer.textContent += "Check the baud rate and ensure that you are not transmitting too much data.\n";
        console.error( e )
    } )

~~~

## Conclusion

I'll add a link to the full example here.
