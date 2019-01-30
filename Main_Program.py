import LEGOKibbleBalanceGUI
import wx
import Phidget
import LabJack_U6
import thread
import matplotlib.pyplot as plt
import numpy as np
import time
import webbrowser

class AboutFrame(LEGOKibbleBalanceGUI.AboutFrame):

        def __init__(self, parent):
                LEGOKibbleBalanceGUI.AboutFrame.__init__(self, parent)

        def GithubURL(self, event):
                url = 'https://github.com/MSLNZ/LEGO_Kibble_Balance'

                # Open URL in a new tab, if a browser window is already open.
                webbrowser.open_new_tab(url)


class LEGOKibbleBalance(LEGOKibbleBalanceGUI.LEGOKibbleBalance):
        numChannels = 4  # Number of Aanalog Input channels being used
        latestAinValues = [0] * numChannels  # Array for storing Voltages for each channel being used

        def __init__(self, parent):
                ''' Constructor for the main program. Also sets the initial conditions for the supply voltages
                        for each coil '''
                LEGOKibbleBalanceGUI.LEGOKibbleBalance.__init__(self, parent)
                self.EventLog.AppendText("Welcome to LEGO Kibble Balance!\n")
                Phidget.initialise()
                self.SetCoilAVoltage.SetValue("0.0")
                self.SetCoilBVoltage.SetValue("0.0")
                self.KiParam = float(self.Ki.GetValue())
                self.KpParam = float(self.Kp.GetValue())
                self.KdParam = float(self.Kd.GetValue())
                self.NumRepeats = int(self.RepeatMeasurements.GetValue())
                #thread.start_new_thread(self.Sine, ())

        def SetCoilASupplyVoltage(self):
                ''' Set the supply voltage for Coil A '''
                Supply_Voltage_A = float(self.SetCoilAVoltage.GetValue())
                # Conditions to prevent Phidget from exceeding output current limit for Coil A
                if (Supply_Voltage_A >= 8):
                        Phidget.setVoltage(8, 0)
                        self.EventLog.AppendText(
                                "Setting Coil A Supply Voltage to 8V to prevent Phidget output current limit\n")
                elif (Supply_Voltage_A <= -8):
                        Phidget.setVoltage(-8, 0)
                        self.EventLog.AppendText(
                                "Setting Coil A Supply Voltage to -8V to prevent Phidget output current limit\n")
                else:
                        Phidget.setVoltage(Supply_Voltage_A, 0)
                        self.EventLog.AppendText(
                                "Setting Coil A Supply Voltage to " + self.SetCoilAVoltage.GetValue() + " V\n")
                self.GetCoilVoltages()
                self.DisplayCoilCurrents()
                self.DisplayResVoltages()
                self.CalculateMass()

        def SetCoilBSupplyVoltage(self):
                ''' Manually set the Supply voltage on Coil B. Also implements safety conditions to prevent over
                                current'''
                self.EventLog.AppendText("Setting Coil B Supply Voltage to " + self.SetCoilBVoltage.GetValue() + " V\n")
                Supply_Voltage_B = float(self.SetCoilBVoltage.GetValue())
                # Conditions to prevent Phidget from exceeding output current limit for Coil A
                if (Supply_Voltage_B >= 8):
                        Phidget.setVoltage(8, 1)
                        self.EventLog.AppendText(
                                "Setting Coil B Supply Voltage to 8V to prevent Phidget output current limit\n")
                elif (Supply_Voltage_B <= -8):
                        Phidget.setVoltage(-8, 1)
                        self.EventLog.AppendText(
                                "Setting Coil B Supply Voltage to -8V to prevent Phidget output current limit\n")
                else:
                        Phidget.setVoltage(Supply_Voltage_B, 1)
                        self.EventLog.AppendText(
                                "Setting Coil B Supply Voltage to " + self.SetCoilBVoltage.GetValue() + " V\n")
                self.GetCoilVoltages()
                self.DisplayCoilCurrents()
                self.DisplayResVoltages()

        def GetCoilVoltages(self):
                ''' Communicate with LabJack U6 and get the voltages across the resistor in series with each coil '''
                global numChannels, latestAinValues
                numChannels = 4  # Number of AIN channels being used
                latestAinValues = [0] * numChannels
                resolutionIndex = 1
                gainIndex = 0
                settlingFactor = 0
                differential = False
                numIterations = 100

                d = LabJack_U6.U6()
                d.getCalibrationData()

                try:
                        # Configure the IOs before the test starts

                        # FIOEIOAnalog = (2 ** numChannels) - 1
                        # fios = FIOEIOAnalog & 0xFF
                        # eios = FIOEIOAnalog // 256

                        d.getFeedback(LabJack_U6.PortDirWrite(Direction=[0, 0, 0], WriteMask=[0, 0, 15]))
                        feedbackArguments = []
                        feedbackArguments.append(LabJack_U6.DAC0_8(Value=125))
                        feedbackArguments.append(LabJack_U6.PortStateRead())

                        for i in range(numChannels):
                                feedbackArguments.append(LabJack_U6.AIN24(i, resolutionIndex, gainIndex, settlingFactor, differential))

                        # start = datetime.now()
                        # Call Feedback 1000 (default) times
                        i = 0
                        while i < numIterations:
                                results = d.getFeedback(feedbackArguments)
                                for j in range(numChannels):
                                        latestAinValues[j] = d.binaryToCalibratedAnalogVoltage(gainIndex, results[2 + j])
                                i += 1

                finally:
                        d.close()

        def DisplayResVoltages(self):
                ''' Display the voltages across each resistor in the GUI '''
                self.VoltageAcrossResA.SetValue(str(latestAinValues[0]))
                self.VoltageAcrossResB.SetValue(str(latestAinValues[1]))

        def DisplayCoilCurrents(self):
                ''' Display the current through each resistor in the GUI '''
                self.CurrentThroughCoilA.SetValue(str(latestAinValues[0]/178.8))
                self.CurrentThroughCoilB.SetValue(str(latestAinValues[1]/178.9))

        def SetCoilAVoltageButtonOnButtonClick(self, event):
                self.SetCoilASupplyVoltage()

        def SetCoilBVoltageButtonOnButtonClick(self, event):
                self.SetCoilBSupplyVoltage()

        def LEGOKibbleBalanceOnClose(self, event):
                ''' Close the program when user selects 'x' on the window '''
                Phidget.close()
                self.Show(False)
                quit()

        def SetCoilAVoltageOnTextEnter(self, event):
                self.SetCoilASupplyVoltage()

        def SetCoilBVoltageOnTextEnter(self, event):
                self.SetCoilBSupplyVoltage()

        def CalculateMass(self):
                ''' Calculate the objects mass and display the mass to the user '''
                currentA = float(self.CurrentThroughCoilA.GetValue())
                averageBL = 11
                gravity = 9.8189
                self.mass = currentA*averageBL/gravity
                self.ObjectMass.SetValue(str(self.mass*1000))

        def SetAutomaticControlOnButtonClick(self, event):
                ''' Sets the Parameters for PID Control '''
                self.KiParam = float(self.Ki.GetValue())
                self.KpParam = float(self.Kp.GetValue())
                self.KdParam = float(self.Kd.GetValue())
                self.NumRepeats = int(self.RepeatMeasurements.GetValue())

        def PID(self):
                ''' PID control for automatically adjusting the Kibble beam '''
                self.integral = 0
                self.target = 0.230056253258
                while(True):
                        global latestAinValues
                        self.GetCoilVoltages()
                        error = self.target - latestAinValues[2]
                        self.integral = self.integral+self.KiParam*error
                        Phidget.setVoltage(self.KpParam*error+self.integral, 0)
                        self.DisplayResVoltages()
                        self.DisplayCoilCurrents()
                        self.Kd.SetValue(str(latestAinValues[2]))
                        self.SetCoilAVoltage.SetValue(str(self.integral))
                        if abs(error) < 0.001:
                                break
                self.DisplayCoilCurrents()
                self.DisplayResVoltages()

        def RunKibbleBalanceOnButtonClick(self, event):
                thread.start_new_thread(self.RunMeasurementsThread, ())

        def RunMeasurementsThread(self):
                ''' Perform a set number of mass measurements specified on the GUI. '''
                self.MassMeasurements = []
                for i in range(0, self.NumRepeats):
                        self.PID()
                        self.CalculateMass()
                        self.MassMeasurements.append(self.mass)
                        self.EventLog.AppendText("Completed measurement " + str(i) + " \n")
                self.EventLog.AppendText("Completed all measurements\n")
                if(self.GraphMassCheckBox.GetValue()):
                        self.PlotMassData()

        def CalibrateShadowSensorOnButtonClick(self, event):
                ''' Obtain the voltage across the photodiode for 1 instance only. '''
                global latestAinValues
                self.GetCoilVoltages()
                self.target = latestAinValues[2]
                self.ShadowSensorFIeld.SetValue(str(self.target))

        def PlotMassData(self):
                ''' Plot the set of mass measurements obtained by RunMeasurementsThread. '''
                plt.plot(self.MassMeasurements, 'b+')
                plt.ylabel('Mass, g')
                plt.xlabel('Iteration, n')
                plt.show()
                print(self.MassMeasurements)

        def Sine(self):
                ''' Make Coil A move at a constant sinusoidal velocity. '''
                global latestAinValues
                i = 0
                o = 0
                oldTime = 0
                timeInit = time.time()
                times = []
                position = []
                coilVolt = []
                BL = []
                while True:
                        i = (time.time() - timeInit)
                        # if oldTime == i:
                        #         continue
                        # oldTime = i
                        self.GetCoilVoltages()
                        times.append(i)
                        position.append(round((0.117*latestAinValues[2]+0.197)/1000, 9))
                        coilVolt.append(round(latestAinValues[3], 9))
                        if i > 15:
                                break
                        #time.sleep(0.001)
                        o = 0.125*np.sin(2*i)+0.25
                        Phidget.setVoltage(o, 0)
                print(times)
                print("\n")
                print(position)
                print("\n")
                print(coilVolt)

        def AboutOnMenuSelection(self, event):
                # mandatory in wx, create an app, False stands for not deteriction stdin/stdout
                # refer manual for details
                app2 = wx.App(False)
                # create an object of CalcFrame
                frame2 = AboutFrame(None)
                # show the frame
                frame2.Show(True)
                # start the applications
                app2.MainLoop()



# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)
# create an object of CalcFrame
frame = LEGOKibbleBalance(None)
# show the frame
frame.Show(True)
# start the applications
app.MainLoop()
