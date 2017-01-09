# CHSGardenPi

Repository for the Clarksburg High School Raspberry Pi Garden Monitoring System 

Goal: create a monitoring and self-irrigating system for one system in the CHS Greenhouse.

Written and maintained by:

-Rahul Shah

#Resources

Future developers can use these resources that I found relevant while making this:

* ModMYPi moisture sensor + sending texts/email https://www.modmypi.com/blog/raspberry-pi-plant-pot-moisture-sensor-with-email-notification-tutorial

* GrovePi github page https://github.com/DexterInd/GrovePi/

This is using the GrovePi+ Starter Kit for Raspberry Pi

#Practicality

Obviously the pi program you wrote won't be useful if you always had to log in and run the program from a computer's shell/PuTTY

My way around this was to edit the pi's rc.local file (found in /etc/). In it you will find this line:

    '#python /home/Desktop/GrovePi/Software/Python/monitor.py &'

Getting rid of the \# comment marker will result in the monitor.py program running as soon as the pi is booted on

If you want to run your own program from boot just copy the statement above and change 'monitor.py' to your file name. 
Remember to keep the '&' at the end of the statement so that the program doesn't go rogue if the pi shuts off unexpectedly.

For portability and user preference purposes, the pi has a "shut down button". **Make sure that when you are done using the pi you run sudo shutdown -h now or some variation to prolong the life of the sd card**

Users should **always** use the shutdown button before unplugging the pi. 

Just like the "run on boot" line above, the shutdown button command is on line 72 of the 'monitor.py' program. Comment it out to get the shutdown button working.

*REMEMBER TO KEEP THE STATEMENT ABOVE THE COMMENTS IF YOU WANT A SCRIPT TO RUN BEFORE LOGIN/ON BOOT*


#Getting started resources

In case you delete everything, don't cry it's right here.

* PuTTY - putty.org this is the windows shell we use for working with the pi since MCPS sadly uses windows computers 

* GrovePi github - https://github.com/DexterInd/GrovePi/ so you can re-clone if you mess up or there's an update

#In case of SD card corruption

No backup cards have been made, however it is very easy to transfer code back on to a new SD card. Here's what to do step by step if the card is corrupted.

1) Take the SD card out
2) Take the new SD card and put it into the Pi
3) You need administrator access to set up the Pi. Either contact Ms. Bailey so you can use her laptop or **ask** to take the Pi home and use your computer
4) Open up terminal on the computer
5) Follow the directions here https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/setting-up-wifi-with-occidentalis
6) Now you must find the IP address of the pi. This requires doing a wlan grep 
7) Write down the IP address you get. It should start with 10.234.something
8) Plug the pi in at school and use the ip address you wrote down to log in!
9) cd into the Desktop and ssh clone the GrovePi github directory 
10) chmod +x the grove_rgb_lcd file since the pi uses the lcd monitor
11) navigate to the python directory 
12) touch monitor.py and paste in the code here from github! Or you can clone it in, whatever
13) remember to go back to rc.local and add the line for the shutdown button!!!!
14) run to class because this probably took all period to do





