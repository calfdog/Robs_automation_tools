"""
    Description - jpype helper
    Developed by: Rob Marchetti 11/17/2014
"""

from jpype import *

# Start the Java JVM - put your the path to your own jvm.dll
startJVM(r"C:\Program Files (x86)\Java\jre7\bin\client\jvm.dll")

# Java packages to use for this automation script
Robot = JPackage('java').awt.Robot
InputEvent = JPackage('java').awt.event.InputEvent
KeyEvent = JPackage('java').awt.event.KeyEvent

# Siukli Helper with Jpype
#  org.sikuli.api.*;
api = JPackage('org').sikuli.api
mouse = JPackage('org').sikuli.api.robot.Mouse
DesktopMouse = JPackage('org').sikuli.api.robot.desktop.DesktopMouse
Canvas = JPackage('org').sikuli.api.visual.Canvas
DesktopCanvas = JPackage('org').sikuli.api.DesktopCanvas
r = Robot()
