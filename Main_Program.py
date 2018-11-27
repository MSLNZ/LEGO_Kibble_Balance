import LEGOKibbleBalanceGUI
import wx
import Phidget
import LabJack_U6

class LEGOKibbleBalance(LEGOKibbleBalanceGUI.LEGOKibbleBalance):
	numChannels = 2  # Number of Aanalog Input channels being used
	latestAinValues = [0] * numChannels  # Array for storing Voltages for each channel being used

	''' Object initialiser for the main program. Also sets the initial conditions for the supply voltages 
	for each coil '''
	def __init__(self, parent):
		LEGOKibbleBalanceGUI.LEGOKibbleBalance.__init__(self, parent)
		self.KibbleLog.AppendText("Welcome to LEGO Kibble Balance!\n")
		Phidget.initialise()
		self.CoilASupplyVoltage.SetValue("0.0")
		self.CoilBSupplyVoltage.SetValue("0.0")

	''' Communicate with LabJack U6 and get the voltages across the resistor in series with each coil '''
	def GetCoilVoltages(self):
		global numChannels, latestAinValues
		numChannels = 2  # Number of AIN channels being used
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

	''' Display the voltages across each resistor in the GUI '''
	def DisplayResVoltages(self):
		self.VoltageAcrossResA.SetValue(str(latestAinValues[0]))
		self.VoltageAcrossResB.SetValue(str(latestAinValues[1]))

	''' Display the current through each resistor in the GUI '''
	def DisplayCoilCurrents(self):
		self.CurrentThroughCoilA.SetValue(str(latestAinValues[0]/178.8))
		self.CurrentThroughCoilB.SetValue(str(latestAinValues[1]/178.9))

	''' Set the supply voltage for Coil A '''
	def SetCoilAVoltageOnButtonClick(self, event):
		Supply_Voltage_A = float(self.CoilASupplyVoltage.GetValue())
		# Conditions to prevent Phidget from exceeding output current limit for Coil A
		if (Supply_Voltage_A > 8):
			Phidget.setVoltage(8, 0)
			self.KibbleLog.AppendText("Setting Coil A Supply Voltage to 8V to prevent Phidget output current limit\n")
		elif (Supply_Voltage_A < -8):
			Phidget.setVoltage(-8, 0)
			self.KibbleLog.AppendText("Setting Coil A Supply Voltage to -8V to prevent Phidget output current limit\n")
		else:
			Phidget.setVoltage(Supply_Voltage_A, 0)
			self.KibbleLog.AppendText("Setting Coil A Supply Voltage to " + self.CoilASupplyVoltage.GetValue() + " V\n")
		self.GetCoilVoltages()
		self.DisplayCoilCurrents()
		self.DisplayResVoltages()

	''' Set the supply voltage for Coil B '''
	def SetCoilBVoltageOnButtonClick(self, event):
		self.KibbleLog.AppendText("Setting Coil B Supply Voltage to " + self.CoilBSupplyVoltage.GetValue() + " V\n")
		Supply_Voltage_B = float(self.CoilBSupplyVoltage.GetValue())
		# Conditions to prevent Phidget from exceeding output current limit for Coil A
		if(Supply_Voltage_B>8):
			Phidget.setVoltage(8, 1)
			self.KibbleLog.AppendText("Setting Coil B Supply Voltage to 8V to prevent Phidget output current limit\n")
		elif(Supply_Voltage_B<-8):
			Phidget.setVoltage(-8, 1)
			self.KibbleLog.AppendText("Setting Coil B Supply Voltage to -8V to prevent Phidget output current limit\n")
		else:
			Phidget.setVoltage(Supply_Voltage_B, 1)
			self.KibbleLog.AppendText("Setting Coil B Supply Voltage to " + self.CoilBSupplyVoltage.GetValue() + " V\n")
		self.GetCoilVoltages()
		self.DisplayCoilCurrents()
		self.DisplayResVoltages()

	''' Close the program when user selects 'x' on the window '''
	def LEGOKibbleBalanceOnClose(self, event):
		Phidget.close()
		self.Show(False)
		quit()


# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)

# create an object of CalcFrame
frame = LEGOKibbleBalance(None)
# show the frame
frame.Show(True)
# start the applications
app.MainLoop()