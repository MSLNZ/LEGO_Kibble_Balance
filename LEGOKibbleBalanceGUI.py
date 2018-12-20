# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class LEGOKibbleBalance
###########################################################################

class LEGOKibbleBalance ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"LEGO Kibble Balance", pos = wx.DefaultPosition, size = wx.Size( 563,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Results" ), wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText11 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Resistor Voltages", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer1.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer1.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.VoltageAcrossResA = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.VoltageAcrossResA.Enable( False )
		
		fgSizer1.Add( self.VoltageAcrossResA, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Voltage Across Res A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer1.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.VoltageAcrossResB = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.VoltageAcrossResB.Enable( False )
		
		fgSizer1.Add( self.VoltageAcrossResB, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Voltage Across Res B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer1.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Coil Currents", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.CurrentThroughCoilA = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CurrentThroughCoilA.Enable( True )
		
		fgSizer1.Add( self.CurrentThroughCoilA, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Current Through Coil A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.CurrentThroughCoilB = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CurrentThroughCoilB.Enable( True )
		
		fgSizer1.Add( self.CurrentThroughCoilB, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Current Through Coil B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Mass of Object", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		fgSizer1.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.m_staticText22 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		fgSizer1.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.ObjectMass = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ObjectMass.Enable( False )
		
		fgSizer1.Add( self.ObjectMass, 0, wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Mass (g)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		fgSizer1.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		
		sbSizer6.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		fgSizer4.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Automatic Control" ), wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText16 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Proportional Gain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		bSizer2.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.Kp = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.Kp, 0, wx.ALL, 5 )
		
		
		sbSizer8.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText161 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Integral Gain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )
		bSizer21.Add( self.m_staticText161, 0, wx.ALL, 5 )
		
		self.Ki = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.Ki, 0, wx.ALL, 5 )
		
		
		sbSizer8.Add( bSizer21, 1, wx.EXPAND, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText162 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Derivative Gain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText162.Wrap( -1 )
		bSizer22.Add( self.m_staticText162, 0, wx.ALL, 5 )
		
		self.Kd = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.Kd, 0, wx.ALL, 5 )
		
		
		sbSizer8.Add( bSizer22, 1, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText25 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Repeat Measurements", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer14.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.RepeatMeasurements = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.RepeatMeasurements, 0, wx.ALL, 5 )
		
		
		sbSizer8.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		self.SetAutomaticControl = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Set Automatic Control", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.SetAutomaticControl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		fgSizer4.Add( sbSizer8, 1, wx.EXPAND, 5 )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Configure Kibble Balance" ), wx.VERTICAL )
		
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ShadowSensorFIeld = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ShadowSensorFIeld.Enable( True )
		
		bSizer23.Add( self.ShadowSensorFIeld, 0, wx.ALL, 5 )
		
		self.CalibrateShadowSensor = wx.Button( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Calibrate Shadow Sensor", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.CalibrateShadowSensor, 0, wx.ALL, 5 )
		
		
		sbSizer9.Add( bSizer23, 1, wx.EXPAND, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.SetCoilAVoltage = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.SetCoilAVoltage, 0, wx.ALL, 5 )
		
		self.SetCoilAVoltageButton = wx.Button( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Set Coil A Voltage", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.SetCoilAVoltageButton, 0, wx.ALL, 5 )
		
		
		sbSizer9.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.SetCoilBVoltage = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.SetCoilBVoltage, 0, wx.ALL, 5 )
		
		self.SetCoilBVoltageButton = wx.Button( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Set Coil B Voltage", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.SetCoilBVoltageButton, 0, wx.ALL, 5 )
		
		
		sbSizer9.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		
		fgSizer4.Add( sbSizer9, 1, wx.EXPAND, 5 )
		
		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Operate Kibble Balance" ), wx.VERTICAL )
		
		self.RunKibbleBalance = wx.Button( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Get Mass", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.RunKibbleBalance.SetMinSize( wx.Size( 200,100 ) )
		
		sbSizer10.Add( self.RunKibbleBalance, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		fgSizer4.Add( sbSizer10, 1, wx.EXPAND, 5 )
		
		sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Event Log" ), wx.VERTICAL )
		
		self.EventLog = wx.TextCtrl( sbSizer14.GetStaticBox(), wx.ID_ANY, u"Welcome to Kibble Balance!\n\n- 'Event Log' displays the systems behaviour at any given point .\n\n- 'Automatic Control' manipulates the PID coefficients for the PID controller. The number of measurements that you want to do is also set here.\n\n- 'Configure Kibble Balance' sets the zero position for the Kibble Balance shadow sensor and allows manual control of the supply voltages to each Coils A & B. \n", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.EventLog.SetMinSize( wx.Size( 270,250 ) )
		
		sbSizer14.Add( self.EventLog, 0, wx.ALL, 5 )
		
		
		fgSizer4.Add( sbSizer14, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.LEGOKibbleBalanceOnClose )
		self.Kp.Bind( wx.EVT_TEXT_ENTER, self.KpOnTextEnter )
		self.Ki.Bind( wx.EVT_TEXT_ENTER, self.KiOnTextEnter )
		self.Kd.Bind( wx.EVT_TEXT_ENTER, self.KdOnTextEnter )
		self.RepeatMeasurements.Bind( wx.EVT_TEXT_ENTER, self.RepeatMeasurementsOnTextEnter )
		self.SetAutomaticControl.Bind( wx.EVT_BUTTON, self.SetAutomaticControlOnButtonClick )
		self.CalibrateShadowSensor.Bind( wx.EVT_BUTTON, self.CalibrateShadowSensorOnButtonClick )
		self.SetCoilAVoltage.Bind( wx.EVT_TEXT_ENTER, self.SetCoilAVoltageOnTextEnter )
		self.SetCoilAVoltageButton.Bind( wx.EVT_BUTTON, self.SetCoilAVoltageButtonOnButtonClick )
		self.SetCoilBVoltage.Bind( wx.EVT_TEXT_ENTER, self.SetCoilBVoltageOnTextEnter )
		self.SetCoilBVoltageButton.Bind( wx.EVT_BUTTON, self.SetCoilBVoltageButtonOnButtonClick )
		self.RunKibbleBalance.Bind( wx.EVT_BUTTON, self.RunKibbleBalanceOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def LEGOKibbleBalanceOnClose( self, event ):
		event.Skip()
	
	def KpOnTextEnter( self, event ):
		event.Skip()
	
	def KiOnTextEnter( self, event ):
		event.Skip()
	
	def KdOnTextEnter( self, event ):
		event.Skip()
	
	def RepeatMeasurementsOnTextEnter( self, event ):
		event.Skip()
	
	def SetAutomaticControlOnButtonClick( self, event ):
		event.Skip()
	
	def CalibrateShadowSensorOnButtonClick( self, event ):
		event.Skip()
	
	def SetCoilAVoltageOnTextEnter( self, event ):
		event.Skip()
	
	def SetCoilAVoltageButtonOnButtonClick( self, event ):
		event.Skip()
	
	def SetCoilBVoltageOnTextEnter( self, event ):
		event.Skip()
	
	def SetCoilBVoltageButtonOnButtonClick( self, event ):
		event.Skip()
	
	def RunKibbleBalanceOnButtonClick( self, event ):
		event.Skip()
	

