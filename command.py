#!/usr/bin/env python3
from simple_rover_sj17 import *

# Following are the commands that are available:
# stop()        # stop
# forward()     # go forward 0.3 meters
# forward(1.0)  # go forward some distance, any positive number in meters
# backward()    # go backward 0.3 meters
# backward(1.0) # go backward some distance, any positive number in meters
# right()       # turn right 90 deg
# right(1.0)    # turn right some angle, any positive number in deg
# left()        # turn left 90 deg
# left(1.0)     # turn left some angle, any positive number in deg
# isblocked()   # returns True if front is blocked, otherwise returns False
# temperature() # returns the temperature in Celsius
# humidity()    # returns the humidity in %
# heading()     # returns the heading in degrees
# zmag()        # returns the magnitude of magnetic field in the z-direction
# arm()         # arms the lance
# disarm()      # disarms the lance
# image()       # takes an image and saves it to /var/www/html/rover_img/.


forward()     # go forward 0.3 meters
backward()    # go backward 0.3 meters
right()       # turn right 90 deg
left()        # turn left 90 deg
isblocked()   # returns True if front is blocked, otherwise returns False
temperature() # returns the temperature in Celsius
humidity()    # returns the humidity in %
heading()     # returns the heading in degrees
zmag()        # returns the magnitude of magnetic field in the z-direction
arm()         # arms the lance
disarm()      # disarms the lance
image()       # takes an image and saves it to /var/www/html/rover_img/.