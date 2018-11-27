import sys
import time 
from Phidget22.Devices.VoltageOutput import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *

try:
    from PhidgetHelperFunctions import *
except ImportError:
    sys.stderr.write("\nCould not find PhidgetHelperFunctions. Either add PhdiegtHelperFunctions.py to your project folder "
                      "or remove the import from your project.")
    sys.exit()

ch0 = None
ch1 = None

'''
* Displays info about the attached Phidget channel.  
* Fired when a Phidget channel with onAttachHandler registered attaches
*
* @param self The Phidget channel that fired the attach event
'''
def onAttachHandler(self):
    
    ph = self

    try:
        #If you are unsure how to use more than one Phidget channel with this event, we recommend going to
        #www.phidgets.com/docs/Using_Multiple_Phidgets for information
        
        print("\nAttach Event:")
        
        """
        * Get device information and display it.
        """
        channelClassName = ph.getChannelClassName()
        serialNumber = ph.getDeviceSerialNumber()
        channel = ph.getChannel()
        if(ph.getDeviceClass() == DeviceClass.PHIDCLASS_VINT):
            hubPort = ph.getHubPort()
            print("\n    -> Channel Class: " + channelClassName + "\n    -> Serial Number: " + str(serialNumber) +
                "\n    -> Hub Port: " + str(hubPort) + "\n    -> Channel:  " + str(channel) + "\n")
        else:
            print("\n    -> Channel Class: " + channelClassName + "\n    -> Serial Number: " + str(serialNumber) +
                    "\n    -> Channel:  " + str(channel) + "\n")
        
    except PhidgetException as e:
        print("\nError in Attach Event:")
        DisplayError(e)
        traceback.print_exc()
        return

"""
* Displays info about the detached Phidget channel.
* Fired when a Phidget channel with onDetachHandler registered detaches
*
* @param self The Phidget channel that fired the attach event
"""
def onDetachHandler(self):

    ph = self

    try:
        #If you are unsure how to use more than one Phidget channel with this event, we recommend going to
        #www.phidgets.com/docs/Using_Multiple_Phidgets for information
        
        print("\nDetach Event:")
        
        """
        * Get device information and display it.
        """
        channelClassName = ph.getChannelClassName()
        serialNumber = ph.getDeviceSerialNumber()
        channel = ph.getChannel()
        if(ph.getDeviceClass() == DeviceClass.PHIDCLASS_VINT):
            hubPort = ph.getHubPort()
            print("\n    -> Channel Class: " + channelClassName + "\n    -> Serial Number: " + str(serialNumber) +
                "\n    -> Hub Port: " + str(hubPort) + "\n    -> Channel:  " + str(channel) + "\n")
        else:
            print("\n    -> Channel Class: " + channelClassName + "\n    -> Serial Number: " + str(serialNumber) +
                    "\n    -> Channel:  " + str(channel) + "\n")
        
    except PhidgetException as e:
        print("\nError in Detach Event:")
        DisplayError(e)
        traceback.print_exc()
        return

"""
* Writes Phidget error info to stderr.
* Fired when a Phidget channel with onErrorHandler registered encounters an error in the library
*
* @param self The Phidget channel that fired the attach event
* @param errorCode the code associated with the error of enum type ph.ErrorEventCode
* @param errorString string containing the description of the error fired
"""
def onErrorHandler(self, errorCode, errorString):

    sys.stderr.write("[Phidget Error Event] -> " + errorString + " (" + str(errorCode) + ")\n")
            
"""
* Creates, configures, and opens a VoltageOutput channel.
* Provides interface for controlling Voltage of the VoltageOutput.
* Closes out VoltageOutput channel
*
* @return 0 if the program exits successfully, 1 if it exits with errors.
"""
def initialise():
    try:
        """
        * Allocate a new Phidget Channel object
        """
        global ch0
        global ch1
        try:
            ch0 = VoltageOutput()
            ch1 = VoltageOutput()
        except PhidgetException as e:
            sys.stderr.write("Runtime Error -> Creating VoltageOutput: \n    ")
            DisplayError(e)
            raise
        except RuntimeError as e:
            sys.stderr.write("Runtime Error -> Creating VoltageOutput: \n    " + e)
            raise

        """
        * Set matching parameters to specify which channel to open
        """
        #You may remove this line and hard-code the addressing parameters to fit your application
        #channelInfo = AskForDeviceParameters(ch)
        
        ch0.setDeviceSerialNumber(493848)
        ch1.setDeviceSerialNumber(493848)
        ch0.setHubPort(0)
        ch1.setHubPort(0)
        ch0.setIsHubPortDevice(0)
        ch1.setIsHubPortDevice(0)
        ch0.setChannel(0)   
        ch1.setChannel(1)
        
        """
        * Add event handlers before calling open so that no events are missed.
        """
        print("\n--------------------------------------")
        print("\nSetting OnAttachHandler...")
        ch0.setOnAttachHandler(onAttachHandler)
        ch1.setOnAttachHandler(onAttachHandler)
        
        print("Setting OnDetachHandler...")
        ch0.setOnDetachHandler(onDetachHandler)
        ch1.setOnDetachHandler(onDetachHandler)
        
        print("Setting OnErrorHandler...")
        ch0.setOnErrorHandler(onErrorHandler)
        ch1.setOnErrorHandler(onErrorHandler)
        
        """
        * Open the channel with a timeout
        """
        print("\nOpening and Waiting for Attachment...")
        
        try:
            ch0.openWaitForAttachment(5000)
        except PhidgetException as e:
            PrintOpenErrorMessage(e, ch0)
            raise EndProgramSignal("Program Terminated: Open Failed")

        try:
            ch1.openWaitForAttachment(5000)
        except PhidgetException as e:
            PrintOpenErrorMessage(e, ch1)
            raise EndProgramSignal("Program Terminated: Open Failed")
    
        except PhidgetException as e:
            sys.stderr.write("\nExiting with error(s)...")
            DisplayError(e)
            traceback.print_exc()
            print("Cleaning up...")
            ch0.close()
            ch1.close()
            return 1
    
    except EndProgramSignal as e:
        print(e)
        print("Cleaning up...")
        ch.close()
        return 1

def setVoltage(voltage, channel):
    try:
        # print("--------------------\n"
        # "\n  | VoltageOutput voltage can be controlled by setting its Target Voltage.\n"
        # "  | The target voltage can be a number between MinVoltage and MaxVoltage.\n"
        # "\nInput a desired voltage and press ENTER\n"
        # "Input Q and press ENTER to quit\n")
        try:
            voltage = float(voltage)
        except ValueError as e:
            print("Input must be a number, or Q to quit.")
            return 0

        if (voltage > ch0.getMaxVoltage() or voltage < ch0.getMinVoltage()):
            print("Voltage must be between %.2f and %.2f\n" % (ch0.getMinVoltage(), ch0.getMaxVoltage()))
            return 0

        print("Setting VoltageOutput Voltage to " + str(voltage))
        if channel == 0:
            ch0.setVoltage(voltage)
        elif channel == 1:
            ch1.setVoltage(voltage)

    except PhidgetException as e:
        sys.stderr.write("\nExiting with error(s)...")
        DisplayError(e)
        traceback.print_exc()
        print("Cleaning up...")
        ch.close()
        return 1
    except EndProgramSignal as e:
        print(e)
        print("Cleaning up...")
        ch.close()
        return 1

'''
* Perform clean up and exit
'''
def close():
    global ch0
    global ch1
    print("Cleaning up...")
    ch0.close()
    ch1.close()
    print("\nExiting...")
    return 0

#main()

