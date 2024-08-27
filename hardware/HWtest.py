# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:40:20 2024

@author: ew
"""
from Phidget22.Phidget import *
from Phidget22.Devices.DigitalOutput import *
import time

def main():
	digitalOutput0 = DigitalOutput()

	digitalOutput0.openWaitForAttachment(5000)

	digitalOutput0.setDutyCycle(1)

	try:
		input("Press Enter to Stop\n")
	except (Exception, KeyboardInterrupt):
		pass

	digitalOutput0.close()

main()
