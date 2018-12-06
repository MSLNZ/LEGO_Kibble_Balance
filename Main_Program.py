import LEGOKibbleBalanceGUI
import wx
import Phidget
import LabJack_U6
import thread

class LEGOKibbleBalance(LEGOKibbleBalanceGUI.LEGOKibbleBalance):
        numChannels = 3  # Number of Aanalog Input channels being used
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

        def SetCoilAVoltage(self):
                ''' Set the supply voltage for Coil A '''
                Supply_Voltage_A = float(self.SetCoilAVoltage.GetValue())
                # Conditions to prevent Phidget from exceeding output current limit for Coil A
                if (Supply_Voltage_A > 8):
                        Phidget.setVoltage(8, 0)
                        self.EventLog.AppendText(
                                "Setting Coil A Supply Voltage to 8V to prevent Phidget output current limit\n")
                elif (Supply_Voltage_A < -8):
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

        def SetCoilBVoltage(self):
                ''' Manually set the Supply voltage on Coil B. Also implements safety conditions to prevent over
                                current'''
                self.EventLog.AppendText("Setting Coil B Supply Voltage to " + self.SetCoilBVoltage.GetValue() + " V\n")
                Supply_Voltage_B = float(self.SetCoilBVoltage.GetValue())
                # Conditions to prevent Phidget from exceeding output current limit for Coil A
                if (Supply_Voltage_B > 8):
                        Phidget.setVoltage(8, 1)
                        self.EventLog.AppendText(
                                "Setting Coil B Supply Voltage to 8V to prevent Phidget output current limit\n")
                elif (Supply_Voltage_B < -8):
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
                numChannels = 3  # Number of AIN channels being used
                latestAinValues = [0] * numChannels
                resolutionIndex = 1
                gainIndex = 0
                settlingFactor = 0
                differential = False
                numIterations = 1000

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
                self.SetCoilAVoltage()

        def SetCoilBVoltageButtonOnButtonClick(self, event):
                self.SetCoilBVoltage()

        def LEGOKibbleBalanceOnClose(self, event):
                ''' Close the program when user selects 'x' on the window '''
                Phidget.close()
                self.Show(False)
                quit()

        def CoilASupplyVoltageOnTextEnter(self, event):
                self.SetCoilAVoltage()

        def CoilBSupplyVoltageOnTextEnter(self, event):
                self.SetCoilBVoltage()

        def CalculateMass(self):
                ''' Calcualte the objects mass and display the mass to the user '''
                currentA = float(self.CurrentThroughCoilA.GetValue())
                averageBL = 17.27576831
                gravity = 9.8189
                self.mass = currentA*averageBL/gravity
                self.ObjectMass.SetValue(str(self.mass*1000))

        def SetAutomaticControlOnButtonClick(self, event):
                self.KiParam = float(self.Ki.GetValue())
                self.KpParam = float(self.Kp.GetValue())
                self.KdParam = float(self.Kd.GetValue())
                self.NumRepeats = int(self.RepeatMeasurements.GetValue())

        def PID(self):
                ''' PID control for automatically adjusting the Kibble beam '''
                self.integral = 0
                while(True):
                        global latestAinValues
                        self.GetCoilVoltages()
                        error = latestAinValues[2] - self.target
                        self.integral = self.integral+self.KiParam*error
                        Phidget.setVoltage(self.integral, 0)
                        self.DisplayResVoltages()
                        self.DisplayCoilCurrents()
                        self.SetCoilAVoltage.SetValue(str(self.integral))
                        if abs(error) < 0.001:
                                break
                self.DisplayCoilCurrents()
                self.DisplayResVoltages()

        def RunKibbleBalanceOnButtonClick(self, event):
                thread.start_new_thread(self.RunMeasurementsThread, ())

        def RunMeasurementsThread(self):
                self.MassMeasurements = []
                for i in range(0, self.NumRepeats):
                        self.PID()
                        self.CalculateMass()
                        self.MassMeasurements.append(self.mass)
                        self.EventLog.AppendText("Completed measurement " + str(i) + " \n")
                self.EventLog.AppendText("Completed all measurements\n")

        def CalibrateShadowSensorOnButtonClick(self, event):
                global latestAinValues
                self.GetCoilVoltages()
                self.target = latestAinValues[2]
                self.ShadowSensorFIeld.SetValue(str(self.target))

                
# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)
# create an object of CalcFrame
frame = LEGOKibbleBalance(None)
# show the frame
frame.Show(True)
# start the applications
app.MainLoop()
