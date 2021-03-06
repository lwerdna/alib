#!/usr/bin/python
#------------------------------------------------------------------------------
#
#	Copyright 2011-2016 Andrew Lamoureux
#
#	This file is a part of autils.
#
#	autils is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#------------------------------------------------------------------------------

# client probably wants something like this:
# 
# import termcolors
# 
# def ColorDebug():
#	 termcolors.ColorOrange()
# def ColorWarn():
#	 termcolors.ColorYellow()
# def ColorError():
#	 termcolors.ColorRed()
# def ColorInfo():
#	 termcolors.ColorGrey()
# def ColorData():
#	 termcolors.ColorBlue()
# def ColorNormal():
#	 termcolors.ColorNormal()
# 
# def printInfo(msg):
#	 ColorInfo()
#	 print msg
#	 termcolors.ColorPop()
# 
# def printError(msg):
#	 ColorError()
#	 print msg
#	 termcolors.ColorPop()
# 
# def printWarn(msg):
#	 ColorWarn()
#	 print msg
#	 termcolors.ColorPop()
# 
# def printDebug(msg):
#	 ColorDebug()
#	 print msg
#	 termcolors.ColorPop()

#experiment with: echo -e "\033[31m ROUGE \033[0m"
FOREGROUND_BLACK = '\033[30m'
FOREGROUND_RED = '\033[31m'
FOREGROUND_GREEN = '\033[32m'
FOREGROUND_YELLOW = '\033[33m'
FOREGROUND_BLUE_DARK = '\033[34m'
FOREGROUND_ORANGE = '\033[35m'
FOREGROUND_BLUE_LIGHT = '\033[36m'
FOREGROUND_WHITE = '\033[37m'
FOREGROUND_ORIG = '\033[0m'

FOREGROUND_DISAS = FOREGROUND_BLUE_LIGHT
FOREGROUND_DISAS_SYM = FOREGROUND_ORANGE

original_color_saved = 0
original_color = 0
color_stack = [FOREGROUND_ORIG]

def ColorPush(color):
	color_stack.append(color)
	print color_stack[-1],

def ColorPop():
	color_stack.pop()
	print color_stack[-1],

# only change color if its not already changed
def ColorNudge(color):
	if len(color_stack) > 1:
		ColorPush(color)

def ColorReset():
	color_stack = [FOREGROUND_ORIG]
	print color_stack[-1],

def ColorDebug():
	ColorPush(FOREGROUND_ORANGE)
def ColorWarn():
	ColorPush(FOREGROUND_YELLOW)
def ColorError():
	ColorPush(FOREGROUND_RED)
def ColorInfo():
	ColorPush(FOREGROUND_GREEN)
def ColorData():
	ColorPush(FOREGROUND_BLUE_LIGHT)
def ColorNormal():
	ColorPush(FOREGROUND_ORIG)

def Info(msg):
	ColorInfo()
	print msg
	ColorPop()

def Error(msg):
	ColorError()
	print msg
	ColorPop()

def Warn(msg):
	ColorWarn()
	print msg
	ColorPop()

def Debug(msg):
	ColorDebug()
	print msg
	ColorPop()

