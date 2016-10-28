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

My way around this was to edit the pi's rc.local file. In it you will find this line:

    '#python /home/Desktop/GrovePi/Software/Python/monitor.py &'

Getting rid of the \# comment marker will result in the monitor.py program running as soon as the pi is booted on

If you want to run your own program from boot just copy the statement above and change 'monitor.py' to your file name. 
Remember to keep the '&' at the end of the statement so that the program doesn't go rogue if the pi shuts off unexpectedly.

*REMEMBER TO KEEP THE STATEMENT ABOVE THE COMMENTS IF YOU WANT A SCRIPT TO RUN BEFORE LOGIN/ON BOOT*


#Getting started resources

In case you delete everything, don't cry it's right here.

* PuTTY - putty.org this is the windows shell we use for working with the pi since MCPS sadly uses windows computers 

* GrovePi github - https://github.com/DexterInd/GrovePi/ so you can re-clone if you mess up or there's an update




