# Smart-Home-IoT-(Poor-Man's-Jarvis)
IoT project about sensors and communication to build a smart home system

# This was my bachelor project, i quite don't remember the wiring of this, but you can mail me for how to make one
Project has an interface and two servers running backend (one was enough but has different pros and cons, and, i had time to do that)
Flask server is controlling all sensors attachted to Raspberry Pi (in that project rPi 3B+) and
NodeJS server is communicating to Flask for data flow and serving to client.

# Flask Server (python)
This one had 3 direct plugged sensors and 2 usb webcams (cheap usb webcams are enough to demonstrate)
Plugged sensors are temp/humidity , light and gas detectors. T/H and Gas had digital outputs and it's very easy to read by rPi. But light sensor was analog and had to converted digital signal by an ADC.

# NodeJS Server
Takes all data from Flask and shows in fancy UI. It's just a simple Node + Express + Vue server, ready to plug a mongoDB but wasn't necessary. 

I used "ngrok" to demonstrate this conceptual smart home system but it's better to configurated on modem and something. It is not so easy to understand with that code, because it was built for my thesis before and pin numbers are depend on them, but it might help to visualize how that data flow works with examples.

For any questions, ask me on misunra.com
Thanks
