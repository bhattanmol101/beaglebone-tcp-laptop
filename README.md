Beaglebone wireless data transfer to PC over WiFi

For my project I have to send data from beaglebone black to my PC wirelessly via WiFi so I connect my beaglebone to a WiFi router via Ethernet cable and then connect my laptop to that router and receive data on PC. I have to send 3 different types of data from my beaglebone to PC and all 3 are independent i.e I can’t merge them into one and send it as one string. Each data has to be sent independently. So I went through lot of sites online and finally came to the following solution and I used python 3.4.2 for it.

First of all there are two things you need to know one is server and other is client. You can either setup your beaglebone as server and let the PC connect to the beaglebone or you can make your PC as server and let beaglebone connect to it. If you have to send data from only one file or one code then anything is fine but if you have to make multiple connections from beaglebone to PC the I would prefer making PC as server and letting beaglebone connect to it.

I made my PC as the server to which my beaglebone has to connect. Below is the code that I used for the server part. Here as my host is blank which means any IP address can connect to my server they just need to know my server’s IP address. As I have to send 3 different types of data I have made 3 threads and all these 3 threads will wait until they get connected by some device.

I made my beaglebone as a client which will connect to my PC via WiFi. Below is the code that I used for the client part. Here my host is the IP address of the server i.e the IP by which the router is connected to my PC. Port can be any 16-bit unsigned integer i.e 0 to 65535.

Here I am just sending “HELLO” to PC for demo you can replace it with anything but make sure to add encode() after it, as in python 2.7 the transfer happens as String but in python 3 and above it changed to bytecode. You need to convert the message to bytecode and the send it. Also you will have to decode the message after you receive it as one can not understand bytecode easily, that’s why I have used decode(‘utf-8’). Here ‘utf-8’ tells the decode function to decode it as UTF-8 format.

So this is how you can achieve wireless/TCP communication between PC and your beaglebone using WiFi.