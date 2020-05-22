# virl-parse

Python script to parse device configurations, interfaces, and device connections from topology files exported from VIRL.
The intention is to make it simpler to import VIRL exported toplogies into either GNS3 or physical devices. I have had success running 
the script against many different VIRL topolgies that included routers, switches, docker container, etc.  YMMV

Run script in the same directory as your *.virl files.  You will be prompted for a keyword.  Only files matching the keyword 
with a .virl extension will be parsed.

The script will create a subdirectory named from the parsed filename_virl.  That directory will contain

* devices.text
 * each device type
 * each device physical interfaces

* connections.text
 * physical connections between devices

* *devicename*.txt
 * Configuration from device in virl.

