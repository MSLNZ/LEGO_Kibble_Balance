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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"LEGO Kibble Balance", pos = wx.DefaultPosition, size = wx.Size( 562,403 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Supply Voltages", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.CoilASupplyVoltage = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.CoilASupplyVoltage, 0, wx.ALL, 5 )
		
		self.SetCoilAVoltage = wx.Button( self, wx.ID_ANY, u"Set Coil A Supply Voltage", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.SetCoilAVoltage, 0, wx.ALL, 5 )
		
		self.CoilBSupplyVoltage = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.CoilBSupplyVoltage, 0, wx.ALL, 5 )
		
		self.SetCoilBVoltage = wx.Button( self, wx.ID_ANY, u"Set Coil B Supply Voltage", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.SetCoilBVoltage, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Resistor Voltages", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer1.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer1.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.VoltageAcrossResA = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.VoltageAcrossResA.Enable( False )
		
		fgSizer1.Add( self.VoltageAcrossResA, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Voltage Across Res A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer1.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.VoltageAcrossResB = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.VoltageAcrossResB.Enable( False )
		
		fgSizer1.Add( self.VoltageAcrossResB, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Voltage Across Res B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer1.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Coil Currents", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.CurrentThroughCoilA = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CurrentThroughCoilA.Enable( False )
		
		fgSizer1.Add( self.CurrentThroughCoilA, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Current Through Coil A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.CurrentThroughCoilB = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CurrentThroughCoilB.Enable( False )
		
		fgSizer1.Add( self.CurrentThroughCoilB, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Current Through Coil B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Mass of Object", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		fgSizer1.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		fgSizer1.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.ObjectMass = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ObjectMass.Enable( False )
		
		fgSizer1.Add( self.ObjectMass, 0, wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Mass (g)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		fgSizer1.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		
		gbSizer1.Add( fgSizer1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		fgSizer5 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"LEGO Kibble Balance Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer5.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.KibbleLog = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,310 ), wx.TE_MULTILINE )
		fgSizer5.Add( self.KibbleLog, 0, wx.ALL, 5 )
		
		
		gbSizer1.Add( fgSizer5, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.LEGOKibbleBalanceOnClose )
		self.SetCoilAVoltage.Bind( wx.EVT_BUTTON, self.SetCoilAVoltageOnButtonClick )
		self.SetCoilBVoltage.Bind( wx.EVT_BUTTON, self.SetCoilBVoltageOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def LEGOKibbleBalanceOnClose( self, event ):
		event.Skip()
	
	def SetCoilAVoltageOnButtonClick( self, event ):
		event.Skip()
	
	def SetCoilBVoltageOnButtonClick( self, event ):
		event.Skip()
	

